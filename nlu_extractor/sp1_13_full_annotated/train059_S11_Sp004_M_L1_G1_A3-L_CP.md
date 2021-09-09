## train059_S11_Sp004_M_L1_G1_A3-L_CP
* intent_find_by_location:السلام و علیکم مجھے اس وقت بہت زیادہ بھوک لگی ہوئی ہے اور میں [مسلم ٹاؤن](location) میں ہوں ، کیا آپ مجھے بتا سکتی ہیں  کہ یہاں پہ کوئی قریب کوئی ریسٹورنٹ ہے.
	- slot{"location":"مسلم ٹاؤن"}
	- action_find_by_location
* intent_find_by_cuisine_price:میں [دہی بھلے ](cuisine)کھانا چاہوں گا جس کی پرائس [دو سو](price) روپے ہونی چاہیے
	- slot{"location":"مسلم ٹاؤن"}
	- slot{"cuisine":"دہی بھلے"}
	- slot{"price":"دو سو"}
	- action_find_by_location_cuisine_price
	-action_restart