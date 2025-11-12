# client_damage Функция вызывается когда один игрок наносит урон другому
[The CSX Module](http://amxxmodx.ru/csx/) [csx.inc](http://amxxmodx.ru/csx/csxinc/)
Функция **client_damage** вызывается каждый раз когда игрок наносит урон другому игроку.  
То есть если игрок пострадает от падения, то функция вызываться не будет. Но я бы рекомендовал использовать модуль [**Ham Sandwich**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2hhbXNhbmR3aWNoLw%3D%3D), для отлова и работы с данным событием.  
  
Инфо из **csx.inc:**  
```
/* Function is called after player to player attacks ,  
* if players were damaged by teammate TA is set to 1 */  
forward client_damage(attacker, victim, damage, wpnindex, hitplace, TA);
```
  
  
**Синтаксис:**  
```
client_damage(attacker, victim, damage, wpnindex, hitplace, TA)
```
  

    * **attacker** - id Атакующего   

    * **victim** - id Жертвы  

    * **damage** - Нанесенный урон  

    * **hitplace** - Место попадания  

    * **TA** - Если урон получен от игрока своей команды, то будет 1  

  
  
**Тип функции:**  
Forward  
  
**Пример:**  
```
#include <amxmodx>  
#include <csx>  
  
#define PLUGIN "[csx.inc] client_damage"  
#define VERSION "1.0"  
#define AUTHOR "Admin"  
  
// максимальная длина имени  
const MAX_NAME_LEN  = 32;  
  
// заменяем ничего не говорящую цифру на константу,  
// ALL - переводится как все или всем   
const ALL = 0;   
  
public plugin_init()  
{  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
}  
  
public client_damage(attacker, victim, damage, wpnindex, hitplace, TA)  
{  
    new attacker_name[MAX_NAME_LEN], victim_name[MAX_NAME_LEN];  
    get_user_name(attacker, attacker_name, charsmax(attacker_name));  
    get_user_name(victim, victim_name, charsmax(victim_name));  
    
    client_print(ALL, print_chat, "[%s][%s][%d][%d][%d]", attacker_name, victim_name, damage, wpnindex, hitplace, TA);  
}
```
  
  
**Описание:**  
Не вижу смысла детально описывать функцию, которой сегодня уже ни кто не пользуется.  
Лучше разу же идите изучать модуль **hamsandwich** ;)
