## 214_S4_SP45_F_L1_G1_A5-P_L_C
* intent_find_by_price:میں [ففٹین ہنڈرڈ](price) میں کھانا کھانا چاہتی ہوں
	- slot{"price":"ففٹین ہنڈرڈ"}
	- action_find_by_price
* intent_find_by_location:میں لاہور [یو ای ٹی](location) کے پاس سے
	- slot{"price":"ففٹین ہنڈرڈ"}
	- slot{"location":"یو ای ٹی"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:[فاسٹ فوڈ ](cuisine)
	- slot{"price":"ففٹین ہنڈرڈ"}
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"فاسٹ فوڈ "}
	- action_find_by_location_cuisine_price
	- action_restart