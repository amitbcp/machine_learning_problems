<!-- markdownlint-disable -->
## interactive_story 1_cuisine_location_budget_provided
* restaurant_search{"cuisine": "chinese", "location": "Kolkata", "budget": "700"}
    - slot{"budget": "700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "amit.pinaki@gmail.com"}
    - slot{"email": "amit.pinaki@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart

## interactive_story 2_full_conversation
* greet
    - utter_greet
* restaurant_search{"location": "Bengaluru"}
    - slot{"location": "Bengaluru"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "amit.pinaki@gmail.com"}
    - slot{"email": "amit.pinaki@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart

## interactive_story 3_full_conversation
* greet
    - utter_greet
* restaurant_search
    - action_ask_restaurant
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - utter_ask_email
* get_email{"email": "ishant30oct@gmail.com"}
    - slot{"email": "ishant30oct@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart

## interactive_story 5_full_conversation
* greet
    - utter_greet
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "invalid"}
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "invalid"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "invalid"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "ishant30oct@gmail.com"}
    - slot{"email": "ishant30oct@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story 4_full_conversation
* greet    
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_ask_location
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"email_message": ""}
    - utter_ask_email
    - utter_ask_email
* get_email{"email": "ishant30oct@gmail.com"}
    - slot{"email": "ishant30oct@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart

## interactive_story 5_location_provided
* greet
    - utter_greet
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "ishant30oct@gmail.com"}
    - slot{"email": "ishant30oct@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart

## interactive_story 6_location_provided
* greet
    - utter_greet
* affirm
    - utter_greet
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - utter_ask_email
* get_email{"email": "ishant30oct@gmail.com"}
    - slot{"email": "ishant30oct@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart

## interactive_story 7_location_provided
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "ishant30oct@gmail.com"}
    - slot{"email": "ishant30oct@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart

## interactive_story 8_location_provided
* greet
    - utter_greet
* restaurant_search{"location": "Bhopal"}
    - slot{"location": "Bhopal"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "ishant30oct@gmail.com"}
    - slot{"email": "ishant30oct@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart
