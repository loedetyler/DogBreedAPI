from django.contrib import admin
from .models import Dog, Breed

class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'breed', 'breed_id', 'gender', 'color', 'favoritefood', 'favoritetoy')
    search_fields = ('name', 'breed', 'breed_id')
    list_filter = ('age', 'breed', 'breed_id')
    list_display_links = ('name',)
    fields = ('breed_id', 'name', 'age', 'breed')

admin.site.register(Dog, DogAdmin)
# Register your models here.

class BreedAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds')
    search_fields = ('name', 'size')
    list_filter = ('name', 'friendliness')
    list_display_links = ('name',)
    fields = ('name', 'size')
    
admin.site.register(Breed, BreedAdmin)
