## 310_S4_SP58_M_L1_G2_A5-P_L_C
* intent_find_by_price:میری جو پرائس کی رینج ہے وہ [ٹو ففٹی](price) اراؤنڈ اباوٹ ہے
	- slot{"price":"ٹو ففٹی"}
	- action_find_by_price
* intent_find_by_location:میں لاہور میں [چوک ناخدا](location) سے کھانا کھانا چاہتا ہوں
	- slot{"price":"ٹو ففٹی"}
	- slot{"location":"چوک ناخدا"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میں [رشیئن](cuisine) :م: کھانا کھانا چاہتا ہوں
	- slot{"price":"ٹو ففٹی"}
	- slot{"location":"چوک ناخدا"}
	- slot{"cuisine":"رشیئن"}
	- action_find_by_location_cuisine_price
	- action_restart