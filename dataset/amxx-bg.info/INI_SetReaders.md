# INI_SetReaders
#### Syntax
```
native INI_SetReaders(INIParser:smc, const kvFunc[], const nsFunc[] = "" );
```

#### Usage
handle | ```Handle to an INI Parse structure.```
---|---
kv | ```A KeyValue callback.```
ns | ```An optional NewSection callback.```
#### Description
```
Sets the two main reader functions.
```

#### Note
```
Below is the prototype of callback:
-
  NewSection:
      Called when the parser finds a new section.

      @param handle           Handle to an INI Parse structure.
      @param section          Name of section in between the [ and ] characters.
      @param invalid_tokens   True if invalid tokens were detected in the name.
      @param close_bracket    True if a closing bracket was detected, false otherwise.
      @param extra_tokens     True if extra tokens were detected on the line.
      @param curtok           Contains current token in the line where the section name starts.
                              You can add to this offset when failing to point to a token.
      @param data             Handle or value passed in INI_ParseFile

      @return                 True to keep parsing, false otherwise.

      public bool:OnNewSection(INIParser:handle, const section[], bool:invalid_tokens, bool:close_bracket, bool:extra_tokens, curtok, any:data)

  KeyValue:
      Called when the parser finds a new key/value pair.

      @param handle           Handle to an INI Parse structure.
      @param key              Name of key.
      @param value            String containing value (with quotes stripped, if any).
      @param invalid_tokens   Whether or not the key contained invalid tokens.
      @param equal_token      There was an '=' sign present (in case the value is missing).
      @param quotes           Whether value was enclosed in quotes.
      @param curtok           Contains the token index of the start of the value string.
                              This can be changed when returning false.
      @param data             Handle or value passed in INI_ParseFile

      @return                 True to keep parsing, false otherwise.

      public bool:OnKeyValue(INIParser:handle, const key[], const value[], bool:invalid_tokens, bool:equal_token, bool:quotes, curtok, any:data)
-
```

#### Return
```
This function has no return value.
```


This code is a part of textparse_ini.inc. To use this code you should include textparse_ini.inc as ```#include <textparse_ini>```


  
  

