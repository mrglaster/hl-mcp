# json_object_has_value
#### Syntax
```
native bool:json_object_has_value(const JSON:object, const name[], JSONType:type = JSONError, bool:dot_not = false);
```

#### Usage
object | ```Object handle```
---|---
name | ```Key name```
type | ```Type of value, if JSONError type will not be checked```
dot_not | ```True to use dot notation, false to not```
#### Description
```
Checks if the object has a value with a specific name and type.
```

#### Return
```
True if has, false if not
```

#### Error
```
If passed handle is not a valid object
```


This code is a part of json.inc. To use this code you should include json.inc as ```#include <json>```


  
  

