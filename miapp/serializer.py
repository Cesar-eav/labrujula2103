from miapp.views import arquitectura
from rest_framework import serializers
from .models import Article, Category, Mira, Otros, Iglesias, Ascensores, Boots, Escaleras, Arquitectura

class ArticleSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Article
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category
        fields = '__all__'

class MiraSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Mira
        fields = '__all__'

class OtrosSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Otros
        fields = '__all__'

class IglesiasSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Iglesias
        fields = '__all__'

class AscensoresSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Ascensores
        fields = '__all__'

class ArquitecturaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Arquitectura
        fields = '__all__'

class BootsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Boots
        fields = '__all__'

class EscalerasSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Escaleras
        fields = '__all__'
