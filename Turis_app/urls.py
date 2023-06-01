from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('Not_found/', views.Not_found, name="Not"),
    path('about_page/', views.about_page, name="about"),
    path('contact', views.contact, name="contact"),
    path('destination_page/', views.destination_page, name="destination"),
    path('package_page/', views.package_page, name="package"),
    path('service_page/', views.service_page, name="service"),
    path('team_page/', views.team_page, name="team"),
    path('testimonial_page/', views.testimonial_page, name="testimonial"),
    path('blog_detail/<int:cat_id>/', views.blog_detail, name='blog_detail'),
]   