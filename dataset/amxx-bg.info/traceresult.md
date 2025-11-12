# traceresult
#### Syntax
```
native traceresult(type, any:...);
```

#### Usage
type | ```Result to retrieve```
---|---
... | ```Depending on the result type a different number of additional parameters should be provided:    int      - Returns the result integer value directly, no               additional parameters required    float    - Stores the result float value into the               variable provided as the second parameter    vector   - Copies the result vector to the Float:array[3]               provided in the second parameter```
#### Description
```
Retrieves a result from the global engine module trace handle.
```

#### Note
```
For a list of trace results available see the TR_* constants in
engine_const.inc.
```

#### Note
```
Usage examples:
value = traceresult(TR_AllSolid);
traceresult(TR_Fraction, floatvalue);
traceresult(TR_EndPos, vector);
```

#### Return
```
Changes depending on the result type:
   int      - Returns the result integer value
   float    - Returns 1
   vector   - Returns 1
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

