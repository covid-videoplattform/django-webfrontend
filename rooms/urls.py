from django.urls import path

from . import views

app_name = 'rooms'
urlpatterns = [
    # ex: /rooms/
    path('', views.IndexView.as_view(), name='appointment-index'),
    # ex: /rooms/5/
    path('<int:pk>/', views.DetailView.as_view(), name='appointment-detail'),
    # ex: /rooms/5/print/
    path('<int:pk>/print/', views.PrintPDFView.as_view(), name='appointment-print_pdf'),
    # ex: /rooms/new/
    path('new/', views.AppointmentCreate.as_view(), name='appointment-new'),
]
