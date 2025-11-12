# get_orig_retval
#### Syntax
```
native get_orig_retval(any:...);
```

#### Description
```
Returns the original return value of an engine function.
This is only valid in forwards that were registered as post.

get_orig_retval() - no params, retrieves integer return value
get_orig_retval(&Float:value) - retrieves float return value by reference
get_orig_retval(value[], len) - retrives string return value
```


This code is a part of fakemeta.inc. To use this code you should include fakemeta.inc as ```#include <fakemeta>```


  
  

