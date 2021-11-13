import json

from rest_framework import serializers
from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=CustomUser.Role.choices)
    role_display = serializers.CharField(source="get_role_display", read_only=True)

    class Meta:
        model = CustomUser
        fields = [
            "uuid",
            "email",
            "name",
            "role",
            "role_display",
            "is_staff",
            "is_active",
            "date_joined",
        ]

    def __new__(cls, *args, **kwargs):
        if kwargs.get("many", False) is True:
            context = kwargs.get("context", {})
            context.update({"has_many": True})
            kwargs.update({"context": context})
        return super().__new__(cls, *args, **kwargs)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if not self.context.get("has_many", False):
            choices = {
                "choices": json.dumps(
                    {f"{key}": f"{val}" for (key, val) in CustomUser.Role.choices}
                )
            }
            ret.update(choices)
        return ret
