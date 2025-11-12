# json_deep_copy
#### Syntax
```
native JSON:json_deep_copy(const JSON:value);
```

#### Usage
value | ```JSON handle to be copied```
---|---
#### Description
```
Creates deep copy of passed value.
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
If passed value is not a valid handle
```


This code is a part of json.inc. To use this code you should include json.inc as ```#include <json>```


  
  

