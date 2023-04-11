from django.contrib import admin
from .models import *

# admin.site.register(Pessoa)


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['nome','importancia']