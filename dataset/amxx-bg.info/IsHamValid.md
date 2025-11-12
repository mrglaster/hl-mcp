# IsHamValid
#### Syntax
```
native bool:IsHamValid(Ham:function);
```

#### Usage
function | ```The function to look up.```
---|---
#### Description
```
Returns whether or not the function for the specified Ham is valid.
Things that would make it invalid would be bounds (an older module version
 may not have all of the functions), and the function not being found in
 the mod's hamdata.ini file.
```

#### Return
```
true if the function is valid, false otherwise.
```


This code is a part of hamsandwich.inc. To use this code you should include hamsandwich.inc as ```#include <hamsandwich>```


  
  

