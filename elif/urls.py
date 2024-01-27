from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.login_page, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    # path("search/", views.search_view, name="search"),
    path("logout/", views.logout_view, name="logout"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
