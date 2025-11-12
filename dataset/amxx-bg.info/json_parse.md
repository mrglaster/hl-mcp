# json_parse
#### Syntax
```
native JSON:json_parse(const string[], bool:is_file = false, bool:with_comments = false);
```

#### Usage
string | ```String to parse```
---|---
is_file | ```True to treat string param as filename, false otherwise```
with_comments | ```True if parsing JSON includes comments (it will ignore them), false otherwise```
#### Description
```
Parses JSON string or a file that contains JSON.
```

#### Note
```
Needs to be freed using json_free() native.
```

#### Return
```
JSON handle, Invalid_JSON if error occurred
```


This code is a part of json.inc. To use this code you should include json.inc as ```#include <json>```


  
  

