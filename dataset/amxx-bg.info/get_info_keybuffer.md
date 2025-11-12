# get_info_keybuffer
#### Syntax
```
native get_info_keybuffer(id, buffer[], length);
```

#### Usage
id | ```Server/client index```
---|---
buffer | ```Buffer to copy keybuffer to```
length | ```Maximum size of buffer```
#### Description
```
Retrieves keyvalue buffer from a client or the server.
```

#### Note
```
There are three different types of keyvalue buffers, depending on the
index passed:
    -1 - "local" buffer (various server information and config values)
     0 - server buffer (usually contains "*gamedir" only)
    >0 - client buffer ("name", "rate" and other client info)
```

#### Note
```
The buffer is formatted as "\key1\value1\key2\value2\...\keyN\valueN"
```

#### Return
```
Number of cells written to buffer
```

#### Error
```
If an invalid entity index is provided or, if the index is a
client index, the client is not connected, an error will be
thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

