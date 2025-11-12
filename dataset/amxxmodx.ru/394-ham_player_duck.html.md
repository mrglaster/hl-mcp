# Ham_Player_Duck
[Ham Sandwich](http://amxxmodx.ru/hamsandwich/) [ham_const.inc](http://amxxmodx.ru/hamsandwich/ham_constinc/)
В данной теме рассмотрим такую функцию из ham_const.inc как Ham_Player_Duck  
Этот момент вызывается покадрово когда человек сидит(DUCK)  
  
Инфо из **ham_const.inc**   
  
```
/**  
 * Description:        Typically called every frame when a player has duck held.  
 * Forward params:    function(this)  
 * Return type:        None.  
 * Execute params:    ExecuteHam(Ham_Player_Duck, this);  
 */  
Ham_Player_Duck
```
  
  
Вызывается каждый кадр когда человек сидит  
function(this) - index того кто сидит  
Функция ни чего не возвращает  
  
**Пример:**  
  
```
#include <amxmodx>  
#include <hamsandwich>  
  
public plugin_init()  
{  
    register_plugin("[HAM]Player Duck", "1.0", "VForVendetta")  
    RegisterHam(Ham_Player_Duck, "player", "Fw_PlayerDuck")  
}  
  
public Fw_PlayerDuck(id)  
{  
    console_print(id, "Вы сидите")  
}
```
  
  
Вот очень простой плагин для примера, данный плагин выводит надпись "Вы сидите" каждый кадр когда вы находитесь в положении сидя.  
  
Таки мне очень понадобится эта функция в одном из моих зомби классов, думаю и вам пригодится)
