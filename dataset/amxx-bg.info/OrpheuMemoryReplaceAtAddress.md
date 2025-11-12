# OrpheuMemoryReplaceAtAddress
#### Syntax
```
native OrpheuMemoryReplaceAtAddress(address,const memoryDataNameName[],count,any:...)
```

#### Usage
address | ```The address to start at```
---|---
memoryDataName | ```The name of the block that qualifies memory as defined in a file at "configs/orpheu/memory"```
count | ```The number of occurence. 0 = infinite```
any | ```A pair "to be replaced" - "replacement". Pair members must be of the same type```
#### Description
```
Replaces data in memory.It works like OrpheuMemoryReplace but starts at a given address
```

#### Return
```
The number of replacements made
```


This code is a part of orpheu_memory.inc. To use this code you should include orpheu_memory.inc as ```#include <orpheu_memory>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. Orpheu is outdated and not recommended for use, so use Include at your own risk.