from django.db import models

# Creation class

from django.db import models

class Matiere(models.Model):
    nom_matiere = models.CharField(max_length=100)
    code_matiere = models.CharField(max_length=20)

    class Meta:
        app_label = 'notes_app'

    def __str__(self):
        return self.nom_matiere

class Etudiant(models.Model):
    nom_etudiant = models.CharField(max_length=100)
    prenom_etudiant = models.CharField(max_length=100)
    numero_etudiant = models.CharField(max_length=20, unique=True)
    
    class Meta:
        app_label = 'notes_app'

    def __str__(self):
        return f"{self.nom_etudiant} {self.prenom_etudiant}"

class Notation(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    note = models.DecimalField(max_digits=5, decimal_places=2)
    date_notation = models.DateField()
    
    class Meta:
        app_label = 'notes_app'
        
    def __str__(self):
        return f"{self.etudiant} - {self.matiere} - {self.note}"

