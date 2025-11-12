# Урок 11. Кнопочные константы (Amx Mod X) или как поймать нажатие кнопки.
[Уроки по скриптингу для начинающих](http://amxxmodx.ru/lessons-on-pawn/)
**Кнопочные константы** используются для того, чтобы отловить момент, когда игровой объект совершает какое то действие, такое как прыжок, атака или передвижение. Этот метод используется из-за того, что движок HL не может «отловить» команды которые имеют противоположные знаки, такие как +jump/-jump  
  
**Этот пример работать будет:**  
```
register_concmd("+explode","explode")
```
  
  
**А вот команда attack имеет _+/-_ состояние и работать не будет**.  
```
register_concmd("+attack","hook_attack")
```
  
  
Полный список всех констант:  
```
#define IN_ATTACK        (1<<0)  
#define IN_JUMP            (1<<1)  
#define IN_DUCK            (1<<2)  
#define IN_FORWARD        (1<<3)  
#define IN_BACK            (1<<4)  
#define IN_USE            (1<<5)  
#define IN_CANCEL         (1<<6)  
#define IN_LEFT            (1<<7)  
#define IN_RIGHT             (1<<8)  
#define IN_MOVELEFT        (1<<9)  
#define IN_MOVERIGHT        (1<<10)  
#define IN_ATTACK2        (1<<11)  
#define IN_RUN            (1<<12)  
#define IN_RELOAD        (1<<13)  
#define IN_ALT1            (1<<14)  
#define IN_SCORE             (1<<15)
```
  
  
Как же все таки поймать момент нажатия кнопки игроком?  
  
Вот рабочий вариант отлова момента когда игрок нажимает кнопку атаки:  
```
#include <amxmodx>   
#include <engine>   
  
public plugin_init(){   
    register_plugin("Attack Test","1.0","Hawk552")  
}   
  
public client_PreThink(id){   
    if(entity_get_int(id,EV_INT_button) & IN_ATTACK)   
    {   
        client_print(id,print_chat,"You in attack")  
    }   
}
```
  
Обращаю ваше внимание, что используется оператор & , основное отличие оператора && от & заключается в том, что оператор & проверяет, есть ли бит после оператора в предыдущем бите до него. То есть в данном случае идет проверка, есть ли нужная нам кнопка, среди множества нажатых одновременно других клавиш.  
  
Если вам необходимо заставить нажать игрока кнопку, можно воспользоваться данным методом:  
```
#include <amxmodx>   
#include <engine>   
  
public plugin_init() {   
    register_plugin("Attack Test","1.0","Hawk552")  
}   
  
public client_PreThink(id) {   
    entity_set_int(id,EV_INT_button,IN_ATTACK)  
} 
```
  
Приведенный код, будет зажимать за игрока кнопку атаки.  
(Для наглядности выберите нож)  
Обратите внимание на то, что эмулируется именно атака, а не нажатие кнопки мышки, так как ее забиндить можно куда угодно.  
  
Чтобы "поймать" нажатые кнопки игрока, а потом "выключить" какую либо кнопку, можно использовать следующий вариант:   
```
#include <amxmodx>   
#include <engine>   
  
public plugin_init(){   
    register_plugin("Attack Test","1.0","Hawk552")  
}   
  
public client_PreThink(id) {   
    entity_set_int(id,EV_INT_button,entity_get_int(id,EV_INT_button) & ~IN_ATTACK)  
}   

```
  
Если игрок **прыгает IN_JUMP** и **атакует IN_ATTACK** в один и тот же момент,то функция ```
entity_get_int(id,EV_INT_button)
```
будет возвращать значения IN_ATTACK и IN_JUMP. С помощью оператора **~** будет удаляться указанное значение бита, в нашем случае IN_ATTACK.  
Для наглядности выберите нож и зажмите кнопку атаки во время прыжка или других действий, "все будет хорошо", кроме прерывающейся атаки.  
  
Первоисточник: [Button_constants (AMX_Mod_X)](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL3dpa2kuYW14bW9keC5vcmcvaW5kZXgucGhwL0J1dHRvbl9jb25zdGFudHNfKEFNWF9Nb2RfWCk%3D)  
  
Маленький бонус от меня:  
Забавный момент:  
```
#include <amxmodx>   
#include <engine>   
  
public plugin_init()   
{   
    register_plugin("Mega AWP","1.0","Admin");   
}   
  
public client_PreThink(id)   
{   
    entity_set_int(id,EV_INT_button,IN_DUCK);   
    entity_set_int(id,EV_INT_button,entity_get_int(id,EV_INT_button) & ~IN_DUCK);   
} 
```
  
Если в таком варианте взять AWP( или другую пуху с оптическим прицелом), зажать кнопку альтернативной атаки ( мышь 2), то вы получите сверх скорострельную пуху с бесконечными патронами.  
  
Разумеется это баг, изночально задумывалось другое, когда я разбирался сам, с данным уроком.
