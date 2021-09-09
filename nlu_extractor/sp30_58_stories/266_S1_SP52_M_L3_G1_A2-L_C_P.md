## 266_S1_SP52_M_L3_G1_A2-L_C_P
* intent_find_by_location:میں اس وقت [گلبرگ](location) میں ہوں اور میں اس وقت کچھ کھانا چاہتا ہوں
	- slot{"location":"گلبرگ"}
	- action_find_by_location
* intent_find_by_cuisine:میں [دیسی](cuisine) کھانا کھانا چاہتا ہوں
	- slot{"location":"گلبرگ"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:نہیں میری پرائس کی رینج اب [پانچ ہزار](price) تک ہے تو آپ اس رینج میں جتنا سا بھی افورڈ ایبل ہو وہ کھانا کھانا چاہتا ہوں
	- slot{"location":"گلبرگ"}
	- slot{"cuisine":"دیسی"}
	- slot{"price":"پانچ ہزار"}
	- action_find_by_location_cuisine_price
	- action_restart