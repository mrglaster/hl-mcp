# json_object_get_real
#### Syntax
```
native Float:json_object_get_real(const JSON:object, const name[], bool:dot_not = false);
```

#### Usage
object | ```Object handle```
---|---
name | ```Key name```
dot_not | ```True to use dot notation, false to not```
#### Description
```
Gets a real number from the object.
```

#### Note
```
If dot notation is used some values may be inaccessible
because valid names in JSON can contain dots.
```

#### Return
```
Real number
```

#### Error
```
If passed handle is not a valid object
```


This code is a part of json.inc. To use this code you should include json.inc as ```#include <json>```


  
  

