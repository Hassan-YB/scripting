## 134_S1_SP31_M_L2_G1_A1-L_C_P
* greet:السلام علیکم
	- utter_salaam
	- utter_help_urdu
* intent_open::م: مجھے بھوک لگ رہی ہے تو کھانے میں کیا ہو گا
	- utter_ask_location
* intent_find_by_location:میں لاہور میں [شاہدرہ](location) سے
	- slot{"location":"شاہدرہ"}
	- action_find_by_location
* intent_find_by_cuisine:میں [فاسٹ فوڈ](cuisine) ٹائپ کھانا چاہ رہا ہوں
	- slot{"location":"شاہدرہ"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:میں [مناسب](price) ریٹ پہ جو بھی ملے گا پسند کروں گا
	- slot{"location":"شاہدرہ"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart