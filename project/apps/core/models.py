from django.db import models


from django.db import models

class Suscriptor(models.Model):
    email = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
