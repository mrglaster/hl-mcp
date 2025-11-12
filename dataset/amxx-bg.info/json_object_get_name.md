# json_object_get_name
#### Syntax
```
native json_object_get_name(const JSON:object, index, buffer[], maxlen);
```

#### Usage
object | ```Object handle```
---|---
index | ```Position from which get key name```
buffer | ```Buffer to copy string to```
maxlen | ```Maximum size of the buffer```
#### Description
```
Gets name of the object's key.
```

#### Return
```
The number of cells written to the buffer
```

#### Error
```
If passed handle is not a valid object
```


This code is a part of json.inc. To use this code you should include json.inc as ```#include <json>```


  
  

