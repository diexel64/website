from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('libros/', views.libros, name='libros'),
    path('cuentos/', views.cuentos, name='cuentos'),
    path('cuentos/<str:historia>/', views.cuento, name='cuento'),
    path('cuentosvip/<str:historia>/', views.cuentovip, name='cuentovip'),
    path('mundo/', views.mundo, name='mundo'),
    path('mundo/mapas', views.mapas, name='mapas'),
    path('mundo/enciclopedia', views.enciclopedia, name='enciclopedia'),
    path('mundo/enciclopedia/<str:article>', views.enciclopedia_articulo, name='enciclopedia_articulo'),
    path('espacio-vip/', views.espacio_vip, name='espacio_vip'),
    path('espacio-vip/bienvenida', views.bienvenida, name='bienvenida'),
    path('espacio-vip/mi-cuenta', views.mi_cuenta, name='mi_cuenta'),
    path('espacio-vip/libro-dinamico', views.libro_dinamico, name='libro_dinamico'),
    path('contacto/', views.contacto, name='contacto'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('subscribe/success/', views.success, name='success'),
    path('subscribe/cancel/', views.cancel, name='cancel'),
    path('error/', views.error, name='error'),

    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
]
