# Ham_Item_Deploy - Вызывается, когда игрок меняет оружие.
[Присланное](http://amxxmodx.ru/other/)
Ham_Item_Deploy - Вызывается, когда игрок меняет оружие.  
  
Инофо из **ham_cons.inc** :  
```
    /**  
     * Description:        Deploys the entity (usually a weapon).  
     * Forward params:    function(this);  
     * Return type:        Integer (boolean).  
     * Execute params:    ExecuteHam(Ham_Item_Deploy, this);  
     */  
    Ham_Item_Deploy,
```
  
  
  
**Пример:**  
```
  
#include <AmxModx>  
#include <HamSandwich>  
  
public plugin_init() {  
RegisterHam(Ham_Item_Deploy, "weapon_knife", "Item_Deploy_Post", 1)  
}  
  
public Item_Deploy_Post(weapon)  
{  
new id = get_pdata_cbase(weapon, 41, 4) //Достаем индекс игрока  
  
client_print(id, print_chat, "Вы сменили оружие на нож") //Сообщение игроку  
  
return HAM_IGNORED //Прекращаем роботу форварда  
}  

```
  
  
Форвард удобный тем, что через него можно установить модель оружия игроку
