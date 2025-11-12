# fm_strip_user_gun Функция отбирает оружие по индексу
[The Fakemeta Module](http://amxxmodx.ru/fakemeta/) [fakemeta_util.inc](http://amxxmodx.ru/fakemeta/fakemeta_utilinc/)
Функция fm_strip_user_gun отбирает оружие по его Индексу ( CSW_* )  
Инфо из **fakemeta_util.inc**  
```
stock bool:fm_strip_user_gun(index, wid = 0, const wname[] = "") {  
    new ent_class[32];  
    if (!wid && wname[0])  
        copy(ent_class, sizeof ent_class - 1, wname);  
    else {  
        new weapon = wid, clip, ammo;  
        if (!weapon && !(weapon = get_user_weapon(index, clip, ammo)))  
            return false;  
          
        get_weaponname(weapon, ent_class, sizeof ent_class - 1);  
    }  
  
    new ent_weap = fm_find_ent_by_owner(-1, ent_class, index);  
    if (!ent_weap)  
        return false;  
  
    engclient_cmd(index, "drop", ent_class);  
  
    new ent_box = pev(ent_weap, pev_owner);  
    if (!ent_box || ent_box == index)  
        return false;  
  
    dllfunc(DLLFunc_Think, ent_box);  
  
    return true;  
}  

```
  
  
**Синтаксис :**  
stock fm_strip_user_gun(index, wid=0, const wname[] = "")   
  
• index - индекс игрока   
• wid - точно не знаю   
• wname[] - индекс оружия  
  
тип функции :  
**Stock**  
  
Пример использования :  
```
#include <amxmodx>  
#include <fakemeta_util>  
  
new pistols[6] = {CSW_USP, CSW_GLOCK18, CSW_ELITE, CSW_FIVESEVEN, CSW_P228, CSW_DEAGLE} // Записали индесы всех пистолетов  
  
public plugin_init()  
{  
 register_clcmd("say /strip", "strip_user_gun") // команда при помощи которой будем отбирать пистолет  
}  
  
public strip_user_gun(id)  
{  
 for(new i = 0; i < 6; i++) // Получаем все пистолеты из pistols[6]  
 {  
  fm_strip_user_gun(id, pistols[i]) // Отобрали пистолет   
 }  
}
```
  
  
и так если игрок зайдёт на сервер и напишет в чате **say /strip** ,  
У игрока будет отобран пистолет
