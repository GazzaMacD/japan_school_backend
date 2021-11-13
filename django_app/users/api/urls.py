from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users.api import views

app_name = "users"
urlpatterns = [
    path(
        "users/",
        views.CustomUserList.as_view(),
        name="api_user_list",
    ),
    path(
        "users/<uuid:uuid>/",
        views.CustomUserDetail.as_view(),
        name="api_user_detail",
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
