## 280_S5_SP54_M_L1_G1_A2-L_P_C
* intent_open:میں نے کھانا کھانا ہے مجھے کوئی لوکیشن ڈھونڈ کے دیں جہاں سے میں کھانا کھا سکوں
	- utter_ask_location
* intent_find_by_location:میں لاہور میں [وحدت روڈ](location) سے کھانا کھانا چاہتا ہوں
	- slot{"location":"وحدت روڈ"}
	- action_find_by_location
* intent_find_by_price:میں [مناسب](price)
	- slot{"location":"وحدت روڈ"}
	- slot{"price":"مناسب"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میں [فاسٹ فوڈ](cuisine) کھانا چاہتا ہوں
	- slot{"location":"وحدت روڈ"}
	- slot{"price":"مناسب"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_location_cuisine_price
	- action_restart