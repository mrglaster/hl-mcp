# admins_lookup
#### Syntax
```
native admins_lookup(num, AdminProp:Property, Buffer[] = "", BufferSize = 0);
```

#### Usage
num | ```Admin storage index```
---|---
Property | ```Admin property to retrieve```
Buffer | ```Buffer to copy property information to, if AdminProp_Auth or AdminProp_Password is specified```
BufferSize | ```Maximum buffer size```
#### Description
```
Retrieves information about a dynamically stored admin.
```

#### Note
```
For a list of possible props, see the AdminProp enum in amxconst.inc
```

#### Return
```
Property value if AdminProp_Access or AdminProp_Flags
is requested, 0 otherwise
```

#### Error
```
If an invalid storage index is specified, an error will
be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

