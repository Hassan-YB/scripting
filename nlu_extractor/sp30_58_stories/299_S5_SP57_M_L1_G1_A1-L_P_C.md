## 299_S5_SP57_M_L1_G1_A1-L_P_C
* intent_find_by_location:میں اس وقت [گڑھی شاہو](location) کے ایریا میں موجود ہوں اس وقت مجھے بھوک لگی ہے تو اس وقت کہاں پر کھانے کی ایشیاز موجود ہیں
	- slot{"location":"گڑھی شاہو"}
	- action_find_by_location
* intent_find_by_price:جی :م: میری پرائس کی رینج [[ہنڈرڈ](price)] روپیز ہے تو اس رینج میں جو ہے وہ بتا دیں
	- slot{"location":"گڑھی شاہو"}
	- slot{"price":"ہنڈرڈ"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:[فاسٹ فوڈ](cuisine)
	- slot{"location":"گڑھی شاہو"}
	- slot{"price":"ہنڈرڈ"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_location_cuisine_price
	- action_restart