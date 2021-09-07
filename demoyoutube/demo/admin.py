from django.contrib import admin
from demo.models.application import application
from demo.models.product import product
from demo.models.indication import indication
from demo.models.personne import Personne
from demo.models.app_type import app_type
from demo.models.region import region


from import_export.admin import ImportExportModelAdmin

@admin.register(application)
class applicationAdmin(ImportExportModelAdmin):
    pass

@admin.register(product)
class productAdmin(ImportExportModelAdmin):
    pass

@admin.register(indication)
class indicationAdmin(ImportExportModelAdmin):
    pass

@admin.register(Personne)
class personneAdmin(ImportExportModelAdmin):
    pass

@admin.register(app_type)
class app_typeAdmin(ImportExportModelAdmin):
    pass

@admin.register(region)
class regionAdmin(ImportExportModelAdmin):
    pass