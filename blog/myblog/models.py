from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    titulo_tag = models.CharField(max_length=255)
    texto = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    data_publicacao = models.DateTimeField(blank=True, null=True, auto_now_add=timezone.now)
    categoria = models.CharField(max_length=255, default="Nenhuma")
    likes = models.ManyToManyField(User, related_name='blog_post')

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("post-details", kwargs={"pk": self.pk})
    
    def publicar(self):
        self.data_publicacao = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo + ' | ' +str(self.autor)