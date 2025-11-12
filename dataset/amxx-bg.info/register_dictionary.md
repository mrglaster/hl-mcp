# register_dictionary
#### Syntax
```
native register_dictionary(const filename[]);
```

#### Usage
filename | ```Dictionary file name```
---|---
#### Description
```
Registers a dictionary file, making sure the words are in the dictionary.
```

#### Note
```
The file should be in "addons/amxmodx/data/lang", but only the name
needs to be given. For example, register_dictionary("file.txt") will
be "addons/amxmodx/data/lang/file.txt".
```

#### Return
```
On success, the function will return 1, otherwise it will
return 0 if the file couldn't be found or opened, and -1 if
the dictionary was already registered by a plugin
```


This code is a part of lang.inc. To use this code you should include lang.inc as ```#include <lang>```


  
  

