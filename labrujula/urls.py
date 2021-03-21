"""labrujula URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings

from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('inicio/', views.index, name='inicio'),
    path('streetart/', views.streetart, name="streetart"),
    path('crear-articulo/<str:title>/<str:content>/<str:public>', views.crear_articulo, name="crear_articulo"),
    path('articulo/', views.articulo, name="articulo"),
    path('editar-articulo/<int:id>', views.editar_articulo),
    path('articulos/', views.articulos, name="articulos"),
    path('borrar-articulo/<int:id>', views.borrar_articulo, name="borrar"),
    path('save-article/', views.save_article, name="save"),
    path('create-article/', views.create_article, name="create"),
    path('create-full-article/', views.create_full_article, name="create_full"),
    path('miradores/', views.miradores, name="miradores"),
    path('otros/', views.otros, name="otros"),
    path('iglesias/', views.iglesias, name="iglesias"),
    path('ascensores/', views.ascensores, name="ascensores"),
    path('escaleras/', views.escaleras, name="escaleras"),
    path('lecheros/', views.lecheros, name="lecheros"),
    path('cordillera/', views.cordillera, name="cordillera"),
    path('polanco/', views.polanco, name="polanco"),
    path('monjas/', views.monjas, name="monjas"),
    path('mariposas/', views.mariposas, name="mariposas"),
    path('florida/', views.florida, name="florida"),
    path('bellavista/', views.bellavista, name="bellavista"),
    path('yungay/', views.yungay, name="yungay"),
    path('sanjuandedios/', views.sanjuandedios, name="sanjuandedios"),
    path('carcel/', views.carcel, name="carcel"),
    path('panteon/', views.panteon, name="panteon"),
    path('alegre/', views.alegre, name="alegre"),
    path('concepcion/', views.concepcion, name="concepcion"),
    path('artilleria/', views.artilleria, name="artilleria"),
    path('playaancha/', views.playaancha, name="playaancha"),
    path('larrain/', views.larrain, name="larrain"),
    path('patrimonio/', views.patrimonio, name="patrimonio"),
    
]

# Configuración para cargar imágenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    