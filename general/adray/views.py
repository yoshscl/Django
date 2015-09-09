from django.shortcuts import render,render_to_response
from adray.models import testDataForm, testData
from django.http import HttpResponse
from django.template import RequestContext, loader, Template
from django.db import models
from adray.test_object2 import test
from django.shortcuts import render_to_response
from formtools.wizard.views import WizardView
from django.db.models import get_app, get_models
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.core.context_processors import csrf

def index(request):
    template = loader.get_template('adray/home page.html')
    Channels_collection = ['You Tube', 'Google search', 'Google search']
    context = {'Channels_collection': Channels_collection}
    #return HttpResponse(template.render())
    return render(request, 'adray/home page.html', {'Channels_collection': Channels_collection})


def insert_data_form(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = testDataForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('adray/existing.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = testDataForm()
    return render(request, "adray/form.html", {'form': form})


def simulate(request):
  context = {'obj': testData.objects.all()}
  return render(request, 'adray/simulate.html', context)

def existing(request):
    data= testData.objects.all()
    myList=[1,2,3,4,5,6,7,8]
    for x in data:
      test1=test(x.TestName,x.StartDate,myList)
    #(test1.computeTestLenght())
    context = {'obj': testData.objects.all()}
    return render(request, 'adray/existing.html', context)


def specific_test(request,existing_test=None):
    return render(request, 'adray/test view.html',{'existing_test': existing_test})

def wizard(request):
    template = loader.get_template('adray/wizard example.html')
    return HttpResponse(template.render())

#for wizard
class ContactWizard(WizardView):
    def done(self, form_list, **kwargs):
        return render_to_response('done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })