from django.contrib.auth.context_processors import auth
from django.shortcuts import render, get_object_or_404
import os
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse
from .forms import ValoracionForm
from Edalom import settings
from .models import Profile, Valoracion
from django.db.models import Avg
from django.http import JsonResponse
import stripe
from djstripe.models import Customer, Subscription


stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def inicio(request):
    return render(request, 'inicio.html')


def libros(request):
    return render(request, 'libros.html')


def cuentos(request):
    return render(request, 'cuentos.html')


def cuento(request, historia):
    template_name = f'cuentos/{historia}.html'  # Constructing the template name dynamically
    valoraciones = Valoracion.objects.filter(activo=True, cuento=historia)
    nueva_valoracion = None
    try:
        existing_valoracion = Valoracion.objects.filter(user=request.user, cuento=historia).first()
    except:
        existing_valoracion = None

    if request.method == 'POST':
        valoracion_form = ValoracionForm(data=request.POST)
        if valoracion_form.is_valid():
            nueva_valoracion = valoracion_form.save(commit=False)
            nueva_valoracion.cuento = historia
            nueva_valoracion.user_id = request.user.id
            nueva_valoracion.save()
    else:
        valoracion_form = ValoracionForm()

    valoracion_global = valoraciones.aggregate(Avg('valoracion'))['valoracion__avg']
    if valoracion_global is not None:
        valoracion_global = round(valoracion_global, 2)
    num_valoraciones = valoraciones.count()

    context = {'cuento': historia,
               'valoraciones': valoraciones,
               'nueva_valoracion': nueva_valoracion,
               'valoracion_form': valoracion_form,
               'valoracion_global': valoracion_global,
               'num_valoraciones': num_valoraciones,
               'existing_valoracion': existing_valoracion}

    return render(request, template_name, context)


@login_required(login_url='signin')
def cuentovip(request, historia):
    template_name = f'cuentos/{historia}.html'  # Constructing the template name dynamically
    valoraciones = Valoracion.objects.filter(activo=True, cuento=historia)
    nueva_valoracion = None
    try:
        existing_valoracion = Valoracion.objects.filter(user=request.user, cuento=historia).first()
    except:
        existing_valoracion = None

    if request.method == 'POST':
        valoracion_form = ValoracionForm(data=request.POST)
        if valoracion_form.is_valid():
            nueva_valoracion = valoracion_form.save(commit=False)
            nueva_valoracion.cuento = historia
            nueva_valoracion.user_id = request.user.id
            nueva_valoracion.save()
    else:
        valoracion_form = ValoracionForm()

    valoracion_global = valoraciones.aggregate(Avg('valoracion'))['valoracion__avg']
    if valoracion_global is not None:
        valoracion_global = round(valoracion_global, 2)
    num_valoraciones = valoraciones.count()

    context = {'cuento': historia,
               'valoraciones': valoraciones,
               'nueva_valoracion': nueva_valoracion,
               'valoracion_form': valoracion_form,
               'valoracion_global': valoracion_global,
               'num_valoraciones': num_valoraciones,
               'existing_valoracion': existing_valoracion}

    return render(request, template_name, context)


def mundo(request):
    return render(request, 'mundo.html')


def mapas(request):
    return render(request, 'mundo/mapas.html')


def enciclopedia(request):
    return render(request, 'mundo/enciclopedia.html')


def enciclopedia_articulo(request, article):
    return render(request, f'mundo/enciclopedia/{article}.html')


def contacto(request):
    return render(request, 'contacto.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Ese email ya existe')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Ese usuario ya existe')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()

                user_login = auth.authenticate(username=username, password=password1)
                auth.login(request, user_login)

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, suscripcion=False)
                new_profile.save()

                return redirect('bienvenida')

        else:
            messages.info(request, 'Las contraseñas no coinciden')
            return redirect('signup')
    else:
        return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('espacio_vip')
        else:
            messages.info(request, 'Credenciales incorrectos')
            return redirect('signin')
    else:
        return render(request, 'signin.html')


@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def espacio_vip(request):
    return render(request, 'espacio_vip.html')


@login_required(login_url='signin')
def bienvenida(request):
    user_profile = Profile.objects.get(user=request.user)
    context = {'user_profile': user_profile}
    return render(request, 'vip/bienvenida.html', context)

def mi_cuenta(request):
    user_profile = Profile.objects.get(user=request.user)
    customer, _ = Customer.get_or_create(subscriber=request.user)
    user_profile.stripe_customer_id = customer.id
    active_subscription = customer.subscriptions.filter(status="active").first()
    if active_subscription:
        user_profile.suscripcion = True
    else:
        user_profile.suscripcion = False
    user_profile.save()

    if request.method == 'POST':

        if request.FILES.get('userimg'):
            image = request.FILES.get('userimg')
            user_profile.userimg = image
            user_profile.save()
            return redirect('mi_cuenta')

    context = {'user_profile': user_profile, 'suscripcion': user_profile.suscripcion}
    return render(request, 'vip/mi_cuenta.html', context)



def libro_dinamico(request):
    pdf_directory = os.path.join(settings.STATICFILES_DIRS[0], 'pdf')   # cambiar a STATIC_ROOT al pasar a producción
    pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]
    chapter_titles = [os.path.splitext(pdf)[0].split('.')[0] for pdf in pdf_files]
    user_profile = Profile.objects.get(user=request.user)
    suscripcion = user_profile.suscripcion
    print(chapter_titles)
    context = {'user_profile': user_profile, 'suscripcion': suscripcion, 'chapter_titles': chapter_titles}
    return render(request, 'vip/libro_dinamico.html', context)

@login_required(login_url='signin')
def subscribe(request):
    user_profile = request.user.profile
    customer, _ = Customer.get_or_create(subscriber=request.user)

    # Create checkout session
    checkout_session = stripe.checkout.Session.create(
        customer=customer.id,
        payment_method_types=['card'],
        line_items=[
            {
                'price': 'price_1PEayNFHROTATiDDfPxZtqVN',
                'quantity': 1,
            },
        ],
        mode='subscription',
        success_url=request.build_absolute_uri('success/'),
        cancel_url=request.build_absolute_uri('cancel/'),
    )

    # Redirect the user to the Stripe checkout page
    return redirect(checkout_session.url)


@login_required(login_url='signin')
def success(request):
    return render(request, 'subscribe/success.html')


@login_required(login_url='signin')
def cancel(request):
    return render(request, 'subscribe/cancel.html')


def error(request):
    error_message = "Ha ocurrido un error. Por favor, vuelva a intentarlo más tarde."
    return render(request, 'subscribe/error.html', {'error_message': error_message})