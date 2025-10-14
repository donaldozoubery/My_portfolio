from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
#from cloudinary.models import CloudinaryField

class Personal(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    role = models.TextField(max_length=500, blank=True, null=True)
    mini_description = models.TextField(max_length=500, blank=True, null=True)
    cv_description = models.TextField(max_length=500, blank=True, null=True)
    cv_link = models.URLField(blank=True, null=True)
    #photo = CloudinaryField('profile_pic/main')
    photo = models.ImageField(upload_to='profile_pics/main', blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    

    def __str__(self):
        return self.name
    
class About(models.Model):
    description = RichTextField(blank=True, null=True)
    #photo = CloudinaryField('profile_pic/about')
    photo = models.ImageField(upload_to='profile_pics/about', blank=True, null=True)
    
class Education(models.Model):
    school_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.CharField(max_length=7)  # Store as string in "MMM YYYY" format
    end_date = models.CharField(max_length=7, null=True, blank=True)  # Store as string in "MMM YYYY" format
    
    @property
    def formatted_start_date(self):
        # Check if the start_date is in the format "MONYYYY"
        if len(self.start_date) == 7:
            month = self.start_date[:3].capitalize()
            year = self.start_date[3:]
            return f"{month} {year}"
        return self.start_date

    @property
    def formatted_end_date(self):
        # Check if the end_date is in the format "MONYYYY"
        if len(self.end_date) == 7:
            month = self.end_date[:3].capitalize()
            year = self.end_date[3:]
            return f"{month} {year}"
        return self.end_date
    
    def __str__(self):
        return self.school_name
    
    class Meta:
        ordering = ['start_date']

    def date_range(self):
        return f"{self.formatted_start_date} - {self.formatted_end_date}"

    def formatted_start_date_as_date(self):
        # Convert the formatted start_date to a date object
        from datetime import datetime
        return datetime.strptime(self.formatted_start_date, "%b %Y")

    def formatted_end_date_as_date(self):
        # Convert the formatted end_date to a date object
        from datetime import datetime
        return datetime.strptime(self.formatted_end_date, "%b %Y")
    
class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.CharField(max_length=7)  # Store as string in "MMM YYYY" format
    end_date = models.CharField(max_length=7, null=True, blank=True)  # Store as string in "MMM YYYY" format
    is_current = models.BooleanField(default=False)
    technologies = models.ManyToManyField('Technology')
    
    @property
    def formatted_start_date(self):
        # Check if the start_date is in the format "MONYYYY"
        if len(self.start_date) == 7:
            month = self.start_date[:3].capitalize()
            year = self.start_date[3:]
            return f"{month} {year}"
        return self.start_date

    @property
    def formatted_end_date(self):
        # Check if the end_date is in the format "MONYYYY"
        if len(self.end_date) == 7:
            month = self.end_date[:3].capitalize()
            year = self.end_date[3:]
            return f"{month} {year}"
        return self.end_date
    
    def __str__(self):
        return self.title

class Description(models.Model):
    text = models.TextField()
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='descriptions')
    order_number = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.text
    
    class Meta:
        unique_together = ('experience', 'order_number')
        
        
class Issuing_Organization(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
        
class Portfolio(models.Model):
    FILTER_CHOICES = [
        ('filter-project', 'Project'),
        ('filter-certification', 'Certification'),
        ('filter-badge', 'Badge'),
    ]

    name = models.CharField(max_length=100)
    filter = models.CharField(max_length=50, choices=FILTER_CHOICES)
    issuer = models.ForeignKey(Issuing_Organization, on_delete=models.CASCADE, null=True, blank=True)
    year = models.CharField(max_length=4, null=True, blank=True)
    object_fit = models.CharField(max_length=100, null=True, blank=True)
    
    
    # def get_cloudinary_folder(self):
    #     if self.filter == 'filter-project':
    #         return 'portfolio/project'
    #     elif self.filter == 'filter-certification':
    #         return 'portfolio/certification'
    #     elif self.filter == 'filter-badge':
    #         return 'portfolio/badge'

    #photo = CloudinaryField(folder=get_cloudinary_folder)
    
    def get_upload_to(self, filename):
        if self.filter == 'filter-project':
            return 'portfolio/project/{}'.format(filename)
        elif self.filter == 'filter-certification':
            return 'portfolio/certification/{}'.format(filename)
        elif self.filter == 'filter-badge':
            return 'portfolio/badge/{}'.format(filename)
        
    photo = models.ImageField(upload_to=get_upload_to, blank=True, null=True)

    link1 = models.URLField(blank=True, null=True)
    link2 = models.URLField(blank=True, null=True)
    link3 = models.URLField(blank=True, null=True)  

    def __str__(self):
        return self.name

# Programming languages and tools
class Technology(models.Model):
    name = models.CharField(max_length=100)
    photo = models.URLField(blank=True, null=True)
    icon = models.CharField(max_length=50, default='fas fa-code', help_text="Icône FontAwesome (ex: fab fa-python)")
    skill_level = models.IntegerField(default=0, help_text="Niveau de compétence de 0 à 100")
    category = models.CharField(max_length=50, choices=[
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Base de données'),
        ('devops', 'DevOps'),
        ('mobile', 'Mobile'),
        ('other', 'Autre')
    ], default='other')
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_position = models.CharField(max_length=100)
    client_company = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField(default=5, help_text="Note de 1 à 5")
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.client_name} - {self.client_company}"

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = RichTextField()
    excerpt = models.TextField(max_length=300)
    featured_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    author = models.CharField(max_length=100, default="Donaldo ZOUBERY")
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=200, blank=True, help_text="Séparés par des virgules")
    view_count = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

