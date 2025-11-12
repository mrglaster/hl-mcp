# Сток для автоматической регистрации списка команд в зависимости от их типа (cmd, impulse)​

```
#include <amxmodx>
#include <engine>

new g_szCmds[][] = {
    "radio1",
    "impulse 201",
    "nightvision"
}

new const MENU_CMD[] = "CMD_MenuOpen";

public plugin_init()
{
    RegisterCmds(g_szCmds, sizeof g_szCmds, MENU_CMD);
}

RegisterCmds(szCmds[][], iLen, const szFunction[])
{
    for(new i; i < iLen; i++)
    {
        if(containi(szCmds, "impulse") != -1)
            register_impulse(str_to_num(szCmds[8]), szFunction);
        else
            register_clcmd(szCmds, szFunction);
    }
}

public MyMenu(pPlayer)
    // Hooked
```
