## 289_S8_SP55_F_L1_G2_A1-L_P_C
* intent_find_by_location::م: السلام علیکم :م: میں کرنٹلی [جوہر ٹاؤن](location) لاہور کے ایریا میں کھڑی ہوں :م: اور اس ٹائم کیونکہ ظہر کا ٹائم ہونے والا ہے تو مجھے کوئی اچھی :م: ریسٹورنٹ یہاں پہ معلوم نہیں ہے یہ ایریا بالکل ایریا ہے میرے لیے تو آپ پلیز مجھے بتا سکتیں ہیں یہاں پہ کوئی اچھے ریسٹورنٹس جو اویل ایبل ہوں
	- slot{"location":"جوہر ٹاؤن"}
	- action_find_by_location
* intent_find_by_price::م: [سستا](price)
	- slot{"location":"جوہر ٹاؤن"}
	- slot{"price":"سستا"}
	- action_find_by_location_and_price
* intent_find_by_cuisine::م: پاکستانی [دیسی](cuisine) فوڈ
	- slot{"location":"جوہر ٹاؤن"}
	- slot{"price":"سستا"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_cuisine_price
	- action_restart