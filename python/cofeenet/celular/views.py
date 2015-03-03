from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType #only for index
from django.views.generic import View # I like class based views
from django.http import HttpResponse
from django.shortcuts import render
from celular.models import MetaCell, ModCell, Celular
from celular.forms import MetaCellForm, ModCellForm, CelularForm



def swap_spc_undscr(string):
    '''swaps between underscore and space of a given string'''
    space = ' '
    underscore = '_'
    fail = -1
    if string.find(space) is not fail:
        return string.replace(space, underscore)
    return string.replace(underscore, space)

# Create your views here.


class Index(View):
    models_of_this_app = ContentType.objects.filter(app_label = 'celular')
    title = 'admin of app celular'
    template = 'celular/index.html'

    def get(self, request):
        return render(request, self.template, {'models' : self.links_and_models(), 'title' : self.title})

    def links_and_models(self):
        return ((swap_spc_undscr(str(i)), i) for i in self.models_of_this_app)

class AdminMetaCell(View):
    model = MetaCell
    template = 'celular/ABC.html'
    model_name = model.__name__
    title = 'admin for {0}'.format(model_name)

    def get(self, request):
        return render(request, self.template, {'models' : self.lst_of_model(), 'title' : self.title, 'model_name': self.model_name})

    def lst_of_model(self):
        return self.model.objects.all()

class AdminModCell(AdminMetaCell):
    model = ModCell
    model_name = model.__name__
    title = 'admin for {0}'.format(model_name)

class AdminCell(AdminMetaCell): ## candidato a otra app
    model = Celular
    model_name = model.__name__
    title = 'admin for {0}'.format(model_name)

class AddMetaCell(View):
    title = 'agregar modelo de celular'
    form = MetaCellForm
    model = MetaCell
    template = 'celular/input_form.html'
    redirect_url = '/celular/meta_cell'

    def get(self, request):
        return render(request, self.template, {'form': self.form(), 'title': self.title})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ban = False
            for elem in cd:
                if elem:
                    break
            else:
                ban = True
            print ban
            if not ban and (cd['marca'] and cd['modelo']): #add more errors here
                self.model.objects.get_or_create(
                    marca = cd['marca'].lower(),
                    modelo = cd['modelo'].lower(),
                    alias = cd['alias'].lower())
                return HttpResponseRedirect(self.redirect_url)
        return render(request, self.template, {'form': form, 'title': self.title})

class AddModelCell(AddMetaCell):
    title = 'agregar modelo y color de celular'
    form = ModCellForm
    model = ModCell
    redirect_url = '/celular/mod_cell'

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            self.model.objects.get_or_create(
                codigo = cd['codigo'].lower(),
                modelo = cd['modelo'],
                color  = cd['color'].lower(),
                extras = cd['extras'].lower())
            return HttpResponseRedirect(self.redirect_url)
        return render(request, self.template, {'form': form, 'title': self.title})

def cell_prod(request):
    title = 'agregar modelo y color de celular'
    form = None
    if request.method == 'POST':
        form = CelularForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Celular.objects.get_or_create(
                codigo = cd['imei'].lower(),
                modelo = cd['modelo'])
    else:
        form = CelularForm()
    return render(request, 'celular/input_form.html', {'form': form, 'title': title})