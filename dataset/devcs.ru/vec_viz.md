# Код для визуализации вектора в пространстве.​

```
#include <amxmodx>
#include <engine>

// #define DEBUG_
// #define _THINK
#define _FASTVIS

const TASK_POINT = 1337;

#if defined DEBUG_

#if !defined _THINK
    public plugin_init()
    register_clcmd("radio1", "test");
    public test(pPlayer)
    #else
    public client_PostThink(pPlayer)
    #endif
    {
        static vOrigin_end[3], vOrigin_start[3];
        get_user_origin(pPlayer, vOrigin_start);            // Start point
        get_user_origin(pPlayer, vOrigin_end, .mode = 3);    // End point

        UTIL_VisualizeVector(
            .vStart = vOrigin_start,
            .vEnd = vOrigin_end,
            .time = 0.1,
            .width = 10
        );

        // return PLUGIN_HANDLED;
    }
#endif    // DEBUG_

new g_pBeamSprite;
new const SPRITE_BEAM[] = "sprites/arrow1.spr";
new const SPRITE_POINT[] = "sprites/3dmflared.spr";

public plugin_precache()
{
    g_pBeamSprite = precache_model(SPRITE_BEAM);
    precache_model(SPRITE_POINT);
}

public UTIL_VisualizeVector(vStart[3], vEnd[3], Float: time, width)
{
    message_begin(MSG_BROADCAST, SVC_TEMPENTITY);
    write_byte(TE_BEAMPOINTS);
    write_coord(vEnd[0]);
    write_coord(vEnd[1]);
    write_coord(vEnd[2]);
    write_coord(vStart[0]);
    write_coord(vStart[1]);
    write_coord(vStart[2]);
    write_short(g_pBeamSprite);
    write_byte(1);            //Стартовый кадр
    write_byte(1);            //Скорость анимации
    write_byte(floatround(time * 10));    //Время существования
    write_byte(width);        //Толщина луча
    write_byte(0);            //Искажение
    write_byte(255);            //Цвет красный
    write_byte(0);            //Цвет зеленый
    write_byte(0);            //Цвет синий
    write_byte(1000);        //Яркость
    write_byte(10);
    message_end();

#if !defined _FASTVIS
    CreatePoint(vStart, .time = time);
    CreatePoint(vEnd, .time = time);
#else
    // Create_Sparks(vStart);
    Create_Sparks(vEnd);
#endif
}

stock CreatePoint(vOrigin[3], Float: time)
{
    static pEnt, Float: fOrigin[3];
    pEnt = create_entity("info_target");
    IVecFVec(vOrigin, fOrigin);

    if(is_valid_ent(pEnt))
    {
        // entity_set_string(pEnt, EV_SZ_classname, "points");
        entity_set_model(pEnt, SPRITE_POINT);
        entity_set_origin(pEnt, fOrigin);
        entity_set_int(pEnt, EV_INT_solid, SOLID_NOT);
        entity_set_int(pEnt, EV_INT_movetype, MOVETYPE_NONE);
        entity_set_float(pEnt, EV_FL_scale, 0.1);
        entity_set_float(pEnt, EV_FL_nextthink, get_gametime());
        entity_set_int(pEnt, EV_INT_rendermode, kRenderTransAdd);
        entity_set_float(pEnt, EV_FL_renderamt, 100.0);
    
        set_task(time, "DeleteEnt", TASK_POINT + pEnt);
    }
}

stock Create_Sparks(vOrigin[3])
{
    message_begin(MSG_BROADCAST, SVC_TEMPENTITY);
    write_byte(TE_SPARKS);
    write_coord(vOrigin[0]);
    write_coord(vOrigin[1]);
    write_coord(vOrigin[2]);
    message_end();
}


public DeleteEnt(pEnt)
{
    pEnt -= TASK_POINT;
    if(is_valid_ent(pEnt))
        remove_entity(pEnt);
}
```

Пример использования:
```
public client_PostThink(pPlayer)
{
    static vOrigin_end[3], vOrigin_start[3];
    get_user_origin(pPlayer, vOrigin_start);            // Start point
    get_user_origin(pPlayer, vOrigin_end, .mode = 3);    // End point

    UTIL_VisualizeVector(
        .vStart = vOrigin_start,
        .vEnd = vOrigin_end,
        .time = 0.1,
        .width = 10
    );
}
```
