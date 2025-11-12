# client_death Функция вызывается когда игрок умирает
[The CSX Module](http://amxxmodx.ru/csx/) [csx.inc](http://amxxmodx.ru/csx/csxinc/)
Функция **client_death** вызывается когда игрок умирает. С помощью данной функции можно узнать убийцу игрока, саму жертву и ещё немного. Подробнее в полной новости.  
  
Инфо из **csx.inc** :  
```
/* Function is called after player death ,  
* if player was killed by teammate TK is set to 1 */  
forward client_death(killer,victim,wpnindex,hitplace,TK);
```
  
  
**Синтаксис:**  

client_death ( killer, victim, wpnindex, hitplace, TK )
  
  

    * **killer** - id убийцы игрока  

    * **victim** - id жертвы  

    * **wpnindex** - индекс оружия убийцы (точно не знаю, если ошибка - пишите в комментарии)  

    * **hitplace** - место происшествия  

    * **TK** - если урон получен от игрока своей команды, то будет 1  

  
  
**Тип функции:**  
Forward  
  
**Пример:**  
```
#include <amxmodx>  
#include <csx>  
  
public plugin_init()  
{  
  register_plugin("Kills mini info", "1.0", "Explain")  
}  
  
public client_death(killer, victim)  
{  
  new Killer_Nick[32]  
  new Victim_Nick[32]  
  get_user_name(killer, Killer_Nick, 32)  
  get_user_name(victim, Victim_Nick, 32)  
  client_print(0, print_chat, "%s was killed by %s.", Victim_Nick, Killer_Nick)  
}
```

