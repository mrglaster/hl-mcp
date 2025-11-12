# funcidx
#### Syntax
```
native funcidx(const name[]);
```

#### Usage
name | ```Function name```
---|---
#### Description
```
Returns the function index of a public function declared in the plugin.
```

#### Return
```
Function index > 0 on success, -1 if function was not found
```

#### Error
```
If the function name is too long (longer than 63 characters)
an error will be thrown.
```


This code is a part of core.inc. To use this code you should include core.inc as ```#include <core>```


  
  

