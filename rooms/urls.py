from django.urls import path

from . import views

app_name = 'rooms'
urlpatterns = [
    # ex: /rooms/
    path('', views.index, name='index'),
    # ex: /rooms/5/
    path('<int:appointment_id>/', views.detail, name='detail'),
    # ex: /rooms/5/print/
    path('<int:appointment_id>/print/', views.print_pdf, name='print_pdf'),
    # ex: /rooms/new/
    path('new/', views.new, name='new'),
]
