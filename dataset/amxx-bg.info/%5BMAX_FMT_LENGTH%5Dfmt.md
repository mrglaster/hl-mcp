# [MAX_FMT_LENGTH]fmt
#### Syntax
```
native [MAX_FMT_LENGTH]fmt(const format[], any:...);
```

#### Usage
format | ```Formatting rules.```
---|---
... | ```Variable number of format parameters.```
#### Description
```
Formats and returns a string according to the AMX Mod X format rules
(see documentation).
```

#### Note
```
Example: menu_additem(menu, fmt("My first %s", "item")).
```

#### Note
```
This should only be used for simple inline formatting like in the above example.
Avoid using this function to store strings into variables as an additional
copying step is required.
```

#### Note
```
The buffer size is defined by MAX_FMT_LENGTH.
```

#### Return
```
Formatted string
```


This code is a part of string.inc. To use this code you should include string.inc as ```#include <string>```


  
  

