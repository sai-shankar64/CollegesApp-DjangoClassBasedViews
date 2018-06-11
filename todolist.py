from django.db import models

class userdetails(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=30)
    email=models.EmailField(max_lenght=50)

class addTodo(models.Model):
    title=models.CharField(max_length=20)
    todo_msg=models.CharField(max_length=50)

