## 156_S8_SP36_M_L1_G1_A2-LP_C
* intent_find_by_location_price:السلام علیکم مجھے کھانا آرڈر کرنا ہے اور :م: میری لوکیشن ہے [ماڈل ٹاؤن](location) اور میری پرائز ہے [فائیو ہنڈرڈ](price) تک
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"price":"فائیو ہنڈرڈ"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میں [فاسٹ فوڈ](cuisine) پسند کرتا ہوں
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"price":"فائیو ہنڈرڈ"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_location_cuisine_price
	- action_restart