# json_array_remove
#### Syntax
```
native bool:json_array_remove(JSON:array, index);
```

#### Usage
array | ```Array handle```
---|---
index | ```Position in the array (starting from 0)```
#### Description
```
Removes an element from the array.
```

#### Note
```
Order of values in array may change during execution.
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


  
  

