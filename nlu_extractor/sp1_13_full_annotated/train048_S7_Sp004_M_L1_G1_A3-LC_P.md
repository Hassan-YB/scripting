## train048_S7_Sp004_M_L1_G1_A3-LC_P
* intent_find_by_location_cuisine:جناب میں [جوہر ٹاؤن](location) کھڑا ہوں اور مجھے اس وقت بہت بھوک لگی ہے اور مجھے [دہی بھلے](cuisine) کھانے ہیں۔
	- slot{"location":"جوہر ٹاؤن"}
	- slot{"cuisine":"دہی بھلے"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:[تین سو سے چار سو کے درمیان](price)۔
	- slot{"location":"جوہر ٹاؤن"}
	- slot{"cuisine":"دہی بھلے"}
	- slot{"price":"تین سو سے چار سو کے درمیان"}
	- action_find_by_location_cuisine_price
	- action_restart