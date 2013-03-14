from django.http import HttpResponseForbidden
from django.template.loader import render_to_string
from uganda_common.models import Access

__author__ = 'kenneth'



class AccessMiddleWare(object):


    def process_request(self, request):
        if request.user.is_authenticated() and Access.denied(request):
            return HttpResponseForbidden(render_to_string('403.html'))
        return None