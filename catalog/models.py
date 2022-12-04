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
        return f'{self.filling_id}/'

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
        return f'{self.category_id}/'

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.category_name


class Dessert(models.Model):

    # Fields
    dessert_id = models.AutoField(primary_key=True)
    dessert_name = models.CharField(max_length=50)
    dessert_description = models.CharField(max_length=500)
    dessert_weight = models.FloatField()
    dessert_price = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
    photo = models.ImageField(null=True, upload_to="images/")

    # Metadata
    class Meta:
        ordering = ["dessert_name"]

    def get_absolute_url(self):
        """
         Returns the url to access a particular instance of MyModelName.
         """
        return f'dessert-{self.dessert_id}/'

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.dessert_name
