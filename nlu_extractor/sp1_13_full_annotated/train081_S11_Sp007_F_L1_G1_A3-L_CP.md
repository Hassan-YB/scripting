## train081_S11_Sp007_F_L1_G1_A3-L_CP
* intent_find_by_location:اچھا جی میں [یو ای ٹی](location) بس سٹاپ پر کھڑی ہوں اور یہاں پر موسم بہت خراب ہے بہت زیادہ بارش ہو رہی ہے اور کھانے کے لیے کچھ بھی اویلیبل نہیں ہے تو کیا آپ مجھے کوئی ریسٹورینٹ ریفر کر سکتی ہیں
	- slot{"location":"یو ای ٹی"}
	- action_find_by_location
* intent_find_by_cuisine_price:میں کوئی مناسب سی پرائس لائک [فائیو ہنڈرڈ ٹو ون تھاؤزنڈ](price)اور مناسب سا کھانا لائک [دیسی](cuisine)
	- slot{"location":"یو ای ٹی"}
	- slot{"price":"فائیو ہنڈرڈ ٹو ون تھاؤزنڈ"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_cuisine_price
	- action_restart