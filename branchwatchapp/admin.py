from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from branchwatchapp.models import CompanyBranch, Branch

class CompanyBranchAdmin(LeafletGeoAdmin):
    # You can specify which fields to display in the admin panel here
    list_display = ('Branch_Id', 'Branch_Name')
    search_fields = ['Branch_Id', 'Branch_Name']
    # ... any other customizations

class BranchAdmin(LeafletGeoAdmin):
    list_display = ('Branch_Id', 'Name')
    search_fields = ['Branch_Id', 'Name']

admin.site.register(CompanyBranch, CompanyBranchAdmin)

admin.site.register(Branch, BranchAdmin)