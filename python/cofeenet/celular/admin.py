from django.contrib import admin
from celular.models import MetaCell, ModCell
from formsAdmin import MetaCellFormAdmin, ModCellFormAdmin
# Register your models here.

@admin.register(MetaCell)
class MetaCellAdmin(admin.ModelAdmin):
    form = MetaCellFormAdmin

@admin.register(ModCell)
class ModCellAdmin(admin.ModelAdmin):
    form = ModCellFormAdmin
