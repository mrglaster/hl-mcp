# set_module_filter
#### Syntax
```
native set_module_filter(const handler[]);
```

#### Description
```
Sets a module/library filter, letting the plugin intercept and handle an
automatic module requirement.
```

#### Note
```
This has to be used inside the plugin_native() forward, otherwise it
has no effect.
```

#### Note
```
This is useful for creating plugins that can dynamically decide which
modules or features to use at runtime, often necessary for cross-mod
plugins. It allows to deploy a single version of the plugin instead
of compiling multiple versions for each use-case.
```

#### Note
```
For a list of possible libtypes see the LibType enum in amxconst.inc
```

#### Note
```
The handler will be called in the following manner:

public module_filter(const library[], LibType:type)

  library     - Shortname of library or class that is required
  libtrype    - Type of requirement being checked (library/module or class)
```

#### Note
```
The handler should return PLUGIN_CONTINUE to let the error through the
filter (which will result in the plugin failing to load), or
PLUGIN_HANDLED to imply that load can continue without the module.
```

#### Note
```
Errors occuring inside the handler will not be filtered and cause the
plugin to fail load as if the handler returned PLUGIN_CONTINUE.
```

#### Return
```
0 on success, -1 if filtering is not available, -2 if handler
could not be found.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

