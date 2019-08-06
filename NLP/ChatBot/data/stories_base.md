## Generated Story 1749353716521741561
* greet
    - utter_greet
* restaurant_search
    - get_all_search_results
    - slot{"requested_slot": "location"}
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - validate_location
    - slot{"location": "bangalore"}
    - get_all_search_results
    - slot{"location": "bangalore"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - validate_cuisine
    - slot{"cuisine": "south indian"}
    - get_all_search_results
    - slot{"cuisine": "south indian"}
    - slot{"requested_slot": "price"}
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - validate_price
    - slot{"price": "1"}
    - get_all_search_results
    - slot{"price": "1"}
    - action_search_restaurant
    - utter_ask_send_email
* affirm
    - utter_ask_email
* send_email{"email": "sasi.424@gmail.com"}
    - slot{"email": "sasi.424@gmail.com"}
    - action_email
    - action_bye
    - export
	- action_restarted
	
## Generated Story 3042610946877266362
* greet
    - utter_greet
* restaurant_search
    - get_all_search_results
    - slot{"requested_slot": "location"}
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - validate_location
    - slot{"location": "hyderabad"}
    - get_all_search_results
    - slot{"location": "hyderabad"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"cuisine": "North Indian"}
    - get_all_search_results
    - slot{"cuisine": "North Indian"}
    - slot{"requested_slot": "price"}
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - validate_price
    - slot{"price": "1"}
    - get_all_search_results
    - slot{"price": "1"}
    - action_search_restaurant
    - utter_ask_send_email
* affirm
    - utter_ask_email
* send_email{"email": "sasi.424@gmail.com"}
    - slot{"email": "sasi.424@gmail.com"}
    - action_email
    - action_bye
    - export
	- action_restarted
	
## Generated Story -7499154272137865934
* greet
    - utter_greet
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - validate_location
    - slot{"location": "agra"}
    - get_all_search_results
    - slot{"location": "agra"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - validate_cuisine
    - slot{"cuisine": "italian"}
    - get_all_search_results
    - slot{"cuisine": "italian"}
    - slot{"requested_slot": "price"}
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - validate_price
    - slot{"price": "2"}
    - get_all_search_results
    - slot{"price": "2"}
    - action_search_restaurant
    - utter_ask_send_email
* send_email{"email": "sasi.424@gmail.com"}
    - slot{"email": "sasi.424@gmail.com"}
    - action_email
    - action_bye
    - export
	- action_restarted
	
## Generated Story 818358368860359043
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - validate_location
    - slot{"location": "delhi"}
    - get_all_search_results
    - slot{"location": "delhi"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - validate_cuisine
    - slot{"cuisine": "mexican"}
    - get_all_search_results
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "price"}
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - validate_price
    - slot{"price": "3"}
    - get_all_search_results
    - slot{"price": "3"}
    - action_search_restaurant
    - utter_ask_send_email
* deny
    - action_bye
    - export
	- action_restarted
	
## Generated Story 7412757966880175471
* greet
    - utter_greet
* restaurant_search
    - get_all_search_results
    - slot{"requested_slot": "location"}
* restaurant_search
    - validate_location
    - slot{"location": null}
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
	- validate_location
	- slot{"location": "bangalore"}
    - get_all_search_results
    - slot{"location": "bangalore"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - validate_cuisine
    - slot{"cuisine": "chinese"}
    - get_all_search_results
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "price"}
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - validate_price
    - slot{"price": "3"}
    - get_all_search_results
    - slot{"price": "3"}
    - action_search_restaurant
    - utter_ask_send_email
* send_email
    - utter_ask_email
* send_email{"email": "sasi.424@gmail.com"}
    - slot{"email": "sasi.424@gmail.com"}
    - action_email
    - action_bye
    - export
	- action_restarted
	
## Generated Story 4804974383885308612
* greet
    - utter_greet
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - validate_location
    - slot{"location": "hyderabad"}
    - get_all_search_results
    - slot{"location": "hyderabad"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - validate_cuisine
    - slot{"cuisine": null}
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
	- validate_cuisine
	- slot{"cuisine": "south indian"}
    - get_all_search_results
    - slot{"cuisine": "south indian"}
    - slot{"requested_slot": "price"}
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - validate_price
    - slot{"price": "2"}
    - get_all_search_results
    - slot{"price": "2"}
    - action_search_restaurant
    - utter_ask_send_email
* deny
    - action_bye
    - export
	- action_restarted
	
## Generated Story 8861739849947018853
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian", "location": "patna"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "patna"}
    - validate_location
    - slot{"location": "patna"}
    - validate_cuisine
    - slot{"cuisine": "North Indian"}
    - get_all_search_results
    - slot{"location": "patna"}
    - slot{"cuisine": "North Indian"}
    - slot{"requested_slot": "price"}
* restaurant_search
    - validate_price
    - slot{"price": null}
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - validate_price
    - slot{"price": "2"}
    - get_all_search_results
    - slot{"price": "2"}
    - action_search_restaurant
    - utter_ask_send_email
* send_email{"email": "sasi.424@gmail.com"}
    - slot{"email": "sasi.424@gmail.com"}
    - action_email
    - action_bye
    - export
	- action_restarted
	
## Generated Story -4959921469667157198
* greet
    - utter_greet
* restaurant_search{"location": "mumbai", "price": "2"}
    - slot{"location": "mumbai"}
    - slot{"price": "2"}
    - validate_location
    - slot{"location": "mumbai"}
    - validate_price
    - slot{"price": "2"}
    - get_all_search_results
    - slot{"location": "mumbai"}
    - slot{"price": "2"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - get_all_search_results
    - slot{"cuisine": "mexican"}
    - action_search_restaurant
    - utter_ask_send_email
* deny
    - action_bye
    - export
	- action_restarted
	
## Generated Story -6958869715324295342
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "bangalore", "price": "2"}
    - slot{"cuisine": "american"}
    - slot{"location": "bangalore"}
    - slot{"price": "2"}
    - validate_location
    - slot{"location": "bangalore"}
    - validate_cuisine
    - slot{"cuisine": "american"}
    - validate_price
    - slot{"price": "2"}
    - get_all_search_results
    - slot{"location": "bangalore"}
    - slot{"cuisine": "american"}
    - slot{"price": "2"}
    - action_search_restaurant
    - utter_ask_send_email
* affirm
    - utter_ask_email
* send_email{"email": "sasi.424@gmail.com"}
    - slot{"email": "sasi.424@gmail.com"}
    - action_email
    - action_bye
    - export
	- action_restarted
	
## Generated Story 5947965027374950300
* greet
    - utter_greet
* restaurant_search{"location": "hyderabad", "price": "1"}
    - slot{"location": "hyderabad"}
    - slot{"price": "1"}
    - validate_location
    - slot{"location": "hyderabad"}
    - validate_price
    - slot{"price": "1"}
    - get_all_search_results
    - slot{"location": "hyderabad"}
    - slot{"price": "1"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - get_all_search_results
    - slot{"cuisine": "italian"}
    - action_search_restaurant
    - utter_ask_send_email
* deny
    - action_bye
    - export
	- action_restarted
	
## Generated Story -713201081145314067
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "price": "3"}
    - slot{"cuisine": "italian"}
    - slot{"price": "3"}
    - get_all_search_results
    - slot{"cuisine": "italian"}
    - slot{"price": "3"}
    - slot{"requested_slot": "location"}
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - validate_location
    - slot{"location": "chennai"}
    - validate_cuisine
    - slot{"cuisine": "italian"}
    - validate_price
    - slot{"price": "3"}
    - get_all_search_results
    - slot{"location": "chennai"}
    - action_search_restaurant
    - utter_ask_send_email
* send_email{"email": "upgrad12werwer@gmail.com"}
    - slot{"email": "upgrad12@gmail.com"}
    - action_email
    - action_bye
    - export
	- action_restarted

## Generated Story 3155086722976270899
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - get_all_search_results
    - slot{"cuisine": "italian"}
    - slot{"requested_slot": "location"}
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - validate_location
    - slot{"location": "delhi"}
    - validate_cuisine
    - slot{"cuisine": "italian"}
    - get_all_search_results
    - slot{"location": "delhi"}
    - slot{"requested_slot": "price"}
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - validate_price
    - slot{"price": "1"}
    - get_all_search_results
    - slot{"price": "1"}
    - action_search_restaurant
    - utter_ask_send_email
* send_email{"email": "marian12@gmail.com"}
    - slot{"email": "marian12@gmail.com"}
    - action_email
    - action_bye
    - export
	- action_restarted

## Generated Story -1998935842164571076
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian", "location": "hyderabad"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "hyderabad"}
    - validate_location
    - slot{"location": "hyderabad"}
    - validate_cuisine
    - slot{"cuisine": "North Indian"}
    - get_all_search_results
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "North Indian"}
    - slot{"requested_slot": "price"}
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - validate_price
    - slot{"price": "1"}
    - get_all_search_results
    - slot{"price": "1"}
    - action_search_restaurant
    - utter_ask_send_email
* affirm
    - utter_ask_email
* send_email{"email": "john@gmail.com"}
    - slot{"email": "john@gmail.com"}
    - action_email
    - action_bye
    - export
	- action_restarted

## Generated Story 1868904741969810973
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "hyderabad"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "hyderabad"}
    - validate_location
    - slot{"location": "hyderabad"}
    - validate_cuisine
    - slot{"cuisine": "mexican"}
    - get_all_search_results
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "price"}
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - validate_price
    - slot{"price": "3"}
    - get_all_search_results
    - slot{"price": "3"}
    - action_search_restaurant
    - utter_ask_send_email
