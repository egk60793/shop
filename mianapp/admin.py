from django.contrib import admin
from mianapp.models import *
from django import forms


class NotebookCategoryChoiceField(forms.ModelChoiceField):
    pass


class SmartphoneCategoryChoiceField(forms.ModelChoiceField):
    pass


class NotebookAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return NotebookCategoryChoiceField(Category.objects.filter(slug='notebooks'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartphoneAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return NotebookCategoryChoiceField(Category.objects.filter(slug='smartphones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class CategoryAdmin(admin.ModelAdmin):
    pass


class CartProductAdmin(admin.ModelAdmin):
    pass


class CartAdmin(admin.ModelAdmin):
    pass


class CustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CartProduct, CartProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Customer, CustomerAdmin)
