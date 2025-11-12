# parse_time
#### Syntax
```
native parse_time(const input[], const format[], time = -1);
```

#### Usage
input | ```Time string to convert```
---|---
format | ```Formatting information for conversion```
time | ```If different from -1, the converted time will be added to this time stamp```
#### Description
```
Converts time strings to unix time stamp.
```

#### Note
```
Uses the strptime C function. For a list of valid format parameters,
see: http://www.cplusplus.com/reference/ctime/strftime/
An example for a input/format combination would be:
Input: "10:32:54 04/02/2013"  Format: "%H:%M:%S %m:%d:%Y"
```

#### Note
```
Information missing from the input will be filled with the current
time and date.
```

#### Return
```
Unix time stamp
```

#### Error
```
If the conversion process fails, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

