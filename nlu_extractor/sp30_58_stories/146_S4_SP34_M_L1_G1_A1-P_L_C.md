## 146_S4_SP34_M_L1_G1_A1-P_L_C
* intent_find_by_price:میری پرائس رینج [پانچ سو](price) سے نیچے ہے
	- slot{"price":"پانچ سو"}
	- action_find_by_price
* intent_find_by_location:میں [یو ای ٹی](location) سے کے قریب کوئی ریسٹورنٹس ہے وہاں پہ کھانا کھانا چاہتا ہوں
	- slot{"price":"پانچ سو"}
	- slot{"location":"یو ای ٹی"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:[چائنیز](cuisine)
	- slot{"price":"پانچ سو"}
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_cuisine_price
	- action_restart