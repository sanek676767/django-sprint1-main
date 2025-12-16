from django.urls import include, path

urlpatterns = [
    # Здесь в будущем могут быть стандартные или служебные URL
    # path('admin/', admin.site.urls),

    # URL-ы приложения — в конце
    path('pages/', include('pages.urls')),
    path('', include('blog.urls')),
]
