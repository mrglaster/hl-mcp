# SetHamParamEntity
#### Syntax
```
native SetHamParamEntity(which, value);
```

#### Usage
which | ```Which parameter to change.  Starts at 1, and works up from the left to right.  1 is always "this".```
---|---
value | ```The value to change it to.```
#### Description
```
Sets a parameter on the fly of the current hook.  This has no effect in post hooks.
Use this on parameters that are entities.
```

#### Note
```
Due to a historical bug, the changes made by this native are not reflected in the corresponding post forward
for backward compatibility reasons. Use SetHamParamEntity2 if this is required.
```


This code is a part of hamsandwich.inc. To use this code you should include hamsandwich.inc as ```#include <hamsandwich>```


  
  

