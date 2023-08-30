from django.db import models
from django.contrib.auth.models import User
from utils.models import BaseModel



class Kurulus(BaseModel):

    KURULUS_TYPE_CHOICES = (
        ('S', 'Şahıs'),
        ('BI', 'Büyük İşletme'),
        ('K', 'KOBİ'),
        ('STK', 'STK'),
    )
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    type = models.CharField(max_length=3, choices=KURULUS_TYPE_CHOICES)
    country = models.CharField(max_length=50)
    date = models.DateField()
    employees = models.IntegerField()


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'kurulus'
        verbose_name = 'Kurulus'


class Subscribe(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscribe_kurulus = models.ForeignKey(Kurulus, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} -> {self.subscribe_kurulus.name}"
    
    class Meta:
        db_table = 'subscribe'
        verbose_name = 'Subscribe'