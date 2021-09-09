## 218_S4_SP46_F_L1_G2_A3-P_L_C
* intent_find_by_price:مجھے ریسٹورنٹ چاہیے جس کی پرائس رینج [ایک ہزار سے دو ہزار](price) تک کے درمیان میں ہو
	- slot{"price":"ایک ہزار سے دو ہزار"}
	- action_find_by_price
* intent_find_by_location:میں لاہور میں [گلبرگ](location) سے کھانا کھانا چاہتی ہوں
	- slot{"price":"ایک ہزار سے دو ہزار"}
	- slot{"location":"گلبرگ"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میں [دیسی](cuisine) کھانا کھانا چاہتی ہوں
	- slot{"price":"ایک ہزار سے دو ہزار"}
	- slot{"location":"گلبرگ"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_cuisine_price
	- action_restart