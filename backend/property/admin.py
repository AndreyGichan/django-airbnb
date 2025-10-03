from django.contrib import admin
from django import forms

from .models import Property, Reservation
from .supabase_utils import upload_image_to_supabase


class PropertyAdminForm(forms.ModelForm):
    image_file = forms.ImageField(required=False)

    class Meta:
        model = Property
        fields = (
            "title", "description", "price_per_night", "bedrooms", "bathrooms",
            "guests", "country", "country_code", "category", "landlord"
        )

class PropertyAdmin(admin.ModelAdmin):
    form = PropertyAdminForm
    readonly_fields = ("image_url",)

    def save_model(self, request, obj, form, change):
        image_file = request.FILES.get("image_file")
        if image_file:
            public_url = upload_image_to_supabase(image_file, image_file.name)
            obj.image_url = public_url
        super().save_model(request, obj, form, change)


admin.site.register(Property, PropertyAdmin)
admin.site.register(Reservation)