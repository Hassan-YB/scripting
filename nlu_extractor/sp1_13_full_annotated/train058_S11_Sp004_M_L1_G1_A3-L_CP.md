## train058_S11_Sp004_M_L1_G1_A3-L_CP
* intent_find_by_location:میں اس وقت [اسکیم موڑ](location) میں ہوں اور مجھے بہت ہی زیادہ بھوک لگی ہوئی ہے۔
	- slot{"location":"اسکیم موڑ"}
	- action_find_by_location
* intent_find_by_cuisine_price:میں [بریانی](cuisine) کھانا پسند کروں گا جس کی پرائس [تین سو](price) روپے ہونی چاہیے۔
	- slot{"location":"اسکیم موڑ"}
	- slot{"cuisine":"بریانی"}
	- slot{"price":"تین سو"}
	- action_find_by_location_cuisine_price
	- action_restart