from django.db import models
from auth_user.models import User


# Create your models here.
class Client(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.user_id.username


class Video(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    img = models.ImageField(upload_to='video_img/')
    video = models.FileField(upload_to='video/')
    price = models.PositiveIntegerField()
    buyers = models.ManyToManyField(Client, related_name='clients')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.name