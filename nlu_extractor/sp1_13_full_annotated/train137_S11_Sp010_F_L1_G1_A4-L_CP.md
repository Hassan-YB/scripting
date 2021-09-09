## train137_S11_Sp010_F_L1_G1_A4-L_CP
* intent_find_by_location:مجھے بہت زیادہ بھوک لگی ہوئی ہے اور میں [شالیمار](location) کے پاس کھڑی ہوئی ہوں
	- slot{"location":"شالیمار"}
	- action_find_by_location
* intent_find_by_cuisine_price:میں اچھا سا [پیزا](cuisine) کھانا پسند کروں گی اور میرے پاس صرف [ہزار](price) روپے ہیں
	- slot{"location":"شالیمار"}
	- slot{"cuisine":"پیزا"}
	- slot{"price":"ہزار"}
	- action_find_by_location_cuisine_price
	- action_restart