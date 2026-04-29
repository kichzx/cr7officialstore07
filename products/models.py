# from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.IntegerField()
#     image = models.ImageField(upload_to='products/')
#     description = models.TextField()

#     def __str__(self):
#         return self.name

# from django.db import models

# class Product(models.Model):
#     # The name of the CR7 item
#     name = models.CharField(max_length=100)
    
#     # Price as a whole number (e.g., 169)
#     price = models.IntegerField()
    
#     # Images will be uploaded to a 'media/products/' folder
#     image = models.ImageField(upload_to='products/')
    
#     # Detailed information about the item
#     description = models.TextField()

#     # This makes the product show up by its name in the Django Admin panel
#     def __str__(self):
#         return self.name

# from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.IntegerField()
#     image = models.ImageField(upload_to='products/')
#     description = models.TextField()

#     def __str__(self):
#         return self.name

# from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.IntegerField()
#     image = models.ImageField(upload_to='products/')
#     description = models.TextField()

#     def __str__(self):
#         return self.name

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    description = models.TextField()

    def __str__(self):
        return self.name