from django.db.models import fields
from django.db.models.base import Model
from store.models import Customer , ProductImage
from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer 
from store.serializers import ProductSerializer as BaseProductSerializer, ProductImageSerializer 
from rest_framework import serializers
from .models import *

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password',
                  'email', 'first_name', 'last_name']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ProductSerializer(BaseProductSerializer):
    
        def to_representation(self, instance):
            
            if isinstance(instance, Cpu):
                return CpuSerializer(instance=instance).data

            elif isinstance(instance, MotherBoard):
                return MotherBoardSerializer(instance=instance).data

            elif isinstance(instance, Gpu):
                return GpuSerializer(instance=instance).data

            elif isinstance(instance, Storage):
                return StorageSerializer(instance=instance).data

            elif isinstance(instance, Memory):
                return MemorySerializer(instance=instance).data
            
            elif isinstance(instance, Case):
                return CaserSerializer(instance=instance).data

            elif isinstance(instance,Cooler):
                return CoolerSerializer(instance=instance).data

            elif isinstance(instance, Psu):
                return Psu(instance=instance).data



class CpuSerializer(BaseProductSerializer):
    
    class Meta:
        model = Cpu
        fields = ['id', 'title', 'description', 'slug', 'inventory',
                  'unit_price', 'collection', 'images','vendor', 'socket','support_socket','support_socket2','support_socket3','support_socket4','support_socket5','support_socket6','wattPower','boxCooler']
        

class MotherBoardSerializer(BaseProductSerializer):
    
    class Meta:
        model = MotherBoard
        fields = ['id', 'title', 'description', 'slug', 'inventory',
                  'unit_price', 'collection', 'images','socket','m2_ports','memory_place','memory_type','size']
    depth = 1

class GpuSerializer(BaseProductSerializer):
    class Meta:
        model = Gpu
        fields = ['id', 'title', 'description', 'slug', 'inventory',
                  'unit_price', 'collection', 'images','wattpower']
        depth = 1

class PsuSerializer(BaseProductSerializer):
    
    class Meta:
        model = Psu
        fields = ['id', 'title', 'description', 'slug', 'inventory',
                  'unit_price', 'collection', 'images','plus_type','wattpower']
        depth = 1

class StorageSerializer(BaseProductSerializer):
    
    class Meta:
        model = Storage
        fields = ['id', 'title', 'description', 'slug', 'inventory',
                  'unit_price', 'collection', 'images','port','size','st_size']
        depth = 1

class CoolerSerializer(BaseProductSerializer):
    
    class Meta:
        model = Cooler
        fields = ['id', 'title', 'description', 'slug', 'inventory',
                  'unit_price', 'collection', 'images','coolType','wattpower','rad','fans','sockets','sockets2','sockets3','sockets4','sockets5','sockets6']
        depth = 1

class CaserSerializer(BaseProductSerializer):
    
    class Meta:
        model = Case
        fields = ['id', 'title', 'description', 'slug', 'inventory',
                  'unit_price', 'collection', 'images','size','hddSupport','radSupport','radSize']
        depth = 1

class MemorySerializer(BaseProductSerializer):
    
    class Meta:
        model = Memory
        fields = ['id', 'title', 'description', 'slug', 'inventory',
                  'unit_price', 'collection', 'images','memory_type','places','size','speed']
        depth = 1