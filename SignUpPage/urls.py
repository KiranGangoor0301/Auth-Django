
from django.contrib import admin
from django.urls import path
from SignUpPage import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.signup,name='signup'),
    path('index',views.index,name='index'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('about',views.about,name='about'),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)


