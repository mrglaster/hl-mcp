# register_shop_item
#### Syntax
```
native register_shop_item(const itemname[], itemcost, itemuse, itemteam, access, maxbuys)
```

#### Usage
itemname | ```Името на итема (пример: "Test Item")```
---|---
itemcost | ```Цена на итема (пример: 15)```
itemuse | ```Кога да може да се използва итема? (USE_BATTLE - в бойната фаза , USE_BUILD - в строителната фаза , USE_BOTH - и в двете фази)```
itemteam | ```Кой може да купува итема? (TEAM_ZOMBIES - зомбитата , TEAM_HUMANS - хората , TEAM_BOTH - всички)```
access | ```Админ достъп нужен за купуване на итема (ADMIN_ALL - за всички)```
maxbuys | ```Колко пъти да може да се купи итемът на рунд? (NO_MAX_BUYS - неограничен брой пъти)```
#### Description
```
Регистрира нов итем в shop менюто
```

#### Return
```
Връща индекса на итема. (int)
```


This code is a part of vzbb_mod.inc. To use this code you should include vzbb_mod.inc as ```#include <vzbb_mod>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.