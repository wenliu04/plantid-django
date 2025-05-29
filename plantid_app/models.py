from django.db import models

# Create your models here.
class PlantImage(models.Model):
    image=models.ImageField(upload_to='plants/')
    uploaded_at=models.DateTimeField(auto_now_add=True)
    

    def _str_(self):
        return self.image.name