## train138_S11_Sp010_F_L1_G1_A4-L_CP
* intent_find_by_location:جی میں [فیروزپور روڈ](location) پر کھڑی ہوئی ہوں اور مجھے بہت زیادہ بھوک لگ رہی ہے میں نے کھانا آرڈر کرنا ہے اپنے لیے
	- slot{"location":"فیروزپور روڈ"}
	- action_find_by_location
* intent_find_by_cuisine_price:جی میں نے کچھ [دیسی](cuisine) آرڈر کرنا ہے اپنے لیے اور میرے پاس ابھی صرف [پانچ سو](price) روپے موجود ہیں
	- slot{"location":"فیروزپور روڈ"}
	- slot{"cuisine":"دیسی"}
	- slot{"price":"پانچ سو"}
	- action_find_by_location_cuisine_price
	- action_restart