# Ловим команду buy
[Присланное](http://amxxmodx.ru/other/)
Многие скорее всего думают 
Да что там прописал register_clcmd("buy", "buy_func") и все 
  
К сожалению нет   
Так как в кс появилось новое так называемое Графическое (или VGUI menu)  
Команду **buy** стало отловить еще сложнее   
Ну так приступим   
  
```
#include <amxmodx>  
  
public plugin_init()  
{  
 register_clcmd("buy", "buy_func") // регистрируем нашу команду которую будем ловить   
}  
  
public buy_func(id)  
{  
 set_task(1.0, "BuyFunc", id) // мы заменяем наше меню покупки на то меню которое хотим  
}  

```
  
  
Кажется вот и отловили, заменили   
К сожалению это не конец   
Нам же нужно отключить VGUI menu так как его посредством амхх не так просто заменить   
  
```
#include <amxmodx>  
#include <fun>  
  
public plugin_init()  
{  
 register_clcmd("buy", "buy_func") // регистрируем нашу команду которую будем ловить   
}  
  
public buy_func(id)  
{  
 set_task(1.0, "BuyFunc", id) // мы заменяем наше меню покупки на то меню которое хотим  
}  
  
public BuyFunc(id)  
{  
 new menu = menu_create("Магазин сервера", "menu_func_buy)  
 menu_additem(menu, " Купить пистолет")  
}  
  
public menu_func_buy(id, menu, item)  
{  
 switch(item)  
 {  
  case 0:  
  {  
    give_item(id, "weapon_deagle")  
  }  
 }  
}  
  
public client_connect(id)  
{  
 client_cmd(id,"setinfo _vgui_menus 0") // Отключаем VGUI menu   
}
```
  
  
Собственно все  
В конечном итоге плагин для отлова **buy**   
```
  
public client_connect(id)  
{  
 client_cmd(id,"setinfo _vgui_menus 0") // Отключаем VGUI menu   
}
```

