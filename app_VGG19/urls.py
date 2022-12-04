from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('imp', views.imporet, name='imp'),
    path('import_img',views.import_img,name='import_img'),
]