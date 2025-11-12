# format_time
#### Syntax
```
native format_time(output[], len, const format[], time = -1);
```

#### Usage
output | ```Buffer to copy formatted time string to```
---|---
len | ```Maximum size of buffer```
format | ```Format string```
time | ```Unix timestamp, use -1 to use the current time```
#### Description
```
Retrieves the provided time using the specified format string.
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

#### Error
```
If the conversion process fails, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

