## 173_S7_SP39_M_L1_G1_A5-LC_P
* greet:جی السلام علیکم
	- utter_salaam
	- utter_help_urdu
* intent_find_by_location_cuisine:جی میم میں اس ٹائم [باغبان پورہ](location) جی ٹی روڈ پہ ہوں تو میں نے :م: [دیسی](cuisine) فوڈ کھانا ہے :م: [دیسی](cuisine) کھانا کھانا ہے تو آپ مجھے کوئی ریسٹورنٹ بتائیں اور اچھا سا
	- slot{"location":"باغبان پورہ"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:جی میم کوئی سا بھی [مناسب](price) سا ہو جائے
	- slot{"location":"باغبان پورہ"}
	- slot{"cuisine":"دیسی"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart