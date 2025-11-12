# Ham_Player_Jump
[Ham Sandwich](http://amxxmodx.ru/hamsandwich/) [ham_const.inc](http://amxxmodx.ru/hamsandwich/ham_constinc/)
Данная функция каждый кадр отслеживает момент прыжка, прошу заметить что бы данная функция срабатывала нужно именно нажать на кнопку прыжка, и потом каждый кадр пока вы будете подниматься в воздух и опускаться на землю будет вызываться эта функция  
  
Инфо из **ham_const.inc**  
  
```
/**  
 * Description:        Typically called every frame when a player has jump held.  
 * Forward params:    function(this)  
 * Return type:        None.  
 * Execute params:    ExecuteHam(Ham_Player_Jump, this);  
 */  
Ham_Player_Jump
```
  
  
Вызывается каждый кадр при "удачном" прыжке   
function(this) - index прыгуна  
Ничего не возвращает  
  
**Пример:**  
  
```
#include <amxmodx>  
#include <hamsandwich>  
  
public plugin_init()  
{  
    register_plugin("[HAM]Player Jump", "1.0", "VForVendetta")  
    RegisterHam(Ham_Player_Jump, "player", "Fw_PlayerJump")  
}  
  
public Fw_PlayerJump(id)  
{  
    console_print(id, "Вы находитесь в прыжке")  
}  

```

