from django.contrib import admin
from django import forms

from .models import User
from .supabase_utils import upload_image_to_supabase

class UserAdminForm(forms.ModelForm):
    avatar_file = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('email', 'name', 'avatar_file', 'is_staff', 'is_superuser', 'is_active')


class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm
    readonly_fields = ('avatar_url',)

    def save_model(self, request, obj, form, change):
        avatar_file = request.FILES.get("avatar_file")
        if avatar_file:
            public_url = upload_image_to_supabase(avatar_file, avatar_file.name)
            obj.avatar_url = public_url
        super().save_model(request, obj, form, change)

admin.site.register(User, UserAdmin)
