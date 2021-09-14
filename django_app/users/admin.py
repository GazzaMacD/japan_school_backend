from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'name', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name', )}),
        ('Permissions', {'fields': ('is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active')}
        ),
    )
    search_fields = ('email', 'name')
    ordering = ('email',)

    def get_fieldsets(self, request, obj=None):
        '''
        This will add fields to fielsets dynamically based on superuser status
        '''
        if not obj:
            return self.add_fieldsets
        fieldsets = super(CustomUserAdmin, self).get_fieldsets(request, obj)
        if request.user.is_superuser:
            # add fields to first (None) fieldset
            fieldsets[0][1]['fields'] = ('email', 'password', 'name','role',)
            # add fields to Permissions fieldset
            fieldsets[1][1]['fields'] = ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)
        return fieldsets


admin.site.register(CustomUser, CustomUserAdmin)
