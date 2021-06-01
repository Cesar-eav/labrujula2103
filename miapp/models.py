from django.db import models

# Create your models here.

class Article(models.Model):
    publicidad = models.BooleanField(verbose_name="Publicidad", default=False) 
    title = models.CharField(max_length=100, verbose_name="Lugar") 
    artista = models.CharField(max_length=100, verbose_name="Artista")  
    gps = models.CharField(max_length=100, verbose_name="GPS") 
    lat = models.CharField(max_length=100, verbose_name="Lat", default="0" ) 
    lon = models.CharField(max_length=100, verbose_name="Lon", default="0") 
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(default='null',verbose_name="Miniatura", upload_to="articles")
    #public = models.BooleanField(verbose_name="¿Publicado?", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= "Street Art"
        verbose_name_plural= "Streets Arts"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.image} - {self.artista}"

    # def __str__(self):

    #     if self.public:
    #         public = "(publicado)"
    #     else:
    #         public = "(privado)"

    #     return f"{self.title} ({public})"

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateField()

    class Meta:
        verbose_name= "Category"
        verbose_name_plural= "Categories"


### MIRADORES ###

class Mira(models.Model):
    cerro = models.CharField(max_length=100, verbose_name="nombre", default="Cerro")
    lugar = models.CharField(max_length=100, verbose_name="Lugar", default="Nombre") 
    gps = models.CharField(max_length=100, verbose_name="GPS", default="gps") 
    lat = models.CharField(max_length=100, verbose_name="Lat", default="lat") 
    lon = models.CharField(max_length=100, verbose_name="Long", default="long") 
    calle = models.CharField(max_length=100, verbose_name="calle", default="calle")   
    image = models.ImageField(default='null',verbose_name="Miniatura", upload_to="miradores")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= "Mirador"
        verbose_name_plural= "Miradores"

    def __str__(self):
        return f"{self.lugar}"


### OTROS ###

class Otros(models.Model):
    lugar = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    gps = models.CharField(max_length=100, verbose_name="GPS", default="gps") 
    lat = models.CharField(max_length=100, verbose_name="Lat", default="0") 
    lon = models.CharField(max_length=100, verbose_name="Lon", default="0")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(default='null',verbose_name="Miniatura", upload_to="otros")

    class Meta:
        verbose_name= "Otro"
        verbose_name_plural= "Otros"

    def __str__(self):
        return f"{self.lugar} - {self.descripcion}"


### IGLESIAS ###

class Iglesias(models.Model):
    nombre = models.CharField(max_length=100, default="")
    direccion = models.CharField(max_length=100, default="")
    lugar = models.CharField(max_length=100, default="")
    descripcion = models.TextField(max_length=250)
    gps = models.CharField(max_length=100, verbose_name="GPS", default="gps") 
    lat = models.CharField(max_length=100, verbose_name="Lat", default="0") 
    lon = models.CharField(max_length=100, verbose_name="Lon", default="0")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(default='null',verbose_name="Miniatura", upload_to="iglesias")

    class Meta:
        verbose_name= "Igleia"
        verbose_name_plural= "Iglesias"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.nombre}"


class Ascensores(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=250)
    gps = models.CharField(max_length=100, verbose_name="GPS", default="gps") 
    lat = models.CharField(max_length=100, verbose_name="Lat", default="0") 
    lon = models.CharField(max_length=100, verbose_name="Lon", default="0")
    content = models.TextField(verbose_name="Descripción", default="Describir")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(default='null',verbose_name="Miniatura", upload_to="ascensores")

    class Meta:
        verbose_name= "Ascensor"
        verbose_name_plural= "Ascensores"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.nombre}"

class Boots(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=250)
    gps = models.CharField(max_length=100, verbose_name="GPS", default="gps") 
    content = models.TextField(verbose_name="Descripción", default="Describir")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(default='null',verbose_name="Miniatura", upload_to="articles")

    class Meta:
        verbose_name= "Boot"
        verbose_name_plural= "Boots"



#################
### ESCALERAS ###
#################

class Escaleras(models.Model):
    modelos = models.CharField(max_length=100, default="")
    lugar = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    autor = models.CharField(max_length=100, default="")
    direccion = models.CharField(max_length=250, default="dir")
    gps = models.CharField(max_length=100, verbose_name="GPS", default="gps") 
    lat = models.CharField(max_length=100, verbose_name="Lat", default="0") 
    lon = models.CharField(max_length=100, verbose_name="Lon", default="0")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(default='null',verbose_name="Miniatura", upload_to="escaleras")

    class Meta:
        verbose_name= "Escalera"
        verbose_name_plural= "Escaleras"

    
    def __str__(self):
        return f"{self.descripcion}"

class Publicidad(models.Model):
    publicidad = models.CharField(max_length=100, default="false")
    local_nombre = models.CharField(max_length=100, verbose_name="Local")
    direccion = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=250)
    gps = models.CharField(max_length=100, verbose_name="GPS") 
    lat = models.CharField(max_length=100, verbose_name="Lat", default="0") 
    lon = models.CharField(max_length=100, verbose_name="Lon", default="0")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(default='null',verbose_name="Miniatura", upload_to="publicidad")

    class Meta:
        verbose_name= "Publicidad"
        verbose_name_plural= "Publicidades"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.local_nombre}"
