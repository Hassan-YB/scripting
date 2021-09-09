## train112_S9_Sp009_F_L1_G1_A4-CP_L
* intent_find_by_cuisine_price:میرے پاس [فائیو ہنڈرڈ](price) ہیں اور مجھے [فرائز](cuisine) کھانے ہیں
	- slot{"cuisine":"فرائز"}
	- slot{"price":"فائیو ہنڈرڈ"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں یہ [جوہر ٹاؤن](location) سے منگوانا چاہوں گی
	- slot{"cuisine":"فرائز"}
	- slot{"price":"فائیو ہنڈرڈ"}
	- slot{"location":"جوہر ٹاؤن"}
	- action_find_by_location_cuisine_price
	- action_restart