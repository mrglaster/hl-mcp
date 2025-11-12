# OrpheuGetNextCallAtAddress
#### Syntax
```
native OrpheuGetNextCallAtAddress(address,number)
```

#### Usage
address | ```The address to start the search at```
---|---
number | ```The number of the the call starting at 1 from the address```
#### Description
```
This native should retrieve the address of functions called from an address
 For example by passing the address of the function X, and 1 as n, it should retrieve the address of the first
function called in X. It isn't confirmed to work on every condition and it should be use for experiments only
to help retrieving functions on Windows
```

#### Return
```
The address of the function called
```


This code is a part of orpheu_advanced.inc. To use this code you should include orpheu_advanced.inc as ```#include <orpheu_advanced>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. Orpheu is outdated and not recommended for use, so use Include at your own risk. 