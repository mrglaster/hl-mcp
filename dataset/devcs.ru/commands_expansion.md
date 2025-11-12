# Автоматическое дополнение-расширение регистрируемых команд до полного списка.

```
const MAX_CMD_LEN = 32;

new const g_szCmds[] = "menu, vipmenu";
new const szPreCmd[][] = {"say ", "say_team ", ""};
new const szCtrlChar[][] = {"!", "/", "\", "." , ""};
new const FUNC_NAME[] = "Show_Menu";

Init_Cmds()
{
    if(strlen(g_szCmds))
    {
        for(new i; i < sizeof(szPreCmd); i++)
        {
            for(new k; k < sizeof(szCtrlChar); k++)
            {
                new szCmd[MAX_CMD_LEN], ePos, stPos, rawPoint[32];

                do
                {
                    ePos = strfind(g_szCmds[stPos],",");
                    formatex(rawPoint, ePos, g_szCmds[stPos]);
                    stPos += ePos + 1;
 
                    trim(rawPoint);
 
                    if(rawPoint[0])
                    {
                        formatex(szCmd, charsmax(szCmd),
                            "%s%s%s",
                            szPreCmd,
                            szCtrlChar[k],
                            rawPoint
                        );
                          
                        register_clcmd(szCmd, FUNC_NAME);
                    }
                }
                while(ePos != -1)
            }
        }
    }
}
```


