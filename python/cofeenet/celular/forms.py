from django import forms
from celular.models import MetaCell, ModCell, Celular

class MetaCellForm(forms.Form):
    marca = forms.CharField(max_length=128, required=False, help_text='LG, Nokia, etc')
    modelo = forms.CharField(max_length=128, required=False, help_text='kg800, ot410, etc')
    alias = forms.CharField(max_length=128, required=False, help_text='choco, moto E, L90, etc')

    class Meta:
        model = MetaCell

class ModCellForm(forms.Form):
    codigo = forms.CharField(max_length=20, required=False, help_text='el codigo de la cubierta')
    modelo = forms.ModelChoiceField(queryset=MetaCell.objects.all())
    color = forms.CharField(max_length=15, required=False, help_text='color (leer junto al imei)')
    extras = forms.CharField(max_length=100, required=False, help_text='tiene microchip, micro sd?')

    class Meta:
        model = ModCell

class CelularForm(forms.Form):
    imei = forms.CharField(max_length=15, required=False, help_text='codigo unico del celular')
    modelo = forms.ModelChoiceField(queryset=ModCell.objects.all())

    class Meta:
        model = Celular
