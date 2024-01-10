from django.shortcuts import render, redirect
from django.views import View
from store.models.rev import reviewTry


from store.models.reviewsys import review



class AddReviewBtn(View):

    products=None
    #def AddReviewBtn(request):
