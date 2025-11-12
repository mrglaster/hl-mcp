# json_object_set_number
#### Syntax
```
native bool:json_object_set_number(JSON:object, const name[], number, bool:dot_not = false);
```

#### Usage
object | ```Object handle```
---|---
name | ```Key name```
number | ```Number to set```
dot_not | ```True to use dot notation, false to not```
#### Description
```
Sets a number in the object.
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


  
  