* affirm
    - utter_ask_email
* send_email{"email": "asrifsumalata.b6@gmail.com"}
    - slot{"email": "asrifsumalata.b6@gmail.com"}
    - action_email
    - utter_goodbye
    - export
	- action_restarted
	
## Generated Story -8468521216288161706
* greet
    - utter_greet
* restaurant_search{"location": "mmbai"}
    - slot{"location": "mmbai"}
    - validate_location
    - slot{"location": "mmbai"}
    - get_all_search_results
    - slot{"location": "mmbai"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"cuisine": "South Indian"}
    - get_all_search_results
    - slot{"cuisine": "South Indian"}
    - slot{"requested_slot": "price"}
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - validate_price
    - slot{"price": "1"}
    - get_all_search_results
    - slot{"price": "1"}
    - action_search_restaurant
    - utter_ask_send_email
* affirm
    - utter_ask_email
* send_email{"email": "sasi673rad@gmail.com"}
    - slot{"email": "sasi673rad@gmail.com"}
    - action_email
    - utter_goodbye
    - export
	- action_restarted

## Generated Story 1770751760018779592
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "allahabad"}
    - slot{"cuisine": "american"}
    - slot{"location": "allahabad"}
    - validate_location
    - slot{"location": "allahabad"}
    - validate_cuisine
    - slot{"cuisine": "american"}
    - get_all_search_results
    - slot{"location": "allahabad"}
    - slot{"cuisine": "american"}
    - slot{"requested_slot": "price"}
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - validate_price
    - slot{"price": "1"}
    - get_all_search_results
    - slot{"price": "1"}
    - action_search_restaurant
    - utter_ask_send_email
