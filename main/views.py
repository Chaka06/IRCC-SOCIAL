from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from django.db.models import Q
from .models import PassportInfo, VisaInfo, ImmigrationApplication, CompanyInfo
from .forms import ImmigrationApplicationForm
from .utils import generate_pdf
import json

def home(request):
    """Page d'accueil avec les vidéos publicitaires"""
    context = {
        'title': 'IMIGATUS - Services d\'Immigration Canadienne',
        'description': 'Votre partenaire de confiance pour l\'immigration au Canada'
    }
    return render(request, 'main/home.html', context)

def passport_checker(request):
    """Page de vérification des numéros de passeport"""
    if request.method == 'POST':
        passport_number = request.POST.get('passport_number', '').strip().upper()
        
        if passport_number:
            try:
                passport_info = PassportInfo.objects.get(passport_number=passport_number)
                context = {
                    'passport_info': passport_info,
                    'found': True,
                    'passport_number': passport_number
                }
            except PassportInfo.DoesNotExist:
                context = {
                    'found': False,
                    'passport_number': passport_number,
                    'error': 'Aucun passeport trouvé avec ce numéro.'
                }
        else:
            context = {
                'found': False,
                'error': 'Veuillez entrer un numéro de passeport valide.'
            }
        
        return render(request, 'main/passport_checker.html', context)
    
    return render(request, 'main/passport_checker.html', {'title': 'Vérification de Passeport'})

def visa_checker(request):
    """Page de vérification des numéros de visa"""
    if request.method == 'POST':
        visa_number = request.POST.get('visa_number', '').strip().upper()
        
        if visa_number:
            try:
                visa_info = VisaInfo.objects.get(visa_number=visa_number)
                context = {
                    'visa_info': visa_info,
                    'found': True,
                    'visa_number': visa_number
                }
            except VisaInfo.DoesNotExist:
                context = {
                    'found': False,
                    'visa_number': visa_number,
                    'error': 'Aucun visa trouvé avec ce numéro.'
                }
        else:
            context = {
                'found': False,
                'error': 'Veuillez entrer un numéro de visa valide.'
            }
        
        return render(request, 'main/visa_checker.html', context)
    
    return render(request, 'main/visa_checker.html', {'title': 'Vérification de Visa'})

def application_form(request):
    """Formulaire de candidature d'immigration"""
    if request.method == 'POST':
        form = ImmigrationApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()
            messages.success(request, 'Votre candidature a été soumise avec succès!')
            return redirect('application_success', application_id=application.id)
    else:
        form = ImmigrationApplicationForm()
    
    context = {
        'form': form,
        'title': 'Formulaire de Candidature'
    }
    return render(request, 'main/application_form.html', context)

def application_success(request, application_id):
    """Page de succès après soumission du formulaire"""
    application = get_object_or_404(ImmigrationApplication, id=application_id)
    
    context = {
        'application': application,
        'title': 'Candidature Soumise'
    }
    return render(request, 'main/application_success.html', context)

def generate_application_pdf(request, application_id):
    """Génération du PDF de candidature"""
    application = get_object_or_404(ImmigrationApplication, id=application_id)
    
    try:
        # Générer le PDF
        pdf_buffer = generate_pdf(application)
        
        # Marquer comme généré
        application.pdf_generated = True
        application.save()
        
        # Retourner le PDF
        response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="candidature_{application.full_name.replace(" ", "_")}.pdf"'
        return response
        
    except Exception as e:
        messages.error(request, f'Erreur lors de la génération du PDF: {str(e)}')
        return redirect('application_success', application_id=application_id)

def whatsapp_redirect(request, application_id):
    """Redirection vers WhatsApp"""
    application = get_object_or_404(ImmigrationApplication, id=application_id)
    
    try:
        company_info = CompanyInfo.objects.first()
        whatsapp_number = (company_info.whatsapp_number if company_info else '+14373750615').replace('+', '').replace(' ', '')
        message = f"Bonjour, j'ai soumis ma candidature d'immigration (ID: {application.id}) et j'aimerais discuter de la suite du processus."
        whatsapp_url = f"https://wa.me/{whatsapp_number}?text={message}"
        return redirect(whatsapp_url)
    except Exception as e:
        messages.error(request, 'Erreur lors de la redirection WhatsApp.')
        return redirect('application_success', application_id=application_id)

def about(request):
    """Page À propos"""
    context = {
        'title': 'À Propos - IMIGATUS'
    }
    return render(request, 'main/about.html', context)

def services(request):
    """Page Services"""
    context = {
        'title': 'Nos Services - IMIGATUS'
    }
    return render(request, 'main/services.html', context)

def contact(request):
    """Page Contact"""
    company_info = CompanyInfo.objects.first()
    # Valeurs par défaut si aucune fiche entreprise en base
    contact_email = company_info.email if company_info else 'no-replay@ircc-social.com'
    contact_whatsapp = company_info.whatsapp_number if company_info else '+14373750615'
    contact_whatsapp_clean = contact_whatsapp.replace('+', '').replace(' ', '')
    context = {
        'title': 'Contact - IMIGATUS',
        'company_info': company_info,
        'contact_email': contact_email,
        'contact_whatsapp': contact_whatsapp,
        'contact_whatsapp_clean': contact_whatsapp_clean,
    }
    return render(request, 'main/contact.html', context)

def procedure(request):
    """Page Procédure"""
    context = {
        'title': 'Procédure d\'Immigration - IRCC'
    }
    return render(request, 'main/procedure.html', context)