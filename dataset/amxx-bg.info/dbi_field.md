# dbi_field
#### Syntax
```
native dbi_field(Result:_result, _fieldnum, any:... );
```

#### Description
```
Gets a field by number.  Returns 0 on failure.
Although internally fields always start from 0,
This function takes fieldnum starting from 1.
No extra params: returns int
One extra param: returns Float: byref
Two extra param: Stores string with length
```


This code is a part of dbi.inc. To use this code you should include dbi.inc as ```#include <dbi>```


  
  

