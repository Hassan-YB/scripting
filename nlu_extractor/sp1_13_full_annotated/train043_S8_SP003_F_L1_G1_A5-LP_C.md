## train043_S8_SP003_F_L1_G1_A5-LP_C
* greet:السلام و علیکم
	- utter_salaam
* intent_find_by_location_price:جی میرے پاس [پانچ سو](price) روپے ہیں. اور میں لاہور [اچھرہ](location) میں کھڑی ہوں ٹھیک ہے ادھر نزدیک کون سا ایسا ریسٹورنٹ ہے جہاں  مجھے پانچ سو روپے کی قیمت میں کچھ اچھا کھانے کو ملے گا یا کوئی اچھا ریسٹورنٹ پاس ہے ۔
	- slot{"price":"پانچ سو"}
	- slot{"location":"اچھرہ"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:جی میں [چائنیز](cuisine) کھانا چاہتی ہوں
	- slot{"price":"پانچ سو"}
	- slot{"location":"اچھرہ"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_cuisine_price
	- action_restart