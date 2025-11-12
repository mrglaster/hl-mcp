# get_addr_val
#### Syntax
```
native get_addr_val(addr);
```

#### Usage
addr | ```Variable address```
---|---
#### Description
```
Returns the value of an address.
```

#### Note
```
Addresses can be acquired using get_var_addr()
```

#### Return
```
Value at address
```

#### Error
```
If the plugin attempts to access an address outside of the
stack or heap limits of the plugin, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

