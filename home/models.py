from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    msg = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name
    

class About(models.Model):
    title = models.CharField(max_length=250)
    video = models.FileField(upload_to='about/')
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.title
    

class Team(models.Model):
    name = models.CharField(max_length=250)
    profesion = models.CharField(max_length=250)
    desc = models.TextField()
    img = models.FileField(upload_to='team/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.name
    


class Website(models.Model):
    name = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    desc = models.TextField()
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name


class WebImg(models.Model):
    web_id = models.ForeignKey(Website, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='web/')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.web_id.name