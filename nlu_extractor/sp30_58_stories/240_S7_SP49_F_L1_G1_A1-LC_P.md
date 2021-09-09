## 240_S7_SP49_F_L1_G1_A1-LC_P
* intent_find_by_location_cuisine::م: مجھے بھوک لگی ہے میں نے کھانا کھانا ہے تو :م: مجھے [زنگر برگر](cuisine) کھانا ہے اور :م: مجھے :م: میں [یو ای ٹی](location) کے پاس ہوں تو آس پاس کے کوئی بھی ریسٹورنٹس مجھے آپ ڈھونڈ دیں
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"زنگر برگر"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:میں [مناسب](price) کھانا کھانا چاہتی ہوں
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"زنگر برگر"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart