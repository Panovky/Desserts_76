from django.db import models


class Filling(models.Model):
    # Fields
    filling_id = models.AutoField(primary_key=True)
    filling_name = models.CharField(max_length=50)
    filling_description = models.CharField(max_length=500)
    photo = models.ImageField(null=True, upload_to="images/")

    # Metadata
    class Meta:
        ordering = ["filling_name"]

    # Methods
    def get_absolute_url(self):
        """
         Returns the url to access a particular instance of MyModelName.
         """
        return '{0} ({1})'.format(self.filling_id, self.filling_name)

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.filling_name


class Category(models.Model):
    # Fields
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    photo = models.ImageField(null=True, upload_to="images/")

    # Metadata
    class Meta:
        ordering = ["category_name"]

    # Methods
    def get_absolute_url(self):
        """
         Returns the url to access a particular instance of MyModelName.
         """
        return '{0} ({1})'.format(self.category_id, self.category_name)

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.category_name
