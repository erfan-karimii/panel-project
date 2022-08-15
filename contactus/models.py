from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    
    class Meta:
        verbose_name='تماس با ما'
        verbose_name_plural='تماس با ما'

    def __str__(self):
        return self.email