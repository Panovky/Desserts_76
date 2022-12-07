from django.db import models


class Order(models.Model):

    order_id = models.AutoField(primary_key=True)
    user_firstname = models.CharField(max_length=50)
    user_lastname = models.CharField(max_length=50)
    date = models.DateField()

    class Meta:
        ordering = ["date"]

    def get_absolute_url(self):
        return f'{self.order_id}/'

    def __str__(self):
        return f'Заказ #{self.order_id}'


