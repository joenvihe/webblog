from django.db import models
# Create your models here.
from django.utils import timezone
# models.Model significa que Post es un modelo de Django, así Django sabe que debe guardarlo en la base de datos.
class Post(models.Model):
    # definir un tipo de campo por cada atributo
    # (https://docs.djangoproject.com/en/1.8/ref/models/fields/#field-types).
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # metodo publicar, que realiza una publicacion en el blog del post
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title