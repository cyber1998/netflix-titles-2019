from django.contrib import admin
from .models import Country, Category, Title

"""
To access the admin panel, it is mandatory in this project for you
to have a superuser account. If you have not done it yet,

then do: python manage.py createsuperuser
and follow along the prompt. After a superuser is created, you can
go to the /admin endpoint and see everything that is listed here.
"""


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Country, CountryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Title, TitleAdmin)