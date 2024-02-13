from django.db import models

# Create your models here.

class Photo(models.Model):
    
    photo_thumb = models.URLField(null=True, blank=True)
    photo_highres = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.photo_thumb}"


class Food(models.Model):

    name = models.CharField(max_length=100)
    es_name = models.CharField(max_length=100)
    csv_name = models.CharField(max_length=100)
    nf_calories = models.FloatField(null=True)
    brand_name = models.CharField(max_length=100, null=True, blank=True)

    serving_qty = models.FloatField(null=True)
    serving_unit = models.CharField(max_length=50)
    serving_weight_grams = models.FloatField()
    nf_total_fat = models.FloatField(null=True)
    nf_saturated_fat = models.FloatField(null=True)
    nf_cholesterol = models.FloatField(null=True)
    nf_sodium = models.FloatField(null=True)
    nf_total_carbohydrate = models.FloatField(null=True)
    nf_dietary_fiber = models.FloatField(null=True)
    nf_sugars = models.FloatField(null=True)
    nf_protein = models.FloatField(null=True)
    nf_potassium = models.FloatField(null=True)
    nf_p = models.FloatField(null=True)

    # Nutritionix DB Number
    ndb_no = models.IntegerField()

    meal_type = models.IntegerField()
    photo_thumb = models.URLField(null=True, blank=True)
    photo_highres = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.es_name}"