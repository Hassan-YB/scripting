## train060_S12_Sp004_M_L1_G1_A3-P_CL
* intent_find_by_price:السلام و علیکم میرے پاس اس وقت جو ہیں وہ [پانچ سو](price) روپے ہیں.اور مجھے بہت ہی زیادہ بھوک لگی ہے کیا آپ  مجھے بتا سکتی ہیں کہ میں کہاں سے کھا سکتا ہوں
	- slot{"price":"پانچ سو"}
	- action_find_by_price
* intent_find_by_location_cuisine:میں اس وقت [مسلم ٹاؤن](location) میں ہوں اور میں [بریانی](cuisine) کھانا پسند کروں گا.
	- slot{"price":"پانچ سو"}
	- slot{"location":"مسلم ٹاؤن"}
	- slot{"cuisine":"بریانی"}
	- action_find_by_location_cuisine_price