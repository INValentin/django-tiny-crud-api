from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from itemmanager.views import ItemViewset

router = DefaultRouter()

router.register(r'items', ItemViewset)



urlpatterns = [
    path('', include(router.urls)),
    path('token/', views.obtain_auth_token),
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]






