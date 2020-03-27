from django.urls import path

from . import views

app_name = 'rooms'
urlpatterns = [
    # ex: /
    path('appointments/', views.AppointmentIndexView.as_view(),
         name='appointment-index'),
    # ex: /appointments/5/
    path('appointments/<int:pk>/', views.AppointmentDetailView.as_view(),
         name='appointment-detail'),
    # ex: /appointments/5/print/
    path('appointments/<int:pk>/print/',
         views.AppointmentPrintPDFView.as_view(),
         name='appointment-print_pdf'),
    # ex: /appointments/new/
    path('appointments/new/', views.AppointmentCreate.as_view(),
         name='appointment-new'),
    # ex: /staff/
    path('staff/', views.StaffIndexView.as_view(),
         name='staff-index'),
    # ex: /staff/5/
    path('staff/<int:pk>/', views.StaffDetailView.as_view(),
         name='staff-detail'),
    # ex: /staff/5/print/
    path('staff/<int:pk>/print/', views.StaffPrintPDFView.as_view(),
         name='staff-print_pdf'),
    # ex: /staff/new/
    path('staff/new/', views.StaffCreate.as_view(),
         name='staff-new'),
]
