from django.urls import path
from . import views

urlpatterns = [
    path('matieres/', views.liste_matieres, name='liste_matieres'),
    path('etudiants/', views.liste_etudiants, name='liste_etudiants'),
    path('etudiant/<int:etudiant_id>/', views.liste_notations, name='liste_notations'),
]
