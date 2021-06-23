from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Article, Category, Mira, Otros, Iglesias, Ascensores, Boots, Escaleras, Arquitectura
from .serializer import ArticleSerializer, CategorySerializer, MiraSerializer, OtrosSerializer, IglesiasSerializer, AscensoresSerializer, BootsSerializer, EscalerasSerializer, ArquitecturaSerializer


class ArticleViewSet(viewsets.ModelViewSet):    
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):   
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class MiraViewSet(viewsets.ModelViewSet):   
    queryset = Mira.objects.all()
    serializer_class = MiraSerializer
    permission_classes = [IsAuthenticated]

class OtrosViewSet(viewsets.ModelViewSet):  
    queryset = Otros.objects.all()
    serializer_class = OtrosSerializer
    permission_classes = [IsAuthenticated]

class IglesiasViewSet(viewsets.ModelViewSet):   
    queryset = Iglesias.objects.all()
    serializer_class = IglesiasSerializer
    permission_classes = [IsAuthenticated]

class AscensoresViewSet(viewsets.ModelViewSet): 
    queryset = Ascensores.objects.all()
    serializer_class = AscensoresSerializer
    permission_classes = [IsAuthenticated]

class BootsViewSet(viewsets.ModelViewSet):  
    queryset = Boots.objects.all()
    serializer_class = BootsSerializer
    permission_classes = [IsAuthenticated]

class EscalerasViewSet(viewsets.ModelViewSet):  
    queryset = Escaleras.objects.all()
    serializer_class = EscalerasSerializer
    permission_classes = [IsAuthenticated]

class ArquitecturaViewSet(viewsets.ModelViewSet):   
    queryset = Arquitectura.objects.all()
    serializer_class = ArquitecturaSerializer
    permission_classes = [IsAuthenticated]

class LecherosViewSet(viewsets.ModelViewSet):   
    queryset = Article.objects.filter(title="Lecheros")
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

class LarrainViewSet(viewsets.ModelViewSet):    
    queryset = Article.objects.filter(title="Larrain")
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

class PolancoViewSet(viewsets.ModelViewSet):    
    queryset = Article.objects.filter(title="Polanco")
    serializer_class = ArticleSerializer   
    permission_classes = [IsAuthenticated]

class MonjasViewSet(viewsets.ModelViewSet): 
    queryset = Article.objects.filter(title="Monjas")
    serializer_class = ArticleSerializer   
    permission_classes = [IsAuthenticated]

class MariposasViewSet(viewsets.ModelViewSet):  
    queryset = Article.objects.filter(title="Mariposas")
    serializer_class = ArticleSerializer   
    permission_classes = [IsAuthenticated]

class FloridaViewSet(viewsets.ModelViewSet):    
    queryset = Article.objects.filter(title="Florida")
    serializer_class = ArticleSerializer   
    permission_classes = [IsAuthenticated]

class BellavistaViewSet(viewsets.ModelViewSet): 
    queryset = Article.objects.filter(title="Bellavista")
    serializer_class = ArticleSerializer  
    permission_classes = [IsAuthenticated]

class YungayViewSet(viewsets.ModelViewSet): 
    queryset = Article.objects.filter(title="Yungay")
    serializer_class = ArticleSerializer  
    permission_classes = [IsAuthenticated]

class SanjuandediosViewSet(viewsets.ModelViewSet):  
    queryset = Article.objects.filter(title="San Juan de Dios")
    serializer_class = ArticleSerializer  
    permission_classes = [IsAuthenticated]

class CarcelViewSet(viewsets.ModelViewSet): 
    queryset = Article.objects.filter(title="Cárcel")
    serializer_class = ArticleSerializer  
    permission_classes = [IsAuthenticated]

class PanteonViewSet(viewsets.ModelViewSet):    
    queryset = Article.objects.filter(title="Panteón")
    serializer_class = ArticleSerializer  
    permission_classes = [IsAuthenticated]

class AlegreViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(title="Alegre")
    serializer_class = ArticleSerializer  
    permission_classes = [IsAuthenticated]

class ConcepcionViewSet(viewsets.ModelViewSet): 
    queryset = Article.objects.filter(title="Concepción")
    serializer_class = ArticleSerializer  
    permission_classes = [IsAuthenticated]

class CordilleraViewSet(viewsets.ModelViewSet): 
    queryset = Article.objects.filter(title="Cordillera")
    serializer_class = ArticleSerializer  
    permission_classes = [IsAuthenticated]

class ArtilleriaViewSet(viewsets.ModelViewSet): 
    queryset = Article.objects.filter(title="Artilleria")
    serializer_class = ArticleSerializer  
    permission_classes = [IsAuthenticated]

class PlayaAnchaViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(title="Playa Ancha").order_by('?')
    serializer_class = ArticleSerializer  
    permission_classes = [IsAuthenticated]