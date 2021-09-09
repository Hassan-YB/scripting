## 229_S4_SP47_F_L1_G1_A2-P_L_C
* intent_find_by_price::م: مجھے :م: [مہنگے](price) ریسٹورنٹس کے بارے میں بتا دیں
	- slot{"price":"مہنگے"}
	- action_find_by_price
* intent_find_by_location:میں :م: لاہور میں [یو ای ٹی](location) سے پاس سے
	- slot{"price":"مہنگے"}
	- slot{"location":"یو ای ٹی"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میں [چائنیز](cuisine) کھانا پسند کروں گی
	- slot{"price":"مہنگے"}
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_cuisine_price
	- action_restart