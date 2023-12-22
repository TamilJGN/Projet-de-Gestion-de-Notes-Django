from django import forms
from .models import Matiere, Etudiant, Notation

class MatiereForm(forms.ModelForm):
    class Meta:
        model = Matiere
        fields = ['nom_matiere', 'code_matiere']

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom_etudiant', 'prenom_etudiant', 'numero_etudiant']

class NotationForm(forms.ModelForm):
    class Meta:
        model = Notation
        fields = ['matiere', 'etudiant', 'note', 'date_notation']
