# get_weaponname Функция возвращает имя оружия по его индексу.
[Ядро AMXx](http://amxxmodx.ru/core/) [amxmodx.inc](http://amxxmodx.ru/core/amxmodxinc/)
Иногда требуется получить имя оружия, но известен только его индекс, в этом случае поможет функция **get_weaponname**.  
  
Инфо из **amxmodx.inc:**  
```
/* Returns weapon name. */  
native get_weaponname(id,weapon[],len);
```
  
  
**Синтаксис:**  

get_weaponname(id,weapon[],len)
  

    * **id** - Индекс оружия  

    * **weapon[]** - Массив для записи имени  

    * **len** - максимальная длинна массива  

  
  
**Тип функции:**  
Native  
  
**Пример:**  
```
#include <amxmodx>  
  
public plugin_init()  
{  
    register_event("CurWeapon", "event_curweapon", "be", "1=1")  
}  
public event_curweapon(id)  
{  
    static weapon_name[33]; get_weaponname(read_data(2), weapon_name,charsmax(weapon_name))  
    client_print(id, print_chat, "%s", weapon_name)  
}
```
  
  
**Описание:**  
При переключении оружия(изменении худа патронов перезарядка, высрел) в чат выводит его имя.  
_Новость отредактировал**Admin** - 18-02-2014, 22:20_
Причина: Добавлен пример от артист'а
