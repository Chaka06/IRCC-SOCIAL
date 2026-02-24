from django.db import models
from django.core.validators import RegexValidator

class PassportInfo(models.Model):
    """Modèle pour stocker les informations des passeports"""
    passport_number = models.CharField(
        max_length=20, 
        unique=True,
        validators=[RegexValidator(
            regex=r'^[A-Z]{2}[0-9]{6}$',
            message='Format du numéro de passeport : 2 lettres suivies de 6 chiffres (ex: NB442748)'
        )],
        verbose_name="Numéro de passeport"
    )
    first_name = models.CharField(max_length=100, verbose_name="Prénom")
    last_name = models.CharField(max_length=100, verbose_name="Nom")
    birth_place = models.CharField(max_length=200, verbose_name="Lieu de naissance")
    birth_date = models.DateField(verbose_name="Date de naissance")
    gender = models.CharField(
        max_length=1,
        choices=[('M', 'Masculin'), ('F', 'Féminin')],
        verbose_name="Sexe"
    )
    nationality = models.CharField(max_length=100, verbose_name="Nationalité")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Information de passeport"
        verbose_name_plural = "Informations de passeports"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.passport_number}"

class VisaInfo(models.Model):
    """Modèle pour stocker les informations des visas"""
    VISA_TYPE_CHOICES = [
        ('tourist', 'Touristique'),
        ('work', 'Travail'),
        ('student', 'Étudiant'),
        ('business', 'Affaires'),
        ('transit', 'Transit'),
        ('permanent', 'Résidence permanente'),
        ('other', 'Autre'),
    ]
    STATUS_CHOICES = [
        ('active', 'Actif'),
        ('expired', 'Expiré'),
        ('pending', 'En attente'),
        ('approved', 'Approuvé'),
    ]

    visa_number = models.CharField(
        max_length=30,
        unique=True,
        validators=[RegexValidator(
            regex=r'^[A-Z][0-9]{9}$',
            message='Format du numéro de visa : une lettre suivie de 9 chiffres (ex: E981296032)'
        )],
        verbose_name="Numéro de visa"
    )
    visa_type = models.CharField(
        max_length=20,
        choices=VISA_TYPE_CHOICES,
        verbose_name="Type de visa"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active',
        verbose_name="Statut"
    )
    first_name = models.CharField(max_length=100, verbose_name="Prénom")
    last_name = models.CharField(max_length=100, verbose_name="Nom")
    nationality = models.CharField(max_length=100, verbose_name="Nationalité")
    passport_number = models.CharField(max_length=20, verbose_name="Numéro de passeport")
    issue_date = models.DateField(verbose_name="Date de délivrance")
    expiry_date = models.DateField(verbose_name="Date d'expiration")
    birth_date = models.DateField(verbose_name="Date de naissance", blank=True, null=True)
    birth_place = models.CharField(max_length=200, verbose_name="Lieu de naissance", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Information de visa"
        verbose_name_plural = "Informations de visas"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.visa_number}"

    @property
    def is_expired(self):
        from django.utils import timezone
        return self.expiry_date < timezone.now().date()

class ImmigrationApplication(models.Model):
    """Modèle pour les candidatures d'immigration"""
    MARITAL_STATUS_CHOICES = [
        ('single', 'Célibataire'),
        ('married', 'Marié(e)'),
        ('divorced', 'Divorcé(e)'),
        ('widowed', 'Veuf/Veuve'),
        ('separated', 'Séparé(e)'),
    ]

    # Informations personnelles
    first_name = models.CharField(max_length=100, verbose_name="Prénom")
    last_name = models.CharField(max_length=100, verbose_name="Nom")
    birth_date = models.DateField(verbose_name="Date de naissance")
    birth_place = models.CharField(max_length=200, verbose_name="Lieu de naissance")
    height = models.PositiveIntegerField(verbose_name="Taille (cm)")
    weight = models.PositiveIntegerField(verbose_name="Poids (kg)")
    marital_status = models.CharField(
        max_length=20,
        choices=MARITAL_STATUS_CHOICES,
        verbose_name="Situation matrimoniale"
    )
    profession = models.CharField(max_length=200, verbose_name="Profession", blank=True)
    
    # Pièce d'identité
    id_document_recto = models.ImageField(
        upload_to='applications/id_recto/',
        blank=True,
        null=True,
        verbose_name="Pièce d'identité (recto)"
    )
    id_document_verso = models.ImageField(
        upload_to='applications/id_verso/',
        blank=True,
        null=True,
        verbose_name="Pièce d'identité (verso)"
    )
    
    # Adresse
    address = models.TextField(verbose_name="Adresse complète")
    country_of_residence = models.CharField(max_length=100, verbose_name="Pays de résidence")
    phone = models.CharField(
        max_length=20,
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message='Format de téléphone invalide'
        )],
        verbose_name="Téléphone"
    )
    
    # Parents
    father_name = models.CharField(max_length=200, verbose_name="Nom du père")
    mother_name = models.CharField(max_length=200, verbose_name="Nom de la mère")
    
    # Métadonnées
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pdf_generated = models.BooleanField(default=False, verbose_name="PDF généré")
    
    class Meta:
        verbose_name = "Candidature d'immigration"
        verbose_name_plural = "Candidatures d'immigration"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.created_at.strftime('%d/%m/%Y')}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class CompanyInfo(models.Model):
    """Modèle pour les informations de l'entreprise"""
    company_name = models.CharField(max_length=200, verbose_name="Nom de l'entreprise")
    address = models.TextField(verbose_name="Adresse")
    phone = models.CharField(max_length=20, verbose_name="Téléphone")
    email = models.EmailField(verbose_name="Email")
    whatsapp_number = models.CharField(max_length=20, verbose_name="Numéro WhatsApp")
    website = models.URLField(blank=True, verbose_name="Site web")
    logo = models.ImageField(upload_to='logos/', blank=True, verbose_name="Logo")
    
    class Meta:
        verbose_name = "Information de l'entreprise"
        verbose_name_plural = "Informations de l'entreprise"

    def __str__(self):
        return self.company_name