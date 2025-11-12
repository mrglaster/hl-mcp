# geoip_timezone
#### Syntax
```
native geoip_timezone(const ip[], result[], len);
```

#### Usage
ip | ```The IP address to look up.```
---|---
result | ```The result of the geoip look up.```
len | ```The maximum length of the result buffer.```
#### Description
```
Look up the full time zone for the given IP address.
e.g. America/Los_Angeles, Europe/Paris.
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


  
  

