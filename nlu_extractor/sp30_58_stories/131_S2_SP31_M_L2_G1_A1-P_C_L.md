## 131_S2_SP31_M_L2_G1_A1-P_C_L
* greet:السلام علیکم میم
	- utter_salaam
	- utter_help_urdu
* intent_find_by_price:میم میری پرائس رینج تقریبا [تھاؤزنڈ](price) کے قریب ہے میں کچھ اچھا کھانا چاہ رہا ہوں
	- slot{"price":"تھاؤزنڈ"}
	- action_find_by_price
* intent_find_by_cuisine:[فاسٹ فوڈ](cuisine) ٹائپ کھانا کھانا چاہ رہا ہوں میں
	- slot{"price":"تھاؤزنڈ"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:یہ گڑھی شاہو والے ایریا سے میم [اقبال ٹاؤن](location) والی سائیڈ پہ
	- slot{"price":"تھاؤزنڈ"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"location":"اقبال ٹاؤن"}
	- action_find_by_location_cuisine_price
	- action_restart