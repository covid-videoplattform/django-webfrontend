from django.urls import path

from . import views

app_name = 'rooms'
urlpatterns = [
    # ex: /rooms/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /rooms/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /rooms/5/print/
    path('<int:pk>/print/', views.PrintPDFView.as_view(), name='print_pdf'),
    # ex: /rooms/new/
    path('new/', views.new, name='new'),
]
