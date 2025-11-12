# emessage_begin
#### Syntax
```
native emessage_begin(dest, msg_type, const origin[3] = {0,0,0}, player = 0);
```

#### Usage
dest | ```Destination type (see MSG_* constants in messages_const.inc)```
---|---
msg_type | ```Message id```
origin | ```Message origin```
player | ```Client index receiving the message or 0 for all clients```
#### Description
```
Marks the beginning of a client message.
```

#### Note
```
You may generate menus, smoke, shockwaves, thunderlights,
intermission and many other messages.
```

#### Note
```
For a list of HL game events, visit https://wiki.alliedmods.net/Half-Life_1_Game_Events
```

#### Note
```
For a list of HL engine messages, visit https://wiki.alliedmods.net/Half-Life_1_Engine_Messages
```

#### Note
```
You may also refer to the messages_const.inc file for examples.
```

#### Note
```
This function is the same as message_begin(), except that the messages
sent with this one are also sent to all other AMXX and Metamod plugins.
This means that if you send one of these messages, other plugins will
be notified of that message, which was previously impossible.
```

#### Note
```
BE CAREFUL! Using this incorrectly, or not for its intended purpose,
could cause infinite recursion or something just as bad!
```

#### Note
```
Each message starts with a emessage_begin() or emessage_begin_f() function
and ends with emessage_end(). The specific message arguments go in between
these two by using the ewrite_*() functions found in messages.inc.
```

#### Return
```
This function has no return value.
```

#### Error
```
If an invalid message id is specified or an invalid number
of parameters is passed, an error will be thrown.
```


This code is a part of messages.inc. To use this code you should include messages.inc as ```#include <messages>```


  
  

