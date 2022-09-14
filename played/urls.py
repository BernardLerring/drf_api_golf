from django.urls import path
from played import views

urlpatterns = [
    path('played/', views.PlayedList.as_view()),
    path('played/<int:pk>/', views.PlayedDetail.as_view())
]