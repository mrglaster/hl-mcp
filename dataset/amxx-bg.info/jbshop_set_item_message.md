# jbshop_set_item_message
#### Syntax
```
native jbshop_set_item_message(shopid, itemid, message[], any:...)
```

#### Usage
shopid | ```Shop index```
---|---
itemid | ```Item index```
message | ```Message that will be displayed in chat```
... | ```Variable number of formatting arguments```
#### Description
```
Sets a message that will be displayed in chat after purchasing the item.
```

#### Note
```
The message will be displayed right after the one saying that you bought the item
so it's much more visible than manually sending a message which will go before the other one.
```

#### Return
```
This function has no return value.
```

#### Error
```
If an invalid shop or item index is specified, an error will be thrown
```


This code is a part of jbshop.inc. To use this code you should include jbshop.inc as ```#include <jbshop>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.