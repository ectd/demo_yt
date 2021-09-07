from demo.models.indication import indication
from django.db import models
from demo.models.product import product
from demo.models.indication import indication
from demo.models.app_type import app_type
from demo.models.region import region

class application(models.Model):
    
    product_id      = models.ForeignKey(product, on_delete=models.CASCADE)
    indication_id   = models.ForeignKey(indication, on_delete=models.CASCADE)
    number          = models.CharField(max_length=6)
    name            = models.CharField(max_length=30)
    region          = models.ForeignKey(region, on_delete=models.CASCADE)
    type            = models.ForeignKey(app_type, on_delete=models.CASCADE)
    created_at      = models.DateField()
    status          = models.CharField(max_length=10, null=True)

    def __str__ (self):
        return f"{self.name}"


    
   
