# xs_log
#### Syntax
```
enum xs_logtypes
{
	xs_debug,
	xs_message,
	xs_warning,
	xs_error,
	xs_fatalerror,
	xs__assertionfailed,

	// must come last
	xs_logtypes_count
}

stock const xs__logtypenames[xs_logtypes_count][] = {"DEBUG", "", "WARNING", "ERROR", "FATAL ERROR", "DEBUG ASSERTION FAILED"};

// tested
stock xs_log(xs_logtypes:logtype, any:...)
```

#### Description
```
**** DEBUGGING / LOGING FUNCTIONS *****
```


This code is a part of xs.inc. To use this code you should include xs.inc as ```#include <xs>```


  
  

