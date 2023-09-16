from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path("", views.subscribeToNewsLetter, name="subscribeToNewsLetter"),
	path("success", views.success, name="success"),
	path("error", views.error, name="error"),
]
