## train100_S11_Sp008_F_L1_G1_A3-L_CP
* intent_find_by_location:میں نا [جوہرٹاؤن](location) میں کھڑی ہوں تو یہاں آپ مجھے بتا سکتے ہیں کوئی آس پاس کوئی اچھی جگہ جہاں میں کھانا کھا سکوں
	- slot{"location":"جوہرٹاؤن"}
	- action_find_by_location
* intent_find_by_cuisine_price:میں [چائنیز](cuisine) کھانا پسند کروں گی [ہزار](price) روپے میں
	- slot{"location":"جوہرٹاؤن"}
	- slot{"cuisine":"چائنیز"}
	- slot{"price":"ہزار"}
	- action_find_by_location_cuisine_price
	- action_restart