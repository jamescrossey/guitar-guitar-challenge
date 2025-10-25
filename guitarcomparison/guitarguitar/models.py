from django.db import models

# Create your models here.
class Genres(models.Model):
    genre = models.CharField(default="N/A")

class Type(models.Model):
    type = models.CharField()

class Products(models.Model):
    product = models.CharField()


class matches(models.Model):
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)



class Guitars(models.Model):
    sku = models.CharField(primary_key=True)
    asn = models.CharField(null=True)
    Category = models.CharField()
    online = models.BinaryField()
    itemName = models.CharField()
    title = models.CharField(null=True)
    brandName = models.CharField()
    Description = models.CharField(null=True)
    productDetail = models.TextField()
    SalesPrice = models.DecimalField(decimal_places=2, max_digits=5)
    pictureMain = models.ImageField()
    qtyInStock = models.IntegerField(default=0)
    qtyOnOrder = models.IntegerField(default=0)
    colour = models.IntegerField()
    pickup = models.IntegerField()
    BodyShape = models.IntegerField()
    CreatedOn = models.DateField()
    imageUrls = models.URLField(null=True)
    rating = models.DecimalField(decimal_places=2, max_digits=5)
    glasgowQty = models.IntegerField(default=0)
    edinburghQty = models.IntegerField(default=0)
    newcastleQty = models.IntegerField(default=0)