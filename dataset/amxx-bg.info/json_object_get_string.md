# json_object_get_string
#### Syntax
```
native json_object_get_string(const JSON:object, const name[], buffer[], maxlen, bool:dot_not = false);
```

#### Usage
object | ```Object handle```
---|---
name | ```Key name```
buffer | ```Buffer to copy string to```
maxlen | ```Maximum size of the buffer```
dot_not | ```True to use dot notation, false to not```
#### Description
```
Gets string data from the object.
```

#### Note
```
If dot notation is used some values may be inaccessible
because valid names in JSON can contain dots.
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


  
  

