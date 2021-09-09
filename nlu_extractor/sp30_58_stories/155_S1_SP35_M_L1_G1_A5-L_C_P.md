## 155_S1_SP35_M_L1_G1_A5-L_C_P
* greet:ہیلو السلام علیکم
	- utter_salaam
	- utter_help_urdu
* intent_open:میم مجھے کھانا آرڈر کرنا ہے
	- utter_ask_location
* intent_find_by_location:میں [ماڈل ٹاؤن](location) والی سائیڈ سے
	- slot{"location":"ماڈل ٹاؤن"}
	- action_find_by_location
* intent_find_by_price:[مناسب](price)
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"price":"مناسب"}
	- action_find_by_location_and_cuisine
* intent_find_by_cuisine:[فاسٹ فوڈ](cuisine)
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"price":"مناسب"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_location_cuisine_price
	- action_restart