from django.contrib import admin
from .models import Pet

class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'colour', 'owner')
    readonly_fields = ('owner',)  # Optional: prevent editing

    def save_model(self, request, obj, form, change):
        if not obj.owner:  # only set owner if it’s not already set
            obj.owner = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Pet, PetAdmin)
