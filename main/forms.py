from django import forms
from .models import ImmigrationApplication

class ImmigrationApplicationForm(forms.ModelForm):
    class Meta:
        model = ImmigrationApplication
        fields = [
            'first_name', 'last_name', 'birth_date', 'birth_place',
            'height', 'weight', 'marital_status', 'profession', 'address',
            'country_of_residence', 'phone', 'father_name', 'mother_name',
            'id_document_recto', 'id_document_verso'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre prénom',
                'required': True
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre nom de famille',
                'required': True
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': True
            }),
            'birth_place': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ville, Pays',
                'required': True
            }),
            'height': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Taille en cm',
                'min': '100',
                'max': '250',
                'required': True
            }),
            'weight': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Poids en kg',
                'min': '30',
                'max': '200',
                'required': True
            }),
            'marital_status': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'profession': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Ingénieur, Médecin, Enseignant...',
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Adresse complète',
                'rows': 3,
                'required': True
            }),
            'country_of_residence': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Pays de résidence actuelle',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+1 234 567 8900',
                'required': True
            }),
            'father_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom complet du père',
                'required': True
            }),
            'mother_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom complet de la mère',
                'required': True
            }),
            'id_document_recto': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }),
            'id_document_verso': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }),
        }
        labels = {
            'first_name': 'Prénom *',
            'last_name': 'Nom de famille *',
            'birth_date': 'Date de naissance *',
            'birth_place': 'Lieu de naissance *',
            'height': 'Taille (cm) *',
            'weight': 'Poids (kg) *',
            'marital_status': 'Situation matrimoniale *',
            'profession': 'Profession',
            'address': 'Adresse complète *',
            'country_of_residence': 'Pays de résidence *',
            'phone': 'Numéro de téléphone *',
            'father_name': 'Nom du père *',
            'mother_name': 'Nom de la mère *',
            'id_document_recto': "Pièce d'identité (recto)",
            'id_document_verso': "Pièce d'identité (verso)",
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            # Nettoyer le numéro de téléphone
            phone = phone.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
            if not phone.startswith('+'):
                phone = '+' + phone
        return phone

    def clean_height(self):
        height = self.cleaned_data.get('height')
        if height and (height < 100 or height > 250):
            raise forms.ValidationError('La taille doit être entre 100 et 250 cm.')
        return height

    def clean_weight(self):
        weight = self.cleaned_data.get('weight')
        if weight and (weight < 30 or weight > 200):
            raise forms.ValidationError('Le poids doit être entre 30 et 200 kg.')
        return weight

