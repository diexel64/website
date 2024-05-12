from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    stripe_subscription_id = models.CharField(max_length=50, blank=True, null=True)
    suscripcion = models.BooleanField(default=False)
    userimg = models.ImageField(upload_to='profile_images/', default='default.png')

    def __str__(self):
        return self.user.username


class Valoracion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    valoracion = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    cuento = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    editado = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ('creado',)

    def __str__(self):
        return 'Valoración de {} en {}'.format(self.user, self.cuento)
