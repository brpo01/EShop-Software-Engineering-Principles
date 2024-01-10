from django.db import models
from .customer import Customer
from .product import Product



class reviewTry(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,null=True)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,null = True )
    comments = models.CharField(max_length=200,default='' , null=True , blank=True)
    rating = models.IntegerField(default=0, null=True)


    def register(self):
        self.save()



    @staticmethod
    def get_reviews_by_product(product_id):
        return reviewTry.objects.filter(product=product_id)

    @staticmethod
    def get_all_reviews():
        return reviewTry.objects.all()
