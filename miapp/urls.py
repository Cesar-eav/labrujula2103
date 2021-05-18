from django.urls import path
from rest_framework import routers

from .viewsets import ArticleViewSet, MiraViewSet, IglesiasViewSet, AscensoresViewSet, EscalerasViewSet, LecherosViewSet, OtrosViewSet, LarrainViewSet, PolancoViewSet, MonjasViewSet, MariposasViewSet, FloridaViewSet, BellavistaViewSet, YungayViewSet, SanjuandediosViewSet, CarcelViewSet, PanteonViewSet, AlegreViewSet, ConcepcionViewSet, CordilleraViewSet, ArtilleriaViewSet, PlayaAnchaViewSet

route = routers.SimpleRouter()
route.register('streetart', ArticleViewSet)
route.register('miradores', MiraViewSet)
route.register('iglesias', IglesiasViewSet)
route.register('ascensores', AscensoresViewSet)
route.register('escaleras', EscalerasViewSet)
route.register('otros', OtrosViewSet)
route.register('lecheros', LecherosViewSet)
route.register('larrain', LarrainViewSet)
route.register('polanco', PolancoViewSet)
route.register('monjas', MonjasViewSet)
route.register('mariposas', MariposasViewSet)
route.register('florida', FloridaViewSet)
route.register('bellavista', BellavistaViewSet)
route.register('yungay', YungayViewSet)
route.register('sanjuandedios', SanjuandediosViewSet)
route.register('carcel', CarcelViewSet)
route.register('panteon', PanteonViewSet)
route.register('alegre', AlegreViewSet)
route.register('concepcion', ConcepcionViewSet)
route.register('cordillera', CordilleraViewSet)
route.register('artilleria', ArtilleriaViewSet)
route.register('playaancha', PlayaAnchaViewSet)


# route.register('category', CategoryViewSet)
# route.register('type', TypeViewSet)

# De define de esta manera porque se está empleando el REST_FRAMEWORK
urlpatterns = route.urls
