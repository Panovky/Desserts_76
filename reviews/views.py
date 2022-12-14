from django.shortcuts import render
from django.utils import timezone
from reviews.models import Review
from django.core.files.storage import FileSystemStorage
from PP_cakes.settings import upRoot, pRoot, up_url, p_url


def reviews_view(request):

    if request.method == "POST":
        review = Review()
        review.user_firstname = request.POST.get("user_firstname")
        review.user_lastname = request.POST.get("user_lastname")

        files = request.FILES
        fs1 = FileSystemStorage(location=upRoot)
        fs2 = FileSystemStorage(location=pRoot)

        if 'user_photo' in files:
            filename = fs1.save(files['user_photo'].name, files['user_photo'])
            review.user_photo = up_url.replace('/media', '')+filename
        else:
            review.user_photo = '/images/placeholder.webp'

        review.review_description = request.POST.get("review_description")
        review.date = timezone.now()

        if 'photo_1' in files:
            filename = fs2.save(files['photo_1'].name, files['photo_1'])
            review.photo_1 = p_url.replace('/media', '') + filename

        if 'photo_2' in files:
            filename = fs2.save(files['photo_2'].name, files['photo_2'])
            review.photo_2 = p_url.replace('/media', '') + filename

        review.save()

    return render(
        request,
        'reviews/review_list.html',
        context={'reviews': Review.objects.all()}
    )





