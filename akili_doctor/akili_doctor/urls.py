from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('Account.urls')),
    path('streaks/', include('streaks.urls')),
    path('articles/', include('articles.urls')),
    path("chatbot/", include("chatbot.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)