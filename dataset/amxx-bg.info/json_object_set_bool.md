# json_object_set_bool
#### Syntax
```
native bool:json_object_set_bool(JSON:object, const name[], bool:boolean, bool:dot_not = false);
```

#### Usage
object | ```Object handle```
---|---
name | ```Key name```
boolean | ```Boolean value to set```
dot_not | ```True to use dot notation, false to not```
#### Description
```
Sets a boolean value in the object.
```

#### Note
```
If dot notation is used some values may be inaccessible
because valid names in JSON can contain dots.
```

#### Note
```
It also removes the old value if any.
```

#### Return
```
True if succeed, false otherwise
```

#### Error
```
If passed handle is not a valid object
```


This code is a part of json.inc. To use this code you should include json.inc as ```#include <json>```


  
  

