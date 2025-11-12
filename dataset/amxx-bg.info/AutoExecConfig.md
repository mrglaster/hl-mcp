# AutoExecConfig
#### Syntax
```
native AutoExecConfig(bool:autoCreate = true, const name[] = "", const folder[] = "");
```

#### Usage
autoCreate | ```If true, and the config file does not exist, such a config file will be automatically created and populated with information from the plugin's registered cvars.```
---|---
name | ```Name of the config file, excluding the .cfg extension. If empty, <plugin.filename.cfg> is assumed.```
folder | ```Folder under plugins/ to use.```
#### Description
```
Specifies that the given config file should be executed after plugin load.
```

#### Note
```
OnConfigsExecuted() will not be called until the config file has executed,
but it will be called if the execution fails.
```

#### Note
```
The name parameter should not contain dots, otherwise file will not be executed.
```

#### Return
```
This function has no return value.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

