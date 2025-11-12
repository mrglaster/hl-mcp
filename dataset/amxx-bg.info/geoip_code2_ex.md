# geoip_code2_ex
#### Syntax
```
native bool:geoip_code2_ex(const ip[], result[3]);
```

#### Usage
ip | ```The IP address to lookup.```
---|---
result | ```The result buffer.  If the lookup does not succeed, the buffer is not modified.```
#### Description
```
Look up the two character country code for a given IP address.
e.g: "US", "CA", etc.
```

#### Return
```
true on a successful lookup, false on a failed lookup.
```


This code is a part of geoip.inc. To use this code you should include geoip.inc as ```#include <geoip>```


  
  

