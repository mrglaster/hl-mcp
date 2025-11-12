# AddMenuItem_call
#### Syntax
```
stock AddMenuItem_call(const MENU_TEXT[], const MENU_CMD[], const MENU_ACCESS, const MENU_PLUGIN[], const bool:ADD_TO_CLIENT_MENU)
```

#### Usage
MENU_TEXT | ```Item text that will be displayed in the menu```
---|---
MENU_CMD | ```Command that will be executed on the client```
MENU_ACCESS | ```Admin access required for menu command```
MENU_PLUGIN | ```Case-insensitive name or filename of plugin providing the menu command```
ADD_TO_CLIENT_MENU | ```If true adds command to client menu, false adds to admin menu```
#### Description
```
Helper function used by AddMenuItem() and AddClientMenuItem()
```

#### Return
```
This function has no return value.
```


This code is a part of amxmisc.inc . To use this code you should include amxmisc.inc as ```#include <amxmisc>```


  
  

