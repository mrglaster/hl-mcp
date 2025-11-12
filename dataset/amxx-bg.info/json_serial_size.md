# json_serial_size
#### Syntax
```
native json_serial_size(const JSON:value, bool:pretty = false, bool:null_byte = false);
```

#### Usage
value | ```JSON handle```
---|---
pretty | ```True to count size for pretty format, false to not```
null_byte | ```True to include null byte, false to not```
#### Description
```
Gets size of serialization.
```

#### Return
```
Size of serialized string
```

#### Error
```
If passed handle is not a valid value
```


This code is a part of json.inc. To use this code you should include json.inc as ```#include <json>```


  
  

