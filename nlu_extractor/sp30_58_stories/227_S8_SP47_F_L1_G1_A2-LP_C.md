## 227_S8_SP47_F_L1_G1_A2-LP_C
* intent_find_by_location_price::م: میں [یو ای ٹی](location) سے بات کر رہی ہوں کوئی :م: [مناسب](price) :م: قیمت پہ ریسٹورنٹس ود ان :م: تھاؤزنڈ رینج ہو تو :م: بتا دیں
	- slot{"price":"مناسب"}
	- slot{"location":"یو ای ٹی"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:[فاسٹ فوڈ](cuisine)
	- slot{"price":"مناسب"}
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_location_cuisine_price
	- action_restart