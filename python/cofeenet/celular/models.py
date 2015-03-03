'''models of celular'''
from django.db import models

# Create your models here.

class MetaCell(models.Model):
    '''para registrar los modelos sin color de un celular.
    (util para ver que productos son para ese modelo)'''
    marca = models.CharField(max_length=128, blank=True) # lg, nokia, etc
    modelo = models.CharField(max_length=128, blank=True) # 5036
    alias = models.CharField(max_length=128, blank=True) # c5

    def __unicode__(self):
        aux = ''
        if self.marca or self.modelo or self.alias:
            aux = 'celular {0} {1}{2}'.format(self.marca,
                                              self.modelo,
                                              self.alias and\
                                              '({0})'.format(self.alias) or\
                                              '')
        return aux

class ModCell(models.Model):
    '''modelo de celular'''
    codigo = models.CharField(max_length=20, blank=True) #verificar el tamano del codigo
    modelo = models.ForeignKey("MetaCell")
    color = models.CharField(max_length=15, blank=True)
    extras = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return '{0} color {1}'.format(self.modelo, self.color)

class Celular(models.Model):
    '''celular concreto de los que se venden'''
    imei = models.CharField(max_length=15, blank=True) #verificar el tamano de un imei
    modelo = models.ForeignKey("ModCell")

    def __unicode__(self):
        return '{0}'.format(self.modelo)
