# json_object_get_value
#### Syntax
```
native JSON:json_object_get_value(const JSON:object, const name[], bool:dot_not = false);
```

#### Usage
object | ```Object handle```
---|---
name | ```Key name```
dot_not | ```True to use dot notation, false to not```
#### Description
```
Gets a value from the object.
```

#### Note
```
Needs to be freed using json_free() native.
```

#### Note
```
If dot notation is used some values may be inaccessible
because valid names in JSON can contain dots.
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


  
  

