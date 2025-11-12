# cs_get_user_mapzones Функция получает в какой из зон находится игрок.
[CStrike](http://amxxmodx.ru/cstrike/)
Инфо из **cstrike.inc:**  
```
#define CS_MAPZONE_BOMBTARGET         (1<<1)  
#define CS_MAPZONE_HOSTAGE_RESCUE     (1<<2)  
#define CS_MAPZONE_ESCAPE        (1<<3)  
#define CS_MAPZONE_VIP_SAFETY         (1<<4)  
  
/* Returns in bitwise form if the user is in a specific map zone.  
 * NOTE: If user can't plant (cs_get_user_plant(index) is 0) then cs_get_user_mapzones(index) & CS_MAPZONE_BOMBTARGET will return 0 too.  
 */  
native cs_get_user_mapzones(index);
```
  
  
**Синтаксис:**  

cs_get_user_mapzones(index)
  

    * **index** - Индекс игрока  

Функция вернет бит соответствующий одной из зон:  

    * CS_MAPZONE_BOMBTARGET  

    * CS_MAPZONE_HOSTAGE_RESCUE  

    * CS_MAPZONE_ESCAPE  

    * CS_MAPZONE_VIP_SAFETY  

  
  
**Тип функции:**  
Native  
  
**Пример:**  
--  
  
**Описание:**  
--
