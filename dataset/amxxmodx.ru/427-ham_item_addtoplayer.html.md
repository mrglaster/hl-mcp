# Ham_Item_AddToPlayer Вызывается при получении оружия игроком
[Ham Sandwich](http://amxxmodx.ru/hamsandwich/) [ham_const.inc](http://amxxmodx.ru/hamsandwich/ham_constinc/)
Данное событие вызывается в момент получения оружия (когда покупаете или подбираете его с земли). Используется во всех оружиях из зомби мода, можете сами посмотреть и немного разобраться. Я приведу небольшой пример по использованию данного события.  
  
Инфо из **ham_const.inc**  
  
```
/**  
* Description:        Adds the item to the player.  
* Forward params:    function(this, idPlayer);  
* Return type:        Integer (boolean).  
* Execute params:    ExecuteHam(Ham_Item_AddToPlayer, this, idPlayer);  
*/  
Ham_Item_AddToPlayer
```
  
  
Параметры:  

(weapon, id)
    * **weapon** - index оружия  

    * **id** - index игрока  

Функция возвращает 1 при успешной работе, иначе 0.  
  
**Пример:**  
  
```
#include <amxmodx>  
#include <fakemeta>  
#include <hamsandwich>  
  
public plugin_init()  
{  
    register_plugin("[http://amxxmodx.ru] Ham_Item_AddToPlayer", "1.0", "Awake")  
      
    // Регистрируем событие получения оружия m4a1  
    RegisterHam(Ham_Item_AddToPlayer, "weapon_m4a1", "fw_Weapon_AddToPlayer_Post", 1)  
}  
  
public fw_Weapon_AddToPlayer_Post(weapon, id)  
{  
    if (!is_user_connected(id) || !pev_valid(weapon))   
        return HAM_IGNORED  
          
    client_print(id, print_chat, "Event Ham_Item_AddToPlayer")   
      
    return HAM_IGNORED  
}
```
  
  
После получения оружия **m4a1** будет вызываться данное событие, можете сами поэкспериментировать.
