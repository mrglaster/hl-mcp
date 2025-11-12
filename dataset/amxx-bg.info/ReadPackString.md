# ReadPackString
#### Syntax
```
native ReadPackString(DataPack:pack, buffer[], maxlen);
```

#### Usage
pack | ```Datapack handle```
---|---
buffer | ```Buffer to copy string to```
maxlen | ```Maximum size of buffer```
#### Description
```
Reads a string from a Datapack.
```

#### Return
```
Number of cells written to buffer
```

#### Error
```
If an invalid handle is provided, or not enough data is left
in the datapack, an error will be thrown.
```


This code is a part of datapack.inc. To use this code you should include datapack.inc as ```#include <datapack>```


  
  

