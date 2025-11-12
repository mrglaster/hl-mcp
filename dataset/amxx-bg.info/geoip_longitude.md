# geoip_longitude
#### Syntax
```
native Float:geoip_longitude(const ip[]);
```

#### Usage
ip | ```The IP address to look up.```
---|---
#### Description
```
Look up the city's longitude for the given IP address.
```

#### Note
```
This native requires GeoIP City database, which can be retrieved from:
http://dev.maxmind.com/geoip/geoip2/geolite2/ (MaxMind DB binary)
```

#### Return
```
The result of the geoip look up, 0 if longitude is not found.
```


This code is a part of geoip.inc. To use this code you should include geoip.inc as ```#include <geoip>```


  
  

