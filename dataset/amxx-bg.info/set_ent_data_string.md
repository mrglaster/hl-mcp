# set_ent_data_string
#### Syntax
```
native set_ent_data_string(entity, const class[], const member[], const value[], element = 0);
```

#### Usage
entity | ```Entity index```
---|---
class | ```Class name```
member | ```Member name```
value | ```String to set```
element | ```Element to set (starting from 0) if member is an array```
#### Description
```
Sets a string to an entity's private data based off a class and member name.
```

#### Note
```
Unlike the [get|set]_pdata_* natives that require compiling the class
member offset into the plugin, this native instead retrieves the
necessary offset from the AMXX gamedata files at runtime, based on the
provided class and member name.
```

#### Note
```
This native is safer than [get|set]_pdata_* as it can perform stricter
offset and typing checks.
```

#### Note
```
This native is used to access the following (C++/engine) data types:
string, stringptr.
```

#### Return
```
Number of cells written to buffer
```

#### Error
```
If an invalid entity is provided, either class or member is
empty, no offset is found or an invalid offset is retrieved,
or the data type does not match, an error will be thrown.
```


This code is a part of fakemeta.inc. To use this code you should include fakemeta.inc as ```#include <fakemeta>```


  
  

