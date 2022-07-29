from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TodoModel(models.Model):
    id = models.IntegerField(primary_key= True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    title = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)


    def __str__(self):
        return self.title