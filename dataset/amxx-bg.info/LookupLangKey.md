# LookupLangKey
#### Syntax
```
native LookupLangKey(Output[], OutputSize, const Key[], const &id);
```

#### Usage
Output | ```Buffer to store the output in```
---|---
OutputSize | ```Maximum buffer size```
Key | ```Language key```
id | ```Client index or LANG_SERVER```
#### Description
```
Looks up the translation of the key for the given type.
```

#### Note
```
This does NOT format the output text! For example, if the key
contains %s, the outputted text will also contain %s.
```

#### Note
```
LANG_PLAYER is invalid in this, use a player index or LANG_SERVER.
```

#### Return
```
1 on success, 0 otherwise
```


This code is a part of lang.inc. To use this code you should include lang.inc as ```#include <lang>```


  
  

