from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from main_page import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_lesson_django/', views.first_lesson_django, name='first_lesson_django'),
    path('image_link/', views.picture_view, name='picture_view'),

]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
