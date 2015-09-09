from django.db import models
from django.forms import ModelForm
from django import forms
from django.shortcuts import render_to_response

class clientData(models.Model):
    clientID = models.CharField(max_length=30)
    clientName = models.CharField(max_length=30)
    registrationDate = models.DateField
    #logoImage = models.ImageField
    #?priror effect of roas anf latency?
    #availabel timing restrictions
    # potemtial regions
    # possible success metric
    # current available success metrics
    #is availabe spent for testing?
    #credentials= models.CharField(max_length=30)

    # Potential channels client would be interested in?

class datelocationchannel(models.Model):
    Date = models.DateField
    clientID = models.ForeignKey(clientData)
    clientName = models.CharField(max_length=30)
    channelName = models.CharField(max_length=30)
    locationID = models.CharField(max_length=30)
    locationName = models.CharField(max_length=30)
    costCount= models.CharField(max_length=30)
    maxbid =models.FloatField
    avgPosition =models.FloatField
    channeltag1=models.FloatField
    channeltag2=models.FloatField
    channeltag3=models.FloatField


class dateLocationResponse(models.Model): #to think if i want response type
    locationID = models.CharField(max_length=30)
    SuccessCount= models.CharField(max_length=30)
    Date = models.DateField
    clientID = models.ForeignKey(clientData)
    clientName = models.CharField(max_length=30)


class testData(models.Model): #some of it will be populated by client , some by client data and some by test class methods
    TestName = models.CharField(max_length=30)
    testId=models.IntegerField
    clientID = models.CharField(max_length=30)
    #clientID=models.ForeignKey(clientData)
    clientName = models.CharField(max_length=30)
   # selectedChannel= models.CharField(max_length=30) #this on is complicated, will involve many channels we might condense this into a string with commas
    testStatus= models.CharField(max_length=30) # to built a function within a table that computes that
    actionToDo =models.CharField(max_length=30) #cpuld be multiple channels & multiple actions
    successMetric=models.CharField(max_length=30)
    StartDate = models.DateField(max_length=30)
    endDate=models.DateField(max_length=30)
    significance= models.FloatField
    power= models.FloatField
    totalAvailableGeos=models.CharField(max_length=30)
    selectedGeos=models.CharField(max_length=30)
    spendDatabyGeo=models.FloatField
    salesDatabyGeo=models.FloatField
    estimationOfCost=models.FloatField
    estimationOfRoas=models.FloatField
    estimationOfVarRoas=models.FloatField

    def __str__(self):              # __unicode__ on Python 2
        return self.TestName

CHANNEL_CHOICES = (
    ('youtube', 'You_ Tube'),
    ('paid_search', 'Paid_Search'),
    )


class testDataForm(ModelForm):

    selectedChannel = forms.MultipleChoiceField(required=True,
        widget=forms.CheckboxSelectMultiple, choices=CHANNEL_CHOICES)
    class Meta:
        model = testData
        fields = ['TestName','StartDate','selectedChannel','actionToDo']

# entry data wizard
class DateForm(ModelForm):
    StartDate = models.DateField(max_length=30)
    class Meta:
        model = testData
        fields = ['StartDate']



#do i need another model with all data of geoJson data to map to location id?
#we may possibly save all poligons for zip codes cities, states or circle with lon lat, also DMA level
class geographyData(models.Model):
  geoID = models.CharField(max_length=30)
  granLevel= models.CharField(max_length=30)
  geoJson=models.CharField
  density=models.FloatField


'''#to think if this is a duplicate ?
class testdateDataArcive(models.Model):
     date=models.DateField(max_length=30)
     TestName = models.CharField(max_length=30)
     clientID = models.ForeignKey(clientData)
     clientName = models.CharField(max_length=30)
     selectedChannel= models.CharField(max_length=30) #this on is complicated, will involve many channels we might condense this into a string with commas
     testStatus= models.CharField(max_length=30)
     actionToDo =models.CharField(max_length=30)  #cpuld be multiple channels & multiple actions
     successMetric=models.CharField(max_length=30)
     StartDate = models.DateField(max_length=30)
     endDate=models.DateField(max_length=30)
     significance= models.DateField(max_length=30)
     power= models.DateField(max_length=30)
     totalAvailableGeos=models.CharField(max_length=30)
     selectedGeos=models.CharField(max_length=30)
     spendDatabyGeo=models.FloatField
     salesDatabyGeo=models.FloatField
     estimationOfCost=models.FloatField
     estimationOfRoas=models.FloatField
     estimationOfVarRoas=models.FloatField'''