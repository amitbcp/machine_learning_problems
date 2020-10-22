import requests
import ast

base_url = "https://developers.zomato.com/api/v2.1/"


def initialize_app(config):
    return Zomato(config)


class Zomato:
    def __init__(self, config):
        self.user_key = config["user_key"]


    def get_categories(self):
        """
        Takes no input.
        Returns a dictionary of IDs and their respective category names.
        """
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "categories", headers=headers).content).decode("utf-8")
        a = ast.literal_eval(r)

        self.is_key_invalid(a)
        self.is_rate_exceeded(a)

        categories = {}
        for category in a['categories']:
            categories.update({category['categories']['id'] : category['categories']['name']})

        return categories


    def get_city_ID(self, city_name):
        """
        Takes City Name as input.
        Returns the ID for the city given as input.
        """
        if city_name.isalpha() == False:
            raise ValueError('InvalidCityName')
        city_name = city_name.split(' ')
        city_name = '%20'.join(city_name)
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "cities?q=" + city_name, headers=headers).content).decode("utf-8")
        a = ast.literal_eval(r)

        self.is_key_invalid(a)
        self.is_rate_exceeded(a)

        if len(a['location_suggestions']) == 0:
            raise Exception('invalid_city_name')
        elif 'name' in a['location_suggestions'][0]:
            city_name = city_name.replace('%20', ' ')
            if str(a['location_suggestions'][0]['name']).lower() == str(city_name).lower():
                return a['location_suggestions'][0]['id']
            else:
                raise ValueError('InvalidCityId')


    def get_city_name(self, city_ID):
        """
        Takes City ID as input.
        Returns the name of the city ID given as input.
        """
        self.is_valid_city_id(city_ID)

        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "cities?city_ids=" + str(city_ID), headers=headers).content).decode("utf-8")
        a = ast.literal_eval(r)

        self.is_key_invalid(a)
        self.is_rate_exceeded(a)

        if a['location_suggestions'][0]['country_name'] == "":
            raise ValueError('InvalidCityId')
        else:
            temp_city_ID = a['location_suggestions'][0]['id']
            if temp_city_ID == str(city_ID):
                return a['location_suggestions'][0]['name']



    def get_collections(self, city_ID, limit=None):
        """
        Takes City ID as input. limit parameter is optional.
        Returns dictionary of Zomato restaurant collections in a city and their respective URLs.
        """
        #self.is_valid_city_id(city_ID)

        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        if limit == None:
            r = (requests.get(base_url + "collections?city_id=" + str(city_ID), headers=headers).content).decode("utf-8")
        else:
            if str(limit).isalpha() == True:
                raise ValueError('LimitNotInteger')
            else:
                r = (requests.get(base_url + "collections?city_id=" + str(city_ID) + "&count=" + str(limit), headers=headers).content).decode("utf-8")
        a = ast.literal_eval(r)

        self.is_key_invalid(a)
        self.is_rate_exceeded(a)

        collections = {}
        for collection in a['collections']:
            collections.update({collection['collection']['title'] : collection['collection']['url']})

        return collections



    def get_cuisines(self, city_ID):
        """
        Takes City ID as input.
        Returns a sorted dictionary of all cuisine IDs and their respective cuisine names.
        """
        self.is_valid_city_id(city_ID)

        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "cuisines?city_id=" + str(city_ID), headers=headers).content).decode("utf-8")
        a = ast.literal_eval(r)

        self.is_key_invalid(a)
        self.is_rate_exceeded(a)

        if len(a['cuisines']) == 0:
            raise ValueError('InvalidCityId')
        temp_cuisines = {}
        cuisines = {}
        for cuisine in a['cuisines']:
            temp_cuisines.update({cuisine['cuisine']['cuisine_id'] : cuisine['cuisine']['cuisine_name']})

        for cuisine in sorted(temp_cuisines):
            cuisines.update({cuisine : temp_cuisines[cuisine]})

        return cuisines



    def get_establishment_types(self, city_ID):
        """
        Takes City ID as input.
        Returns a sorted dictionary of all establishment type IDs and their respective establishment type names.
        """
        self.is_valid_city_id(city_ID)

        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "establishments?city_id=" + str(city_ID), headers=headers).content).decode("utf-8")
        a = ast.literal_eval(r)

        self.is_key_invalid(a)
        self.is_rate_exceeded(a)

        temp_establishment_types = {}
        establishment_types = {}
        if 'establishments' in a:
            for establishment_type in a['establishments']:
                temp_establishment_types.update({establishment_type['establishment']['id'] : establishment_type['establishment']['name']})

            for establishment_type in sorted(temp_establishment_types):
                establishment_types.update({establishment_type : temp_establishment_types[establishment_type]})

            return establishment_types
        else:
            raise ValueError('InvalidCityId')



    def get_nearby_restaurants(self, latitude, longitude):
        """
        Takes the latitude and longitude as inputs.
        Returns a dictionary of Restaurant IDs and their corresponding Zomato URLs.
        """
        try:
            float(latitude)
            float(longitude)
        except ValueError:
            raise ValueError('InvalidLatitudeOrLongitude')

        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "geocode?lat=" + str(latitude) + "&lon=" + str(longitude), headers=headers).content).decode("utf-8")
        a = ast.literal_eval(r)

        nearby_restaurants = {}
        for nearby_restaurant in a['nearby_restaurants']:
            nearby_restaurants.update({nearby_restaurant['restaurant']['id'] : nearby_restaurant['restaurant']['url']})

        return nearby_restaurants



    def get_restaurant(self, restaurant_ID):
        """
        Takes Restaurant ID as input.
        Returns a dictionary of restaurant details.
        """
        self.is_valid_restaurant_id(restaurant_ID)

        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "restaurant?res_id=" + str(restaurant_ID), headers=headers).content).decode("utf-8")
        a = ast.literal_eval(r)

        if 'code' in a:
            if a['code'] == 404:
                raise('InvalidRestaurantId')

        restaurant_details = {}
        restaurant_details.update({"name" : a['name']})
        restaurant_details.update({"url" : a['url']})
        restaurant_details.update({"location" : a['location']['address']})
        restaurant_details.update({"city" : a['location']['city']})
        restaurant_details.update({"city_ID" : a['location']['city_id']})
        restaurant_details.update({"user_rating" : a['user_rating']['aggregate_rating']})

        restaurant_details = DotDict(restaurant_details)
        return restaurant_details


    def restaurant_search(self, query="", latitude="", longitude="", cuisines="", limit=5):
        """
        Takes either query, latitude and longitude or cuisine as input.
        Returns a list of Restaurant IDs.
        """
        cuisines = "%2C".join(cuisines.split(","))
        if str(limit).isalpha() == True:
            raise ValueError('LimitNotInteger')
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "search?q=" + str(query) + "&count=" + str(limit) + "&lat=" + str(latitude) + "&lon=" + str(longitude) + "&cuisines=" + str(cuisines), headers=headers).content).decode("utf-8")
        return r#a = ast.literal_eval(r)


    def get_location(self, query="", limit=5):
        """
        Takes either query, latitude and longitude or cuisine as input.
        Returns a list of Restaurant IDs.
        """
        if str(limit).isalpha() == True:
            raise ValueError('LimitNotInteger')
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "locations?query=" + str(query) + "&count=" + str(limit), headers=headers).content).decode("utf-8")
        return r

    def restaurant_search_by_keyword(self, query="", cuisines="", limit=5):
        """
        Takes either query, latitude and longitude or cuisine as input.
        Returns a list of Restaurant IDs.
        """
        cuisines = "%2C".join(cuisines.split(","))
        if str(limit).isalpha() == True:
            raise ValueError('LimitNotInteger')
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "search?q=" + str(query) + "&count=" + str(limit) + "&cuisines=" + str(cuisines), headers=headers).content).decode("utf-8")
        return r




    def is_valid_restaurant_id(self, restaurant_ID):
        """
        Checks if the Restaurant ID is valid or invalid.
        If invalid, throws a InvalidRestaurantId Exception.
        """
        restaurant_ID = str(restaurant_ID)
        if restaurant_ID.isnumeric() == False:
            raise ValueError('InvalidRestaurantId')



    def is_valid_city_id(self, city_ID):
        """
        Checks if the City ID is valid or invalid.
        If invalid, throws a InvalidCityId Exception.
        """
        city_ID = str(city_ID)
        if city_ID.isnumeric() == False:
            return True# raise ValueError('InvalidCityId')



    def is_key_invalid(self, a):
        """
        Checks if the API key provided is valid or invalid.
        If invalid, throws a InvalidKey Exception.
        """
        if 'code' in a:
            if a['code'] == 403:
                raise ValueError('InvalidKey')



    def is_rate_exceeded(self, a):
        """
        Checks if the request limit for the API key is exceeded or not.
        If exceeded, throws a ApiLimitExceeded Exception.
        """
        if 'code' in a:
            if a['code'] == 440:
                raise Exception('ApiLimitExceeded')



class DotDict(dict):
    """
    Dot notation access to dictionary attributes
    """

    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
