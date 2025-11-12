# cshop_register_item
#### Syntax
```
native cshop_register_item(id[], name[], price, limit = 0, sound[] = DEFAULT_SOUND, Float:duration = 0.0, points = 0, team = 0, flag[] = "")
```

#### Usage
id | ```Item short name (id).```
---|---
name | ```Item name.```
price | ```Item price.```
limit | ```Item limit.```
sound | ```Sound when buying the item.```
duration | ```If you want the item to be removed after X seconds, instead of right away.```
points | ```If you want to change the price with points.```
team | ```If you want it to be available for a specific team only.```
flag | ```If you want only players with a specific flag to be able to buy the item.```
#### Description
```
Registers a new item.
```

#### Return
```
Item ID.
```


This code is a part of customshop.inc. To use this code you should include customshop.inc as ```#include <customshop>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.