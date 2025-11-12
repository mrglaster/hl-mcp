# SMC_SetReaders
#### Syntax
```
native SMC_SetReaders(SMCParser:smc, const kvFunc[], const nsFunc[] = "", const esFunc[] = "");
```

#### Usage
handle | ```Handle to an SMC Parse structure.```
---|---
kv | ```A KeyValue callback.```
ns | ```An optional NewSection callback.```
es | ```An optional EndSection callback.```
#### Description
```
Sets the three main reader functions.
```

#### Note
```
Enclosing quotes are always stripped.
```

#### Note
```
Below is the prototype of callbacks:
-
  NewSection:
      Called when the parser finds a new section or sub-section.

      @param handle           Handle to an SMC Parse structure.
      @param name             String containing section name.
      @param data             Handle or value passed in SMC_ParseFile

      @return                 An SMCResult action to take.

      public SMCResult:OnNewSection(SMCParser:handle, const name[], any:data)

  KeyValue:
      Called when the parser finds a new key/value pair.

      @param handle        Handle to an SMC Parse structure.
      @param key           String containing key name.
      @param value         String containing value name.
      @param data          Handle or value passed in SMC_ParseFile

      @return              An SMCResult action to take.

      public SMCResult:OnKeyValue(SMCParser:handle, const key[], const value[], any:data)

  EndSection:
      Called when the parser finds the end of the current section.

      @param handle        Handle to an SMC Parse structure.
      @param data          Handle or value passed in SMC_ParseFile

      @return              An SMCResult action to take.

      public SMCResult:OnEndSection(SMCParser:handle, any:data)
-
```

#### Return
```
This function has no return value.
```


This code is a part of textparse_smc.inc. To use this code you should include textparse_smc.inc as ```#include <textparse_smc>```


  
  

