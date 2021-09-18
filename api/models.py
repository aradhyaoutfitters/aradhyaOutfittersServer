from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False)
    phone = models.BigIntegerField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    subject = models.CharField(max_length=400, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " --> " + self.subject


class Category(models.Model):
    category_name = models.CharField(max_length=300, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)


class ProductImage(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=300, blank=False, null=False)
    product_image = models.ImageField(upload_to="product_image/", null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
