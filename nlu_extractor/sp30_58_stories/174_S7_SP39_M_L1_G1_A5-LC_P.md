## 174_S7_SP39_M_L1_G1_A5-LC_P
* greet:جی السلام علیکم
	- utter_salaam
	- utter_help_urduجی میم میں [جیل روڈ](location) پہ ہوں اور میں [چائنیز](cuisine) کھانا چاہتا ہوں تو جھے کوئی اچھا سا ریسٹورنٹ بتاتا جائے
	- slot{"location":"جیل روڈ"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:میم کوئی سا بھی [سستا](price) سا ہو جائے
	- slot{"location":"جیل روڈ"}
	- slot{"cuisine":"چائنیز"}
	- slot{"price":"سستا"}
	- action_find_by_location_cuisine_price
	- action_restart