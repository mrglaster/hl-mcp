# get_global_vector
#### Syntax
```
native get_global_vector(variable, Float:vector[3]);
```

#### Usage
variable | ```Entry to retrieve from```
---|---
vector | ```Array to store vector in```
#### Description
```
Returns a vector type value from the server globals.
```

#### Note
```
For a list of valid vector type entries, see the GL_* constants in
engine_const.inc under the "Vector" section.
```

#### Return
```
This function has no return value.
```

#### Error
```
If an invalid entry is provided, an error will be thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

