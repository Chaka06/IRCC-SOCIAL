"""
Génération de PDF professionnels pour les candidatures d'immigration.
Style institutionnel inspiré des documents officiels (IRCC, gouvernement canadien).
"""
from io import BytesIO
import urllib.request
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image,
    PageBreak, Frame, PageTemplate
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib.colors import HexColor
from django.conf import settings
import os
from .models import CompanyInfo


# Couleurs officielles (IRCC / gouvernement canadien)
COLORS = {
    'ircc_blue': HexColor('#1B365D'),      # Bleu institutionnel
    'canada_red': HexColor('#C8102E'),     # Rouge canadien
    'text_dark': HexColor('#333333'),      # Texte principal
    'text_muted': HexColor('#555555'),     # Texte secondaire
    'border_light': HexColor('#DDDDDD'),   # Bordures légères
    'bg_header': HexColor('#F0F4F8'),      # Fond en-têtes section
    'bg_label': HexColor('#F8F9FA'),       # Fond colonne labels
    'white': HexColor('#FFFFFF'),
}


def _create_styles():
    """Crée les styles de paragraphe professionnels."""
    base = getSampleStyleSheet()
    
    return {
        'doc_title': ParagraphStyle(
            'DocTitle',
            parent=base['Heading1'],
            fontName='Helvetica-Bold',
            fontSize=16,
            leading=20,
            alignment=TA_CENTER,
            textColor=COLORS['ircc_blue'],
            spaceAfter=6,
            spaceBefore=0,
        ),
        'doc_subtitle': ParagraphStyle(
            'DocSubtitle',
            parent=base['Normal'],
            fontName='Helvetica',
            fontSize=11,
            leading=14,
            alignment=TA_CENTER,
            textColor=COLORS['text_muted'],
            spaceAfter=20,
            spaceBefore=0,
        ),
        'section_title': ParagraphStyle(
            'SectionTitle',
            parent=base['Heading2'],
            fontName='Helvetica-Bold',
            fontSize=11,
            leading=14,
            textColor=COLORS['ircc_blue'],
            spaceBefore=22,
            spaceAfter=10,
            leftIndent=0,
            rightIndent=0,
        ),
        'body': ParagraphStyle(
            'Body',
            parent=base['Normal'],
            fontName='Helvetica',
            fontSize=10,
            leading=14,
            textColor=COLORS['text_dark'],
            alignment=TA_JUSTIFY,
            spaceAfter=8,
            spaceBefore=0,
        ),
        'footer_note': ParagraphStyle(
            'FooterNote',
            parent=base['Normal'],
            fontName='Helvetica',
            fontSize=8,
            leading=11,
            textColor=COLORS['text_muted'],
            alignment=TA_CENTER,
            spaceAfter=0,
            spaceBefore=16,
            wordWrap='LTR',
        ),
        'company': ParagraphStyle(
            'Company',
            parent=base['Normal'],
            fontName='Helvetica',
            fontSize=8,
            leading=11,
            textColor=COLORS['text_muted'],
            alignment=TA_CENTER,
            spaceAfter=14,
            spaceBefore=0,
        ),
    }


def _cell_para(text, bold=False):
    """Crée un Paragraph pour cellule de tableau (retour à la ligne automatique)."""
    style = ParagraphStyle(
        'Cell',
        fontName='Helvetica-Bold' if bold else 'Helvetica',
        fontSize=9,
        leading=12,
        textColor=COLORS['text_dark'],
        wordWrap='LTR',
        leftIndent=0,
        rightIndent=0,
    )
    # Échapper les caractères spéciaux HTML
    safe = str(text).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return Paragraph(safe, style)


def _table_style_institutional():
    """Style de tableau institutionnel : bordures fines, padding généreux."""
    return [
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
        ('BACKGROUND', (0, 0), (0, -1), COLORS['bg_label']),
        ('BACKGROUND', (1, 0), (1, -1), COLORS['white']),
        ('TEXTCOLOR', (0, 0), (0, -1), COLORS['text_dark']),
        ('TEXTCOLOR', (1, 0), (1, -1), COLORS['text_dark']),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 0.5, COLORS['border_light']),
        ('BOX', (0, 0), (-1, -1), 0.5, COLORS['border_light']),
    ]


