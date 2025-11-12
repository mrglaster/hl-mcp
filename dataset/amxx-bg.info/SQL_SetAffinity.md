# SQL_SetAffinity
#### Syntax
```
native SQL_SetAffinity(const driver[]);
```

#### Usage
driver | ```The name of a driver to use.```
---|---
#### Description
```
Sets driver affinity. You can use this to force a particular driver implementation.
This will automatically change all SQL natives in your plugin to be "bound" to
the module in question.
```

#### Note
```
Using this while you have open handles to another database type will
cause problems. I.e., you cannot open a handle, switch affinity,
then close the handle with a different driver.
```

#### Note
```
Switching affinity is an O(n * m) operation, where n is the number of
SQL natives and m is the number of used natives in total.
```

#### Note
```
Intuitive programmers will note that this causes problems for
threaded queries. You will have to either force your script to work
under one affinity, or to pack the affinity type into the query data,
check it against the current, then set the new affinity if necessary.
Then, restore the old one for safety.
```

#### Return
```
If no module with the given name is found, returns 0.
Unless your plugin is bult to handle different driver
types at once, you should let this error pass.
```


This code is a part of sqlx.inc. To use this code you should include sqlx.inc as ```#include <sqlx>```


  
  

