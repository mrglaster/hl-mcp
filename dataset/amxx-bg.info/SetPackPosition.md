# SetPackPosition
#### Syntax
```
native SetPackPosition(DataPack:pack, DataPackPos:position);
```

#### Usage
pack | ```Datapack handle```
---|---
position | ```New position to set```
#### Description
```
Sets the datapack read/write position.
```

#### Note
```
This should only ever be used with (known to be valid) positions
returned by GetPackPosition(). It is not possible for plugins to safely
compute datapack positions.
```

#### Return
```
This function has no return value.
```

#### Error
```
If an invalid handle is provided, or the new position is
out of datapack bounds, an error will be thrown.
```


This code is a part of datapack.inc. To use this code you should include datapack.inc as ```#include <datapack>```


  
  

