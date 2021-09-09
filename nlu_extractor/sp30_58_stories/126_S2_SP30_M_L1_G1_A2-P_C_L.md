* greet:السلام علیکم میرا نام موئیز ہے
	- utter_salaam
	- utter_help_urdu
* intent_find_by_price:میں نے کھانے کے بارے میں جاننا ہے میری :م: رینج ہے نا وہ [ففٹین ہنڈرڈ سے ٹو تھاؤزنڈ ](price)ہے
	- slot{"price":"ففٹین ہنڈرڈ سے ٹو تھاؤزنڈ "}
	- action_find_by_price
* intent_find_by_cuisine:میں [فاسٹ فوڈ](cuisine) کھانا کھانا چاہتا ہوں
	- slot{"price":"ففٹین ہنڈرڈ سے ٹو تھاؤزنڈ "}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں یہاں [باغبان پورہ](location) سے کھانا چاہتا ہوں
	- slot{"price":"ففٹین ہنڈرڈ سے ٹو تھاؤزنڈ "}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"location":"باغبان پورہ"}
	- action_find_by_location_cuisine_price
	- action_restart
