from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.utils import timezone
from reviews.models import Review
from django.core.files.storage import FileSystemStorage
from PP_cakes.settings import upRoot, pRoot, up_url, p_url


class ReviewsView(generic.ListView):
    model = Review
    context_object_name = 'reviews'


def create_new_review(request):
    if request.method == "POST":
        review = Review()
        review.user_firstname = request.POST.get("user_firstname")
        review.user_lastname = request.POST.get("user_lastname")

        files = request.FILES
        fs1 = FileSystemStorage(location=upRoot)
        fs2 = FileSystemStorage(location=pRoot)

        filename = fs1.save(files['user_photo'].name, files['user_photo'])
        review.user_photo = up_url.replace('/media', '')+filename

        review.review_description = request.POST.get("review_description")
        review.date = timezone.now()

        if len(files) >= 2:
            filename = fs2.save(files['photo_1'].name, files['photo_1'])
            review.photo_1 = p_url.replace('/media', '') + filename

        if len(files) >= 3:
            filename = fs2.save(files['photo_2'].name, files['photo_2'])
            review.photo_2 = p_url.replace('/media', '') + filename

        if len(files) >= 4:
            filename = fs2.save(files['photo_3'].name, files['photo_3'])
            review.photo_3 = p_url.replace('/media', '') + filename

        if len(files) >= 5:
            filename = fs2.save(files['photo_4'].name, files['photo_4'])
            review.photo_4 = p_url.replace('/media', '') + filename

        if len(files) >= 6:
            filename = fs2.save(files['photo_5'].name, files['photo_5'])
            review.photo_5 = p_url.replace('/media', '') + filename

        review.save()
        return HttpResponseRedirect(reverse('reviews'))
    else:
        return render(
            request,
            'reviews/form_review.html',
        )



