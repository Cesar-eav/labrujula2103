from rest_framework import viewsets


from .models import Article, Category, Mira, Otros, Iglesias, Ascensores, Boots, Escaleras
from .serializer import ArticleSerializer, CategorySerializer, MiraSerializer, OtrosSerializer, IglesiasSerializer, AscensoresSerializer, BootsSerializer, EscalerasSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MiraViewSet(viewsets.ModelViewSet):
    queryset = Mira.objects.all()
    serializer_class = MiraSerializer

class OtrosViewSet(viewsets.ModelViewSet):
    queryset = Otros.objects.all()
    serializer_class = OtrosSerializer

class IglesiasViewSet(viewsets.ModelViewSet):
    queryset = Iglesias.objects.all()
    serializer_class = IglesiasSerializer

class AscensoresViewSet(viewsets.ModelViewSet):
    queryset = Ascensores.objects.all()
    serializer_class = AscensoresSerializer

class BootsViewSet(viewsets.ModelViewSet):
    queryset = Boots.objects.all()
    serializer_class = BootsSerializer

class EscalerasViewSet(viewsets.ModelViewSet):
    queryset = Escaleras.objects.all()
    serializer_class = EscalerasSerializer

class LecherosViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(title="Lecheros")
    serializer_class = ArticleSerializer

class LarrainViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(title="Larrain")
    serializer_class = ArticleSerializer

class PolancoViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(title="Polanco")
    serializer_class = ArticleSerializer   

class MonjasViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(title="Monjas")
    serializer_class = ArticleSerializer   

class MariposasViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(title="Mariposas")
    serializer_class = ArticleSerializer   

class FloridaViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(title="Florida")
    serializer_class = ArticleSerializer   

class BellavistaViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(title="Bellavista")
    serializer_class = ArticleSerializer  

class YungayViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(title="Yungay")
    serializer_class = ArticleSerializer  

class SanjuandediosViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(title="San Juan de Dios")
    serializer_class = ArticleSerializer  

class CarcelViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(title="Cárcel")
    serializer_class = ArticleSerializer  

class PanteonViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(title="Panteón")
    serializer_class = ArticleSerializer  

class AlegreViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(title="Alegre")
    serializer_class = ArticleSerializer  

class ConcepcionViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(title="Concepción")
    serializer_class = ArticleSerializer  

class CordilleraViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(title="Cordillera")
    serializer_class = ArticleSerializer  

class ArtilleriaViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(title="Artilleria")
    serializer_class = ArticleSerializer  

class PlayaAnchaViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(title="Playa Ancha").order_by('?')
    serializer_class = ArticleSerializer  