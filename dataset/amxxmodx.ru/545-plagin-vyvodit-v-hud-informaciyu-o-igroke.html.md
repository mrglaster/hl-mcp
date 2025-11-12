# Плагин выводит в HUD информацию о игроке
[Плагины с официального сайта](http://amxxmodx.ru/amxmodx_plugins/) [Плагины связанные с данными и статистикой](http://amxxmodx.ru/amxmodx_plugins/statistical/)
**Описание:**  
Когда вы находитесь в спектаторах и наблюдаете от первого лица за игроком, то вам в HUD сообщении выводится информация о здоровье, броне и деньгах этого игрока  
  
**Настройки:**  

amx_spec_hud_color "RRR GGG BBB" <default : "250 250 250">
  
Квар с настройкой цвета сообщения.  
  
**Необходимые модули:**  
Engine  
  
**Исходный код:**  

![](http://amxxmodx.ru/templates/3week92/dleimages/spoiler-plus.gif) [Показать / Скрыть текст](javascript:ShowOrHide\('sp7b864b98de52fa362b13fc85ad9084e3'\))
```
/*    Formatright © 2010, ConnorMcLeod  
  
    This plugin is free software;  
    you can redistribute it and/or modify it under the terms of the  
    GNU General Public License as published by the Free Software Foundation.  
  
    This program is distributed in the hope that it will be useful,  
    but WITHOUT ANY WARRANTY; without even the implied warranty of  
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the  
    GNU General Public License for more details.  
  
    You should have received a copy of the GNU General Public License  
    along with this plugin; if not, write to the  
    Free Software Foundation, Inc., 59 Temple Place - Suite 330,  
    Boston, MA 02111-1307, USA.  
*/  
  
#include <amxmodx>  
#include <engine>  
  
#define VERSION "0.0.1"  
#define PLUGIN "Spectator Hud Informations"  
  
#define MAX_PLAYERS        32  
#define FIRST_PERSON_VIEW 4  
  
new const g_iWeaponIdToAmmoId[] = {  
        0, 9, 0, 2, 12, 5, 14, 6, 4, 13, 10, 7, 6, 4, 4, 4, 6, 10, 1, 10, 3, 5, 4, 10, 2, 11, 8, 4, 2, 0, 7}  
          
new g_iHealth[MAX_PLAYERS+1]  
new g_iArmor[MAX_PLAYERS+1]  
new g_iMoney[MAX_PLAYERS+1]  
new g_iCurWeapon[MAX_PLAYERS+1]  
new g_iAmmo[MAX_PLAYERS+1]  
new g_iBpAmmo[MAX_PLAYERS+1][15]  
  
new g_dhud_color  
  
public plugin_init()  
{  
    register_plugin(PLUGIN, VERSION, "ConnorMcLeod")  
  
    register_cvar("amx_spec_hud_color", "250 250 250")  
  
    register_event("Money", "Event_Money", "b")  
    register_event("CurWeapon", "Event_CurWeapon", "b", "1=1")  
    register_event("Health", "Event_Health", "b")  
    register_event("Battery", "Event_Battery", "b")  
    register_event("AmmoX", "Event_AmmoX", "b", "1<15")  
  
    new szColor[12], szRed[4], szGreen[4], szBlue[4], r, g, b  
    get_cvar_string("amx_spec_hud_color", szColor, charsmax(szColor))  
    parse(szColor, szRed, charsmax(szRed), szGreen, charsmax(szGreen), szBlue, charsmax(szBlue))  
    r = clamp( str_to_num(szRed), 0, 255)  
    g = clamp( str_to_num(szGreen), 0, 255)  
    b = clamp( str_to_num(szBlue), 0, 255)  
    g_dhud_color = b + ( g << 8 ) + ( r << 16 )  
  
    new iEnt = create_entity("info_target")  
    if( iEnt )  
    {  
        entity_set_float(iEnt, EV_FL_nextthink, get_gametime() + 0.1)  
        entity_set_string(iEnt, EV_SZ_classname, "_hud_spec")  
        register_think("_hud_spec", "UpdateSpecHud")  
    }  
    else  
    {  
        set_task(0.1, "UpdateSpecHud", .flags="b")  
    }  
}  
  
public UpdateSpecHud( iEnt )  
{  
    if( iEnt )  
    {  
        entity_set_float(iEnt, EV_FL_nextthink, get_gametime() + 0.1)  
    }  
    static iAlivePlayers[32], iDeadPlayers[32], iAliveCount, iDeadCount, iAlivePlayer, iDeadPlayer, i  
    static iAmmo  
    static bool:bRetrievedValues, szMessage1[128], szMessage2[128], iLen1, iLen2  
    get_players(iAlivePlayers, iAliveCount, "a")  
    if( !iAliveCount )  
    {  
        return  
    }  
    get_players(iDeadPlayers, iDeadCount, "bch")  
    if( !iDeadCount )  
    {  
        return  
    }  
  
    for(--iAliveCount; iAliveCount>=0; iAliveCount--)  
    {  
        bRetrievedValues = false  
        iAlivePlayer = iAlivePlayers[iAliveCount]  
        for(i=0; i<iDeadCount; i++)  
        {  
            iDeadPlayer = iDeadPlayers[i]  
            if( entity_get_int(iDeadPlayer, EV_INT_iuser2) == iAlivePlayer && entity_get_int(iDeadPlayer, EV_INT_iuser1) == FIRST_PERSON_VIEW )  
            {  
                if( !bRetrievedValues )  
                {  
                    iLen1 = 31+ formatex(szMessage1, charsmax(szMessage1), "%3d HP^t^t^t%3d AP", g_iHealth[iAlivePlayer], g_iArmor[iAlivePlayer])  
                    iAmmo = g_iAmmo[iAlivePlayer]  
                    if( iAmmo != -1 )  
                    {  
                        iLen2 = 31 + formatex(  
                                        szMessage2, charsmax(szMessage2),   
                                        "$ %5d^n%3d|%3d",   
                                        g_iMoney[iAlivePlayer], iAmmo, g_iBpAmmo[iAlivePlayer][  g_iWeaponIdToAmmoId[ g_iCurWeapon[iAlivePlayer] ]  ]  
                                        )  
                    }  
                    else  
                    {  
                        iLen2 = 31 + formatex(szMessage2, charsmax(szMessage2), "$ %5d^n", g_iMoney[iAlivePlayer])  
                    }  
                    bRetrievedValues = true  
                }  
  
                __show__dhudmessage(iDeadPlayer, szMessage1, iLen1, _:0.01, _:0.98)  
                __show__dhudmessage(iDeadPlayer, szMessage2, iLen2, _:0.92, _:0.93)  
  
                iDeadPlayers[i--] = iDeadPlayers[--iDeadCount]  
                if( !iDeadCount )  
                {  
                    return  
                }  
            }  
        }  
    }  
}  
  
public Event_Money( id )  
{  
    g_iMoney[id] = read_data(1)  
}  
  
public Event_CurWeapon(id)  
{  
    g_iCurWeapon[id] = read_data(2)  
    g_iAmmo[id] = read_data(3)  
}  
  
public Event_AmmoX(id)  
{  
    g_iBpAmmo[id][read_data(1)] = read_data(2)  
}  
  
public Event_Health(id)  
{  
    g_iHealth[id] = read_data(1)  
}  
  
public Event_Battery(id)  
{  
    g_iArmor[id] = read_data(1)  
}  
  
// code extracted from Director Hud Message include file  
// forums.alliedmods.net/showthread.php?t=149210  
__show__dhudmessage(id, const szMessage[], iLen, x, y)  
{  
    message_begin( MSG_ONE_UNRELIABLE , SVC_DIRECTOR, .player=id )  
    {  
        write_byte( iLen )  
        write_byte( DRC_CMD_MESSAGE )  
        write_byte( 0 )  
        write_long( g_dhud_color )  
        write_long( x )  
        write_long( y )  
        write_long( 0x38D1B717 )  
        write_long( 0x38D1B717 )  
        write_long( 0x3DF5C28F )  
        write_long( 0 )  
        write_string( szMessage )  
    }  
    message_end()  
}
```

  
  
**Скачать плагин:**  
Вы не можете скачивать файлы с нашего сервера  
  
В плагине показано как получить данные о игроке кто наблюдает и за кем наблюдает игрок.
