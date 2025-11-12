# jbshop_shop_created
#### Syntax
```
forward jbshop_shop_created(shopid, key[], commands[], name[], CsTeams:team, flag, JBShop_PriceTypes:pricetype)
```

#### Usage
shopid | ```Shop index```
---|---
key | ```Shop key```
commands | ```Commands that open the shop, separated by commas```
name | ```Shop name```
team | ```Team that has access to the shop```
flag | ```Admin access flag```
pricetype | ```Currency used to purchase items within the shop```
#### Description
```
Called when a shop is created. Use this to add additional items to the shop via other plugins.
```

#### Return
```
This forward ignores the return value.
```


This code is a part of jbshop.inc. To use this code you should include jbshop.inc as ```#include <jbshop>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.