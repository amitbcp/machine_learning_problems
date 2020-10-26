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

## interactive_story 18_location_provided_invalid
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

## interactive_story 19_location_provided_invalid
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
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_get_budget
* get_budget{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* stop{"stop": "no dont want to"}
    - utter_goodbye
    - action_restart

* greet
    - utter_greet
* restaurant_search{"location": "pune", "cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "pune"}
    - action_check_location
    - action_cuisine_valid
    - action_location_valid
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - action_cuisine_valid
    - action_check_location
    - action_cuisine_valid
    - action_check_location
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - utter_ask_email
    - utter_ask_email
* stop{"stop": "no"}
    - utter_goodbye
    - action_restart

* greet
    - utter_greet

## interactive_story 20_budget_location_provided
* restaurant_search{"budget": "500", "location": "Kolkata"}
    - slot{"budget": "500"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "amit.pinaki@gmail.com"}
    - slot{"email": "amit.pinaki@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart

## interactive_story 20_invalid_location_provided
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangladesh"}
    - slot{"location": "bangladesh"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_invalid
    - utter_ask_location
* restaurant_search{"location": "kashmiri"}
    - slot{"location": "kashmiri"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_invalid
    - utter_ask_location
* stop
    - utter_goodbye
    - action_restart

## interactive_story 21_invalid_location_retry
* restaurant_search{"budget": "299", "cuisine": "chinese"}
    - slot{"budget": "299"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "india"}
    - slot{"location": "india"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_invalid
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart

## interactive_story 20_invalid_cusine_invalid_location_provided
* restaurant_search{"cuisine": "ita", "location": "delli"}
    - slot{"cuisine": "ita"}
    - slot{"location": "delli"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "invalid"}
    - utter_cuisine_invalid
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_ask_location
* restaurant_search{"location": "usa"}
    - slot{"location": "usa"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_invalid
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "amit.p@gmail.com"}
    - slot{"email": "amit.p@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart

## interactive_story 20_unhappy_results_redo_search
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* restaurant_search
    - utter_ask_howcanhelp
* get_budget
    - utter_get_budget
* get_budget{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* restaurant_search{"stop": "no"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
* get_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart

## interactive_story 21_budget_first
* restaurant_search{"budget": "200"}
    - slot{"budget": "200"}
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "a@gmail.com"}
    - slot{"email": "a@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart

## interactive_story 22_budget_location
* restaurant_search{"budget": "400"}
    - slot{"budget": "400"}
    - utter_ask_location
* restaurant_search{"location": "patna"}
    - slot{"location": "patna"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* stop{"stop": "no"}
    - utter_goodbye
    - action_restart

## interactive_story 23_resend_email
* restaurant_search{"cuisine": "chinese", "budget": "400"}
    - slot{"budget": "400"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "amit.pinaki@gmail.com"}
    - slot{"email": "amit.pinaki@gmail.com"}
    - action_send_email
    - utter_confirm_email
* get_email
    - action_send_email
    - utter_confirm_email
* affirm
    - utter_goodbye
    - action_restart

* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "alibaug"}
    - slot{"cuisine": "american"}
    - slot{"location": "alibaug"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "invalid"}
    - utter_cuisine_invalid
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "invalid"}
    - utter_ask_location
* restaurant_search{"location": "japan"}
    - slot{"location": "japan"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_invalid
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "invalid"}
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_goodbye
    - action_restart

* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "701"}
    - slot{"budget": "701"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "ishant30oct@gmail.com"}
    - slot{"email": "ishant30oct@gmail.com"}
    - action_send_email
    - utter_confirm_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "Bengaluru"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "Bengaluru"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_location_valid
* restaurant_search
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - utter_ask_email
    - utter_ask_email
* get_email{"email": "amit.pinaki@gmail.com"}
    - slot{"email": "amit.pinaki@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart

* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "a.pranshu15@gmail.com"}
    - slot{"email": "a.pranshu15@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart

* greet
    - utter_greet
* restaurant_search
    - action_ask_restaurant
* restaurant_search

* restaurant_search
    - utter_ask_location
    - utter_ask_location
* restaurant_search{"location": "Bengaluru"}
    - slot{"location": "Bengaluru"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
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

* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "amit.pinaki@gmail.com"}
    - slot{"email": "amit.pinaki@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart
