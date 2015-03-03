'''urls del esta app'''
from django.conf.urls import patterns, url
# from celular.views import Index, AdminMetaCell, AdminModCell, AdminCell
from celular.views import Index, AdminMetaCell, AdminModCell
from celular.views import AddMetaCell, AddModelCell
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('celular.views',
                       # Examples:
                       url(r'^$', Index.as_view()),
                       url(r'^meta_cell/$', AdminMetaCell.as_view()),
                       url(r'^meta_cell/agregar/$', AddMetaCell.as_view()),
                       url(r'^mod_cell/$', AdminModCell.as_view()),
                       url(r'^mod_cell/agregar/$', AddModelCell.as_view()),
                       # url(r'^celular/$', AdminCell.as_view()),
                       url(r'^agregar_cel_prod/$', 'cell_prod', name='cell_prod'),
                      )
