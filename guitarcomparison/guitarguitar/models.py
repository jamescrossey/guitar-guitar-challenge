from django.db import models


class matches(models.Model):
    genre = models.TextField()
    type = models.TextField()

class Guitars(models.Model):
    sku = models.CharField(primary_key=True)
    asn = models.CharField(null=True)
    Category = models.CharField()
    online = models.CharField()
    itemName = models.CharField()
    title = models.CharField(null=True)
    brandName = models.CharField()
    productDetail = models.TextField()
    SalesPrice = models.DecimalField(decimal_places=2, max_digits=10)
    pictureMain = models.ImageField()
    qtyInStock = models.IntegerField(default=0)
    qtyOnOrder = models.IntegerField(default=0)
    colour = models.IntegerField()
    pickup = models.IntegerField()
    BodyShape = models.IntegerField()
    CreatedOn = models.DateField()
    rating = models.DecimalField(decimal_places=2, max_digits=10)
    glasgowQty = models.IntegerField(default=0)
    edinburghQty = models.IntegerField(default=0)
    newcastleQty = models.IntegerField(default=0)
    guitarType = models.TextField() 
    
