from django.db import models


class Review(models.Model):

    review_id = models.AutoField(primary_key=True)
    user_firstname = models.CharField(max_length=50)
    user_lastname = models.CharField(max_length=50)
    user_photo = models.ImageField(null=True, upload_to="images/users_photos")
    review_description = models.CharField(max_length=500)
    date = models.DateField()
    photo_1 = models.ImageField(null=True, blank=True, upload_to="images/reviews")
    photo_2 = models.ImageField(null=True, blank=True, upload_to="images/reviews")
    photo_3 = models.ImageField(null=True, blank=True, upload_to="images/reviews")
    photo_4 = models.ImageField(null=True, blank=True, upload_to="images/reviews")
    photo_5 = models.ImageField(null=True, blank=True, upload_to="images/reviews")

    class Meta:
        ordering = ["date"]

    def get_absolute_url(self):
        return f'{self.review_id}/'

    def __str__(self):
        return f'Review {self.review_id}'
