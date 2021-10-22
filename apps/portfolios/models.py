from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Portfolio(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name = 'hotels_user',
        null=True, blank=True
    )

    title = models.CharField(
        max_length=255, 
        blank=True,
        verbose_name='Название:'
    )

    development = models.CharField(
        max_length=255, 
        blank=True,
        verbose_name='Разработка:'
    )

    portfolio_image = models.ImageField(
        upload_to='portfolio_image',
        verbose_name='Портфолио'
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'
        ordering = ('-created',)

    def __str__(self):
        return f"{self.title}"