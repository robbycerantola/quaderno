
# Create your models here.
# Modelli per il quaderno di campagna
from django.db import models
from django.contrib.auth.models import User

class Campo(models.Model):
    nome = models.CharField(max_length=100)
    superficie = models.FloatField()  # Superficie in ettari
    varieta = models.CharField(max_length=100)
    posizione = models.TextField()
    coordinate_catastali = models.CharField(max_length=255, blank=True, null=True)
    latitudine = models.FloatField(blank=True, null=True)
    longitudine = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Parcele"

    def __str__(self):
        return self.nome
    
    def google_maps_link(self):
        if self.latitudine and self.longitudine:
            return f"https://www.google.com/maps/search/?api=1&query={self.latitudine},{self.longitudine}"
        return ""

class MezzoAgricolo(models.Model):
    nome = models.CharField(max_length=100)
    modello = models.CharField(max_length=100)
    targa = models.CharField(max_length=50, unique=True)
    note = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Mijloace agricole"
    
    def __str__(self):
        return f"{self.nome} ({self.modello})"

class Operatore(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    ruolo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Operatori"

    def __str__(self):
        return f"{self.nome} {self.cognome} ({self.ruolo})"

class Operazione(models.Model):
     tipo = models.CharField(max_length=15)
     descrizione = models.TextField(blank=True, null=True)
 
     class Meta:
        verbose_name_plural = "Operatii"
     
     def __str__(self):
        return self.tipo  	

class Attivita(models.Model):   
    STATUS_CHOICES = [
		('todo','DeFacut'),
		('pending','InExecutie'),
		('done','Executat'),
		('delayed','Probleme'),
	]
    
    status = models.CharField(max_length=10, default= 'todo', choices=STATUS_CHOICES)
    campo = models.ForeignKey(Campo, on_delete=models.CASCADE)
    data = models.DateField()
    operazione = models.ForeignKey(Operazione, on_delete=models.SET_NULL, null=True)
    descrizione = models.TextField(null=True, blank=True) 
    responsabile = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    mezzo_agricolo = models.ForeignKey(MezzoAgricolo, on_delete=models.SET_NULL, null=True, blank=True)
    operatore = models.ForeignKey(Operatore, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Activitati"

    list_filter= [STATUS_CHOICES]
    
    def __str__(self):
        return f"{self.operazione} - {self.campo.nome} ({self.data}) - {self.operatore}"

class ProdottoFitosanitario(models.Model):
    nome = models.CharField(max_length=100)
    principio_attivo = models.CharField(max_length=100)
    tempo_carenza = models.IntegerField(help_text="Tempo di carenza in giorni")
    note = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Produse fitosanitare"

    def __str__(self):
        return self.nome

class Trattamento(models.Model):
    STATUS_CHOICES = [
        ('todo','DeFacut'),
        ('pending','InExecutie'),
        ('done','Executat'),
        ('delayed','Probleme'),
    ]

    status = models.CharField(max_length=10, default= 'todo', choices=STATUS_CHOICES)
    campo = models.ForeignKey(Campo, on_delete=models.CASCADE)
    prodotto = models.ForeignKey(ProdottoFitosanitario, on_delete=models.CASCADE)
    dose = models.FloatField(help_text="Dose in litri/ettaro")
    data = models.DateField()
    operatore = models.ForeignKey(Operatore, on_delete=models.SET_NULL, null=True)
    responsabile = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    class Meta:
        verbose_name_plural = "Tratamente"

    def __str__(self):
        return f"{self.prodotto.nome} su {self.campo.nome} ({self.data}) {self.operatore}"
