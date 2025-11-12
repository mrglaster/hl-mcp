# jbshop_item_selected
#### Syntax
```
forward jbshop_item_selected(id, shopid, itemid, itemkey[], class[])
```

#### Usage
id | ```Client index```
---|---
shopid | ```Shop index```
itemid | ```Item index```
itemkey | ```Item key```
class | ```Item class```
#### Description
```
Called when the client attempts to buy an item from a shop.
```

#### Return
```
PLUGIN_HANDLED to deny access to the item or PLUGIN_CONTINUE to buy normally
```


This code is a part of jbshop.inc. To use this code you should include jbshop.inc as ```#include <jbshop>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.