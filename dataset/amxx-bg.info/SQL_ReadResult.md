# SQL_ReadResult
#### Syntax
```
native SQL_ReadResult(Handle:query, column, any:...);
```

#### Usage
query | ```Handle of a query to read results from.```
---|---
column | ```Which column to get the value from.```
... | ```Passing no extra arguments - returns an integer. Passing one extra argument - returns a float in the first extra argument Passing two extra params - returns a string in the first argument with a maximum string length in the second argument.```
#### Description
```
Retrieves the current result.
```

#### Note
```
A successful query starts at the first result, so you should not call
SQL_NextRow() first.
```

#### Note
```
Example how to get different types of values:
  new num = SQL_ReadResult(query, 0)
  new Float:num2
  new string[32]
  SQL_ReadResult(query, 1, num2)
  SQL_ReadResult(query, 2, string, charsmax(string))
```

#### Return
```
If no extra arguments are passed, returns an integer value.
```

#### Error
```
Invalid query handle.
```


This code is a part of sqlx.inc. To use this code you should include sqlx.inc as ```#include <sqlx>```


  
  

