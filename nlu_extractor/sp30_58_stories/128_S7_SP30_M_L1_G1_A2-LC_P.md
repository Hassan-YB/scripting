## 128_S7_SP30_M_L1_G1_A2-LC_P
* greet:السلام علیکم
	- utter_salaam
	- utter_help_urdu
* intent_open:میں نے آپ سے فوڈ کے بارے میں جانکاری لینی ہے
	- utter_ask_location
* intent_find_by_location_cuisine:میں [باغبان پورہ](location) سے [فاسٹ فوڈ](cuisine) کھانا چاہتا ہوں
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"location":"باغبان پورہ"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:میں [مناسب](price) کھانا کھانا
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"location":"باغبان پورہ"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart