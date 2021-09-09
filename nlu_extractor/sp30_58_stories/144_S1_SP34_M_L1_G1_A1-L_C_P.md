## 144_S1_SP34_M_L1_G1_A1-L_C_P
* greet:السلام علیکم
	- utter_salaam
	- utter_help_urdu
* intent_find_by_location:میڈم مجھے بتائیے گا کہ [یو ای ٹی](location) کے پاس کون سے ریسٹورنٹس ہیں
	- slot{"location":"یو ای ٹی"}
	- action_find_by_location
* intent_find_by_cuisine:[فاسٹ فوڈ](cuisine)
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:[سستا](price)
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"price":"سستا"}
	- action_find_by_location_cuisine_price
	- action_restart