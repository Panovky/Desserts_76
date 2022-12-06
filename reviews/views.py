from django.shortcuts import render
from django.views import generic
from reviews.models import Review


class ReviewsView(generic.ListView):
    model = Review
    context_object_name = 'reviews'


def create_new_review(request):

    return render(
        request,
        'reviews/form_review.html',
    )

