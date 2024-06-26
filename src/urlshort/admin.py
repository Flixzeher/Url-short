from django.contrib import admin
from .models import ShortUrl
# Register your models here.

admin.site.register(ShortUrl)

class ShortUrlAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_url', 'time_date_created')