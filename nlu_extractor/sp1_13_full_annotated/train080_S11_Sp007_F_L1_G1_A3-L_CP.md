## train080_S11_Sp007_F_L1_G1_A3-L_CP
* intent_find_by_location:اچھا جی میں [یو ای ٹی](location) بس سٹینڈ پر کھڑی ہوں اور یہاں پر بہت زیادہ بارش ہو رہی ہے اور کھانے کے لیے کچھ بھی اویلیبل نہیں ہے تو کیا مجھے کھانے کے لیے آپ کوئی ریسٹورنٹ ریفر کر سکتی ہیں
	- slot{"location":"یو ای ٹی"}
	- action_find_by_location
* intent_find_by_cuisine_price:میں کوئی [مناسب](price) سی پرائس رینج ہو اور میں [دیسی](cuisine) کھانا پسند کروں گی
	- slot{"location":"یو ای ٹی"}
	- slot{"price":"مناسب"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_cuisine_price
	- action_restart