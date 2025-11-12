# get_user_msgid
#### Syntax
```
native get_user_msgid(const name[]);
```

#### Usage
name | ```Client message name```
---|---
#### Description
```
Returns unique id of a client message.
```

#### Note
```
Example usage: get_user_msgid("TextMsg")
```

#### Note
```
The message id is unique as long as the server is running, but might
change between updates. They should not be hardcoded into plugins.
```

#### Note
```
On first server start, this function will return 0 if used inside
plugin_precache(). Consider hooking RegUserMsg in order to retrieve
the correct message id.
```

#### Return
```
Message id, 0 if message was not found
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

