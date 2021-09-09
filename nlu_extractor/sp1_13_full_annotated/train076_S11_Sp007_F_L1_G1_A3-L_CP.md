## train076_S11_Sp007_F_L1_G1_A3-L_CP
* intent_find_by_location:اچھا جی میں [پنجاب یونیورسٹی](location) سے بات کر رہی ہوں اور یہاں پر کھانے کے لیے کچھ بھی اویلیبل نہیں ہے تو کیا مجھے کھانے کے لیے کچھ مل سکتا ہے
	- slot{"location":"پنجاب یونیورسٹی"}
	- action_find_by_location
* intent_find_by_cuisine_price:اچھا جی میں [فاسٹ فوڈ](cuisine) کھانا پسند کروں گی اور [مناسب](price) ریٹس پر
	- slot{"location":"پنجاب یونیورسٹی"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart