from django.contrib import admin

# Register your models here para que aparezcan en el admin.

from .models import SpacexItem

admin.site.register(SpacexItem)
