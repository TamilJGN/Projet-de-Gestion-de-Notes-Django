from django.shortcuts import render

def home(request):
    return render(request, 'home.html')



from django.shortcuts import render, redirect
from .models import Matiere, Etudiant, Notation
from .forms import MatiereForm, EtudiantForm, NotationForm

def liste_matieres(request):
    matieres = Matiere.objects.all()
    return render(request, 'liste_matieres.html', {'matieres': matieres})

def liste_etudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'liste_etudiants.html', {'etudiants': etudiants})

def liste_notations(request, etudiant_id):
    etudiant = Etudiant.objects.get(pk=etudiant_id)
    notations = Notation.objects.filter(etudiant=etudiant)
    moyenne_annuelle = calculer_moyenne_annuelle(etudiant)
    return render(request, 'liste_notations.html', {'etudiant': etudiant, 'notations': notations, 'moyenne_annuelle': moyenne_annuelle})

def calculer_moyenne_annuelle(etudiant):
    notations = Notation.objects.filter(etudiant=etudiant)
    total_notes = sum(n.note for n in notations)
    moyenne_annuelle = total_notes / len(notations) if len(notations) > 0 else 0
    return round(moyenne_annuelle, 2)
