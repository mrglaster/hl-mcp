# json_object_get_value_at
#### Syntax
```
native JSON:json_object_get_value_at(const JSON:object, index);
```

#### Usage
object | ```Object handle```
---|---
index | ```Position from which get key name```
#### Description
```
Gets a value at the specified position from the object.
```

#### Note
```
Needs to be freed using json_free() native.
```

#### Return
```
JSON handle, Invalid_JSON if error occurred
```

#### Error
```
If passed handle is not a valid object
```


This code is a part of json.inc. To use this code you should include json.inc as ```#include <json>```


  
  

