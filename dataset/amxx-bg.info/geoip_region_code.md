# geoip_region_code
#### Syntax
```
native geoip_region_code(const ip[], result[], len);
```

#### Usage
ip | ```The IP address to look up.```
---|---
result | ```The result of the geoip look up.```
len | ```The maximum length of the result buffer.```
#### Description
```
Look up the region/state code for the given IP address.
e.g. "US-OH", "DE-HH", IT-82, "FR-U", etc.
```

#### Note
```
This native requires GeoIP City database, which can be retrieved from:
http://dev.maxmind.com/geoip/geoip2/geolite2/ (MaxMind DB binary)
```

#### Return
```
The result length on successful lookup, 0 otherwise.
```


This code is a part of geoip.inc. To use this code you should include geoip.inc as ```#include <geoip>```


  
  

