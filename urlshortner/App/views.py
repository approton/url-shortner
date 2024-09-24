from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import URL
from django.views.decorators.csrf import csrf_exempt
import json

# Function to shorten URL via POST request
@csrf_exempt
def shorten_url(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        long_url = data.get('longUrl')

        if not long_url:
            return JsonResponse({'error': 'Invalid URL'}, status=400)

        # Check if the long URL already exists in the database
        url_obj, created = URL.objects.get_or_create(long_url=long_url)

        if created:
            # If it's new, generate a short URL
            url_obj.short_url = URL.generate_short_url()
            url_obj.save()

        short_url = request.build_absolute_uri('/') + url_obj.short_url
        return JsonResponse({'shortUrl': short_url})

    return JsonResponse({'error': 'Invalid request method'}, status=405)

# Function to handle redirection
def redirect_to_long_url(request, short_url):
    try:
        url_obj = URL.objects.get(short_url=short_url)
        return redirect(url_obj.long_url)
    except URL.DoesNotExist:
        return HttpResponse('URL not found', status=404)
    
def index(request):
    return render(request, 'index.html')