* affirm
    - utter_ask_email
* send_email{"email": "sasi.424@gmail.com"}
    - slot{"email": "sasi.424@gmail.com"}
    - action_email
    - slot{"email": "sasi.424@gmail.com"}
    - action_bye
    - reset_slots
    - export
	
## Generated Story -8468521216288161706
* greet
    - utter_greet
* restaurant_search{"location": "jabalpur"}
    - slot{"location": "jabalpur"}
    - validate_location
    - slot{"location": "jabalpur"}
    - get_all_search_results
    - slot{"location": "jabalpur"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - validate_cuisine
    - slot{"cuisine": "american"}
    - get_all_search_results
    - slot{"cuisine": "american"}
    - slot{"requested_slot": "price"}
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - validate_price
    - slot{"price": "1"}
    - get_all_search_results
    - slot{"price": "1"}
    - action_search_restaurant
    - utter_ask_send_email
* affirm
    - utter_ask_email
* send_email{"email": "sasi.424@gmail.com"}
    - slot{"email": "sasi.424@gmail.com"}
    - action_email
    - utter_goodbye
    - export
	- action_restarted

## Generated Story 2182074300828345856
* greet
    - utter_greet
* restaurant_search{"location": "jabalpur"}
    - slot{"location": "jabalpur"}
    - validate_location
    - slot{"location": "jabalpur"}
    - get_all_search_results
    - slot{"location": "jabalpur"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - validate_cuisine
    - slot{"cuisine": "mexican"}
    - get_all_search_results
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "price"}
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - validate_price
    - slot{"price": "2"}
    - get_all_search_results
    - slot{"price": "2"}
    - action_search_restaurant
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_search_restaurant
    - utter_ask_send_email
* deny
    - action_bye
    - reset_slots
    - export
	- action_restarted

## Generated Story -534230361192230185
* greet
    - utter_greet
* restaurant_search
    - get_all_search_results
    - slot{"requested_slot": "location"}
* restaurant_search
    - validate_location
    - slot{"location": null}
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - validate_location
    - slot{"location": "bangalore"}
    - get_all_search_results
    - slot{"location": "bangalore"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search
    - validate_cuisine
    - slot{"cuisine": null}
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - validate_cuisine
    - slot{"cuisine": "chinese"}
    - get_all_search_results
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "price"}
* restaurant_search
    - validate_price
    - slot{"price": null}
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - validate_price
    - slot{"price": "1"}
    - get_all_search_results
    - slot{"price": "1"}
    - action_search_restaurant
    - utter_ask_send_email
* affirm
    - utter_ask_email
* send_email{"email": "sasi.424@gmail.com"}
    - slot{"email": "sasi.424@gmail.com"}
    - action_email
    - slot{"email": "sasi.424@gmail.com"}
    - utter_goodbye
	- reset_slots
    - export
	- action_restarted

## Generated Story 5043863906147771821
* greet
    - utter_greet
* restaurant_search{"location": "visakhapatnam"}
    - slot{"location": "visakhapatnam"}
    - validate_location
    - slot{"location": "visakhapatnam"}
    - get_all_search_results
    - slot{"location": "visakhapatnam"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - validate_cuisine
    - slot{"cuisine": "south indian"}
    - get_all_search_results
    - slot{"cuisine": "south indian"}
    - slot{"requested_slot": "price"}
* restaurant_search
    - validate_price
    - slot{"price": null}
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - validate_price
    - slot{"price": "2"}
    - get_all_search_results
    - slot{"price": "2"}
    - action_search_restaurant
    - utter_ask_send_email
* affirm
    - utter_ask_email
* restaurant_search
    - action_email
    - slot{"email": null}
* send_email{"email": "sasi.424@gmail.com"}
    - slot{"email": "sasi.424@gmail.com"}
    - action_email
    - slot{"email": "sasi.424@gmail.com"}
    - utter_goodbye
	- reset_slots
    - export
	- action_restarted
	
## Generated Story 1086234191541999019
* greet
    - utter_greet
* restaurant_search
    - get_all_search_results
    - slot{"requested_slot": "location"}
* send_email
    - validate_location
    - slot{"location": null}
* send_email{"location": "nellore"}
    - slot{"location": "nellore"}
    - validate_location
    - slot{"location": "nellore"}
    - get_all_search_results
    - slot{"location": "nellore"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - validate_cuisine
    - slot{"cuisine": "south indian"}
    - get_all_search_results
    - slot{"cuisine": "south indian"}
    - slot{"requested_slot": "price"}
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - validate_price
    - slot{"price": "1"}
    - get_all_search_results
    - slot{"price": "1"}
    - action_search_restaurant
    - utter_ask_send_email
* deny
    - action_bye
    - reset_slots
    - export

## Generated Story -7626790259110895065
* greet
    - utter_greet
* restaurant_search
    - get_all_search_results
    - slot{"requested_slot": "location"}
* affirm{"location": "agra"}
    - slot{"location": "agra"}
    - validate_location
    - slot{"location": "agra"}
    - get_all_search_results
    - slot{"location": "agra"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - validate_cuisine
    - slot{"cuisine": "mexican"}
    - get_all_search_results
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "price"}
* restaurant_search
    - validate_price
    - slot{"price": null}
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - validate_price
    - slot{"price": "2"}
    - get_all_search_results
    - slot{"price": "2"}
    - action_search_restaurant
    - utter_ask_send_email
* send_email{"email": "23122124"}
    - slot{"email": "23122124"}
    - action_email
    - slot{"email": "23122124"}
* send_email{"email": "sasi.424@gmail.com"}
    - slot{"email": "sasi.424@gmail.com"}
    - action_email
    - slot{"email": "sasi.424@gmail.com"}
    - action_bye
    - reset_slots
    - export
	- action_restarted

## Generated Story 9131826395850737704
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - validate_location
    - slot{"location": "mumbai"}
    - get_all_search_results
    - slot{"location": "mumbai"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - validate_cuisine
    - slot{"cuisine": "south indian"}
    - get_all_search_results
    - slot{"cuisine": "south indian"}
    - slot{"requested_slot": "price"}
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - validate_price
    - slot{"price": "1"}
    - get_all_search_results
    - slot{"price": "1"}
    - action_search_restaurant
    - utter_ask_send_email
* affirm
    - utter_ask_email
* restaurant_search
    - action_email
    - slot{"email": null}
* send_email{"email": "sasi.424@gmail.com"}
    - slot{"email": "sasi.424@gmail.com"}
    - action_email
    - slot{"email": "sasi.424@gmail.com"}
    - utter_goodbye
    - reset_slots
    - export
	- action_restarted

## Generated Story -4181568588208725183
* greet
    - utter_greet
* restaurant_search
    - validate_location
    - slot{"location": null}
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - validate_location
    - slot{"location": "allahabad"}
    - get_all_search_results
    - slot{"location": "allahabad"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - validate_cuisine
    - slot{"cuisine": "chinese"}
    - get_all_search_results
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "price"}
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - validate_price
    - slot{"price": "3"}
    - get_all_search_results
    - slot{"price": "3"}
    - action_search_restaurant
    - utter_ask_send_email
* affirm
    - utter_ask_email
* send_email{"email": "sasi.424@gmail.com"}
    - slot{"email": "sasi.424@gmail.com"}
    - action_email
    - slot{"email": "sasi.424@gmail.com"}
    - action_bye
    - reset_slots
    - export
	- action_restarted
	
## Generated Story 2867671120161483336
* greet
    - utter_greet
* restaurant_search
    - get_all_search_results
    - slot{"requested_slot": "location"}
* restaurant_search{"location": "Visakhapatnam"}
    - slot{"location": "Visakhapatnam"}
    - validate_location
    - slot{"location": "Visakhapatnam"}
    - get_all_search_results
    - slot{"location": "Visakhapatnam"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - validate_cuisine
    - slot{"cuisine": "mexican"}
    - get_all_search_results
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "price"}
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - validate_price
    - slot{"price": "1"}
    - get_all_search_results
    - slot{"price": "1"}
    - action_search_restaurant
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_search_restaurant
    - utter_ask_send_email
* deny
    - action_bye
    - reset_slots
    - export
	- action_restarted
	
## Generated Story -8312113386869263583
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - validate_location
    - slot{"location": null}
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - validate_location
    - slot{"location": "allahabad"}
    - get_all_search_results
    - slot{"location": "allahabad"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - validate_cuisine
    - slot{"cuisine": "chinese"}
    - get_all_search_results
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "price"}
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - validate_price
    - slot{"price": "3"}
    - get_all_search_results
    - slot{"price": "3"}
    - action_search_restaurant
    - utter_ask_send_email
* affirm
    - utter_ask_email
* restaurant_search{"email": "sasi.424@gmail.com"}
    - slot{"email": "sasi.424@gmail.com"}
    - action_email
    - slot{"email": "sasi.424@gmail.com"}
    - action_bye
    - reset_slots
    - export
	- action_restarted

## Generated Story 4562113386869263583

* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - validate_location
    - slot{"location": null}
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - validate_location
    - slot{"location": "allahabad"}
    - get_all_search_results
    - slot{"location": "allahabad"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - validate_cuisine
    - slot{"cuisine": "chinese"}
    - get_all_search_results
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "price"}
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - validate_price
    - slot{"price": "3"}
    - get_all_search_results
    - slot{"price": "3"}
    - action_search_restaurant
    - utter_ask_send_email
* deny
    - action_bye
    - reset_slots
    - export
	- action_restarted

## Generated Story 232787386869263583
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - validate_location
    - slot{"location": null}
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - validate_location
    - slot{"location": "allahabad"}
    - get_all_search_results
    - slot{"location": "allahabad"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - validate_cuisine
    - slot{"cuisine": "chinese"}
    - get_all_search_results
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "price"}
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - validate_price
    - slot{"price": "3"}
    - get_all_search_results
    - slot{"price": "3"}
    - action_search_restaurant
    - utter_ask_email
* restaurant_search{"email": "sasi.424@yahoo.com"}
    - slot{"email": "sasi.424@yahoo.com"}
    - action_email
    - slot{"email": "sasi.424@yahoo.com"}
    - action_bye
    - reset_slots
    - export
	- action_restarted










