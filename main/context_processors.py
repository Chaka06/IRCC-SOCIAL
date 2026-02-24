from django.conf import settings


# Image de partage (réseaux sociaux) et favicon (URLs externes)
OG_IMAGE_URL = "https://images.radio-canada.ca/q_auto,w_700/v1/ici-info/16x9/sean-fraser-ministre-immigration-refugies-citoyennete.jpg"
FAVICON_URL = "https://drjob.ca/wp-content/uploads/2024/05/canada-leaf-600nw-589189172.jpg"


def seo(request):
    """Contexte pour le SEO : URL absolues pour partage et JSON-LD."""
    if not request:
        return {}
    base = request.build_absolute_uri('/').rstrip('/')
    static_prefix = (settings.STATIC_URL or 'static/').lstrip('/')
    return {
        'og_image_absolute': OG_IMAGE_URL,
        'logo_absolute': FAVICON_URL,
        'canonical_url': request.build_absolute_uri(request.path),
        'site_base_url': base,
    }
