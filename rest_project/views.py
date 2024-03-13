from django.shortcuts import redirect, get_object_or_404
from links.models import Link

def qr_redirect(request, link_id):
    link = get_object_or_404(Link, id=link_id)
    return redirect(link.link)
