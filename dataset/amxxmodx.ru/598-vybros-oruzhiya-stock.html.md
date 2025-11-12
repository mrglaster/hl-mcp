# Выброс оружия (stock)
[Присланное](http://amxxmodx.ru/other/)
**Описание:**  
Данный сток нужен для создания новой пушки.  
А точнее чтобы не было бага что игрок носит по 2 и более основного/вторичного оружия.  
  
**Тип функции:**  
Stock  
  
**Требуемые инклюди:**  
amxmodx  
fakemeta  
fakemeta_util  
hamsandwich  
  
Сам сток:  
```
stock UTIL_DropWeapons(id, dropwhat)  
{  
    static weapons[32], num, i, weaponid  
    num = 0  
    get_user_weapons(id, weapons, num)  
      
    for (i = 0; i < num; i++)  
    {  
        weaponid = weapons[i]  
          
        if ((dropwhat == 1 && ((1<<weaponid) & PRIMARY_WEAPONS_BIT_SUM)) || (dropwhat == 2 && ((1<<weaponid) & SECONDARY_WEAPONS_BIT_SUM)))  
        {  
            static wname[32], weapon_ent  
            get_weaponname(weaponid, wname, charsmax(wname))  
            weapon_ent = fm_find_ent_by_owner(-1, wname, id)  
              
            set_pev(weapon_ent, PEV_ADDITIONAL_AMMO, cs_get_user_bpammo(id, weaponid))  
              
            engclient_cmd(id, "drop", wname)  
            cs_set_user_bpammo(id, weaponid, 0)  
        }  
    }  
}
```
  
  
**Функциональность стока:**  
```
UTIL_DropWeapons(id, 1)
```
- выбрасивает основное оружие  
```
UTIL_DropWeapons(id, 2)
```
- выбрасивает вторичное оружие  
  
Пример использования:  
```
  
    new weaponid = get_weaponid(weapon)  
    if(!weaponid) return;  
      
    if(((1<<weaponid) & PRIMARY_WEAPONS_BIT_SUM)) UTIL_DropWeapons(id, 1)  
    else if(((1<<weaponid) & SECONDARY_WEAPONS_BIT_SUM)) UTIL_DropWeapons(id, 2)
```
  
  
p.s. Пример сам по себе работать не будет.
