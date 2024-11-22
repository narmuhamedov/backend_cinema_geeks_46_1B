from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from main_page import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_lesson_django/', views.first_lesson_django, name='first_lesson_django'),
    path('image_link/', views.picture_view, name='picture_view'),
    path('', include('main_page.urls')),
    path('', include('hashtags.urls')),
    path('', include('todo.urls')),
    path('', include('cbv.urls')),
    path('', include('parsing_rezka.urls')),
    path('', include('users.urls')),
]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
