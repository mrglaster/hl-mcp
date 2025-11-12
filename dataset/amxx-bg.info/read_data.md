# read_data
#### Syntax
```
native read_data(value, any:...);
```

#### Usage
value | ```Argument number to retrieve value from```
---|---
... | ```Changes the native's behavior depending on how many additional parameters are provided:    0 - Return the argument integer value directly    1 - Store the argument float value in the variable passed        as the second parameter    2 - Copy the argument string value to the buffer provided        in the second parameter, using the third as the        maximum buffer size```
#### Description
```
Retrieves values from a client message.
```

#### Note
```
For use within callbacks registered with register_event_ex()
```

#### Note
```
Usage examples:
value = read_data(1);
read_data(2, floatvalue);
written = read_data(3, buffer, buffersize);
```

#### Return
```
Changes depending on how many additional parameters are
provided:
   0 - Returns the argument integer value
   1 - Returns the argument float value, converted
       (truncated) to an integer
   2 - Returns the number of cells written to the buffer
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

