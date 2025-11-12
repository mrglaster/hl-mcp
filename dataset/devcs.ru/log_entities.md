# Плагин логирует список entity на карте в файл amxmodx/logs/entities.log

```
#include <amxmodx>
#include <amxmisc>
#include <engine>

new g_Dir[128];

public plugin_precache(){
    get_basedir(g_Dir, charsmax(g_Dir));
    add(g_Dir, charsmax(g_Dir), "/logs/entities.log");
}

public pfn_keyvalue(pEntityId)
{

    if(!is_valid_ent(pEntityId))
        return;

    static szClassName[64], szKeyName[64], szKeyValue[64];
    copy_keyvalue(
        szClassName,charsmax(szClassName),
        szKeyName,charsmax(szKeyName),
        szKeyValue,charsmax(szKeyValue)
    );

    Log_entity(g_Dir,
        "> %i, %s,%s,%s",
        pEntityId,
        szClassName,
        szKeyName,
        szKeyValue

    );
}


stock Log_entity(szLogsDir[], Message[], any:...) {
    static szMsg[512], pFile;
    vformat(szMsg, charsmax(szMsg), Message, 3);
    pFile = fopen(szLogsDir, "at");
    fprintf(pFile, "%s^n", szMsg);
    fclose(pFile);

}

```
