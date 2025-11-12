# GetModelBoundingBox
#### Syntax
```
native GetModelBoundingBox(entity, Float:mins[3], Float:maxs[3], sequence = Model_DefaultSize);
```

#### Usage
entity | ```The entity index to use.```
---|---
mins | ```The local negative bounding box distance.```
maxs | ```The local positive bounding box distance.```
sequence | ```The animation sequence to retrieve. Model_DefaultSize retrieves ideal moevement hull size. Model_CurrentSequence retrieves hull size of the current sequence. Values >= 0 will specify which sequence to retrieve size from.```
#### Description
```
Gets size of a model bounding box.
```

#### Return
```
1 on success, 0 on faillure.
```

#### Error
```
Invalid entity.
Invalid model pointer.
```


This code is a part of fakemeta.inc. To use this code you should include fakemeta.inc as ```#include <fakemeta>```


  
  

