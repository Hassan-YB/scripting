## 147_S1_SP34_M_L1_G1_A1-L_P_C
* intent_find_by_location:اچھا میڈم مجھے بتائیے گا کہ [شالیمار](location) کے قریب قریب کون سے ریسٹورنٹس ہیں
	- slot{"location":"شالیمار"}
	- action_find_by_location
* intent_find_by_price:کوئی [مہنگا](price) :م: ریسٹورنٹ بتا سکتیں ہیں آپ
	- slot{"location":"شالیمار"}
	- slot{"price":"مہنگا"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:[دیسی](cuisine)
	- slot{"location":"شالیمار"}
	- slot{"price":"مہنگا"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_cuisine_price
	- action_restart