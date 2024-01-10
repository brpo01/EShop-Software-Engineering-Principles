from django.db import models
from .customer import Customer
from .product import Product


class review(models.Model):
    comments = models.CharField(max_length=200,default='' , null=True , blank=True)
    rating = models.IntegerField(default=0)


    def register(self):
        self.save()



    @staticmethod
    def get_reviews_by_product(product_id):
        return review.objects.filter(id__in=product_id)

    @staticmethod
    def get_all_reviews():
        return review.objects.all()