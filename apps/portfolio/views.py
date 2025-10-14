from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse, Http404
from django.core.mail import send_mail
from django.contrib import messages
from django.db.models import Q, Count
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.conf import settings
from operator import attrgetter
import os
import mimetypes
from xhtml2pdf import pisa
from io import BytesIO
from .models import (
    Personal, About, Experience, Description, Education, Technology, Portfolio,
    Testimonial, BlogPost, Project, ContactMessage, SiteSettings, RoadmapStep, Certification
)
from .forms import ContactForm

class HomePageView(TemplateView):
    template_name = 'portfolio/portfolio_main.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personal'] = Personal.objects.all()
        context['current_theme'] = self.request.session.get('theme', 'dark')
        context['about'] = About.objects.all()
        context['technologies'] = Technology.objects.filter(is_featured=True).order_by('-skill_level')[:18]
        context['portfolio'] = Portfolio.objects.all()
        context['testimonials'] = Testimonial.objects.filter(is_featured=True)[:3]
        context['featured_projects'] = Project.objects.filter(is_featured=True)[:6]
        context['blog_posts'] = BlogPost.objects.filter(published=True)[:3]
        context['roadmap_steps'] = RoadmapStep.objects.filter(is_featured=True).order_by('-start_date', 'order')[:8]
        context['certifications'] = Certification.objects.filter(is_featured=True).order_by('-issue_date', 'order')[:6]
        context['contact_form'] = ContactForm()
        context['message_sent'] = False
        
        # Statistiques
        context['total_projects'] = Project.objects.count()
        context['total_technologies'] = Technology.objects.count()
        # Années d'expérience (modifiable ici)
        context['total_experience'] = 3  # Changez ce nombre selon votre expérience
        context['total_certifications'] = Certification.objects.count()
        
        return context
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            your_name = form.cleaned_data['your_name']
            your_email = form.cleaned_data['your_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Sauvegarder le message en base
            ContactMessage.objects.create(
                name=your_name,
                email=your_email,
                subject=subject,
                message=message
            )

            email_body = f"Name: {your_name}\nEmail: {your_email}\nSubject: {subject}\n\n{message}"

            # Envoyer l'email
            try:
                send_mail(
                    f"Portfolio Contact: {subject}",
                    email_body,
                    your_email,
                    ['dzoubery@icloud.com'],
                    fail_silently=False,
                )
                message_sent = True
            except Exception as e:
                message_sent = True  # Message sauvé même si email échoue

            return JsonResponse({'status': 'success', 'message_sent': message_sent})
        else:
            errors = {field: form.errors[field][0] for field in form.errors}
            return JsonResponse({'status': 'error', 'errors': errors})

class DigitalCVPageView(TemplateView):
    template_name = 'portfolio/digital_cv.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        experiences = Experience.objects.all()

        for experience in experiences:
            descriptions = Description.objects.filter(experience=experience).order_by('order_number')
            experience.descriptions.set(descriptions)

        context['experiences'] = experiences
        context['personal'] = Personal.objects.all()
        context['education'] = Education.objects.all()
        context['technologies'] = Technology.objects.all()
        context['portfolio'] = Portfolio.objects.filter(
            Q(filter='filter-certification')
        )
        
        grouped_portfolio = {}
        portfolios = sorted(context['portfolio'], key=attrgetter('year'), reverse=True) 
        for item in portfolios:
            issuer_name = item.issuer.name if item.issuer else "Unknown Issuer"
            if issuer_name not in grouped_portfolio:
                grouped_portfolio[issuer_name] = []
            grouped_portfolio[issuer_name].append(item)

        context['grouped_portfolio'] = grouped_portfolio

        return context
    
    
# Nouvelles vues pour les fonctionnalités avancées
class BlogListView(ListView):
    model = BlogPost
    template_name = 'portfolio/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_queryset(self):
        return BlogPost.objects.filter(published=True)

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'portfolio/blog_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    
    def get_object(self):
        obj = super().get_object()
        obj.view_count += 1
        obj.save(update_fields=['view_count'])
        return obj

class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/project_list.html'
    context_object_name = 'projects'
    paginate_by = 9
    
    def get_queryset(self):
        return Project.objects.all()

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'

def handle_not_found(request, exception):
    return render(request, "layouts/page-404.html")

def toggle_theme(request):
    """Vue pour basculer entre les thèmes clair et sombre"""
    if request.method == 'POST':
        current_theme = request.session.get('theme', 'dark')
        new_theme = 'light' if current_theme == 'dark' else 'dark'
        request.session['theme'] = new_theme
        
        # Retourner une réponse JSON pour les requêtes AJAX
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'theme': new_theme,
                'icon': 'fas fa-sun' if new_theme == 'light' else 'fas fa-moon'
            })
        
        # Rediriger vers la page précédente pour les requêtes normales
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
    # Pour les requêtes GET, basculer le thème et rediriger
    current_theme = request.session.get('theme', 'dark')
    new_theme = 'light' if current_theme == 'dark' else 'dark'
    request.session['theme'] = new_theme
    return redirect(request.META.get('HTTP_REFERER', '/'))

