# jbshop_register_shop
#### Syntax
```
native jbshop_register_shop(key[], commands[], name[], CsTeams:team = CS_TEAM_UNASSIGNED, flag = ADMIN_ALL, JBShop_PriceTypes:pricetype = JBSHOP_PT_ALIEN_CELLS, JBShop_SortTypes:sorttype = JBSHOP_ST_PRICE_ASC)
```

#### Usage
key | ```Key string used for the shop in order to be found from other plugins```
---|---
commands | ```Commands that open the shop, separated by commas Start the command with "/" to make it a chat command```
name | ```Shop name```
team | ```Team that has access to the shop (CS_TEAM_T or CS_TEAM_CT) Use CS_TEAM_UNASSIGNED to make it available for all teams```
flag | ```Admin access flag or ADMIN_ALL for everyone```
pricetype | ```Currency used to purchase items within the shop     JBSHOP_PT_ALIEN_CELLS to use Alien Cells     JBSHOP_PT_MONEY to use default in-game money```
sorttype | ```Items sorting method     JBSHOP_ST_PRICE_ASC to sort items by price in ascending order     JBSHOP_ST_PRICE_DESC to sort items by price in desscending order```
#### Description
```
Registers a shop.
```

#### Return
```
Shop id
```

#### Error
```
If a command overlaps with another shop, an error will be thrown
```


This code is a part of jbshop.inc. To use this code you should include jbshop.inc as ```#include <jbshop>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.