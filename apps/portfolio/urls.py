from django.urls import path
from .views import (
    HomePageView, DigitalCVPageView, BlogListView, BlogDetailView,
    ProjectListView, ProjectDetailView, CertificationListView, CertificationDetailView,
    download_cv_pdf
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('digital_cv/', DigitalCVPageView.as_view(), name='digital_cv'),
    path('download-cv/', download_cv_pdf, name='download_cv_pdf'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('certifications/', CertificationListView.as_view(), name='certification_list'),
    path('certifications/<int:pk>/', CertificationDetailView.as_view(), name='certification_detail'),
]
