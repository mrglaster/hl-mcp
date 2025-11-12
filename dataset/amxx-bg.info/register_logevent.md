# register_logevent
#### Syntax
```
native register_logevent(const function[], argsnum, ...);
```

#### Usage
function | ```Name of callback function```
---|---
argsnum | ```Number of arguments of the log event```
... | ```Any number of conditions used for filtering events A condition string is built as: "<argument number><comparison operator><string>" Argument number is the argument position to be filtered The comparison operator may be:   - "=" for equality comparison   - "&" for substring comparison The argument is compared to the specified string accordingly```
#### Description
```
Registers a function to be called on a given log event.
```

#### Note
```
Examples for log conditions:
"0 = World triggered" "1 = Game_Commencing"
"1 = say"
"3 = Terrorists_Win"
"1 = entered the game"
"0 = Server cvar"
```

#### Return
```
Log event handle
```

#### Error
```
If an invalid callback function is provided, an error will
be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

