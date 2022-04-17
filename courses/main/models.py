from django.db import models


# Create your models here.
class Data(models.Model):
    first_name = models.CharField('Имя', max_length=100)
    second_name = models.CharField('Фамилия', max_length=100)
    email = models.EmailField('Почта')
    telephone = models.CharField('Номер телефона', max_length=100)

    def __str__(self):
        return f"{self.first_name}_{self.second_name}"

    class Meta:
        verbose_name = "Форма обратной связи"
        verbose_name_plural = "Формы обратной связи"
