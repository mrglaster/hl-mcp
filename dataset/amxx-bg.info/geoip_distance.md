# geoip_distance
#### Syntax
```
#define SYSTEM_METRIC   0 // kilometers
#define SYSTEM_IMPERIAL 1 // statute miles

native Float:geoip_distance(Float:lat1, Float:lon1, Float:lat2, Float:lon2, system = SYSTEM_METRIC);
```

#### Usage
lat1 | ```The first IP latitude.```
---|---
lon1 | ```The first IP longitude.```
lat2 | ```The second IP latitude.```
lon2 | ```The second IP longitude.```
system | ```The system of measurement, 0 = Metric(kilometers) or 1 = English(miles).```
#### Description
```
Calculate the distance between geographical coordinates, latitude and longitude.
```

#### Note
```
This native requires GeoIP City database, which can be retrieved from:
http://dev.maxmind.com/geoip/geoip2/geolite2/ (MaxMind DB binary)
```

#### Return
```
The distance as result in specified system of measurement.
```


This code is a part of geoip.inc. To use this code you should include geoip.inc as ```#include <geoip>```


  
  

