# OrpheuGetStructMember
#### Syntax
```
native OrpheuGetStructMember(OrpheuStruct:struct,const memberName[],any:...)
```

#### Usage
struct | ```A handler to the struct```
---|---
memberName | ```The name of the member of the struct we want to deal with```
any | ```In case the value is multi cell (string or vector), an holder to receive them by ref```
#### Description
```
Retrieves the value of a member of a struct given a struct handler and the member name
```

#### Return
```
In case the value is uni cell, the value itself
```


This code is a part of orpheu.inc. To use this code you should include orpheu.inc as ```#include <orpheu>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. Orpheu is outdated and not recommended for use, so use Include at your own risk. 