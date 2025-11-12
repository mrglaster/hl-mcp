# jbshop_register_item
#### Syntax
```
native jbshop_register_item(shopid, key[], name[], price, CsTeams:team = CS_TEAM_UNASSIGNED, bool:playsound = true, JBShop_WhenBuy:whenbuy = JBSHOP_WB_ONLY_ALIVE, JBShop_PriceTypes:pricetype = JBSHOP_PT_OBEY_SHOP, JBShop_ExpireTypes:expiretype = JBSHOP_ET_INSTANT, flag = ADMIN_ALL, sound[] = "", menuname[] = "", class[] = "", bool:newline = false, bool:locked = false, level = 0)
```

#### Usage
shopid | ```Shop index```
---|---
key | ```Key string used for the item in order to be found from other plugins The same key can be used for multiple items if they are present in more than one shop or do the same thing```
name | ```Item name```
price | ```Item price```
team | ```Team that has access to the item (CS_TEAM_T or CS_TEAM_CT) Use CS_TEAM_UNASSIGNED to make it available for all teams```
playsound | ```Whether to play a sound when purchasing the item```
whenbuy | ```When can players purchase this item     JBSHOP_WB_ONLY_ALIVE only when alive     JBSHOP_WB_ONLY_DEAD only when dead     JBSHOP_WB_DEAD_ALIVE both dead and alive```
pricetype | ```Currency used to purchase the item     JBSHOP_PT_ALIEN_CELLS to use Alien Cells     JBSHOP_PT_MONEY to use default in-game money     JBSHOP_PT_OBEY_SHOP to use the same currency defined in the shop```
expiretype | ```When is the item going to expire after purchase     JBSHOP_ET_INSTANT to expire instantly and allow infinite purchases     JBSHOP_ET_RESPAWN to expire at respawn, making it purchasable only once per spawn     JBSHOP_ET_MANUAL for items that need to be removed manually with jbshop_user_remove_item()```
flag | ```Admin access flag or ADMIN_ALL for everyone```
sound | ```Custom sound that will be played if playsound = true Leave blank to play the default buy sound```
menuname | ```If set, this name will be displayed in the menu itself, while the original name will appear in chat Useful if you want to add menu colors or additional information that shouldn't appear in chat```
class | ```Item class used for multiple item selection via other plugins Multiple classes can be assigned to one item, e.g. "weapon|upgrade|health"```
newline | ```Adds an empty line in the menu after the item if set to true```
locked | ```If true, the item will be locked with and marked with [SOON] in the menu```
level | ```If non-zero, the item will require a certain level from OciXCrom's Rank System```
#### Description
```
Registers a shop item.
```

#### Return
```
Item id
```

#### Error
```
If an invalid shop index is specified, an error will be thrown
```


This code is a part of jbshop.inc. To use this code you should include jbshop.inc as ```#include <jbshop>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.