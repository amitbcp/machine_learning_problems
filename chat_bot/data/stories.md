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
