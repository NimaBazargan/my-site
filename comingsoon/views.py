from django.shortcuts import render

def coming_soon_view(request):
    return render(request, 'coming_soon.html')