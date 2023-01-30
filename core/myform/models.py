from django.db import models

class HomeLogo(models.Model):
    logo = models.ImageField('logo', upload_to='media')

class HamaImage(models.Model):
    imagehama = models.ImageField('Hamazgest Image', upload_to='media')

class KoshikImgae(models.Model):
    koshikimage = models.ImageField('Koshik Image', upload_to='media')
# Create your models here.
class ZenqerImage(models.Model):
    zenqerimage = models.ImageField('Zenqer Image', upload_to='media')

class AqsImage(models.Model):
    aqsimage = models.ImageField('Aqs Image', upload_to='media')