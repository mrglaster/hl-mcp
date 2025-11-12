# tickcount
#### Syntax
```
native tickcount(&granularity = 0);
```

#### Usage
granularity | ```Unused```
---|---
#### Description
```
Returns the elapsed CPU seconds.
```

#### Note
```
This is a debugging function that is not intended for general plugin
use.
```

#### Note
```
This uses the C clock() function internally and comes with all its
drawbacks attached.
```

#### Return
```
Number of CPU seconds elapsed
```


This code is a part of core.inc. To use this code you should include core.inc as ```#include <core>```


  
  

