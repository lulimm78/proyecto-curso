from django.db import models

# Create your models here.
class Rectificado(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo",null=True, blank=True)
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to="rectificados")
    video = models.URLField(verbose_name="URLVideo",null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "rectificado"
        verbose_name_plural = "rectificados"
        ordering = ['-created']

    def __str__(self):
        return self.title
    
    