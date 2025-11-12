# set_addr_val
#### Syntax
```
native set_addr_val(addr, val);
```

#### Usage
addr | ```Variable address```
---|---
val | ```Value to set```
#### Description
```
Sets the value of an address.
```

#### Note
```
Addresses can be acquired using get_var_addr()
```

#### Return
```
This function has no return value.
```

#### Error
```
If the plugin attempts to access an address outside of the
stack or heap limits of the plugin, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

