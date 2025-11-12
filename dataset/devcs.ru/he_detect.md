# Детект броска и взрыва HEGRENADE (для Counter Strike 1.6)

```
#include <amxmodx>
#include <engine>
#include <hamsandwich>
#include <reapi>


new g_HookGrenadeThink;
new g_FwdThrow, g_FwdExplode, g_Ret;



public plugin_init() {
    register_plugin("HEGrenade API", "0.1", "[email protected]");
    RegisterHam(Ham_Spawn, "grenade", "HookGrenadeSpawn", 1);
    register_think("grenade", "HookGrenadeThinkExplode");
    g_FwdThrow = CreateMultiForward("gapi_grenade_throw", ET_IGNORE, FP_CELL, FP_CELL);
    g_FwdExplode = CreateMultiForward("gapi_grenade_explode", ET_IGNORE, FP_CELL, FP_CELL);

}


public HookGrenadeSpawn(ent) {
    g_HookGrenadeThink = register_think("grenade", "HookGrenadeThink");
}



public HookGrenadeThink(ent) {
    unregister_think(g_HookGrenadeThink);
    if (Float:get_entvar(ent, var_dmg) > 40.0) {
        ExecuteForward(g_FwdThrow, g_Ret, get_entvar(ent, var_owner), ent);

    }

}



public HookGrenadeThinkExplode(ent) {

    static dmgtime, gametime;
    if (Float:get_entvar(ent, var_dmg) > 40.0) {
        dmgtime = floatround(Float:get_entvar(ent, var_dmgtime) * 100.0, floatround_floor);
        gametime = floatround(get_gametime() * 100.0, floatround_floor);
        if (dmgtime == gametime) {
            ExecuteForward(g_FwdExplode, g_Ret, get_entvar(ent, var_owner), ent);

        }

    }

}
```


