## 225_S7_SP47_F_L1_G1_A2-LC_P
* intent_find_by_location_cuisine::م: میں [یو ای ٹی](location) میں :م: [یو ای ٹی](location) سے بات کر رہی ہوں میں نے کچھ [دیسی](cuisine) آرڈر کرانا ہے تو مجھے ریسٹورنٹس کا آپ بتا دیں
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_and_cuisine
* intent_find_by_price::م: میں [مناسب](price) کھانا پسند کروں گی
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"دیسی"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart