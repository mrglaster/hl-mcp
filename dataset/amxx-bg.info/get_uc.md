# get_uc
#### Syntax
```
native get_uc(uc_handle, UserCmd:member, any:...);
```

#### Description

Allows to get user control. The following example completely removes +use ability for players.

```
#include <amxmodx>
#include <fakemeta>

#define PLUGIN "New Plugin"
#define VERSION "1.0"
#define AUTHOR "Author"

public plugin_init() 
{
    register_plugin(PLUGIN, VERSION, AUTHOR)
    register_forward(FM_CmdStart, "fwdCmdStart");
}

public fwdCmdStart(id, handle)
{
    if(!is_user_alive(id))
        return FMRES_IGNORED;
        
    static button;
    button = get_uc(handle, UC_Buttons);
                
    if((button & IN_USE))
        button = (button & ~IN_USE)
                
    set_uc(handle, UC_Buttons, button);
        
    return FMRES_SUPERCEDE;
```


This code is a part of fakemeta.inc. To use this code you should include fakemeta.inc as ```#include <fakemeta>```


  
  

