# xs_strmid
#### Syntax
```
stock xs_strmid(const oldmsg[], newmsg[], start, end, outlen=-1)
```

#### Usage
oldmsg | ```The string to copy from.```
---|---
newmsg | ```The string to copy to.```
start | ```Starting position of the @oldmsg string to copy from.```
end | ```Ending position of the @oldmsg string to copy from.```
outlen | ```If positive, specifies the maximum number of characters to be copied. Otherwise, the function assumes that newmsg is at least @end - @start + 1 characters long.```
#### Description
```
Copies characters from @oldmsg to @newmsg, starting at @start and ending
at @end (includes the end character).
```

#### Return
```
This function has no return value.
```


This code is a part of xs.inc. To use this code you should include xs.inc as ```#include <xs>```


  
  

