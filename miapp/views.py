from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Arquitectura, Article, Boots, Mira, Otros, Iglesias, Ascensores, Escaleras
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages
from django.core.paginator import Paginator

from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

# Create your views here.


@api_view(['POST'])
def login(request):

    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
        user = User.objects.get(username=username)

    except User.DoesNotExist:
        return Response("Usuario Inválido")

    pwd_valid = check_password(password,user.password)

    if not pwd_valid:   
            return Response("Contrasñea invalida")

    token, _ = Token.objects.get_or_create(user=user)

    return Response(token.key)


def index(request):


    return render(request, 'index.html')
     

def streetart(request):
    return render(request, 'streetart.html')

def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public 
    )

    articulo.save()

    return HttpResponse(f"Articulo creado: <strong>{articulo.title}</strong>")

def save_article(request):

    if request.method == 'POST':

        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']

        articulo = Article(
            title = title,
            content = content,
            public = public 
        )
        
        articulo.save()

        return HttpResponse(f"Articulo creado: <strong>{articulo.title}</strong>")

    else:
        return HttpResponse ("<h2> No se ha podido crear el articulo </h2>")



def create_article(request):

    return render(request, 'create_article.html')



def create_full_article(request):

    if request.method == 'POST':
        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title = data_form.get('title')
            content = data_form['content']
            public = data_form ['public']

            articulo = Article(
                title = title,
                content = content,
                public = public
        )
            
            articulo.save()

            # Crear mensaje Flash

            messages.success(request, f'Creado correctamente el articulo {articulo.id}')

            return redirect('articulos')

           #return HttpResponse(articulo.title + ' ' + articulo.content + ' ' + str(articulo.public))

    else:
        formulario = FormArticle() 

    return render(request, 'create_full_article.html',{
        'form': formulario
    })



def articulo(request):

    
    try:
        articulo = Article.objects.POST(id=2, public=False)
        response = f"Articulo: <br/> {articulo.id}. {articulo.title}"

    except:
        response = "<h1>Artículo no encontrado</h1>"

    return HttpResponse(response)

def editar_articulo(request, id):

    articulo = Article.objects.POST(pk=id)

    articulo.title = "Batman"
    articulo.content = "Pelicula del 2017"
    articulo.public = True

    articulo.save()

    return HttpResponse(f"Articulo editado: <strong>{articulo.title}. {articulo.content}</strong>")

def articulos(request):

    articulos = Article.objects.all().order_by('?')
    # Paginar articulos (articulos x pagina)
    paginator = Paginator(articulos, 15)
    # Recoger número página
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)
    #articulos = Article.objects.filter(title="Cordillera")
    return render(request, 'articulos.html',{
        'articulos': page_articles
    })

def miradores(request):
    miradores = Mira.objects.all().order_by('-id')
    return render(request, 'miradores.html',{
        'miradores': miradores
    })

def iglesias(request):
    iglesias = Iglesias.objects.all().order_by('-id')
    return render(request, 'iglesias.html',{
        'iglesias': iglesias
    })

def ascensores(request):
    ascensores = Ascensores.objects.all().order_by('-id')
    return render(request, 'ascensores.html',{
        'ascensores': ascensores
    })


def escaleras(request):
    escaleras = Escaleras.objects.all().order_by('?')
    #ascensores = Ascensores.objects.all().order_by('?')
    return render(request, 'escaleras.html',{
        'escaleras': escaleras,
        #'ascensores': ascensores
    })

def arquitectura(request):
    arquitectura = Arquitectura.objects.all()
    return render(request, 'arquitectura.html',{
        'arquitecturas': arquitectura,
    
    })



def otros(request):
    otros = Otros.objects.all().order_by('-id')
    #concepcion = Article.objects.filter(cerro='Concepcion')
    return render(request, 'otros.html',{
        'otros': otros
    })

def borrar_articulo(request, id):
    articulo = Article.objects.POST(pk=id)
    articulo.delete()
    return redirect('articulos')

##################################################
############################ MODELOS POR CERRO ###
##################################################

def lecheros(request):
    articulos = Article.objects.filter(title="Lecheros")
    return render(request, 'articulos.html',{
        'articulos': articulos
    })

def polanco(request):
    articulos = Article.objects.filter(title="Polanco")
    return render(request, 'articulos.html',{
        'articulos': articulos
    })

def monjas(request):
    articulos = Article.objects.filter(title="Monjas")
    return render(request, 'articulos.html',{
        'articulos': articulos
    })

def mariposas(request):
    articulos = Article.objects.filter(title="Mariposas")
    return render(request, 'articulos.html',{
        'articulos': articulos,
        
    })

def florida(request):
    articulos = Article.objects.filter(title="Florida")
    return render(request, 'articulos.html',{
        'articulos': articulos
    })

def yungay(request):
    articulos = Article.objects.filter(title="Yungay")
    return render(request, 'articulos.html',{
        'articulos': articulos
    })

def bellavista(request):
    articulos = Article.objects.filter(title="Bellavista")
    return render(request, 'articulos.html',{
        'articulos': articulos
    })

def sanjuandedios(request):
    articulos = Article.objects.filter(title="San Juan de Dios")
    return render(request, 'articulos.html',{
        'articulos': articulos
    })

def carcel(request):
    articulos = Article.objects.filter(title="Cárcel")
    return render(request, 'articulos.html',{
        'articulos': articulos
    })

def panteon(request):
    articulos = Article.objects.filter(title="Panteón")
    return render(request, 'articulos.html',{
        'articulos': articulos
    })

def alegre(request):
    articulos = Article.objects.filter(title="Alegre")
    return render(request, 'articulos.html',{
        'articulos': articulos
    })

def concepcion(request):
    articulos = Article.objects.filter(title="Concepción")
    return render(request, 'articulos.html',{
        'articulos': articulos
    })

def cordillera(request):
    articulos = Article.objects.filter(title="Cordillera")
    return render(request, 'articulos.html',{
        'articulos': articulos
    })

def artilleria(request):
    articulos = Article.objects.filter(title="Artilleria")
    return render(request, 'articulos.html',{
        'articulos': articulos
    })

def playaancha(request):
    articulos = Article.objects.filter(title="Playa Ancha")
    return render(request, 'articulos.html',{
        'articulos': articulos
    })

def larrain(request):
    articulos = Article.objects.filter(title="Larrain")
    return render(request, 'articulos.html',{
        'articulos': articulos
    })

def patrimonio(request):
    return render(request, 'patrimonio.html')