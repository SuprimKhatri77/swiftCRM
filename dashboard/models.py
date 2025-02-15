from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CustomerDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    