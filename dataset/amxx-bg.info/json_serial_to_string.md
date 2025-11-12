# json_serial_to_string
#### Syntax
```
native json_serial_to_string(const JSON:value, buffer[], maxlen, bool:pretty = false);
```

#### Usage
value | ```JSON handle```
---|---
buffer | ```Buffer to copy string to```
maxlen | ```Maximum size of the buffer```
pretty | ```True to format pretty JSON string, false to not```
#### Description
```
Copies serialized string to the buffer.
```

#### Return
```
The number of cells written to the buffer
```

#### Error
```
If passed handle is not a valid value
```


This code is a part of json.inc. To use this code you should include json.inc as ```#include <json>```


  
  

