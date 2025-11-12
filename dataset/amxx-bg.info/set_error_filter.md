# set_error_filter
#### Syntax
```
native set_error_filter(const handler[]);
```

#### Usage
handler | ```Function name to call```
---|---
#### Description
```
Allows to trap error messages that occur in a plugin.
```

#### Note
```
This can be used to override the debug messages that occur when the
plugin causes some kind of runtime error.
```

#### Note
```
The handler will be called in the following manner:

public error_filter(error_code, bool:debugging, message[])

  error_code      - AMX_ERR_* code.
  debugging       - True if the plugin is in debug mode, false otherwise
  message[]       - Message sent along with the error
```

#### Note
```
The handler should return PLUGIN_CONTINUE to let the error through the
filter, or PLUGIN_HANDLED to block the error from displaying.
```

#### Return
```
This function has no return value.
```

#### Error
```
If an invalid callback function is provided, an error
is thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

