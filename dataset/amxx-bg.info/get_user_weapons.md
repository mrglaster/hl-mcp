# get_user_weapons
#### Syntax
```
native get_user_weapons(index, weapons[32], &num);
```

#### Usage
index | ```Client index```
---|---
weapons | ```Array to store weapon indexes in```
num | ```Variable to store number of weapons in the inventory to```
#### Description
```
Retrieves all weapons in the client inventory, stores them in an array, and
returns the inventory as a bitflag sum.
```

#### Note
```
Make sure that num has an initial value of 0 or the native will not
work correctly.
```

#### Return
```
Bitflag sum of weapon indexes, 0 if client is not connected
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

