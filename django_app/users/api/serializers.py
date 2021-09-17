from rest_framework import serializers

from  users.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=CustomUser.Role.choices) 
    role_display = serializers.CharField(
        source='get_role_display',
        read_only=True
        )

    class Meta:
        model = CustomUser 
        fields = ['uuid', 'email', 'name', 'role', 'role_display', 'is_staff', 'is_active', 'date_joined']
