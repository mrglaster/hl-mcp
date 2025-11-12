# ExecuteHamB
#### Syntax
```
native ExecuteHamB(Ham:function, this, any:...);
```

#### Usage
function | ```The function to call.```
---|---
id | ```The id of the entity to execute it on.```
#### Description
```
Executes the virtual function on the entity, this will trigger all hooks on that function.
Be very careful about recursion!
Look at the Ham enum for parameter lists.
```


This code is a part of hamsandwich.inc. To use this code you should include hamsandwich.inc as ```#include <hamsandwich>```


  
  

