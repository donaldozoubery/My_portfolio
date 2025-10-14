from django.contrib import admin
from .models import (
    Personal, About, Experience, Description, Technology, Education, Portfolio, 
    Issuing_Organization, Testimonial, BlogPost, Project, ContactMessage, SiteSettings, RoadmapStep, Certification
)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date', 'is_current')
    list_filter = ('is_current',)  # Add a filter for is_current field
    search_fields = ('title', 'company', 'start_date', 'end_date')  # Add search fields
    list_editable = ('is_current',)  # Allow editing is_current directly from the list view
    ordering = ('is_current',)

class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('text', 'experience', 'order_number')

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_position', 'client_company', 'is_featured', 'created_at')
    list_filter = ('is_featured', 'created_at')
    search_fields = ('client_name', 'client_company', 'client_position')
    list_editable = ('is_featured',)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'created_at', 'updated_at')
    list_filter = ('published', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'author')
    list_editable = ('published',)
    prepopulated_fields = {'slug': ('title',)}

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'status', 'is_featured', 'start_date', 'end_date')
    list_filter = ('category', 'status', 'is_featured', 'start_date', 'end_date')
    search_fields = ('name', 'description', 'technologies')
    list_editable = ('category', 'status', 'is_featured')
    filter_horizontal = ('technologies',)
    fieldsets = (
        ('Informations générales', {
            'fields': ('name', 'description', 'short_description', 'category')
        }),
        ('Image', {
            'fields': ('featured_image',)
        }),
        ('Technologies', {
            'fields': ('technologies',)
        }),
        ('Statut et dates', {
            'fields': ('status', 'is_featured', 'start_date', 'end_date')
        }),
        ('Liens', {
            'fields': ('github_url', 'live_url', 'demo_url'),
            'classes': ('collapse',)
        }),
    )

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_editable = ('is_read',)

class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_title', 'site_description', 'is_maintenance_mode', 'contact_email')
    list_editable = ('is_maintenance_mode',)

class RoadmapStepAdmin(admin.ModelAdmin):
    list_display = ('title', 'step_type', 'start_date', 'end_date', 'is_current', 'is_featured', 'order')
    list_filter = ('step_type', 'is_current', 'is_featured', 'start_date')
    search_fields = ('title', 'description')
    list_editable = ('is_current', 'is_featured', 'order')
    filter_horizontal = ('skills',)
    fieldsets = (
        ('Informations générales', {
            'fields': ('title', 'description', 'step_type', 'icon', 'color')
        }),
        ('Dates et statut', {
            'fields': ('start_date', 'end_date', 'is_current', 'is_featured', 'order')
        }),
        ('Contenu enrichi', {
            'fields': ('image', 'external_link', 'skills'),
            'classes': ('collapse',)
        }),
    )

# Enregistrement des modèles dans l'admin
admin.site.register(Portfolio)
admin.site.register(Personal)
admin.site.register(About)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Description, DescriptionAdmin)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'skill_level', 'category', 'is_featured')
    list_filter = ('category', 'is_featured', 'skill_level')
    search_fields = ('name',)
    list_editable = ('skill_level', 'is_featured')
    fieldsets = (
        ('Informations générales', {
            'fields': ('name', 'icon', 'category')
        }),
        ('Compétence', {
            'fields': ('skill_level', 'is_featured')
        }),
        ('Image', {
            'fields': ('photo',),
            'classes': ('collapse',)
        }),
    )

admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Education)
admin.site.register(Issuing_Organization)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(SiteSettings, SiteSettingsAdmin)
admin.site.register(RoadmapStep, RoadmapStepAdmin)

class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuing_organization', 'issue_date', 'expiry_date', 'is_featured', 'is_verified', 'order', 'status')
    list_filter = ('is_featured', 'is_verified', 'issue_date', 'expiry_date')
    search_fields = ('title', 'issuing_organization', 'credential_id')
    list_editable = ('is_featured', 'is_verified', 'order')
    filter_horizontal = ('skills',)
    fieldsets = (
        ('Informations générales', {
            'fields': ('title', 'issuing_organization', 'description')
        }),
        ('Détails du certificat', {
            'fields': ('credential_id', 'credential_url', 'image')
        }),
        ('Dates', {
            'fields': ('issue_date', 'expiry_date')
        }),
        ('Configuration', {
            'fields': ('is_featured', 'is_verified', 'order')
        }),
        ('Compétences', {
            'fields': ('skills',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('status',)

admin.site.register(Certification, CertificationAdmin)