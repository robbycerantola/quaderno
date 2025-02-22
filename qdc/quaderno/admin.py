

# Register your models here.
# Registrazione modelli nell'admin
from django.contrib import admin
from .models import Campo, MezzoAgricolo, Operatore, Attivita, ProdottoFitosanitario, Trattamento, Operazione

admin.site.register(Campo)
admin.site.register(MezzoAgricolo)
admin.site.register(Operatore)
admin.site.register(Attivita)
admin.site.register(ProdottoFitosanitario)
admin.site.register(Trattamento)
admin.site.register(Operazione)
