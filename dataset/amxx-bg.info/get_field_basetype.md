# get_field_basetype
#### Syntax
```
stock BaseFieldType:get_field_basetype(FieldType:type, type_name[] = "", maxlen = 0)
```

#### Usage
type | ```Class member type (FIELD_* constants)```
---|---
type_name | ```Optional buffer to store base type name in```
maxlen | ```Maximum size of the buffer```
#### Description
```
Returns the data field base type based off a specific field type.
```

#### Note
```
From an AMXX plugin perspective, the (C++/engine) data types can be grouped
in five base types: integer, float, vector, entity and string. This stock is
essentially for convenience and debug purpose.
```

#### Return
```
Base field type (BASEFIELD_* constants)
```


This code is a part of fakemeta.inc. To use this code you should include fakemeta.inc as ```#include <fakemeta>```


  
  

