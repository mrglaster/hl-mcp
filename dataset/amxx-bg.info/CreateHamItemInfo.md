# CreateHamItemInfo
#### Syntax
```
native CreateHamItemInfo();
```

#### Description
```
Creates an ItemInfo handle.  This value should never be altered.
The handle can be used in Get/SetHamItemInfo.

NOTE: You must call FreeHamItemInfo() on every handle made with CreateHamItemInfo().
```

#### Return
```
A new ItemInfo handle.
```


This code is a part of hamsandwich.inc. To use this code you should include hamsandwich.inc as ```#include <hamsandwich>```


  
  

