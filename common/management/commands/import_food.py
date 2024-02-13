import os
import csv
from django.core.management.base import BaseCommand
from googletrans import Translator
import requests

from food_planner.settings import BASE_DIR
from food.models import Food


x_app_id = os.environ["NUTRITIONIX_APP_ID"]
x_app_key = os.environ["NUTRITIONIX_APP_KEY"]


"""
Class to get all the name of possible fruits and import them into the Django project's database
using the Nutritionix information.
"""
class FoodSeeder:

    
    headers = {
        'Accept':'application/json',
        'Content-Type': 'application/json',
        "x-app-id": x_app_id,
        "x-app-key": x_app_key,
    }

    translator = Translator()
    url = 'https://trackapi.nutritionix.com/v2/natural/nutrients/'

    def get_details(self, query):
        food_details = requests.post(self.url, headers=self.headers, json={"query": query}).json()
        return food_details

    def import_food(self, name):
        existing_food = Food.objects.filter(csv_name=name).first()
        if not existing_food:
            details = self.get_details(name)
            if (len(details['foods']) == 1):
                food_to_import = details['foods'][0]
                es_name = self.translator.translate(food_to_import['food_name'], src='en', dest='es').text
                # Create a Food Object
                Food.objects.create(
                    name=food_to_import['food_name'],
                    es_name=es_name,
                    csv_name=name,
                    nf_calories=food_to_import['nf_calories'],
                    brand_name=food_to_import.get('brand_name', None),
                    serving_qty=food_to_import['serving_qty'],
                    serving_unit=food_to_import['serving_unit'],
                    serving_weight_grams=food_to_import['serving_weight_grams'],
                    nf_total_fat=food_to_import.get('nf_total_fat', None),
                    nf_saturated_fat=food_to_import.get('nf_saturated_fat', None),
                    nf_cholesterol=food_to_import.get('nf_cholesterol', None),
                    nf_sodium=food_to_import.get('nf_sodium', None),
                    nf_total_carbohydrate=food_to_import.get('nf_total_carbohydrate', None),
                    nf_dietary_fiber=food_to_import.get('nf_dietary_fiber', None),
                    nf_sugars=food_to_import.get('nf_sugars', None),
                    nf_protein=food_to_import.get('nf_protein', None),
                    nf_potassium=food_to_import.get('nf_potassium', None),
                    nf_p=food_to_import.get('nf_p', None),
                    ndb_no=food_to_import['ndb_no'],
                    meal_type=food_to_import['meal_type'],
                    photo_thumb=food_to_import['photo'].get('thumb', None),
                    photo_highres=food_to_import['photo'].get('highres', None),
                )
                print(f"Successfully created food object {name}")
        else:
            print(f"Moving on since {name} already exists...")

    def seed_food(self, path_to_open):
        with open(path_to_open, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    self.import_food(row['FoodItem'])
                except Exception as e:
                    print(f"Error trying to import food item: {row['FoodItem']}")
                    print(f"Exception Details: {repr(e)}")

class Command(BaseCommand):

    def handle(self, *args, **options):
        path_to_open = str(BASE_DIR) + \
            '/common/management/commands/food_calories.csv'
        FoodSeeder().seed_food(path_to_open)
