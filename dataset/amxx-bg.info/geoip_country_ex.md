# geoip_country_ex
#### Syntax
```
native geoip_country_ex(const ip[], result[], len, id = -1);
```

#### Usage
ip | ```The IP address to lookup.```
---|---
result | ```The result of the geoip lookup.```
len | ```The maximum length of the result buffer.```
id | ```An optional player's index in order to return the result in the player's language, if supported. -1: the default language, which is english.  0: the server language. You can use LANG_SERVER define.                 >=1: the player's language.```
#### Description
```
Lookup the full country name for the given IP address.
```

#### Return
```
The result length on successful lookup, 0 otherwise.
```


This code is a part of geoip.inc. To use this code you should include geoip.inc as ```#include <geoip>```


  
  

