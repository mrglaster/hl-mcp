# geoip_country
#### Syntax
```
#pragma deprecated Use geoip_country_ex() instead.
native geoip_country(const ip[], result[], len = 45);
```

#### Usage
ip | ```The IP address to lookup.```
---|---
result | ```The result of the geoip lookup.```
len | ```The maximum length of the result buffer.```
#### Description
```
Lookup the full country name for the given IP address.  Sets the buffer to "error" on
an unsuccessful lookup.
```

#### Return
```
The result length.
```


This code is a part of geoip.inc. To use this code you should include geoip.inc as ```#include <geoip>```


  
  

