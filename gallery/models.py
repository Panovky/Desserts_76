from django.db import models


class Photo(models.Model):

    photo_id = models.AutoField(primary_key=True)
    photo = models.ImageField(null=True, upload_to="gallery/")

    def get_absolute_url(self):
        return f'{self.photo_id}/'
