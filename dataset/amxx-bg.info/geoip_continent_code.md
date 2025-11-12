# geoip_continent_code
#### Syntax
```
enum Continent
{
	CONTINENT_UNKNOWN = 0,
	CONTINENT_AFRICA,
	CONTINENT_ANTARCTICA,
	CONTINENT_ASIA,
	CONTINENT_EUROPE,
	CONTINENT_NORTH_AMERICA,
	CONTINENT_OCEANIA,
	CONTINENT_SOUTH_AMERICA,
};
native Continent:geoip_continent_code(const ip[], result[3]);
```

#### Usage
ip | ```The IP address to look up.```
---|---
result | ```The result of the geoip look up.```
#### Description
```
Look up the continent code for a given IP address.
```

#### Note
```
This native requires GeoIP City database, which can be retrieved from:
http://dev.maxmind.com/geoip/geoip2/geolite2/ (MaxMind DB binary)
```

#### Note
```
The code can be retrieved as integer (See CONTINENT_* constants.) or string (2 characters).
```

#### Note
```
Possible continent codes are AF, AN, AS, EU, NA, OC, SA for
Africa(1), Antarctica(2), Asia(3), Europe(4), North America(5), Oceania(6), South America(7).
```

#### Return
```
The continent id on successful lookup, 0 otherwise.
```


This code is a part of geoip.inc. To use this code you should include geoip.inc as ```#include <geoip>```


  
  

