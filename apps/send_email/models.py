from django.db import models

# Create your models here.
class MessageSender(models.Model):
    full_name = models.CharField(
        max_length=255, 
        blank=True,
        verbose_name='Полное имя клиента:'
    )

    email = models.EmailField(
        verbose_name="E-mail", max_length=255, blank=True, null=True
    )

    describe = models.TextField(
        verbose_name='Описание'
    )

    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.id} -- {self.email}"