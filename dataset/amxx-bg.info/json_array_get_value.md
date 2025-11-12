# json_array_get_value
#### Syntax
```
native JSON:json_array_get_value(const JSON:array, index);
```

#### Usage
array | ```Array handle```
---|---
index | ```Position in the array (starting from 0)```
#### Description
```
Gets a value from the array.
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
If passed handle is not a valid array
```


This code is a part of json.inc. To use this code you should include json.inc as ```#include <json>```


  
  

