# register_menu Функция ярлык для функции register_menucmd и register_menuid.
[Ядро AMXx](http://amxxmodx.ru/core/) [amxmodx.inc](http://amxxmodx.ru/core/amxmodxinc/) [Старое меню](http://amxxmodx.ru/core/amxmodxinc/oldmenu/)
Лично мне не очень нравиться работать с функциями register_menucmd и register_menuid.  
И на мое счастье есть сток функция **register_menu** совмещающая эти две функции в одной, да и по названию более логична.  
  
Инфо из **amxmisc.inc:**  
```
stock register_menu(const title[],keys,const function[],outside=0)  
{  
    register_menucmd(register_menuid(title,outside),keys,function);  
}
```
  
  
**Синтаксис:**  

register_menu(const title[],keys,const function[],outside=0)
  

    * **const title[]** - Идентификатор меню  

    * **keys** - поразрядное число всех пунктов меню. Должно соответствовать числу пунктов меню.  

    * **const function[]** - Вызываемая функция при выборе элемента меню  

    * **outside=0** - если 1 то меню будет доступно другим плагинам.  

  
  
**Тип функции:**  
stock  
  
**Пример:**  
```
#include <amxmodx>  
#include <amxmisc>  
  
#define PLUGIN "[amxmisc.inc] old menu register_menu"  
#define VERSION "1.0"  
#define AUTHOR "author"  
#define Menu_Keys (1<<0)|(1<<1)|(1<<2)|(1<<3)|(1<<4)|(1<<5)|(1<<6)|(1<<7)|(1<<8)|(1<<9)  
  
new MenuPos  
new MenuPlayers[32]  
  
  
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
      
    //было  
    new menu_id = register_menuid("KICK_PLAYER")  
    register_menucmd(menu_id, Menu_Keys, "Pressed")  
      
    //стало  
    register_menu("KICK_PLAYER",Menu_Keys,"Pressed",0)  
  
}
```
  
  
**Описание:**  
В данном примере явно видно преимущество использования данной функции.  
Удобство и красота кода :)
