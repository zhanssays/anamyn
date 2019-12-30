from django.urls import include, path
from rest_framework import routers
from .views import ChildViewSet, ProfileViewSet, PlanningChildViewSet, UserViewSet

app_name = "userapi"
router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'users', UserViewSet)
router.register(r'planningchild', PlanningChildViewSet)
router.register(r'child', ChildViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('userapi/', include(router.urls)),
]