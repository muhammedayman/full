from django.db import router
from rest_framework import routers
from django.urls import path
from .views import TagView
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView
from django.conf import settings
from django.conf.urls.static import static

router = routers.SimpleRouter()
router.register(r'tags', TagView, basename='tag')
urlpatterns=[
    path('token',TokenObtainPairView.as_view(),name="refresh"),
    path('refresh',TokenRefreshView.as_view(),name="refresh")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls