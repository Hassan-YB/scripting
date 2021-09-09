## train139_S12_Sp010_F_L1_G1_A4-P_CL
* intent_find_by_price:مجھے بہت زیادہ بھوک لگی ہوئی ہے اور میرے پاس صرف [دو ہزار](price) روپے ہیں
	- slot{"price":"دو ہزار"}
	- action_find_by_price
* intent_find_by_location_cuisine:میں نے [چائنیز](cuisine) کھانا کھانا ہے اور [فیروزپور روڈ](location) سے اچھا ملتا ہے تو میں وہاں سے آرڈر کروں گی
	- slot{"price":"دو ہزار"}
	- slot{"cuisine":"چائنیز"}
	- slot{"location":"فیروزپور روڈ"}
	- action_find_by_location_cuisine_price
	- action_restart