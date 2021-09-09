## 177_S6_SP39_M_L1_G1_A5-C_L_P
* intent_find_by_cuisine:السلام علیکم میم میں [اٹالک](cuisine) فوڈ کھانا چاہتا ہوں کائنڈلی مجھے کچھ کوئی ریسٹورنٹ :م: بتایا جائے
	- slot{"cuisine":"اٹالک"}
	- action_find_by_cuisine
* intent_find_by_location:میم اس ٹائم [اپر مال](location) :م: اور مجھے کچھ بتایا جائے اس کے بارے میں
	- slot{"cuisine":"اٹالک"}
	- slot{"location":"اپر مال"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:میم [مناسب](price) سا
	- slot{"cuisine":"اٹالک"}
	- slot{"location":"اپر مال"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart