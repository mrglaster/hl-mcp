# json_get_string
#### Syntax
```
native json_get_string(const JSON:value, buffer[], maxlen);
```

#### Usage
value | ```JSON handle```
---|---
buffer | ```Buffer to copy string to```
maxlen | ```Maximum size of the buffer```
#### Description
```
Gets string data.
```

#### Return
```
The number of cells written to the buffer
```

#### Error
```
If passed value is not a valid handle
```


This code is a part of json.inc. To use this code you should include json.inc as ```#include <json>```


  
  

