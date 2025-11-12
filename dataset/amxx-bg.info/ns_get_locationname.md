# ns_get_locationname
#### Syntax
```
native ns_get_locationname(Float:x, Float:y, name[], len, titlelookup=0);
```

#### Description
```
Returns the location name of the provided x/y position
(z origin is ignored; can't have location over location)
-
Note that as of NS 3.2 beta 2, on the following maps
the returned string should be passed through ns_lookup_title
to be human readable:
  ns_bast, ns_hera, ns_nothing, ns_tanith,
  ns_nancy, ns_caged, ns_eclipse, ns_veil

Passing the 5th parameter as non zero will auto look up
the title if it exists.
```


This code is a part of ns.inc. To use this code you should include ns.inc as ```#include <ns>```


  
  

Warning: This include is compatible only with Natural Selection and will not function with other mods (e.g., Valve, Counter Strike 1.6, etc.).