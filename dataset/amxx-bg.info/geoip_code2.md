# geoip_code2
#### Syntax
```
#pragma deprecated Use geoip_code2_ex() instead.
native geoip_code2(const ip[], ccode[3]);
```

#### Usage
ip | ```The IP address to lookup.```
---|---
result | ```The result buffer.```
#### Description
```
Lookup the two character country code for a given IP address. Sets the buffer to "error" on
an unsuccessful lookup.
```

This function is deprecated, do NOT use it!
**Reason:** This native will overflow the buffer by one cell on an unknown ip lookup! Use geoip_code2_ex instead.
#### Return
```
The result length.
```


This code is a part of geoip.inc. To use this code you should include geoip.inc as ```#include <geoip>```


  
  

