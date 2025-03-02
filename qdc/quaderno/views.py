# Create your views here.
# Views per la gestione del quaderno di campagna
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from quaderno.models import Campo, MezzoAgricolo, Operatore, Attivita, Trattamento
from django.utils.translation import gettext as _

def home(request):
    #return HttpResponse("Benvenuto nel Quaderno di Campagna")
	return render(request, 'base.html')
	
def lista_campi(request):
    campi = Campo.objects.all()
    return render(request, 'campi/lista_campi.html', {'campi': campi})

def lista_mezzi(request):
    mezzi = MezzoAgricolo.objects.all()
    return render(request, 'mezzi/lista_mezzi.html', {'mezzi': mezzi})

def lista_operatore(request):
    operatore = Operatore.objects.all()
    return render(request, 'operatore/lista_operatore.html', {'operatore': operatore})

def cambia_status_attivita(request, attivita_id):
    attivita = get_object_or_404(Attivita, id=attivita_id)
    nuovo_status = request.POST.get('status')
    if nuovo_status in dict(Attivita.STATUS_CHOICES):
        attivita.status = nuovo_status
        attivita.save()
    return redirect('lista_attivita')

def lista_trattamenti(request):
    status_filter = request.GET.get('status', '')
    operatore_filter = request.GET.get('operatore', '')
    trattamento = Trattamento.objects.all()
    
    if status_filter:
        trattamento = trattamento.filter(status=status_filter)
    if operatore_filter:
        trattamento = trattamento.filter(operatore__id=operatore_filter)
    
    return render(request, 'trattamenti/lista_trattamenti.html', {
        'trattamento': trattamento,
        'status_choices': Trattamento.STATUS_CHOICES,
        'operatore_list': Operatore.objects.all()
    })
	

def modifica_trattamento(request, trattamento_id):
    trattamento = get_object_or_404(Trattamento, id=trattamento_id)
    if request.method == 'POST':
        nuovo_status = request.POST.get('status')
        nuova_nota = request.POST.get('nota')
        if nuovo_status in dict(Trattamento.STATUS_CHOICES):
            trattamento.status = nuovo_status
        trattamento.nota = nuova_nota
        trattamento.save()
        return redirect('lista_trattamenti')
    return redirect('lista_trattamenti')

def modifica_attivita(request, attivita_id):
    attivita = get_object_or_404(Attivita, id=attivita_id)
    if request.method == 'POST':
        nuovo_status = request.POST.get('status')
        nuova_descrizione = request.POST.get('descrizione')
        if nuovo_status in dict(Attivita.STATUS_CHOICES):
            attivita.status = nuovo_status
        attivita.descrizione = nuova_descrizione
        attivita.save()
        return redirect('lista_attivita')
    return redirect('lista_attivita')
	
def lista_attivita(request):
    status_filter = request.GET.get('status', '')
    operatore_filter = request.GET.get('operatore', '')
    attivita = Attivita.objects.all()
    
    if status_filter:
        attivita = attivita.filter(status=status_filter)
    if operatore_filter:
        attivita = attivita.filter(operatore__id=operatore_filter)
    
    return render(request, 'attivita/lista_attivita.html', {
        'attivita': attivita,
        'status_choices': Attivita.STATUS_CHOICES,
        'operatore_list': Operatore.objects.all()
    })


def lista_attivita_semplice(request):
    status_filter = request.GET.get('status', '')
    operatore_filter = request.GET.get('operatore', '')
    attivita = Attivita.objects.all()
    
    if status_filter:
        attivita = attivita.filter(status=status_filter)
    if operatore_filter:
        attivita = attivita.filter(operatore__id=operatore_filter)
    
    return render(request, 'attivita/lista_attivita.html', {
        'attivita': attivita,
        'status_choices': Attivita.STATUS_CHOICES,
        'operatore_list': Operatore.objects.all()
    })
