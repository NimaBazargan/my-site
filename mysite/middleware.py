from django.shortcuts import redirect
from django.conf import settings

class ComingSoonMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.startswith('/coming-soon/') and settings.COMING_SOON:
            return redirect('coming_soon')
        response = self.get_response(request)
        return response