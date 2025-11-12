# jbshop_shop_selected
#### Syntax
```
forward jbshop_shop_selected(id, shopid, shopkey[])
```

#### Usage
id | ```Client index```
---|---
shopid | ```Shop index```
shopkey | ```Shop key```
#### Description
```
Called when the client attempts to open a shop.
```

#### Return
```
PLUGIN_HANDLED to deny access to the shop or PLUGIN_CONTINUE to open normally
```


This code is a part of jbshop.inc. To use this code you should include jbshop.inc as ```#include <jbshop>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.