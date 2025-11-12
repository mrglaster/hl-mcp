# register_menu
#### Syntax
```
stock register_menu(const title[], keys, const function[], outside = 0)
```

#### Usage
title | ```Menu name```
---|---
keys | ```Key flags```
function | ```Callback function```
outside | ```Catch menus outside the calling plugin```
#### Description
```
Provides a shorthand to register a working menu.
```

#### Note
```
Combines the necessary calls to register_menuid() and
register_menucmd() into a single function.
```

#### Return
```
This function has no return value.
```

#### Error
```
If an invalid callback function is specified, an error will
be thrown.
```


This code is a part of amxmisc.inc . To use this code you should include amxmisc.inc as ```#include <amxmisc>```


  
  

