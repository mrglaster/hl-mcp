# OrpheuMemoryGetAtAddress
#### Syntax
```
native OrpheuMemoryGetAtAddress(address,const memoryDataName[],any:...)
```

#### Usage
address | ```The address to start at```
---|---
memoryDataName | ```The name of the block that qualifies memory as defined in a file at "configs/orpheu/memory"```
any | ```If the type of the memory location is passed by ref, the variables needed to get the value You can give an extra argument to retrieve the address where the data retrieved lies```
#### Description
```
Retrieves data in memory. It works like OrpheuMemoryGet but starts at a given address
```

#### Return
```
If the type of the memory location is not passed by ref, its value
```


This code is a part of orpheu_memory.inc. To use this code you should include orpheu_memory.inc as ```#include <orpheu_memory>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. Orpheu is outdated and not recommended for use, so use Include at your own risk.