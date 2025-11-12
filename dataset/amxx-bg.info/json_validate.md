# json_validate
#### Syntax
```
native bool:json_validate(const JSON:schema, const JSON:value);
```

#### Usage
schema | ```JSON handle```
---|---
value | ```JSON handle```
#### Description
```
Validates json by checking if object have identically named
fields with matching types.
```

#### Note
```
Schema {"name":"", "age":0} will validate
{"name":"Joe", "age":25} and {"name":"Joe", "age":25, "gender":"m"},
but not {"name":"Joe"} or {"name":"Joe", "age":"Cucumber"}.
```

#### Note
```
In case of arrays, only first value in schema
is checked against all values in tested array.
```

#### Note
```
Empty objects ({}) validate all objects,
empty arrays ([]) validate all arrays,
null validates values of every type.
```

#### Return
```
True if passed value is valid, false otherwise
```

#### Error
```
If a schema handle or value handle is invalid
```


This code is a part of json.inc. To use this code you should include json.inc as ```#include <json>```


  
  

