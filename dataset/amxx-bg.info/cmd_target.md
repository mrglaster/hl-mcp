# cmd_target
#### Syntax
```
stock cmd_target(id, const arg[], flags = CMDTARGET_OBEY_IMMUNITY)
```

#### Usage
id | ```Client index of admin performing an action```
---|---
arg | ```Target pattern```
flags | ```Filtering flags, see CMDTARGET_* constants above```
#### Description
```
Processes a generic target pattern and tries to match it to a client based
on filtering flags. If no unique target is found an appropriate message is
displayed to the admin.
```

#### Note
```
The pattern is first matched case insensitively against client names.
If no match is found it is matched against client authids. If still no
match is found and the pattern starts with '#' it is finally matched
against client userids.
```

#### Note
```
Since client names are matched by substring the pattern can potentially
match multiple targets. In that case the function will return 0 and ask
the admin to provide a unique pattern.
```

#### Note
```
The filtering flags are applied after the pattern matching has
finished. That means the pattern has to be unique against all clients
on the server even if some of them are not eligible.
```

#### Return
```
Client index, or 0 if no or multiple clients matched
```


This code is a part of amxmisc.inc . To use this code you should include amxmisc.inc as ```#include <amxmisc>```


  
  

