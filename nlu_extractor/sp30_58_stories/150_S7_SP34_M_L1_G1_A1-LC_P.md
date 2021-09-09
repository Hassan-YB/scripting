## 150_S7_SP34_M_L1_G1_A1-LC_P
* intent_find_by_location_cuisine:میں [بحریہ ٹاؤن](location) لاہور سے ہوں تو مجھے کوئی ایک اچھا سا ریسٹورنٹ چاہیے :م :جو آس پاس :م: میں [دیسی](cuisine) فوڈ ٹرائے کرنا چاہ رہا ہوں یہاں پہ
	- slot{"location":"بحریہ ٹاؤن"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:[سستا](price)
	- slot{"location":"بحریہ ٹاؤن"}
	- slot{"cuisine":"دیسی"}
	- slot{"price":"سستا"}
	- action_find_by_location_cuisine_price
	- action_restart