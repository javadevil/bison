from django.contrib import admin
from contact.models import Contact,Tel
# Register your models here.
class TelInline(admin.TabularInline):
	model = Tel

class ContactAdmin(admin.ModelAdmin):
	inlines = [
		TelInline,
	]
admin.site.register(Contact,ContactAdmin)