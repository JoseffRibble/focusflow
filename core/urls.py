from django.urls import include, path
from rest_framework.routers import DefaultRouter

import core.views.pages as pages
from core.views.role_view import RoleUpdateView
from core.views.team_view import TeamViewSet
from core.views.user_view import RegisterView
from core.views.task_view import TaskViewSet

router = DefaultRouter()
router.register(r"teams", TeamViewSet, basename="teams")
router.register(r"tasks", TaskViewSet, basename="tasks")

urlpatterns = [
    path("", pages.index, name="index"),
    path("api/register", RegisterView.as_view(), name="register"),
    path("api/users/<int:user_id>/role", RoleUpdateView.as_view(), name="set-role"),
    path("api/", include(router.urls)),
    path("api/tasks", TaskViewSet.as_view({"post": "create"}), name="get-tasks"),
]
