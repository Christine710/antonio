from django.db import models
from django.core.urlresolvers import reverse

class Product(models.Model):
    product_type = models.CharField(max_length=200)
    supplier = models.CharField(max_length=200)
    quantity = models.CharField(max_length=10)
    published_date = models.DateTimeField(
        blank=True, null=True)
    product_image = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('market:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.product_type + ' - ' + self.supplier
