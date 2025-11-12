# copy
#### Syntax
```
native copy(dest[],len,const src[]);
```

#### Usage
dest | ```Destination string buffer to copy to.```
---|---
len | ```Destination buffer length.```
src | ```Source string buffer to copy from.```
#### Description
```
Copies one string to another string.
```

#### Note
```
If the destination buffer is too small to hold the source string, the
destination will be truncated.
```

#### Return
```
Number of cells written.
```


This code is a part of string.inc. To use this code you should include string.inc as ```#include <string>```


  
  

