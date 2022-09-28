from django.db import models

# Create your models here.
class UrlShortner(models.Model):
    link=models.CharField(max_length=256)
    uid_field=models.CharField(max_length=256,null=True,blank=True)
    short_url=models.URLField(null=True,blank=True)
    qr=models.ImageField(upload_to='qr/',null=True,blank=True)