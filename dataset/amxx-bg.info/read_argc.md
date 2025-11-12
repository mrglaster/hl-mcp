# read_argc
#### Syntax
```
native read_argc();
```

#### Description
```
Returns number of client command arguments.
```

#### Note
```
Should only be used inside of the client_command() forward.
```

#### Note
```
This count includes the command itself. I.e. in a command with 4
arguments, this will return 5.
```

#### Return
```
Number of arguments in the command
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

