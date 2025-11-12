# cmd_targetex
#### Syntax
```
stock cmd_targetex(id, const arg[], players[MAX_PLAYERS], name[], len, TargetexFlags:flags = TARGETEX_OBEY_IMM_SINGLE)
```

#### Usage
id | ```Client index of admin performing the action```
---|---
arg | ```Target pattern```
players | ```Array to store the matched clients in```
name | ```Buffer to store the client name or argument translation```
len | ```Maximum buffer length```
flags | ```Optional filtering flags (enum TargetexFlags); valid flags are:   TARGETEX_NONE - no filter (default)   TARGETEX_OBEY_IMM_SINGLE - immunity will be obeyed when using arguments that target a single client   TARGETEX_OBEY_IMM_GROUP - immunity will be obeyed when using arguments that target a group of clients   TARGETEX_NO_SELF - doesn't allow the admin to target himself   TARGETEX_NO_GROUPS - doesn't allow usage of arguments that target a group of clients   TARGETEX_NO_BOTS - doesn't allow targeting bots   TARGETEX_NO_ALIVE - doesn't allow targeting alive clients   TARGETEX_NO_DEAD - doesn't allow targeting dead clients```
#### Description
```
Processes a generic target pattern and tries to match it to a client or a
group of clients based on filtering flags and the usage of special arguments.
```

#### Note
```
If no clients were matched an appropriate message is displayed
to the admin.
```

#### Note
```
If no group matching symbol is used, the function will use the
cmd_target() stock instead.
```

#### Note
```
In order to use the special arguments provided by this function,
the admin must start the <player> argument with the "@" symbol.
```

#### Note
```
This is a list of all the available arguments that admins can use:
  @aim - targets the player that the admin is aiming at
  @all - targets all players
  @alive - targets alive players
  @bots - targets all bots
  @dead - targets dead players
  @humans - targets all humans
  @me - targets the admin himself
  @spectating - targets the client that the admin is spectating
  @view - targets all clients in the admin's field of view
```

#### Note
```
For arguments that are used to target more than one client,
the admin can also specify a team name after the argument itself,
e.g. @alivect will target all alive counter-terrorists. All the
valid team names and argument codes can be found in the TargetEx_Teams
constant in targetex.inc.
```

#### Note
```
When using an argument that targets a group of clients, the admin
can also exclude himself from the command by adding a "!" symbol
right after the "@" one, e.g. @!humans will target all humans
except the admin that used the command.
```

#### Note
```
If only one client is matched, the client's name will be copied
in the "name" buffer, otherwise a translated string using one
of the language keys found in cmdtarget.txt will be copied in the
same buffer.
```

#### Return
```
Number of clients matched
```


This code is a part of targetex.inc. To use this code you should include targetex.inc as ```#include <targetex>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.