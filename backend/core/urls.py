from django.urls import include, path
from rest_framework.routers import DefaultRouter

import core.views.pages as pages
from core.views import LoginView, RegisterView, RoleUpdateView, TaskViewSet, TeamViewSet

router = DefaultRouter()
router.register(r"teams", TeamViewSet, basename="teams")
router.register(r"tasks", TaskViewSet, basename="tasks")

urlpatterns = [
    path("", pages.index, name="index"),
    path("api/register/", RegisterView.as_view(), name="register"),
    path("api/users/<int:user_id>/role", RoleUpdateView.as_view(), name="set-role"),
    path("api/", include(router.urls)),
    path("api/tasks", TaskViewSet.as_view({"post": "create"}), name="get-tasks"),
    # path("api/login/", LoginView.as_view(), name="login"),
    path("api/login/", LoginView.as_view(), name="login"),
]
