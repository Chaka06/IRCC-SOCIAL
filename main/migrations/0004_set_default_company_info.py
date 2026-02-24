# Generated manually - Données de contact institution

from django.db import migrations


def create_default_company(apps, schema_editor):
    CompanyInfo = apps.get_model('main', 'CompanyInfo')
    if not CompanyInfo.objects.exists():
        CompanyInfo.objects.create(
            company_name='IRCC / IMIGATUS',
            address='5343 Dundas St W, Toronto, ON M9B 6K5, Canada',
            phone='+14373750615',
            email='no-replay@ircc-social.com',
            whatsapp_number='+14373750615',
            website='',
        )


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_add_profession_and_id_documents'),
    ]

    operations = [
        migrations.RunPython(create_default_company, noop),
    ]
