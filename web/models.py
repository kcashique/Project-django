from django.db import models

COLOR_CHOICES = (
    ("Red","Red"), ("Blue","Blue"), ("Yellow","Yellow"), ("Orange","Orange"),
)
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,blank=True,null=True,unique=True)
    class Meta:
        ordering = ("-title","id")
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')
    def __str__(self):
        return f"{self.title}"
class Department(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        ordering = ("-name","id")
    def __str__(self):
        return f"{self.name}"
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.PROTECT,blank=True,null=True)
    color = models.CharField(max_length=200,choices=COLOR_CHOICES)
    size = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    photo = models.ImageField()
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    mrp = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    description = models.TextField(blank=True,null=True)
    class Meta:
        ordering = ("-name","id")
    def __str__(self):
        return f"{self.name}"