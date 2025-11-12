# cs_set_user_plant Функция дает возможность закладывать бомбу
[CStrike](http://amxxmodx.ru/cstrike/)
Если вы выдали игроку бомбу допустим с помощью функции **fm_give_item** , то игрок все равно не сможет ее поставить, если выбросит и поднимет то сможет. Функция **cs_set_user_plant** исправляет эту проблему.   
  
Инфо из **cstrike.inc:**  
```
/* If plant is 1, a user will be set to be able to plant bomb within the usual bomb target areas if having one.  
 * You should use this if you give a player a weapon_c4, or he won't be able to plant it  
 * without dropping it and picking it up again (only possible for terrorists).  
 * If showbombicon is 1, the green C4 icon will be shown on user hud (if plant "skill" was enabled).  
 */  
native cs_set_user_plant(index, plant = 1, showbombicon = 1);  

```
  
  
**Синтаксис:**  

cs_set_user_plant(index, plant = 1, showbombicon = 1)
  

    * **index** - id игрока  

    * **plant = 1** - Устанавливает возможность заложить бомбу.  

    * **showbombicon = 1** - Показывать иконку бомбы  

  
  
**Тип функции:**  
Native  
  
**Пример:**  
```
#include <amxmodx>  
#include <amxmisc>  
#include <cstrike>  
#include <fakemeta_util>  
  
#define PLUGIN "[http://amxxmodx.ru] cs_set_user_plant"  
#define VERSION "1.0"  
#define AUTHOR "Admin"  
  
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
      
    register_clcmd("say /plant","plant)  
    register_clcmd("say /givec4","give_c4")  
  
}  
public give_c4(id){  
      
    fm_give_item(id, "weapon_c4")  
      
}  
public plant(id){  
      
    cs_set_user_plant(id,1,1)  
      
}
```
  
  
**Описание:**  
Две команды:  

    1. **say /givec4** Функция выдаст бомбу  

    2. **say /plant** Команда установит возможность заложить бомбу  

  
Зайдя в игру, выбросите бомбу, получите помощью первой команду и попробуйте ее поставить на пленте, после неудавшейся попытки выполните воторую команду и у вас все получится.
