# EnableHamForward Функция возобновляет работу ham форварда.
[Ham Sandwich](http://amxxmodx.ru/hamsandwich/) [hamsandwich.inc](http://amxxmodx.ru/hamsandwich/hamsandwichinc/)
После того как с помощью функции **[DisableHamForward](http://amxxmodx.ru/hamsandwich/hamsandwichinc/296-disablehamforward-funkciya-prekraschaet-rabotu-zaregistrirovannogo-ham-forvarda.html)** была приостановлена работа форварда, не редко требуется вновь его запустить, делается это с помощью функции **EnableHamForward**  
  
Инфо из **hamsandwich.inc:**  
```
/**  
 * Starts a ham forward back up.  
 * Use the return value from RegisterHam as the parameter here!  
 *  
 * @param fwd            The forward to re-enable.  
 */  
native EnableHamForward(HamHook:fwd);
```
  
  
**Синтаксис:**  

EnableHamForward(HamHook:fwd)
  

    * **HamHook:fwd** - Идентификатор форварда (возвращаемое значение RegisterHam (при регистрации события))  

  
  
**Тип функции:**  
Native  
  
**Пример:**  
```
#include <amxmodx>  
#include <amxmisc>  
#include <hamsandwich>  
  
#define PLUGIN "[http://amxxmodx.ru] EnableHamForward"  
#define VERSION "1.0"  
#define AUTHOR "Admin"  
  
new HamHook:g_fwdTakeDamage  
  
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
      
    g_fwdTakeDamage = RegisterHam(Ham_TakeDamage,"player","damager",0)  
      
    register_clcmd("say /off","f_off")  
    register_clcmd("say /on","f_on")  
}  
public f_on(){  
    EnableHamForward(g_fwdTakeDamage)  
    client_print(0,print_chat,"Forward TakeDamege is enable")  
}  
public f_off(){  
    DisableHamForward(g_fwdTakeDamage)  
    client_print(0,print_chat,"Forward TakeDamege is desable")  
}  
public damager(victim, inflicator, attacker, Float:damage){  
    if(!is_user_connected(attacker))  
        return;  
      
    if(victim == attacker || !victim)  
        return;  
      
    client_print(0,print_chat,"Damage: %.1f health:%d",damage,get_user_health(victim))  
      
}
```
  
  
**Описание:**  
Прочитайте описание для функции **[DisableHamForward](http://amxxmodx.ru/hamsandwich/hamsandwichinc/296-disablehamforward-funkciya-prekraschaet-rabotu-zaregistrirovannogo-ham-forvarda.html)** и сразу же поймете что **EnableHamForward** полная противоположность ей, но принцип использования одинаков.
