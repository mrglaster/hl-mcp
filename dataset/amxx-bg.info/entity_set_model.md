# entity_set_model
#### Syntax
```
native entity_set_model(iIndex, const szModel[]);
```

#### Usage
iIndex | ```Entity index```
---|---
szModel | ```Model to set```
#### Description
```
Sets the model of an entity.
```

#### Note
```
This native uses an engine function to set the model, keeping it
properly updated with the game. Simply writing to EV_SZ_model is an
error and will cause problems.
```

#### Return
```
This function has no return value.
```

#### Error
```
If an invalid entity index is provided, an error will be
thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

