from django.db import models



class test(models.Model):
    a = models.CharField(max_length=200,default='' , null=True , blank=True)
    b = models.IntegerField(default=0)
