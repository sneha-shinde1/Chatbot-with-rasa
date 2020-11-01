## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
  
## find department
* find_department
  - utter_count_of_department
  
## find department name
* find_name_of_dep
  - utter_names_of_department
  
## college status 
* College_status
  - utter_show_status
  
## time zone of city
* find_timezone_for_location
  - utter_find_time
  
## ask city
* find_timezone
  - utter_ask_city
* city_info
 - utter_find_time 
 - action_show time_zone