## train092_S8_Sp008_F_L1_G1_A3-LP_C
* intent_find_by_location_price:میں [ڈی ایچ اے](location) سے بات کر رہی ہوں اور میرے پاس صرف [پانچ سو](price) روپے ہیں
	- slot{"location":"ڈی ایچ اے"}
	- slot{"price":"پانچ سو"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میں [برگر](cuisine) کھانا پسند کروں گی
	- slot{"location":"ڈی ایچ اے"}
	- slot{"price":"پانچ سو"}
	- slot{"cuisine":"برگر"}
	- action_find_by_location_cuisine_price
	- action_restart