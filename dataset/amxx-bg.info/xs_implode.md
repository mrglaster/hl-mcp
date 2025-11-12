# xs_implode
#### Syntax
```
stock xs_implode(output[], outsize, delimiter, const input[][], elemsnum)
```

#### Usage
output | ```The string to store the impoded string into.```
---|---
outsize | ```The size of the output buffer.```
delimeter | ```The character to put between imploded strings.```
input | ```The array of strings to implode.```
elemsnum | ```The number of strings in the input array.```
#### Description
```
The opposite of xs_explode(). Takes an array of strings and puts them together
in a single string, delimeted by the @delimeter character.
```

#### Return
```
The number of characters in the final output buffer.
```


This code is a part of xs.inc. To use this code you should include xs.inc as ```#include <xs>```


  
  

