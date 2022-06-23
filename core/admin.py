from django.contrib import admin
from .models import Cargo, Funcionario, Animal, Pet, Social


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', )


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('animal', )


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'criado')


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('nome', 'animal', 'ativo', 'criado')


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('twitter', 'facebook', 'youtube', 'instagram', 'ativo', 'criado')