def _image_from_url(url, width=1.4*inch, height=0.75*inch):
    """Charge une image depuis une URL pour l'usage dans le PDF."""
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (compatible; IMIGATUS/1.0)'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = response.read()
        buf = BytesIO(data)
        img = Image(buf, width=width, height=height)
        return img
    except Exception:
        return None


def generate_pdf(application):
    """
    Génère un PDF professionnel de candidature d'immigration.
    Structure et style inspirés des documents officiels IRCC.
    """
    buffer = BytesIO()
    
    # Format A4, marges institutionnelles (25 mm)
    margin = 25 * mm
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        leftMargin=margin,
        rightMargin=margin,
        topMargin=margin,
        bottomMargin=margin,
    )
    
    styles = _create_styles()
    company_info = CompanyInfo.objects.first()
    
    story = []
    
    # ----- En-tête document : logos (gauche = organisation, droite = ministère) -----
    logo_org_url = "https://ircc.com/wp-content/uploads/2024/01/IRCC-Png-Logo.png"
    logo_ministere_url = "https://upload.wikimedia.org/wikipedia/commons/c/c7/Citizenship_and_Immigration_Canada_Logo.png"
    
    logo_org = _image_from_url(logo_org_url, width=1.0*inch, height=0.5*inch)
    logo_ministere = _image_from_url(logo_ministere_url, width=2.8*inch, height=0.65*inch)
    
    header_cells = []
    if logo_org:
        header_cells.append(logo_org)
    else:
        header_cells.append("")
    if logo_ministere:
        header_cells.append(logo_ministere)
    else:
        header_cells.append("")
    
    if logo_org or logo_ministere:
        header_table = Table([header_cells], colWidths=[doc.width / 2, doc.width / 2])
        header_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (0, 0), 'LEFT'),
            ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        story.append(header_table)
        story.append(Spacer(1, 16))
    
    story.append(Paragraph(
        "Demande d'immigration au Canada / Canadian Immigration Application",
        styles['doc_title']
    ))
    
    if company_info:
        company_text = f"{company_info.company_name}<br/>"
        company_text += f"{company_info.address} &nbsp;·&nbsp; Tél: {company_info.phone} &nbsp;·&nbsp; {company_info.email}"
        story.append(Paragraph(company_text, styles['company']))
    
    story.append(Spacer(1, 8))
    
    # Référence candidature
    ref_para = Paragraph(
        f"<b>Réf. / Reference:</b> IMIG-{application.id:06d} &nbsp;&nbsp; "
        f"<b>Date:</b> {application.created_at.strftime('%d/%m/%Y %H:%M')}",
        styles['body']
    )
    story.append(ref_para)
    story.append(Spacer(1, 20))
    
    # ----- Section 1 : Informations personnelles -----
    story.append(Paragraph(
        "1. Informations personnelles / Personal Information",
        styles['section_title']
    ))
    
    personal_data = [
        [_cell_para('Nom de famille / Surname', bold=True), _cell_para(application.last_name)],
        [_cell_para('Prénom(s) / Given name(s)', bold=True), _cell_para(application.first_name)],
        [_cell_para('Date de naissance / Date of birth', bold=True), _cell_para(application.birth_date.strftime('%d/%m/%Y'))],
        [_cell_para('Lieu de naissance / Place of birth', bold=True), _cell_para(application.birth_place)],
        [_cell_para('Taille / Height', bold=True), _cell_para(f"{application.height} cm")],
        [_cell_para('Poids / Weight', bold=True), _cell_para(f"{application.weight} kg")],
        [_cell_para('Situation matrimoniale / Marital status', bold=True), _cell_para(application.get_marital_status_display())],
        [_cell_para('Profession / Profession', bold=True), _cell_para(application.profession or '-')],
    ]
    
    # Largeurs colonnes : labels 35%, valeurs 65% (plus d'espace pour texte long)
    page_width = A4[0] - 2 * margin
    col_label = page_width * 0.35
    col_value = page_width * 0.65
    
    personal_table = Table(personal_data, colWidths=[col_label, col_value])
    personal_table.setStyle(TableStyle(_table_style_institutional()))
    story.append(personal_table)
    story.append(Spacer(1, 4))
    
    # ----- Section 2 : Contact -----
    story.append(Paragraph(
        "2. Informations de contact / Contact Information",
        styles['section_title']
    ))
    
    contact_data = [
        [_cell_para('Adresse complète / Complete address', bold=True), _cell_para(application.address)],
        [_cell_para('Pays de résidence / Country of residence', bold=True), _cell_para(application.country_of_residence)],
        [_cell_para('Téléphone / Phone number', bold=True), _cell_para(application.phone)],
    ]
    
    contact_table = Table(contact_data, colWidths=[col_label, col_value])
    contact_table.setStyle(TableStyle(_table_style_institutional()))
    story.append(contact_table)
    story.append(Spacer(1, 4))
    
    # ----- Section 3 : Famille -----
    story.append(Paragraph(
        "3. Informations familiales / Family Information",
        styles['section_title']
    ))
    
    family_data = [
        [_cell_para("Nom du père / Father's name", bold=True), _cell_para(application.father_name)],
        [_cell_para("Nom de la mère / Mother's name", bold=True), _cell_para(application.mother_name)],
    ]
    
    family_table = Table(family_data, colWidths=[col_label, col_value])
    family_table.setStyle(TableStyle(_table_style_institutional()))
    story.append(family_table)
    story.append(Spacer(1, 20))
    
    # ----- Déclaration -----
    story.append(Paragraph(
        "4. Déclaration / Declaration",
        styles['section_title']
    ))
    
    decl_fr = (
        "Je soussigné(e), <b>%s %s</b>, déclare que les renseignements fournis dans la présente "
        "demande sont exacts et complets. J’accepte que toute fausse déclaration pourrait entraîner "
        "le rejet de ma demande ou des mesures légales."
    ) % (application.first_name, application.last_name)
    
    decl_en = (
        "I, <b>%s %s</b>, declare that the information provided in this application is true and complete. "
        "I understand that any misrepresentation may result in refusal of my application or legal action."
    ) % (application.first_name, application.last_name)
    
    story.append(Paragraph(decl_fr, styles['body']))
    story.append(Spacer(1, 8))
    story.append(Paragraph(decl_en, styles['body']))
    story.append(Spacer(1, 20))
    
    # ----- Pièce d'identité (recto / verso) -----
    if application.id_document_recto or application.id_document_verso:
        story.append(Paragraph(
            "5. Pièce d'identité / Identity Document",
            styles['section_title']
        ))
        img_width = 2.2 * inch
        img_height = 1.5 * inch
        
        def _load_id_image(image_field):
            if not image_field:
                return _cell_para('Non fourni', bold=True)
            try:
                img_path = os.path.join(settings.MEDIA_ROOT, str(image_field))
                if os.path.exists(img_path):
                    return Image(img_path, width=img_width, height=img_height)
            except Exception:
                pass
            return _cell_para('Non disponible', bold=True)
        
        id_row = [
            _load_id_image(application.id_document_recto),
            _load_id_image(application.id_document_verso),
        ]
        id_table = Table([id_row], colWidths=[(col_label + col_value) / 2] * 2)
        id_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (0, 0), 'CENTER'),
            ('ALIGN', (1, 0), (1, 0), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        labels_row = Table([
            [Paragraph("<b>Recto</b>", styles['body']), Paragraph("<b>Verso</b>", styles['body'])]
        ], colWidths=[(col_label + col_value) / 2] * 2)
        labels_row.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER')]))
        story.append(labels_row)
        story.append(Spacer(1, 4))
        story.append(id_table)
        story.append(Spacer(1, 20))
    
    # ----- Note de bas de page -----
    whatsapp = company_info.whatsapp_number if company_info else '+14373750615'
    note = (
        "Ce document constitue votre candidature officielle. Conservez-le et transmettez-le à notre "
        "équipe via WhatsApp pour la suite du processus."
    )
    if whatsapp:
        note += f" Contact: {whatsapp}"
    story.append(Paragraph(note, styles['footer_note']))
    story.append(Spacer(1, 24))
    
    # ----- Cachet de l'institution -----
    cachet_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'cachet_institution.png')
    if os.path.exists(cachet_path):
        cachet = Image(cachet_path, width=2.6*inch, height=1.4*inch)
        cachet.hAlign = 'CENTER'
        story.append(cachet)
    
    doc.build(story)
    buffer.seek(0)
    return buffer
