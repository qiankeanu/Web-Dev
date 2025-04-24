from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from ai.views import greeting
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('skills/', include('skills.urls')),
    path('ai/', include('ai.urls')),
    path('users/', include('users.urls')),  # Add this line
    path('', greeting, name='greeting'),
    path('chat/', include('chat.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
