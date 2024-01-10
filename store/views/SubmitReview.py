from django.shortcuts import render, redirect
from store.models.rev import reviewTry
from store.models.customer import Customer
from.RreviewSystem import Review
from store.models.product import Product


def SubmitReview(request):
    if request.method == 'POST':
        postData = request.POST
        product=Review.product
        print("product : ", product)
        customer= request.session.get('customer')
        print("customer",customer)
        comment = postData.get('comment')
        rating = postData.get('rate')
        rev= reviewTry(product=Product(id=product),customer=Customer(id=customer),
                       comments=comment, rating=rating)
        rev.register()
        return render(request, 'ReviewSubmitted.html')




