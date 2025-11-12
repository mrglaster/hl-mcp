# get_pdata_string
#### Syntax
```
native get_pdata_string(entity, offset, dest[], maxlength, byref=1, linux, mac=cellmin);
```

#### Description

Allows to get plauer data as string 

```
#define MAX_TEAMNAME_LENGTH    16

const m_szTeamName = 383
const XTRA_OFS_PLAYER = 5

new szTeamName[MAX_TEAMNAME_LENGTH]

get_pdata_string(iPlayer, m_szTeamName * 4, szTeamName, MAX_TEAMNAME_LENGTH, 0, XTRA_OFS_PLAYER)
set_pdata_string(iPlayer, m_szTeamName * 4, szTeamName, -1, XTRA_OFS_PLAYER)  
```


This code is a part of fakemeta.inc. To use this code you should include fakemeta.inc as ```#include <fakemeta>```


  
  

