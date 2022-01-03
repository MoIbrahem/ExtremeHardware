from django.contrib.auth.models import AbstractUser
from store.models import Product , ProductImage as BaseProductImage
from django.db import models

# Create your models here.
class User(AbstractUser):
  email = models.EmailField(unique=True)

class MotherBoard(Product):
    socket = models.CharField(max_length=255)
    sata_ports=models.IntegerField()
    m2_ports=models.IntegerField()
    memory_place= models.IntegerField()
    memory_type=models.CharField(max_length=255)
    size=models.CharField(max_length=255)

class Cpu(Product):
    vendor = models.CharField(max_length=255)
    socket = models.CharField(max_length=255)
    support_socket = models.CharField(max_length=255)
    support_socket2 = models.CharField(max_length=255,null=True,blank= True)
    support_socket3 = models.CharField(max_length=255,null=True,blank= True)
    support_socket4 = models.CharField(max_length=255,null=True,blank= True)
    support_socket5 = models.CharField(max_length=255,null=True,blank= True)
    support_socket6 = models.CharField(max_length=255,null=True,blank= True)
    wattPower = models.IntegerField()
    boxCooler = models.BooleanField()

class Gpu(Product):
    wattpower = models.IntegerField()

class Storage(Product):
    port = models.TextField()
    size = models.TextField()
    st_size= models.IntegerField()

class Psu(Product):
    wattpower= models.IntegerField()
    plus_type = models.CharField(max_length=255)

class Case(Product):
    size = models.CharField(max_length=255)
    hddSupport = models.IntegerField(null=True,blank=True)
    radSupport = models.IntegerField(null = True, blank= True)
    radSize = models.CharField(max_length=255)

class Cooler(Product):
    coolType = models.CharField(max_length=255)
    wattpower = models.IntegerField()
    rad = models.IntegerField(null=True)
    fans=models.IntegerField()
    sockets = models.CharField(max_length=255)
    sockets2 = models.CharField(max_length=255,null=True,blank= True)
    sockets3 = models.CharField(max_length=255,null=True,blank= True)
    sockets4 = models.CharField(max_length=255,null=True,blank= True)
    sockets5 = models.CharField(max_length=255,null=True,blank= True)
    sockets6 = models.CharField(max_length=255,null=True,blank= True)

class Memory(Product):
    memory_type = models.CharField(max_length=255)
    places=models.IntegerField()
    size = models.IntegerField()
    speed = models.IntegerField()


