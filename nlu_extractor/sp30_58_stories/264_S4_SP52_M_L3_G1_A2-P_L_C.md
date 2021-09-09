## 264_S4_SP52_M_L3_G1_A2-P_L_C
* intent_find_by_price:میں [پندرہ سو](price) روپے کی پرائس میں کچھ کھانا چاہتا ہوں
	- slot{"price":"پندرہ سو"}
	- action_find_by_price
* intent_find_by_location:لاہور میں [یو ای ٹی](location)  کے پاس
	- slot{"price":"پندرہ سو"}
	- slot{"location":"یو ای ٹی"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میں [فاسٹ فوڈ](cuisine) کھانا پسند کروں گا
	- slot{"price":"پندرہ سو"}
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_location_cuisine_price
	- action_restart