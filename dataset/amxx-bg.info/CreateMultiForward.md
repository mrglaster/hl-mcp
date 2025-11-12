# CreateMultiForward
#### Syntax
```
native CreateMultiForward(const name[], stop_type, ...);
```

#### Usage
name | ```Function name to call```
---|---
stop_type | ```Treatment of the plugin return values```
... | ```List of parameter types```
#### Description
```
Creates a global forward that will be called in all plugins.
```

#### Note
```
For a list of valid stop types, see the ET_* constants in amxconst.inc
```

#### Note
```
For a list of valid parameter types, see the FP_* constants in
amxconst.inc
```

#### Return
```
Forward handle, -1 on failure
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

