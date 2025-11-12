# nvault_get
#### Syntax
```
native nvault_get(vault, const key[], any:...);
```

#### Usage
vault | ```A vault handle returned from nvault_open()```
---|---
key | ```A key to get the value from```
... | ```If three argument are given, gets a float value and puts it in the third argument by reference. If four arguments are given, gets a string from the vault and copies it to the third argument, up to 4th argument characters.```
#### Description
```
Retrieves a value from the given key.
```

#### Note
```
An example of retrieving a string:
nvault_get(vaultHandle, "myKey", myString, charsmax(myString));
```

#### Return
```
Result as integer if only the first two arguments
of the function are used.
1 if only the first three arguments are used.
String length if all four parameters are used.
```

#### Error
```
On invalid vault handle.
```


This code is a part of nvault.inc. To use this code you should include nvault.inc as ```#include <nvault>```


  
  

