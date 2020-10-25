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

## interactive_story 9_location_provided
* greet
    - utter_greet
* restaurant_search{"location": "raipur"}
    - slot{"location": "raipur"}
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
    - utter_ask_email
* get_email{"email": "amit.pinaki@gmail.com"}
    - slot{"email": "amit.pinaki@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart

## interactive_story 10_location_provided
* greet
    - utter_greet
* restaurant_search{"location": "patna"}
    - slot{"location": "patna"}
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
* get_email{"email": "amit.pinaki@gmail.com"}
    - slot{"email": "amit.pinaki@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart

## interactive_story 11_location_provided
* greet
    - utter_greet
* restaurant_search{"location": "banglore"}
    - slot{"location": "banglore"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
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
    - utter_ask_email
    - utter_ask_email
* get_email{"email": "amit.pinaki@gmail.com"}
    - slot{"email": "amit.pinaki@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart

## interactive_story 12_location_provided
* greet
    - utter_greet
* restaurant_search{"location": "Chandigarh"}
    - slot{"location": "Chandigarh"}
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
* get_email{"email": "amit.pinaki@gmail.com"}
    - slot{"email": "amit.pinaki@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart

## interactive_story 13_location_provided
* greet
    - utter_greet
* restaurant_search{"location": "ahmednagar"}
    - slot{"location": "ahmednagar"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - action_restart

## interactive_story 14_location_provided
* greet
    - utter_greet
* restaurant_search{"location": "ahmednagar"}
    - slot{"location": "ahmednagar"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_invalid
* restaurant_search{"location": "bhilai"}
    - slot{"location": "bhilai"}
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
* get_email{"email": "amit.pinaki@gmail.com"}
    - slot{"email": "amit.pinaki@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart

## interactive_story 15_location_provided
* restaurant_search{"location": "nerul"}
    - slot{"location": "nerul"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_cuisine_invalid
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
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
* get_email{"email": "amit.pinaki@gmail.com"}
    - slot{"email": "amit.pinaki@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart

## interactive_story 16_location_provided
* greet
    - utter_greet
* restaurant_search{"location": "nerul"}
    - slot{"location": "nerul"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_invalid
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
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
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "ishant30oct@gmail.com"}
    - slot{"email": "ishant30oct@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart

## interactive_story 17_location_provided
* greet
    - utter_greet
* restaurant_search{"location": "nerul"}
    - slot{"location": "nerul"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_invalid
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
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
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_goodbye
    - action_restart

## interactive_story 18_location_provided
* greet
    - utter_greet
* restaurant_search{"location": "panvel"}
    - slot{"location": "panvel"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_invalid
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_get_budget
* get_budget{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "ishant30oct@gmail.com"}
    - slot{"email": "ishant30oct@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart
