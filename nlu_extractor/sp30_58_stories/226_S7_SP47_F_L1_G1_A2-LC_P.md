## 226_S7_SP47_F_L1_G1_A2-LC_P
* intent_find_by_location_cuisine::م: میں [آر اے بازار](location) سے بات کر رہی ہوں میں نے :م: [فاسٹ فوڈ](cuisine) آرڈر کروانا ہے تو اس کے لیے مجھے ریسٹورنٹس کا بتا دیں
	- slot{"location":"آر اے بازار"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_location_and_cuisine
* intent_find_by_price::م: میں [سستا](price) پسند
	- slot{"location":"آر اے بازار"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"price":"سستا"}
	- action_find_by_location_cuisine_price
	- action_restart