# OrpheuMemoryReplace
#### Syntax
```
native OrpheuMemoryReplace(const memoryDataName[],count,any:...)
```

#### Usage
memoryDataName | ```The name of the block that qualifies memory as defined in a file at "configs/orpheu/memory"```
---|---
count | ```The number of occurences to replace. 0 = infinite```
any | ```A pair "to be replaced" - "replacement". Pair members must be of the same type```
#### Description
```
Replaces data in memory in the full extent of a library
```

#### Return
```
The number of replacements made

Example:

     Replacing the value 16000 by 100000 in a library

     OrpheuMemoryReplace("name",0,16000,100000) (where name should be related to a block of data that qualifies the memory as holding a long value)

     Replacing the string "weapon_smokegrenade","weapon_flashbang"

     OrpheuMemoryReplace("name",0,"weapon_smokegrenade","weapon_flashbang") (where name should be related to a block of data that qualifies the memory as holding a string)
```


This code is a part of orpheu_memory.inc. To use this code you should include orpheu_memory.inc as ```#include <orpheu_memory>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. Orpheu is outdated and not recommended for use, so use Include at your own risk.