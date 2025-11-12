# get_time
#### Syntax
```
native get_time(const format[], output[], len);
```

#### Usage
format | ```Format string```
---|---
output | ```Buffer to copy formatted time string to```
len | ```Maximum size of buffer```
#### Description
```
Retrieves the current time using the specified format string.
```

#### Note
```
Uses the strftime C function. For a list of valid format parameters,
see: http://cplusplus.com/reference/clibrary/ctime/strftime.html
A common example for a format string would be: "%m/%d/%Y - %H:%M:%S"
```

#### Return
```
Number of cells written to buffer
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

