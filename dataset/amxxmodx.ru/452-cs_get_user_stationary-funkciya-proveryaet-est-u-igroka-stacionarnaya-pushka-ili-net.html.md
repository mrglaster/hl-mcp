# cs_get_user_stationary Функция проверяет есть у игрока стационарная пушка или нет.
[CStrike](http://amxxmodx.ru/cstrike/)
Инфо из **cstrike.inc:**  
```
/* Returns 1 if user is using a stationary gun, else 0.  
 */  
native cs_get_user_stationary(index);  

```
  
  
**Синтаксис:**  

cs_get_user_stationary(index)
  

    * **index** - Индекс игрока  

  
  
**Тип функции:**  
Native  
  
**Пример:**  

Заходим на карту cs_rats2 (или другую, с прикрученным оружием). Нажимаем Е у оружия на кораблике в ванной, и видим в чате 1 вместо 0.

```
#include <amxmodx>
#include <cstrike>
 
public client_PreThink(id)
{
    client_print(id, print_chat, "%i", cs_get_user_stationary(id))
}
```
