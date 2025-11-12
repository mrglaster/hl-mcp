# register_event
#### Syntax
```
native register_event(const event[], const function[], const flags[], const cond[] = "", ...);
```

#### Usage
event | ```Name of event that should be hooked```
---|---
function | ```Name of callback function```
flags | ```Flags used for filtering events, the valid flags are: "a" - Global event (sent to every client) "b" - Event sent to single client "c" - Call only once when repeated to multiple clients "d" - Call only if sent to dead client "e" - Call only if sent to alive client "f" - Call only if sent to human client ("b" flag required) "g" - Call only if sent to bot ("b" flag required)```
cond | ```Condition string used for filtering events, built as: "<argument number><comparison operator><value>" Argument number is the argument position to be filtered The comparison operator may be:   - "=" for equality comparison (all argument types)   - "!" for inequality comparison (all argument types)   - "&" for bitwise and (int argument) or substring     comparison (string argument)   - "<" for less than comparison (int/float arguments)   - ">" for greater than comparison (int/float arguments) The argument is compared to the specified value accordingly```
... | ```Any number of additional conditions```
#### Description
```
Registers a function to be called on a given game event.
```

#### Note
```
Please consider using register_event_ex() instead which allows you to
use named constants for flags instead of letters.
```

#### Note
```
Examples for event conditions:
"2=c4" - Second parameter of message must be the string "c4"
"3>10" - Third parameter of message must be greater than 10
"3!4" - Third parameter of message must not be equal to 4
"2&Buy" - Second parameter of message must contain "Buy" substring
"2!Buy" - Second parameter of message must not equal "Buy"
```

#### Note
```
Due to a long-standing bug that would break compatibility with older
plugins, the client id should be checked for alive/dead state if using
flags "d" or "e".
```

#### Note
```
If multiple conditions are specified for a single parameter, only one
of them has to hold true for the event function to be called.
```

#### Return
```
Event handle
```

#### Error
```
If an invalid event name or callback function is provided,
an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

