from django.contrib import admin
from .models import Country, Category, Title


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Country, CountryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Title, TitleAdmin)