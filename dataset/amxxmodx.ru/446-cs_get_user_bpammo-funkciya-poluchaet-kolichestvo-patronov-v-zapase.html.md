# cs_get_user_bpammo Функция получает количество патронов в запасе
[CStrike](http://amxxmodx.ru/cstrike/)
Обратите внимание на то, что функция получает количество патронов по типу, а не для того оружия что у вас есть.  
То есть если вы купили Мку с 90 патронами + 30 в магазине, затем ее выкинули и подобрали АК, то в запасе у вас все равно останутся 90 патронов для Мки.  
  
Инфо из **cstrike.inc:**  
```
/* Get amount of ammo in backpack on a user for a specific weapon.  
 * Look in amxconst.inc for weapon types: CSW_*.  
 * Weapons on the same line uses the same ammo type:  
 * awm  
 * scout, ak, g3  
 * para  
 * famas, m4a1, aug, sg550, galil, sg552  
 * m3, xm  
 * usp, ump, mac  
 * fiveseven, p90  
 * deagle  
 * p228  
 * glock, mp5, tmp, elites  
 * flash  
 * he  
 * smoke  
 */  
native cs_get_user_bpammo(index, weapon);
```
  
  
**Синтаксис:**  

cs_get_user_bpammo(index, weapon)
  

    * **index** - id игрока  

    * **weapon** - Константа оружия вида CSW_*:  

      * awm  

      * scout, ak, g3  

      * para  

      * famas, m4a1, aug, sg550, galil, sg552  

      * m3, xm  

      * usp, ump, mac  

      * fiveseven, p90  

      * deagle  

      * p228  

      * glock, mp5, tmp, elites  

      * flash  

      * he  

      * smoke  

  
  

  
  
**Тип функции:**  
Native  
  
**Пример:**  
```
#include <amxmodx>  
#include <amxmisc>  
#include <cstrike>  
  
#define PLUGIN "[http://amxxmodx.ru] func_get_ammo"  
#define VERSION "1.0"  
#define AUTHOR "Admin"  
  
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
      
    register_clcmd("say /my_ammo","func_get_ammo")  
  
}  
public func_get_ammo(id){  
    client_print(id,print_chat,"You have usp [%d] ammo",cs_get_user_bpammo(id,CSW_USP))  
    client_print(id,print_chat,"You have m4a1 [%d] ammo",cs_get_user_bpammo(id,CSW_M4A1))  
      
}
```
  
  
**Описание:**  
При выполнении команды **say /my_ammo** будет выдано 2 сообщения в чат, о наличии у вас в запасе патронов для USP и M4A1.  
Попробуйте выкинуть/купить/подобрать/пострелять и т.п.
