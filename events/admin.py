from django.contrib import admin
from .models import Event
# Register your models here.
@admin.register(Event)
class eventAdmin(admin.ModelAdmin):
    list_display=('title','state','category')
    list_filter=('title','state','category')
    list_per_page=2
    ordering=('title','state','category')
    search_fields=['title']
#pass
#admin.site.register(Event,eventAdmin)