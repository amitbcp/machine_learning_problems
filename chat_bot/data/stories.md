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
* affirm
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
* affirm
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
* affirm
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
* affirm
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
* affirm
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
* affirm
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
* affirm
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
* affirm
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
* affirm
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
* affirm
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
* stop
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
* affirm
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
* affirm
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
* affirm
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
* goodbye
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
* goodbye
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
* goodbye
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

## interactive_story 24_invalid_loc_invalid_cuisine
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
* affirm
    - utter_goodbye
    - action_restart

## interactive_story 25_cuisine_budget
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
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story 26_good_case
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
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story 27
* greet
    - utter_greet
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
* stop
    - utter_goodbye
    - action_restart

## interactive_story 28
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
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story 28 hi-bye
* greet
    - utter_greet
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story 29
* restaurant_search
    - utter_ask_location
* restaurant_search
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
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "a@a.com"}
    - slot{"email": "a@a.com"}
    - action_send_email
    - utter_confirm_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story 30
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* stop
* restaurant_search{"budget": "50"}
    - slot{"budget": "50"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* affirm
    - utter_ask_email
* get_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_send_email
    - utter_confirm_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story 31
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_invalid
    - utter_ask_location
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_invalid
    - utter_ask_location
* stop
    - utter_goodbye
    - action_restart

## interactive_story 32
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
* greet
    - utter_greet
* restaurant_search{"location": "alibaug"}
    - slot{"location": "alibaug"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_invalid
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* affirm
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "a@gmail.com"}
    - slot{"email": "a@gmail.com"}
    - action_send_email
    - utter_confirm_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story 33
* restaurant_search{"budget": "50", "cuisine": "mexican"}
    - slot{"budget": "50"}
    - slot{"cuisine": "mexican"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
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
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story 34
* restaurant_search{"budget": "299", "location": "Bengaluru"}
    - slot{"budget": "299"}
    - slot{"location": "Bengaluru"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* affirm
    - utter_get_budget
* get_budget{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "amit@gmail.com"}
    - slot{"email": "amit@gmail.com"}
    - action_send_email
    - utter_confirm_email
* stop
    - utter_goodbye
    - action_restart

## interactive_story 34
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "50"}
    - slot{"budget": "50"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_cuisine
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* affirm
    - utter_get_budget
* get_budget{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - utter_confirm_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story 35
* get_budget{"budget": "299"}
    - slot{"budget": "299"}
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* restaurant_search
    - utter_search_invalid_location
* affirm
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
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
* goodbye
    - utter_goodbye
    - action_restart


## interactive_story 36
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story 37
* restaurant_search{"budget": "299", "location": "delhi"}
    - slot{"budget": "299"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* restaurant_search
    - utter_search_invalid_cuisine
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* stop
    - utter_search_invalid_cuisine
* restaurant_search
    - utter_search_invalid_location
* affirm
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* affirm
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "a@abc.com"}
    - slot{"email": "a@abc.com"}
    - action_send_email
    - utter_confirm_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story 38
* restaurant_search{"cuisine": "chinese", "budget": "10", "location": "chennai"}
    - slot{"budget": "10"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chennai"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* affirm
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - utter_confirm_email
* stop
    - utter_goodbye
    - action_restart


## interactive_story 39
* restaurant_search{"cuisine": "italian", "location": "nepal"}
    - slot{"cuisine": "italian"}
    - slot{"location": "nepal"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_invalid
    - utter_location_retry
* affirm
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
* stop
    - utter_goodbye
    - action_restart

## interactive_story 40
* restaurant_search{"budget": "299", "cuisine": "american", "location": "Chennai"}
    - slot{"budget": "299"}
    - slot{"cuisine": "american"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_cuisine
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "amit@gmail.com"}
    - slot{"email": "amit@gmail.com"}
    - action_send_email
    - utter_confirm_email
* stop
    - utter_goodbye
    - action_restart

## interactive_story 41
* restaurant_search{"location": "India"}
    - slot{"location": "India"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_retry
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
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
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
* get_email{"email": "amit@gmail.com"}
    - slot{"email": "amit@gmail.com"}
    - action_send_email
    - utter_confirm_email
* stop
    - utter_goodbye
    - action_restart

* greet
    - utter_greet
* restaurant_search{"location": "nerul"}
    - slot{"location": "nerul"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_invalid
* affirm

## interactive_story 42
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
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
* stop
    - utter_goodbye
    - action_restart

## interactive_story 43
* greet
    - utter_greet
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
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story 44
- utter_greet
* greet
    - utter_greet
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
* get_email{"email": "ishant30oct@gmail.com"}
    - slot{"email": "ishant30oct@gmail.com"}
    - action_send_email
    - utter_confirm_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story 45
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
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
* stop
    - utter_goodbye
    - action_restart

## interactive_story 46
- utter_greet
* greet
    - utter_greet
* restaurant_search{"location": "south delhi"}
    - slot{"location": "south delhi"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_invalid
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
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
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "a.pranshu15@gmail.com"}
    - slot{"email": "a.pranshu15@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart

## interactive_story 47
- utter_greet
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story 48
* greet
    - utter_greet
* restaurant_search{"location": "pune", "cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "pune"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_location_valid
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
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
* affirm
    - utter_goodbye
    - action_restart

## interactive_story 49
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "Bengaluru"}
    - slot{"cuisine": "american"}
    - slot{"location": "Bengaluru"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_location_valid
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "Bengaluru"}
    - slot{"cuisine": "american"}
    - slot{"location": "Bengaluru"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_location_valid
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "amit.pinaki@gmail.com"}
    - slot{"email": "amit.pinaki@gmail.com"}
    - action_send_email
    - utter_confirm_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story 50
* affirm
    - utter_greet
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "ishant30oct@gmail.com"}
    - slot{"email": "ishant30oct@gmail.com"}
    - action_send_email
    - utter_confirm_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story 51
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
* get_budget{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
    - utter_ask_email
* get_email{"email": "a.pranshu15@gmail.com"}
    - slot{"email": "a.pranshu15@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart


## interactive_story 52
* greet
    - utter_greet
* restaurant_search{"cuisine": "indian", "location": "Kolkata"}
    - slot{"cuisine": "indian"}
    - slot{"location": "Kolkata"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "invalid"}
    - utter_cuisine_invalid
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "amit.pinaki@gmail.com"}
    - slot{"email": "amit.pinaki@gmail.com"}
    - action_send_email
    - utter_confirm_email
* affirm
    - utter_goodbye
    - action_restart


## interactive_story 54
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
    - utter_ask_location
* restaurant_search{"location": "Bengaluru"}
    - slot{"location": "Bengaluru"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
* get_email
    - utter_ask_email
* get_email{"email": "ishant30oct@gmail.com"}
    - slot{"email": "ishant30oct@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart


## interactive_story 55
* restaurant_search{"location": "Hyderabad", "cuisine": "american"}
    - slot{"cuisine": "american"}
    - slot{"location": "Hyderabad"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* affirm
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
* affirm
    - utter_goodbye
    - action_restart


## interactive_story 56
* restaurant_search{"cuisine": "mexican", "location": "delhi"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "delhi"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
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
* restaurant_search{"cuisine": "mexican", "location": "hyderbad"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "hyderbad"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_location_valid
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "Hyderabad"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Hyderabad"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_location_valid
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "Hyderabad"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Hyderabad"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_location_valid
    - utter_get_budget
* get_budget{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
    - utter_ask_email
* stop
    - utter_goodbye
    - action_restart

## interactive_story 57
* restaurant_search{"cuisine": "indian"}
    - slot{"cuisine": "indian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "invalid"}
    - utter_cuisine_invalid
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* get_budget
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

## interactive_story 58
* restaurant_search{"budget": "299", "cuisine": "mexican", "location": "pune"}
    - slot{"budget": "299"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* affirm
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "amit.@gmail.com"}
    - slot{"email": "amit.@gmail.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart

## interactive_story 59
* restaurant_search{"cuisine": "chinese", "location": "nagar"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "nagar"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_invalid
    - utter_location_retry
* restaurant_search{"location": "tilak nagar, delhi"}
    - slot{"location": "tilak nagar, delhi"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_invalid
    - utter_location_retry
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* restaurant_search
    - utter_search_invalid_cuisine
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "a@abc.com"}
    - slot{"email": "a@abc.com"}
    - action_send_email
    - utter_confirm_email
    - utter_goodbye
    - action_restart

## interactive_story 60
* restaurant_search{"budget": "299", "cuisine": "mexican", "location": "Chennai"}
    - slot{"budget": "299"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story 61
* restaurant_search{"budget": "299", "cuisine": "american", "location": "Chennai"}
    - slot{"budget": "299"}
    - slot{"cuisine": "american"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_cuisine
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* restaurant_search{"stop": "no"}
    - utter_search_invalid_location
* affirm
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_cuisine
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* affirm
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story 61
* restaurant_search{"budget": "299", "cuisine": "mexican", "location": "Kolkata"}
    - slot{"budget": "299"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_cuisine
* restaurant_search{"stop": "no"}
    - utter_search_invalid_budget
* affirm
    - utter_get_budget
* get_budget{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story 63
* restaurant_search{"budget": "299", "cuisine": "mexican"}
    - slot{"budget": "299"}
    - slot{"cuisine": "mexican"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story 64
* restaurant_search{"budget": "299", "location": "Kolkata"}
    - slot{"budget": "299"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_cuisine
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* restaurant_search{"stop": "no"}
    - utter_search_invalid_location
* affirm
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_cuisine
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story 65
* restaurant_search{"budget": "701", "cuisine": "chinese", "location": "delhi"}
    - slot{"budget": "701"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
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
* affirm
    - utter_goodbye
    - action_restart

## interactive_story 66
* restaurant_search{"budget": "299", "location": "delhi"}
    - slot{"budget": "299"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "a@a.com"}
    - slot{"email": "a@a.com"}
    - action_send_email
    - utter_confirm_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story 67
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "a@abc.com"}
    - slot{"email": "a@abc.com"}
    - action_send_email
    - utter_confirm_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story 68
* restaurant_search{"budget": "299", "cuisine": "chinese", "location": "Kolkata"}
    - slot{"budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* affirm
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "a@abc.com"}
    - slot{"email": "a@abc.com"}
    - action_send_email
    - utter_confirm_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story 69
* restaurant_search{"budget": "299", "cuisine": "american", "location": "Kolkata"}
    - slot{"budget": "299"}
    - slot{"cuisine": "american"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "a@abc.com"}
    - slot{"email": "a@abc.com"}
    - action_send_email
    - utter_confirm_email
* stop
    - utter_goodbye
    - action_restart

## interactive_story 70
* restaurant_search{"budget": "299", "cuisine": "american", "location": "delhi"}
    - slot{"budget": "299"}
    - slot{"cuisine": "american"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_cuisine
* restaurant_search
    - utter_search_invalid_budget
* affirm
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "a@gmail.com"}
    - slot{"email": "a@gmail.com"}
    - action_send_email
    - utter_confirm_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story 71
* restaurant_search{"budget": "299", "cuisine": "mexican", "location": "pune"}
    - slot{"budget": "299"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* stop
    - utter_search_invalid_location
* affirm
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* affirm
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "a@abc.com"}
    - slot{"email": "a@abc.com"}
    - action_send_email
    - utter_confirm_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story 72
* greet
    - utter_greet
* restaurant_search{"budget": "701", "cuisine": "chinese", "location": "Kolkata"}
    - slot{"budget": "701"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "a@abc.vom"}
    - slot{"email": "a@abc.vom"}
    - action_send_email
    - utter_confirm_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story 73
* restaurant_search{"cuisine": "chinese", "location": "nepal"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "nepal"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_invalid
    - utter_location_retry
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
* get_email{"email": "amit.pinaki@gmail.com"}
    - slot{"email": "amit.pinaki@gmail.com"}
    - action_send_email
    - utter_confirm_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story 74
* restaurant_search{"cuisine": "chinese", "location": "Kolkata"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kolkata"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "a@a.com"}
    - slot{"email": "a@a.com"}
    - action_send_email
    - utter_confirm_email
* stop
    - utter_goodbye
    - action_restart

## interactive_story 75
* restaurant_search{"location": "Kolkata", "cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kolkata"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* restaurant_search
    - utter_search_invalid_cuisine
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "a@a.com"}
    - slot{"email": "a@a.com"}
    - action_send_email
    - utter_confirm_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story 76
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_ask_location
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "a@a.com"}
    - slot{"email": "a@a.com"}
    - action_send_email
    - utter_confirm_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story 77
* restaurant_search{"cuisine": "chinese", "location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* restaurant_search
    - utter_search_invalid_cuisine
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* affirm
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_send_email
    - utter_confirm_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story 78
* restaurant_search{"budget": "299", "cuisine": "chinese", "location": "kolakta"}
    - slot{"budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "kolakta"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_invalid
    - utter_location_retry
* affirm
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* affirm
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story 79
* restaurant_search{"budget": "299", "cuisine": "chinese"}
    - slot{"budget": "299"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* stop{"stop": "no"}
    - utter_search_invalid_cuisine
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* affirm
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story 80
* restaurant_search{"budget": "299", "cuisine": "chinese", "location": "kolkaaata"}
    - slot{"budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "kolkaaata"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_invalid
    - utter_location_retry
* stop{"stop": "no"}
    - utter_goodbye
    - action_restart

## interactive_story 81
* restaurant_search{"budget": "299", "cuisine": "chinese", "location": "kolakata"}
    - slot{"budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "kolakata"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_invalid
    - utter_location_retry
* affirm
    - utter_ask_location
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story 82
* restaurant_search{"budget": "299", "cuisine": "american", "location": "Mumbai"}
    - slot{"budget": "299"}
    - slot{"cuisine": "american"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* stop{"stop": "no"}
    - utter_search_invalid_cuisine
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* affirm
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* stop
    - utter_goodbye
    - action_restart

## interactive_story 83
* restaurant_search{"budget": "299", "cuisine": "chinese", "location": "Kolkata"}
    - slot{"budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_cuisine
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* affirm
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_send_email
    - utter_confirm_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story 84
* greet
    - utter_greet
* restaurant_search{"budget": "701", "cuisine": "chinese", "location": "Kolkata"}
    - slot{"budget": "701"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
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
* affirm
    - utter_goodbye
    - action_restart

## interactive_story 85
* restaurant_search{"budget": "299", "cuisine": "american", "location": "alibag"}
    - slot{"budget": "299"}
    - slot{"cuisine": "american"}
    - slot{"location": "alibag"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_invalid
    - utter_location_retry
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* affirm
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "a@a.com"}
    - slot{"email": "a@a.com"}
    - action_send_email
    - utter_confirm_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story 86
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "a@a.com"}
    - slot{"email": "a@a.com"}
    - action_send_email
    - utter_confirm_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story 87
* restaurant_search{"location": "alibag", "budget": "299", "cuisine": "chinese"}
    - slot{"budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "alibag"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_invalid
    - utter_location_retry
* affirm
    - utter_ask_location
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "a@a.com"}
    - slot{"email": "a@a.com"}
    - action_send_email
    - utter_confirm_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story 88
* restaurant_search{"budget": "299", "cuisine": "american", "location": "Kolkata"}
    - slot{"budget": "299"}
    - slot{"cuisine": "american"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* get_email{"email": "a@a.com"}
    - slot{"email": "a@a.com"}
    - action_send_email
    - utter_confirm_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story 89
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "china"}
    - slot{"location": "china"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_invalid
    - utter_location_retry
* affirm
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
* get_email{"email": "a@a.com"}
    - slot{"email": "a@a.com"}
    - action_send_email
    - utter_confirm_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story 90
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_ask_location
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
    - utter_ask_email
* restaurant_search
    - utter_search_invalid_cuisine
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story 91
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}

## interactive_story 92
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_invalid
    - utter_location_retry
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* get_budget{"budget": "500"}
    - slot{"budget": "500"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story 93
* restaurant_search{"cuisine": "chinese", "location": "Chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Chandigarh"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story 94
* restaurant_search{"budget": "299", "cuisine": "chinese", "location": "Kolkata"}
    - slot{"budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"check_search_validity": "invalid"}
    - slot{"email_message": "Sorry No Resturants Found !!"}
    - utter_search_invalid_budget
* stop{"stop": "no. thanks"}
    - utter_search_invalid_cuisine
* stop
    - utter_search_invalid_location
* stop
    - utter_goodbye
    - action_restart

## interactive_story 95
* restaurant_search{"cuisine": "chinese", "location": "Chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Chandigarh"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* stop{"stop": "no"}
    - utter_goodbye
    - action_restart

## interactive_story 96
* restaurant_search{"cuisine": "chinese", "location": "Kolkata"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kolkata"}
    - action_cuisine_valid
    - slot{"check_cuisine_validity": "valid"}
    - action_check_location
    - slot{"check_location_validity": "valid"}
    - utter_get_budget
* get_budget{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* stop{"stop": "no"}
    - utter_goodbye
    - action_restart

## interactive_story 97
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
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
    - slot{"check_search_validity": "valid"}
    - slot{"email_message": ""}
    - utter_ask_email
* stop{"stop": "no"}
    - utter_goodbye
    - action_restart

## interactive_story 98
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
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
* stop
    - utter_goodbye
    - action_restart

## interactive_story 99
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"check_location_validity": "invalid"}
    - utter_location_retry
* affirm
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
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
* get_email{"email": "a@a.com"}
    - slot{"email": "a@a.com"}
    - action_send_email
    - utter_confirm_email
* affirm
    - utter_goodbye
    - action_restart
