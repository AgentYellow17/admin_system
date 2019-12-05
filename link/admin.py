from django.contrib import admin
from .models import Role, Link

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
  list_display = ('name', 'display_role')
admin.site.register(Role)
