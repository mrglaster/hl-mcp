# register_event_ex
#### Syntax
```
native register_event_ex(const event[], const function[], RegisterEventFlags:flags, const cond[] = "", ...);
```

#### Usage
event | ```Name of event that should be hooked```
---|---
function | ```Name of callback function```
flags | ```Flags used for filtering events (enum RegisterEventFlags); the valid flags are:   RegisterEvent_Global - Global event (sent to every client)   RegisterEvent_Single - Event sent to single client   RegisterEvent_OnceForMultiple - Call only once when repeated to multiple clients   RegisterEvent_OnlyDead - Call only if sent to dead client   RegisterEvent_OnlyAlive - Call only if sent to alive client   RegisterEvent_OnlyHuman - Call only if sent to human client (RegisterEvent_Single required)   RegisterEvent_OnlyBots - Call only if sent to bot (RegisterEvent_Single required)```
cond | ```Condition string used for filtering events, built as: "<argument number><comparison operator><value>" Argument number is the argument position to be filtered The comparison operator may be:   "=" for equality comparison (all argument types)   "!" for inequality comparison (all argument types)   "&" for bitwise and (int argument) or substring       comparison (string argument)   "<" for less than comparison (int/float arguments)   ">" for greater than comparison (int/float arguments) The argument is compared to the specified value accordingly```
... | ```Any number of additional conditions```
#### Description
```
Registers a function to be called on a given game event.
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


  
  

