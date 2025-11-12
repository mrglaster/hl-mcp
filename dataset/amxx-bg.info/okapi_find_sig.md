# okapi_find_sig
#### Syntax
```
native okapi_find_sig(start_address, range_length, const signature[], count = sizeof signature);
```

#### Usage
start_address | ```Address where the search starts```
---|---
range_length | ```Range length of bytes where function is allowed to search in.```
signature[] | ```Signature to find```
size | ```Size of the signature```
#### Description
```
Searches for a signature in the mod library in a given range and starting address.
```

#### Note
```
For bytes to ignore, use "*" or any number above 0xFF like:
  {0x51,0x56,"*","*",0x8B,0x86}.
  {0x51,0x56,0xDEF,0xDEF,0x8B,0x86}.
```

#### Note
```
Available helpers: okapi_mod_find_sig_at  okapi_engine_find_sig_at
                   okapi_mod_find_sig     okapi_engine_find_sig
```

#### Return
```
Address where the sig was first found, 0 otherwise.
```


This code is a part of okapi_memory.inc. To use this code you should include okapi_memory.inc as ```#include <okapi_memory>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.