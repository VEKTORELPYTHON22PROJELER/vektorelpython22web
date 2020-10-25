from django.db import models
from django.utils import timezone
# Create your models here.

class GonderiModel(models.Model):
    yazar=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    baslik=models.CharField(max_length=200,verbose_name="Başlık")
    yazi=models.TextField(verbose_name="Yazı")
    olusturzaman=models.DateTimeField(default=timezone.now)
    yayimzaman=models.DateTimeField(blank=True,null=True)
    GONDERI_CHOICES = (
        ('1','Romantik Komedi'),
        ('2', 'Drama'),
        ('3','Korku'),
    )
    tur = models.CharField(max_length=5,verbose_name="Gönderi Türü",\
        choices=GONDERI_CHOICES,default="1")

    def yayımla(self):
        self.yayimzaman=timezone.now()
        self.save()
    def __str__(self):
        return self.baslik

    



