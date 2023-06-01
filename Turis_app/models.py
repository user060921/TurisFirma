from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField



class about(models.Model):
    title = models.CharField(max_length=250)
    title1 = models.CharField(max_length=250)
    description1 = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    img = models.ImageField(upload_to='media')
    class Meta:
        verbose_name_plural='Biz haqimizda'
    def __str__(self):
        return f'{self.title}'

class aboutcarusel(models.Model):
    img = models.ImageField(upload_to='media')
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    facebook=models.CharField(max_length=255,blank=True,null=True)
    twitter=models.CharField(max_length=255,blank=True,null=True)
    instagram=models.CharField(max_length=255,blank=True,null=True)
    class Meta:
        verbose_name_plural='Karusel'
    def __str__(self):
        return self.name


class service(models.Model):
    img = models.ImageField(upload_to='img/',blank=True,null=True)
    name = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    class Meta:
        verbose_name_plural='Xizmatlar'
    def __str__(self):
        return self.name


class packages(models.Model):
    img = models.ImageField(upload_to='media')
    country = models.CharField(max_length=250)
    data = models.CharField(max_length=250)
    people = models.CharField(max_length=250)
    money = models.FloatField(max_length=100)
    description = RichTextUploadingField()
    class Meta:
        verbose_name_plural='Paketlar'

    def __str__(self):
        return self.country


class des(models.Model):
    img = models.ImageField(upload_to='media')
    percentage = models.FloatField(max_length=250)
    country = models.CharField(max_length=250)

    img1 = models.ImageField(upload_to='media')
    percentage1 = models.FloatField(max_length=250)
    country1 = models.CharField(max_length=250)

    img2 = models.ImageField(upload_to='media')
    percentage2 = models.FloatField(max_length=250)
    country2 = models.CharField(max_length=250)

    img3 = models.ImageField(upload_to='media')
    percentage3 = models.FloatField(max_length=250)
    country3 = models.CharField(max_length=250)
    class Meta:
        verbose_name_plural='Manzil'
    def __str__(self):
        return f'{self.img}'



class ContactUs(models.Model):
    fullname=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=250)
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural='Biz bilan aloqa'

class Map(models.Model):
    map = models.CharField(max_length=250,null=True,blank=True)
    class Meta:
        verbose_name_plural='Mening turar manzilim'
        

