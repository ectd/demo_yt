from django.db import models

class app_type(models.Model):
       
    name            = models.CharField(max_length=60)
    

    def __str__ (self):
        return f"{self.name}"