# json_serial_to_file
#### Syntax
```
native bool:json_serial_to_file(const JSON:value, const file[], bool:pretty = false);
```

#### Usage
value | ```JSON handle```
---|---
file | ```Path to the file```
pretty | ```True to format pretty JSON string, false to not```
#### Description
```
Copies serialized string to the file.
```

#### Return
```
True if succeed, false otherwise
```

#### Error
```
If passed handle is not a valid value
```


This code is a part of json.inc. To use this code you should include json.inc as ```#include <json>```


  
  

