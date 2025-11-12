# Functions in orpheu_memory.inc
Function | Description  
---|---  
[OrpheuMemoryReplace](https://amxx-bg.info/api/orpheu_memory/OrpheuMemoryReplace) | ```
Replaces data in memory in the full extent of a library
```
  
[OrpheuMemoryReplaceAtAddress](https://amxx-bg.info/api/orpheu_memory/OrpheuMemoryReplaceAtAddress) | ```
Replaces data in memory.It works like OrpheuMemoryReplace but starts at a given address
```
  
[OrpheuMemoryGet](https://amxx-bg.info/api/orpheu_memory/OrpheuMemoryGet) | ```
Retrieves data in memory. The block of data that qualifies memory must also identify it by having identifier blocks,
Memory can be located given an offset or a signature
```
  
[OrpheuMemoryGetAtAddress](https://amxx-bg.info/api/orpheu_memory/OrpheuMemoryGetAtAddress) | ```
Retrieves data in memory. It works like OrpheuMemoryGet but starts at a given address
```
  
[OrpheuMemorySet](https://amxx-bg.info/api/orpheu_memory/OrpheuMemorySet) | ```
Alters data in memory.  The block of data that qualifies memory must also identify it by having identifier blocks.
Memory can be located given an offset or a signature
```
  
[OrpheuMemorySetAtAddress](https://amxx-bg.info/api/orpheu_memory/OrpheuMemorySetAtAddress) | ```
Alters data in memory.  It works like OrpheuMemorySet but starts at a given address
```
  

This code is a part of orpheu_memory.inc. To use this code you should include orpheu_memory.inc as ```#include <orpheu_memory>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. Orpheu is outdated and not recommended for use, so use Include at your own risk.