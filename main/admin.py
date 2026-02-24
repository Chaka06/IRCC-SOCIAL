from django.contrib import admin
from .models import PassportInfo, VisaInfo, ImmigrationApplication, CompanyInfo

@admin.register(PassportInfo)
class PassportInfoAdmin(admin.ModelAdmin):
    list_display = ['passport_number', 'first_name', 'last_name', 'birth_date', 'gender', 'created_at']
    list_filter = ['gender', 'nationality', 'created_at']
    search_fields = ['passport_number', 'first_name', 'last_name', 'birth_place']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Informations du passeport', {
            'fields': ('passport_number', 'nationality')
        }),
        ('Informations personnelles', {
            'fields': ('first_name', 'last_name', 'birth_date', 'birth_place', 'gender')
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(VisaInfo)
class VisaInfoAdmin(admin.ModelAdmin):
    list_display = ['visa_number', 'first_name', 'last_name', 'visa_type', 'status', 'expiry_date', 'created_at']
    list_filter = ['visa_type', 'status', 'nationality', 'created_at']
    search_fields = ['visa_number', 'first_name', 'last_name', 'passport_number']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Informations du visa', {
            'fields': ('visa_number', 'visa_type', 'status', 'issue_date', 'expiry_date')
        }),
        ('Informations personnelles', {
            'fields': ('first_name', 'last_name', 'nationality', 'passport_number', 'birth_date', 'birth_place')
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(ImmigrationApplication)
class ImmigrationApplicationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'birth_date', 'country_of_residence', 'marital_status', 'created_at', 'pdf_generated']
    list_filter = ['marital_status', 'country_of_residence', 'created_at', 'pdf_generated']
    search_fields = ['first_name', 'last_name', 'phone', 'father_name', 'mother_name']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Informations personnelles', {
            'fields': ('first_name', 'last_name', 'birth_date', 'birth_place', 'height', 'weight', 'marital_status')
        }),
        ('Contact et adresse', {
            'fields': ('address', 'country_of_residence', 'phone')
        }),
        ('Informations familiales', {
            'fields': ('father_name', 'mother_name')
        }),
        ('Statut', {
            'fields': ('pdf_generated',)
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'phone', 'email', 'whatsapp_number']
    
    def has_add_permission(self, request):
        # Permettre seulement une entrée
        return not CompanyInfo.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False