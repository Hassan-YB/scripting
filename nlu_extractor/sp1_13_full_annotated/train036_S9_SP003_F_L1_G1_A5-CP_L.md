## train036_S9_SP003_F_L1_G1_A5-CP_L
* greet:السلام و علیکم
	- utter_salaam
* intent_find_by_cuisine_price:دیکھیں میں کچھ کھانا چاہتی ہوں کوئی [دیسی](cuisine) قسم کا لائٹلی ہو ٹھیک ہے.اور میرے پاس صرف [پانچ سو](price) روپے ہیں.اور اس میں آپ مجھے بہترین سا فوڈ بتائیں.
	- slot{"cuisine":"دیسی"}
	- slot{"price":" پانچ سو"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں [ڈیفنس](location) فیز فائیو میں منگوانا چاہوں گی.
	- slot{"cuisine":"دیسی"}
	- slot{"price":" پانچ سو"}
	- slot{"location":"ڈیفنس"}
	- action_find_by_location_cuisine_price
	- action_restart