## train067_S7_Sp007_F_L1_G1_A3-LC_P
* greet:ہیلو
	- utter_salaam
* intent_find_by_location_cuisine:میم میں [لنک روڈ](location) سے بات کر رہی ہوں لاہور اور میں اپنے لیے [فاسٹ فوڈ](cuisine) آرڈر کرنا چاہتی ہوں
	- slot{"location":"لنک روڈ"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:مہنگا کیونکہ میرے پاس جو پرائس رینج ہے وہ [ٹو تھاؤزنڈ](price) تک ہے
	- slot{"location":"لنک روڈ"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"price":"ٹو تھاؤزنڈ"}
	- action_find_by_location_cuisine_price
	- action_restart