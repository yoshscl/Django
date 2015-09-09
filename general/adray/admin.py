from django.contrib import admin
from .models import testData,clientData,datelocationchannel,dateLocationResponse,geographyData
'''from general.adray.models import Author
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Author, AuthorAdmin)'''

admin.site.register(testData)
admin.site.register(clientData)
admin.site.register(datelocationchannel)
admin.site.register(dateLocationResponse)
admin.site.register(geographyData)