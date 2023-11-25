from django.db import models
# from django.contrib.auth.models import User


class Articles(models.Model):
    full_text = models.TextField('Обращение')
    # date = models.DateTimeField('Дата', auto_now_add=True)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_text

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'


class Moder(models.Model):
    category_theme = models.TextField()
    theme = models.TextField()
    text = models.TextField()

    def __str__(self):
        return self.text
