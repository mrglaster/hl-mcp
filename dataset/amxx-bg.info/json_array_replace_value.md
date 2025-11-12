# json_array_replace_value
#### Syntax
```
native bool:json_array_replace_value(JSON:array, index, const JSON:value);
```

#### Usage
array | ```Array handle```
---|---
index | ```Position in the array to be replaced```
value | ```JSON handle to set```
#### Description
```
Replaces an element in the array with value.
```

#### Return
```
True if succeed, false otherwise
```

#### Error
```
If passed handle is not a valid array
```


This code is a part of json.inc. To use this code you should include json.inc as ```#include <json>```


  
  

