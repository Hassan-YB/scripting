## 239_S2_SP48_F_L2_G1_A4-P_C_L
* intent_find_by_price:میری :م: پرائس رینج :م: [پانچ سو سے ہزار](price) ہے
	- slot{"price":"پانچ سو سے ہزار"}
	- action_find_by_price
* intent_find_by_cuisine:مجھے [ٹریڈیشنل](cuisine) کھانا کھانا ہے
	- slot{"price":"پانچ سو سے ہزار"}
	- slot{"cuisine":"ٹریڈیشنل"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:مجھے [برکت مارکیٹ](location) سے کھانا کھانا ہے
	- slot{"price":"پانچ سو سے ہزار"}
	- slot{"cuisine":"ٹریڈیشنل"}
	- slot{"location":"برکت مارکیٹ"}
	- action_find_by_location_cuisine_price
	- action_restart