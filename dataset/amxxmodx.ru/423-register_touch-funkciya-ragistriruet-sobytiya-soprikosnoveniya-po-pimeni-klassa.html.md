# register_touch Функция рагистрирует события соприкосновения по имени класса
[The Engine Module](http://amxxmodx.ru/engine/) [engine.inc](http://amxxmodx.ru/engine/engineinc/)
С помощью функции **register_touch** можно отлавливать различные соприкосновения в игре, например: игроков друг с другом или игрока и лежащего на земле оружия и другие объекты по имени их класса.  
  
Инфо из **engine.inc:**  
```
/* Registers a touch action to a function by classnames.  Use * to specify any classname. */  
native register_touch(const Touched[], const Toucher[], const function[]);
```
  
  
**Синтаксис:**  

register_touch(const Touched[], const Toucher[], const function[])
  

    * **const Touched[]** - Кто/что  

    * **const Toucher[]** - С чем соприкоснется  

    * **const function[]** - Какая функция будет вызываться  

  
  
**Тип функции:**  
Native  
  
**Пример:**  
```
#include <amxmodx>  
#include <amxmisc>  
#include <engine>  
  
#define PLUGIN "[http://amxxmodx.ru] register_touch"  
#define VERSION "1.0"  
#define AUTHOR "Admin"  
  
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
  
    /*  
    Регистрируем касание weaponbox (оружие лежащие на земле)  
    С любым другим классом * ( можно оставить только player  
    Тогда функция будет срабатывать только когда соприкоснется игрок  
    */  
    register_touch("weaponbox","*","fwd_touch")  
}  
public fwd_touch(w_box,other){  
      
    client_print(other,print_chat,"Touched")  
      
}
```
  
  
**Описание:**  
Зайдя на сервер, попробуйте выкинуть свое оружие.  
На это действие вы получите целый флуд в чат со словом Touched, так как функция **register_touch** будет выполняться до тех пор, пока соприкасаются два отлавливаемых класса, в данном случае weaponbox и любого другого.  
список всех классов можно найти [здесь](http://amxxmodx.ru/hamsandwich/43-the-ham-sandwich-module.html)  
  
**Мини задание для самоконтроля:**  
Попробуйте отловить соприкосновение любых двух игроков.  
Свои варианты прячьте под спойлер.
