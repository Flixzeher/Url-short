from django.shortcuts import render
from .models import ShortUrl
from .forms import CreateNewShortURL
from datetime import datetime
import random, string


# Create your views here.
def home(request):
    return render(request, "home.html")

def redirect(request, url):
    current_obj = ShortUrl.objects.filter(short_url=url)
    if len(current_obj) == 0:
        return render(request, 'pagenotfound.html')
    context = {'obj':current_obj[0]}
    return render(request, 'redirect.html', context)

def createShortURL(request):
    if request.method == 'POST':
        form = CreateNewShortURL(request.POST)
        if form.is_valid():
            original_website = form.cleaned_data['original_url']
            custom_short_url = form.cleaned_data.get('custom_short_url', '')

            # Validate custom short URL if provided
            if custom_short_url:
                if ShortUrl.objects.filter(short_url=custom_short_url).exists():
                    form.add_error('custom_short_url', 'This short URL is already taken.')
                else:
                    short_url = custom_short_url
            else:
                # Generate random characters for the short URL
                random_chars_list = list(string.ascii_letters)
                random_chars = ''.join(random.choice(random_chars_list) for _ in range(6))
                while ShortUrl.objects.filter(short_url=random_chars).exists():
                    random_chars = ''.join(random.choice(random_chars_list) for _ in range(6))
                short_url = random_chars

            if not form.errors:
                d = datetime.now()
                s = ShortUrl(original_url=original_website, short_url=short_url, time_date_created=d)
                s.save()
                return render(request, 'urlcreated.html', {'chars': short_url})
    
    else:
        form = CreateNewShortURL()

    context = {'form': form}
    return render(request, 'create.html', context)

        