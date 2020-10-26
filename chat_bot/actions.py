from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted
from requests.models import REDIRECT_STATI
from api import zomato as z_api
import json
import yaml
from mail import send_mail
import logging
import pandas as pd
from pretty_html_table import build_table

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("__name__")

with open(r'credentials.yml') as file:
    config = yaml.full_load(file)

zomato = z_api.initialize_app(config["zomato"])

with open(r'data/cuisine.json', 'r') as file:
    cuisines_dict = json.load(file)

with open(r'data/city.json', 'r') as file:
    cities_dict = json.load(file)

tier1_cities = [city.lower() for city in cities_dict["tier1"]]
tier2_cities = [city.lower() for city in cities_dict["tier2"]]

print(cuisines_dict)
print(config)


class ActionSearchRestaurants(Action):

    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        # config = {"user_key": "f4924dc9ad672ee8c4f8c84743301af5"}

        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        budget = tracker.get_slot('budget')
        search_validity = "valid"
        print("Location : {} || Cuisine : {} || Budget : {}".format(
          loc, cuisine, budget))
        search_results = self.get_restuarant(loc, cuisine, budget)
        print("Results Shape after Buget Filtering : {}".format(
          search_results.shape[0]))
        search_results = search_results.head(10)

        if search_results.shape[0] > 0:
            response = 'Showing you top results:' + "\n"
            for index, row in search_results.iterrows():
                response = response + str(
                  row['restaurant_name']) + ' in ' + row[
                    'restaurant_address'] + ' has been rated ' + row[
                      'restaurant_rating'] + "\n"

            dispatcher.utter_message("-----" + response)
            response = build_table(search_results, 'blue_light')
            response = "Here are your search results ! Enjoy Eating :) \n" + response
            # response = ""  # For creating stories lets keep message empty

        else:
            response = "Sorry No Resturants Found !!"
            search_validity = "invalid"
            dispatcher.utter_message("-----" + response)

        # response_body = build_table(search_results, 'blue_light')
        return [
          SlotSet("check_search_validity", search_validity),
          SlotSet("email_message", response)
        ]

    def get_location(self, loc):
        location_detail = zomato.get_location(loc, 1)
        response = json.loads(location_detail)
        if response["status"] == "success":

            lat = response["location_suggestions"][0]["latitude"]
            lon = response["location_suggestions"][0]["longitude"]
            city_id = response["location_suggestions"][0]["city_id"]
            print("Zomato : {} Lat  || {} Long || {} City ID".format(
              lat, lon, city_id))
            return lat, lon, city_id
        else:
            raise Exception

    def get_restuarant(self, loc, cuisine, budget):

        lat, lon, city_id = self.get_location(loc)
        restuarant_detail = zomato.restaurant_search(
          "", lat, lon, str(cuisines_dict.get(cuisine)), limit=25)
        response = json.loads(restuarant_detail)
        # print("Zomato Response :: \n{}".format(response))
        if response["results_found"] == 0:
            raise Exception

        result_df = pd.DataFrame([{
          'restaurant_name':
            x['restaurant']['name'],
          'restaurant_rating':
            x['restaurant']['user_rating']['aggregate_rating'],
          'restaurant_address':
            x['restaurant']['location']['address'],
          'budget_for2people':
            x['restaurant']['average_cost_for_two'],
          'restaurant_photo':
            x['restaurant']['featured_image'],
          'restaurant_url':
            x['restaurant']['url']
        } for x in response['restaurants']])

        # print(result_df['budget_for2people'])
        # print(budget)
        # result_df['budget'] = result_df.apply(lambda row: self.get_budget(row),
        #                                       axis=1)

        restaurant_df = self.filter_budget(result_df, budget)

        # restaurant_df = result_df[(result_df.budget == budget)]
        print(restaurant_df.head())
        restaurant_df = restaurant_df.sort_values(['restaurant_rating'],
                                                  ascending=0)

        return restaurant_df

    def filter_budget(self, results, user_budget):
        user_budget = int(user_budget)
        if user_budget <= 299:
            return results[results.budget_for2people <= 299]
        elif user_budget > 700:
            return results[results.budget_for2people > 700]
        else:
            return results[(results.budget_for2people <= 700) &
                           (results.budget_for2people >= 300)]


""" Custom action to validate input location
"""


class ActionCheckLocation(Action):

    def name(self):
        return "action_check_location"

    def run(self, dispatcher, tracker, domain):

        location = tracker.get_slot("location")
        location = location.lower()
        location_validity = "valid"
        print
        if not location:
            location_validity = "invalid"
            print("Not Location is making in Invalid")
        elif location not in tier1_cities and location not in tier2_cities:
            location_validity = "invalid"
            print("Not in Tiers is making it Invalid")
            print(tier1_cities)

        return [SlotSet("check_location_validity", location_validity)]


class ActionValidateCuisine(Action):

    def name(self):
        return "action_cuisine_valid"

    def run(self, dispatcher, tracker, domain):

        cuisine = tracker.get_slot("cuisine")
        cuisine_validity = "valid"

        if not cuisine:
            cuisine_validity = "invalid"
        else:
            cuisine_validity = ("invalid"
                                if cuisine.lower() not in cuisines_dict.keys()
                                else "valid")

        return [SlotSet("check_cuisine_validity", cuisine_validity)]


class ActionSendMail(Action):

    def name(self):
        return 'action_send_email'

    def run(self, dispatcher, tracker, domain):
        recipient = tracker.get_slot('email')
        email_response = tracker.get_slot('email_message')
        send_mail(recipient, email_response)

        dispatcher.utter_message("Have a great day! Mail is sent")


class ActionSlotReset(Action):

    def name(self):
        return 'action_slot_reset'

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]


class ActionRestarted(Action):

    def name(self):
        return 'action_restart'

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]