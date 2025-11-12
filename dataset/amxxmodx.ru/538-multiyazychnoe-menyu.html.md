# Мультиязычное меню
[Присланное](http://amxxmodx.ru/other/)
Это урок о том как создать мультиязычное меню через функцию formatex  
```
#include <amxmodx>  
#inclued <amxmisc>  
  
#define PLUGIN "[http://amxmodx.ru] Menu lang"  
#define AUTHOR "Nesquik"  
#define VERSION "1.0"  
  
public plugin_init() // Нужно нам зарегистрировать команду для вызова меню  
{  
 register_plugin(PLUGIN,AUTHOR,VERSION)  
 reigster_clcmd("say /menu","menu") // Команда вызова нашего меню  
}  
  
public menu(id) //наше меню которое вызывается командой say /menu  
{  
 // Сначала создадим переменную для formatex  
 new szMenuMulti[64] //szMenuMulti это мы будем использовать для foramtex 64 - длина сообщение  
 foramtex(szMenuMulti,63,"%L",id,"TITLE_MENU") // Вот мы сформировали наш мультиланг  
 new menu = create_menu(szMenuMulti,"menu_handled") // Записали мултиланг в созданное нами меню, теперь перейдем к созданию нашим мультиязычных кнопок ))  
 formatex(szMenuMulti,63,"%L",id,"ITEM_MENU_1") // Сформировали нашу мультиязычную кнопку   
 menu_additem(szMenuMulti,"1",0) // Ну вот собственно и все наше меню приобрело мультиязычный вид ,далее можно сделать кнопки EXIT,BACK,EXIT тоже мультиязычными   
 formatex(szMenuMulti,63,"%L",id,"EXIT") // Вот наша кнопка EXIT приобрела мультиязычный вид впишем ее в menu_setprop  
 menu_setprop(menu,MPROP_EXIT,szMenuMulti) // menu_setprop - задает меню определенный функции такие как выход далее и назад ,  
 menu - это созданое нами меню ,MPROP_EXIT - функция задает меню кнопку выхода , szMenuMulti - это сформированный выше нами мультиланг ,так же можно сделать и с Далее и назад   
 menu_display(id,menu,0) // id - кому показываем меню ,menu - это что мы сделали выше ,0 - точно незнаю но вроде для флага  
}
```
  
  
ну вот собственно получилось у нас великолепное меню при помощи мультиланга
