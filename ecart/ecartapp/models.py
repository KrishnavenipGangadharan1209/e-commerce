from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    cat_name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)

    class Meta:
        ordering=('cat_name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_urls(self):
        return reverse('ecartapp:prod_by_categ',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.cat_name)

class Product(models.Model):
    p_name=models.CharField(max_length=250,unique=True)
    p_slug=models.SlugField(max_length=250,unique=True)
    p_desc=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    p_cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product',blank=True)
    stock=models.IntegerField()
    avail=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateField(auto_now=True)

    def get_url(self):
        return reverse('ecartapp:prodDetail', args=[self.p_cat.slug,self.p_slug])

    class Meta:
        ordering=('p_name',)
        verbose_name='product'
        verbose_name_plural='products'

    def __str__(self):
        return '{}'.format(self.p_name)
