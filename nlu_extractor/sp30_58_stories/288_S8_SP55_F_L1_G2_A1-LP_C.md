## 288_S8_SP55_F_L1_G2_A1-LP_C
* intent_find_by_location_price::م: السلام علیکم :م: میرا نام تحریم ہے اور میں کرنٹلی اس ٹائم لاہور [گلبرگ](location) کے ایریا میں کھڑی ہوں اور کیونکہ لنچ ٹائم ہو رہا ہے  تو میں کچھ :م: اچھے ریسٹورنٹ پہ جانا چاہتی ہوں  لیکن مجھے اتنی اکنامکل جگہ پہ جانا ہے جہاں پرائسز بہت [مناسب](price) ہوں تو کائنڈلی آپ مجھے کچھ ریکومنڈ کریں
	- slot{"location":"گلبرگ"}
	- slot{"price":"مناسب"}
	- action_find_by_location_and_price
* intent_find_by_cuisine::م: [فاسٹ فوڈ](cuisine)
	- slot{"location":"گلبرگ"}
	- slot{"price":"مناسب"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_location_cuisine_price
	- action_restart