def get_theme(request):
    """Vue pour obtenir le thème actuel"""
    theme = request.session.get('theme', 'dark')
    return JsonResponse({
        'theme': theme,
        'icon': 'fas fa-sun' if theme == 'light' else 'fas fa-moon'
    })

# Vues pour les listes complètes
class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/project_list.html'
    context_object_name = 'projects'
    paginate_by = 10
    
    def get_queryset(self):
        # Limiter à 10 projets maximum, ordonnés par date de création
        return Project.objects.filter(is_featured=True).order_by('-created_at')[:10]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Project.STATUS_CHOICES
        context['current_category'] = self.request.GET.get('category', '')
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'
    slug_field = 'id'
    slug_url_kwarg = 'id'

class BlogListView(ListView):
    model = BlogPost
    template_name = 'portfolio/blog_list.html'
    context_object_name = 'blog_posts'
    paginate_by = 6
    
    def get_queryset(self):
        return BlogPost.objects.filter(published=True).order_by('-created_at')

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'portfolio/blog_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class CertificationListView(ListView):
    model = Certification
    template_name = 'portfolio/certification_list.html'
    context_object_name = 'certifications'
    paginate_by = 9
    
    def get_queryset(self):
        return Certification.objects.filter(is_featured=True).order_by('-issue_date', 'order')

class CertificationDetailView(DetailView):
    model = Certification
    template_name = 'portfolio/certification_detail.html'
    context_object_name = 'certification'
    slug_field = 'id'
    slug_url_kwarg = 'id'

def download_cv_pdf(request):
    """
    Vue pour générer et télécharger le CV en PDF à partir du template HTML
    """
    try:
        # Récupérer les données nécessaires (exactement comme dans DigitalCVPageView)
        personal = Personal.objects.all()
        if not personal.exists():
            raise Http404("Informations personnelles non trouvées")
        
        education = Education.objects.all()
        experiences = Experience.objects.all()
        technologies = Technology.objects.all()
        
        # Grouper les portfolios par issuer (comme dans le CV digital)
        from django.db.models import Q
        portfolios = Portfolio.objects.all()
        grouped_portfolio = {}
        for portfolio in portfolios:
            issuer = portfolio.issuer if portfolio.issuer else "Autre"
            if issuer not in grouped_portfolio:
                grouped_portfolio[issuer] = []
            grouped_portfolio[issuer].append(portfolio)
        
        # Contexte pour le template (exactement comme le CV digital)
        context = {
            'personal': personal,
            'education': education,
            'experiences': experiences,
            'technologies': technologies,
            'grouped_portfolio': grouped_portfolio,
        }
        
        # Rendre le template HTML (optimisé pour A4)
        html_string = render_to_string('portfolio/cv_digital_perfect_pdf.html', context)
        
        # Créer le PDF avec xhtml2pdf
        pdf_buffer = BytesIO()
        pisa_status = pisa.CreatePDF(html_string, dest=pdf_buffer)
        pdf_buffer.seek(0)
        
        if pisa_status.err:
            raise Exception("Erreur lors de la génération PDF")
        
        # Créer la réponse HTTP
        response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="Donaldo_ZOUBERY_CV.pdf"'
        response['Content-Length'] = len(pdf_buffer.getvalue())
        
        return response
        
    except Exception as e:
        raise Http404(f"Erreur lors de la génération du PDF: {str(e)}")
    
