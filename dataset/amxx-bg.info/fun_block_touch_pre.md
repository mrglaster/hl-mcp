# fun_block_touch_pre
#### Syntax
```
forward fun_block_touch_pre(id, ent, funtype)
```

#### Usage
id | ```Индекс на играча```
---|---
id | ```Индекс на ентитито на блока```
funtype | ```Забавен тип на блока (BLOCKS_YELLOW - бързодвижещ се блок , BLOCKS_BLACK - недвижим блок , BLOCKS_BLUE - забавящ блок , BLOCKS_RED - запалващ блок)```
#### Description
```
Извиква се преди докосване на играч със забавен блок
```

#### Note
```
Върнете стойност FORWARD_CONTINUE, за да блокирате ефекта на забавния блок.
```


This code is a part of vzbb_mod.inc. To use this code you should include vzbb_mod.inc as ```#include <vzbb_mod>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.