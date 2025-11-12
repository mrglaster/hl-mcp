# GetHamReturnStatus Функция получает статус возврата исполняемого форварда.
[Ham Sandwich](http://amxxmodx.ru/hamsandwich/) [hamsandwich.inc](http://amxxmodx.ru/hamsandwich/hamsandwichinc/)
Очень редко встречающаяся функция, если точнее всего в одном плагине нашел пример и долго не мог смоделировать ее работу, но в итоге получилось и ее смысл стал понятен мне, теперь делюсь с вами. Представьте себе что у вас на сервере установлено несколько плагинов которые работают с одним и тем же событием, ну скажем получение урона:  
  
**Первый плагин:**  
Блокирует урон от своих.  
  
**Второй плагин:**  
Показывает нанесенный урон.  
  
Если зайти на сервер где установлены такие плагины и выстрелить в своего, то будет показано сообщение что нанесен такой то урон, но фактически его нету.  
Так как блокировался урон с помощью **return HAM_SUPERCEDE** ( это не самый верный способ, просто как самый простой и наглядный пример). И сообщение в итоге будет не верным, что бы такого не было, с помощью функции **GetHamReturnStatus** можно проверить статус данного события и сделать соответствующие корректировки.  
  
Инфо из **hamsandwich.inc:**  
```
/**  
 * Gets the return status of the current hook.  
 * This is useful to determine what return natives to use.  
 *  
 * @return                The current status of the hook (such as HAM_SUPERCEDE).  
 */  
native GetHamReturnStatus();
```
  
  
**Синтаксис:**  

GetHamReturnStatus();
  
Функция вернет статус форварда:  
```
#define HAM_IGNORED        1    /**< Calls target function, returns normal value */  
#define HAM_HANDLED        2    /**< Tells the module you did something, still calls target function and returns normal value */  
#define HAM_OVERRIDE    3    /**< Still calls the target function, but returns whatever is set with SetHamReturn*() */  
#define HAM_SUPERCEDE    4    /**< Block the target call, and use your return value (if applicable) (Set with SetHamReturn*()) */
```
  
  
**Тип функции:**  
Native  
  
**Пример:**  
**Плагин 1:**  
```
#include <amxmodx>  
#include <amxmisc>  
#include <hamsandwich>  
#include <fakemeta>  
  
#define PLUGIN "[http://amxxmodx.ru] GetHamReturnStatus 1"  
#define VERSION "1.0"  
#define AUTHOR "Admin"  
  
  
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
      
    RegisterHam(Ham_TakeDamage,"player","damager",0)  
  
}  
public damager(victim, inflicator, attacker, Float:damage){  
      
    new Vteam[32]  
    new Ateam[32]  
  
    get_user_team(victim,Vteam,31)  
    get_user_team(attacker,Ateam,31)  
      
    if(equali(Vteam,Ateam)){  
        return HAM_SUPERCEDE  
          
    }  
      
    return HAM_IGNORED  
}
```
  
  
**Плагин 2:**  
```
#include <amxmodx>  
#include <amxmisc>  
#include <hamsandwich>  
  
#define PLUGIN "[http://amxxmodx.ru] GetHamReturnStatus 2"  
#define VERSION "1.0"  
#define AUTHOR "Admin"  
  
  
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
      
    RegisterHam(Ham_TakeDamage,"player","damager",0)  
      
}  
public damager(victim, inflicator, attacker, Float:damage){  
      
    if(GetHamReturnStatus() != HAM_SUPERCEDE)  
        client_print(0,print_chat,"Damage: %.1f health:%d",damage,get_user_health(victim))  
      
}  

```
  
  
**Описание:**  
Необходимо установить оба плагина для наглядной работы.  
Включите **Friendly fire** ( если он у вас на сервере выключен) и попробуйте пострелять в своего и противника.  
Затем закоментируйте или удалите строчку:   
**if(GetHamReturnStatus() != HAM_SUPERCEDE)**  
И вновь атакуйте своих, и вы увидите что урон не наносится, но его количество пишется.  
  
Вот такая вот не хитрая, но в определенных моментах весьма полезная функция.
