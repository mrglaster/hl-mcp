# constraint_offset
#### Syntax
```
stock constraint_offset(low, high, seed, offset)
```

#### Usage
low | ```Lower bound```
---|---
high | ```Higher bound```
seed | ```Base value```
offset | ```Offset to move```
#### Description
```
Computes an offset from a given value while constraining it between the
specified bounds, rolling over if necessary.
```

#### Note
```
Example: The range is 1-5 and the base value (seed) is 3, the offset
that the value should be moved by is also 3. Offsetting the value by 3
would result in 6, but it is to be constrained between 1 and 5. With
clamp() this would result in 5, but this function rolls the value over
and returns 1 instead.
```

#### Return
```
Computed offset value between specified bounds
```


This code is a part of amxmisc.inc . To use this code you should include amxmisc.inc as ```#include <amxmisc>```


  
  

