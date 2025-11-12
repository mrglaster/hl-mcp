# xs_explode
#### Syntax
```
stock xs_explode(const input[], output[][], delimiter, maxelems, elemsize)
```

#### Usage
input | ```The input string to be exploded.```
---|---
output | ```The output array of string where exploded string will be stored.```
delimeter | ```The character to break the string at.```
maxelems | ```Maximum amount of elements in @output.```
elemsize | ```Maximum size of each string in the @output array.```
#### Description
```
"Explodes" a string, breaking it at the @delimeter character and putting
each exploded part into the @output array.
```

#### Return
```
The number of strings successfully exploded.
```


This code is a part of xs.inc. To use this code you should include xs.inc as ```#include <xs>```


  
  

