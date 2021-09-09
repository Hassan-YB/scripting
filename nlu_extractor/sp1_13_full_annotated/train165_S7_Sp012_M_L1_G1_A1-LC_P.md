## train165_S7_Sp012_M_L1_G1_A1-LC_P
* intent_find_by_location_cuisine:جی میں اس وقت [اقبال ٹاؤن](location) میں بیٹھا ہوا ہوں اور میرا [نوڈلز](cuisine) کھانے کو دل کر رہا ہے
	- slot{"location":"اقبال ٹاؤن"}
	- slot{"cuisine":"نوڈلز"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:میری جیب میں اس وقت [سو](price) روپیہ ہے
	- slot{"location":"اقبال ٹاؤن"}
	- slot{"cuisine":"نوڈلز"}
	- slot{"price":"سو"}
	- action_find_by_location_cuisine_price
	- action_restart