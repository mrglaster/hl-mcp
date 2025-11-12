# okapi_get_ptr_symbol
#### Syntax
```
native bool:okapi_get_ptr_symbol(ptr, str[], len);
```

#### Usage
ptr | ```Address of the function```
---|---
str[] | ```String to save the name```
len | ```Max length that the string will hold```
#### Description
```
Retrieves the symbolic name of an address, if one exists.
This functions just works/makes sense on linux/osx.
```

#### Return
```
true on succes or false otherwise
```


This code is a part of okapi_extra.inc. To use this code you should include okapi_extra.inc as ```#include <okapi_extra>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.