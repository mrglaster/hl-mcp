# Релиз плагина - Damage Killer
[Готовые скрипты](http://amxxmodx.ru/scripts/)
**Автор** : Valer4  
**Версия** : 1.0 специально для <http://amxxmodx.ru>  
**Плагин** : пишет игрокам цветные сообщения в чат с именем, количеством  
здоровья и брони его убийцы, а также сколько здоровья он отнял у Вас и Вы у него.  
Команда для игроков - dk - включить/отключить, в общий или командный чат, со слешем или без.  
Значение команды сохраняется в конфиге игрока - setinfo dk on/off.  
Есть квар: dk_delay - через сколько секунд после смерти выводить сообщение, чтобы учитывался урон от гранаты взорвавшейся после смерти, по умолчанию 2 секунды.  
Для работы необходимы плагин colorchat и инклуд chatcolor.  
```
#include<amxmodx>  
#include<chatcolor>  
  
new g_DK_Damage[32][32]  
  
public plugin_init()  
{  
    register_plugin("[http://amxxmodx.ru] Damage Killer", "1.0", "Valer4")  
    register_clcmd("say /dk", "dk_switch")  
    register_clcmd("say dk", "dk_switch")  
    register_cvar("dk_delay", "2.0")  
}  
  
public client_damage(b_DK_Attacker_A, b_DK_Victim_A, b_DK_Damage)  
    g_DK_Damage[b_DK_Attacker_A][b_DK_Victim_A] += b_DK_Damage  
  
public client_death(b_DK_Attacker_B, b_DK_Victim_B)  
{  
    if(b_DK_Attacker_B != b_DK_Victim_B)  
    {  
        new DK_Killer_Name[32], DK_Damage_Killer_A[32]  
        get_user_info(b_DK_Victim_B, "damage_killer", DK_Damage_Killer_A, 31)  
        if(!equali(DK_Damage_Killer_A, "off"))  
        {  
            get_user_name(b_DK_Attacker_B, DK_Killer_Name, 31)  
            client_print_color(b_DK_Victim_B, Red, "^4Вас убил ^3%s^4, у него осталось ^3%d ^4HP и ^3%d ^4AP", DK_Killer_Name, get_user_health(b_DK_Attacker_B), get_user_armor(b_DK_Attacker_B))  
            client_print_color(b_DK_Victim_B, Red, "^4Он отнял у Вас ^3%d ^4HP, а Вы у него ^3%d ^4HP", g_DK_Damage[b_DK_Attacker_B][b_DK_Victim_B], g_DK_Damage[b_DK_Victim_B][b_DK_Attacker_B])  
        }  
    }  
    set_task(get_cvar_float("dk_delay"), "dk_reset", b_DK_Victim_B)  
}  
  
public dk_reset(b_DK_PID_A)  
{  
    new DK_Players[32], DK_Num, DK_Item  
    get_players(DK_Players, DK_Num)  
    for(DK_Item = 0; DK_Item < DK_Num; DK_Item ++)  
    {  
        g_DK_Damage[DK_Players[DK_Item]][b_DK_PID_A] = 0  
        g_DK_Damage[b_DK_PID_A][DK_Players[DK_Item]] = 0  
    }  
}  
  
public dk_switch(b_DK_PID_B)  
{  
    new DK_Damage_Killer_B[32]  
    get_user_info(b_DK_PID_B, "damage_killer", DK_Damage_Killer_B, 31)  
    if(equali(DK_Damage_Killer_B, "off"))  
    {  
        client_cmd(b_DK_PID_B, "setinfo damage_killer on")  
        client_print_color(b_DK_PID_B, Red, "^4Показ сообщений об уроне - ^3ВКЛЮЧЕН^4!")  
        return PLUGIN_HANDLED  
    }  
    else  
    {  
        client_cmd(b_DK_PID_B, "setinfo damage_killer off")  
        client_print_color(b_DK_PID_B, Red, "^4Показ сообщений об уроне - ^3ОТКЛЮЧЕН^4!")  
        return PLUGIN_HANDLED  
    }  
    return PLUGIN_CONTINUE  
}
```
  
![Релиз плагина - Damage Killer](http://amxxmodx.ru/uploads/posts/2013-01/1358163344_damage_killer.png)  
  
  
Вы не можете скачивать файлы с нашего сервера
