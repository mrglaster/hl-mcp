# ArrayDestroy
#### Syntax
```
native ArrayDestroy(&Array:which);
```

#### Usage
which | ```Array to destroy```
---|---
#### Description
```
Destroys the array and frees its memory.
```

#### Note
```
The function automatically sets the variable passed to it to 0 to aid
in preventing accidental usage after destroy.
```

#### Return
```
1 if the Array was destroyed, 0 if nothing had to be
destroyed (invalid handle)
```


This code is a part of cellarray.inc. To use this code you should include cellarray.inc as ```#include <cellarray>```


  
  

