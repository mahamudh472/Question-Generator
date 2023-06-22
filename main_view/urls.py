from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),
    path('add_question', views.add_question, name="add"),
    path('view_question', views.view_question, name="view"),
    path('generate', views.generate, name='generate'),
    path('login', views.Login, name="login"),
    path('logout', views.Logout, name="logout")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)