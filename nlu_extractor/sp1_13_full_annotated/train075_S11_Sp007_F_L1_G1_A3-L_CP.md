## train075_S11_Sp007_F_L1_G1_A3-L_CP
* intent_find_by_location:اچھا جی میں اپنی یونیورسٹی میں ہوں اس وقت اور بہت زیادہ بارش ہو رہی ہے اور میں نے ابھی تک کچھ بھی نہیں کھایا تو میں کچھ کھانا چاہ رہی تھی میں اپنی یعنی کہ لائک یونیورسٹی کا جو نیم ہے وہ ہے [پنجاب یونیورسٹی](location)
	- slot{"location":"پنجاب یونیورسٹی"}
	- action_find_by_location
* intent_find_by_cuisine_price:میں پسند کروں گی [دیسی](cuisine) کھانا اور جو پرائس رینج ہے وہ [فائیو ہنڈرڈ سے ون تھاؤزنڈ](price) ہے
	- slot{"location":"پنجاب یونیورسٹی"}
	- slot{"cuisine":"دیسی"}
	- slot{"price":"فائیو ہنڈرڈ سے ون تھاؤزنڈ"}
	- action_find_by_location_cuisine_price
	- action_restart