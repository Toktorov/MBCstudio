from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Team(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name = 'team_user',
        null=True, blank=True
    )

    full_name = models.CharField(
        max_length=255, 
        blank=True,
        verbose_name='ФИО:'
    )

    position = models.CharField(
        max_length=255, 
        blank=True,
        verbose_name='Должность:'
    )

    member_image = models.ImageField(
        upload_to='portfolio_image',
        verbose_name='Фото'
    )

    created = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команда'
        ordering = ('-created',)

    def __str__(self):
        return f"{self.full_name}"
