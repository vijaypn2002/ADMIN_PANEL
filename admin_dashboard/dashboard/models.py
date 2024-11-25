from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=100)
    permissions = models.JSONField(default=dict)  # Store permissions as JSON

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
