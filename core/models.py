from django.db import models
from stdimage.models import StdImageField


class Base(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Cargo(models.Model):
    cargo = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length = 100)
    descricao = models.TextField('Descrição', max_length =100)
    cargo = models.ForeignKey('core.Cargo', on_delete = models.SET_NULL, null = True)
    foto = StdImageField('Foto', upload_to='equipe', variations={'thumb':{'width': 410, 'height': 410, 'crop': True}})
    instagram = models.CharField('Instagram', max_length=100)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class Animal(models.Model):
    animal = models.CharField(max_length = 50)

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'

    def __str__(self):
        return self.animal


class Pet (Base):
    nome = models.CharField('Nome', max_length = 100)
    descricao = models.TextField('Descrição', max_length = 1000)
    animal = models.ForeignKey('core.Animal', on_delete = models.SET_NULL, null = True)
    foto = StdImageField('Foto', upload_to='Pets', variations={'thumb': {'width': 410, 'height': 275, 'crop': True}})

    class Meta:
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'

    def __str__(self):
        return self.nome


class Social(Base):
    twitter = models.CharField('Twitter', max_length=100)
    facebook = models.CharField('Facebook', max_length=100)
    youtube = models.CharField('Youtube', max_length=100)
    instagram = models.CharField('Instagram', max_length=100)

    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Sociais'





# Create your models here.
