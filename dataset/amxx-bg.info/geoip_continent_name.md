# geoip_continent_name
#### Syntax
```
native geoip_continent_name(const ip[], result[], len, id = -1);
```

#### Usage
ip | ```The IP address to look up.```
---|---
result | ```The result of the geoip look up.```
len | ```The maximum length of the result buffer.```
id | ```An optional player's index in order to return the result in the player's language, if supported. -1: the default language, which is english.  0: the server language. You can use LANG_SERVER define.                 >=1: the player's language.```
#### Description
```
Look up the full continent name for the given IP address.
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


  
  

