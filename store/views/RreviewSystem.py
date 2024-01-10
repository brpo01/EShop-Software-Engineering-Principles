
from django.shortcuts import render, redirect
from store.models.rev import reviewTry
from django.views import View


class Review(View):
    product=0
    def ReviewSysten(request):
        postData = request.POST
        Review.product = postData.get('product')
        print("product : ", Review.product)
        reviews = reviewTry.get_reviews_by_product(Review.product)
        print("Respective product comment",reviews)
        return render(request, 'Review.html',{'reviews': reviews})













