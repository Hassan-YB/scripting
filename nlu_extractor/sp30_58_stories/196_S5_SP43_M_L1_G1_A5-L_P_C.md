## 196_S5_SP43_M_L1_G1_A5-L_P_C
* intent_find_by_location:السلام علیکم میں اس وقت [گڑھی شاہو](location) میں کھڑا ہوں اور مجھے کسی ریسٹورنٹ میں کھانا کھانا ہے
	- slot{"location":"گڑھی شاہو"}
	- action_find_by_location
* intent_find_by_price:نہیں میں [مناسب](price) کھانا کھانا چاہتا ہوں
	- slot{"location":"گڑھی شاہو"}
	- slot{"price":"مناسب"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میں [فاسٹ فوڈ](cuisine) کھانا چاہتا ہوں
	- slot{"location":"گڑھی شاہو"}
	- slot{"price":"مناسب"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_location_cuisine_price
	- action_restart