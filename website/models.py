from django.db import models
from django.contrib.auth.hashers import check_password

class Utilisateur(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    todolist = models.TextField()

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'website_utilisateur'

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)