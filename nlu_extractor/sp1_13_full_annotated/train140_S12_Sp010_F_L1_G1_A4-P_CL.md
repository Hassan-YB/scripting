## train140_S12_Sp010_F_L1_G1_A4-P_CL
* intent_find_by_price:میرے پاس صرف [پانچ سو](price) روپے موجود ہیں اور مجھے بہت زیادہ بھوک لگی ہوئی ہے میں نے کھانا آرڈر کرنا ہے
	- slot{"price":"پانچ سو"}
	- action_find_by_price
* intent_find_by_location_cuisine:میں نے اپنے لیے [پیزا](cuisine) آرڈر کرنا ہے اور [اقبال ٹاؤن](location) کا [پیزا](cuisine) بہت اچھا ہے تو میں وہاں سے آرڈر کروں گی
	- slot{"price":"پانچ سو"}
	- slot{"cuisine":"پیزا"}
	- slot{"location":"اقبال ٹاؤن"}
	- action_find_by_location_cuisine_price
	- action_restart