class Project(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Terminé'),
        ('in_progress', 'En cours'),
        ('planned', 'Planifié'),
    ]
    
    CATEGORY_CHOICES = [
        ('web', 'Web'),
        ('mobile', 'Mobile'),
        ('desktop', 'Desktop'),
        ('devops', 'DevOps'),
        ('ai', 'Intelligence Artificielle'),
        ('other', 'Autre'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=300)
    featured_image = models.ImageField(upload_to='projects/', blank=True, null=True)
    technologies = models.ManyToManyField(Technology)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='web')
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    demo_url = models.URLField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"

class SiteSettings(models.Model):
    site_title = models.CharField(max_length=100, default="Donaldo ZOUBERY")
    site_description = models.TextField(default="Portfolio professionnel")
    hero_title = models.CharField(max_length=200, default="Développeur Full-Stack")
    hero_subtitle = models.TextField(default="Passionné par la création d'expériences digitales exceptionnelles")
    about_text = RichTextField(blank=True, null=True)
    contact_email = models.EmailField(default="contact@donaldozoubery.com")
    contact_phone = models.CharField(max_length=20, default="+261 34 00 000 00")
    address = models.CharField(max_length=200, default="Antananarivo, Madagascar")
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    cv_file = models.FileField(upload_to='documents/', blank=True, null=True)
    is_maintenance_mode = models.BooleanField(default=False)
    maintenance_message = models.TextField(default="Site en maintenance")
    
    class Meta:
        verbose_name = "Paramètres du site"
        verbose_name_plural = "Paramètres du site"
    
    def __str__(self):
        return "Paramètres du site"

class RoadmapStep(models.Model):
    """Modèle pour les étapes du parcours professionnel"""
    STEP_TYPES = [
        ('education', 'Formation'),
        ('experience', 'Expérience'),
        ('project', 'Projet'),
        ('achievement', 'Réalisation'),
        ('certification', 'Certification'),
        ('milestone', 'Étape importante'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Titre")
    description = models.TextField(verbose_name="Description")
    step_type = models.CharField(max_length=20, choices=STEP_TYPES, default='experience', verbose_name="Type d'étape")
    start_date = models.DateField(verbose_name="Date de début")
    end_date = models.DateField(blank=True, null=True, verbose_name="Date de fin")
    is_current = models.BooleanField(default=False, verbose_name="Étape actuelle")
    is_featured = models.BooleanField(default=False, verbose_name="Mise en avant")
    icon = models.CharField(max_length=50, default='fas fa-circle', verbose_name="Icône FontAwesome")
    color = models.CharField(max_length=7, default='#6366f1', verbose_name="Couleur (hex)")
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")
    skills = models.ManyToManyField(Technology, blank=True, verbose_name="Compétences associées")
    image = models.ImageField(upload_to='roadmap/', blank=True, null=True, verbose_name="Image")
    external_link = models.URLField(blank=True, null=True, verbose_name="Lien externe")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-start_date', 'order']
        verbose_name = "Étape du parcours"
        verbose_name_plural = "Étapes du parcours"
    
    def __str__(self):
        return f"{self.title} ({self.get_step_type_display()})"
    
    @property
    def duration(self):
        """Calculer la durée de l'étape"""
        if self.end_date:
            delta = self.end_date - self.start_date
            months = delta.days // 30
            if months >= 12:
                years = months // 12
                remaining_months = months % 12
                if remaining_months == 0:
                    return f"{years} an{'s' if years > 1 else ''}"
                else:
                    return f"{years} an{'s' if years > 1 else ''} {remaining_months} mois"
            else:
                return f"{months} mois"
        elif self.is_current:
            return "En cours"
        else:
            return "Durée non spécifiée"

# Certifications
class Certification(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre de la certification")
    issuing_organization = models.CharField(max_length=200, verbose_name="Organisme émetteur")
    credential_id = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID du certificat")
    credential_url = models.URLField(blank=True, null=True, verbose_name="URL du certificat")
    issue_date = models.DateField(verbose_name="Date d'obtention")
    expiry_date = models.DateField(blank=True, null=True, verbose_name="Date d'expiration")
    image = models.ImageField(upload_to='certifications/', blank=True, null=True, verbose_name="Image du certificat")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    skills = models.ManyToManyField(Technology, blank=True, verbose_name="Compétences associées")
    is_featured = models.BooleanField(default=True, verbose_name="Mise en avant")
    is_verified = models.BooleanField(default=True, verbose_name="Vérifiée")
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")
    
    class Meta:
        ordering = ['-issue_date', 'order']
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"
    
    def __str__(self):
        return f"{self.title} - {self.issuing_organization}"
    
    @property
    def is_expired(self):
        if self.expiry_date:
            from django.utils import timezone
            return timezone.now().date() > self.expiry_date
        return False
    
    @property
    def status(self):
        if self.is_expired:
            return "Expirée"
        elif self.expiry_date:
            from django.utils import timezone
            days_until_expiry = (self.expiry_date - timezone.now().date()).days
            if days_until_expiry <= 30:
                return "Expire bientôt"
        return "Valide"