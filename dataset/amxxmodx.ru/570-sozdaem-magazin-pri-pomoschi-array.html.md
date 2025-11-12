# Создаем магазин при помощи Array
[Присланное](http://amxxmodx.ru/other/)
Для начала нам нужно внимательно прочитать [этот](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L290aGVyLzU2OC1penVjaGFlbS1jZWxsYXJyYXktdm1lc3RlLmh0bWw%3D) урок про Array  
Знать как использовать [ExecuteForward](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2NvcmUvYW14bW9keGluYy8zMjItZXhlY3V0ZWZvcndhcmQtZnVua2NpeWEtdnl6eXZhZXQtemFyZWdpc3RyaXJvdmFubm9lLXNvYnl0aWUtZm9yd2FyZC1mdW5rY2l5dS5odG1s) и [CreateMultiForward](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2NvcmUvYW14bW9keGluYy8zMjEtY3JlYXRlbXVsdGlmb3J3YXJkLWZ1bmtjaXlhLXNvemRhZXQtbXVsdGktcGxhZ2luLWZvcnZhcmQuaHRtbA%3D%3D)  
  
```
  
  
#include <amxmodx>  
#include <cstrike> // будем использовать валюту КС  
  
new Array:ItemName // Будет хранить наши названия предметов  
new Array:ItemCost // Будет хранить нашу стоимость предметов  
  
new result, g_item_selected // сокращенное имя нашего CreateMultiForward  
  
public plugin_init()  
{  
    register_plugin("Shop Array", "1.0", "Nesquik for http://amxxmodx.ru")  
    register_clcmd("say /shop", "open_shop") // Вызов нашего меню при помощи команды в чате /shop  
    g_item_selected = CreateMultiForward("ItemSelected", ET_CONTINUE, FP_CELL, FP_CELL) // наш форвард который вызывается когда выбирается предмет   
}  
  
public plugin_precache()  
{  
    ItemName = ArrayCreate(32, 1) // Наше имя предмета  
    ItemCost = ArrayCreate(1, 1) // Наша стоимость предмета  
}  
  
public open_shop(id)  
{  
    new name[32] // массив для записи имени нашего предмета  
    new size = ArraySize(ItemName) // Получаем сколько всего зарегистрировано предметов   
    if(!size) // нужно проверить есть ли предметы в меню , если нет выводим следующее  
    {  
        client_print(id, print_chat, "В магазине нет предметов")   
        return PLUGIN_HANDLED  
    }  
    new menu = menu_create("Магазин сервера", "menu_func")  
    new cost // наша стоимость предмета   
    new FormatItem[64] // будет использовано для записи информации о предмете   
    for(new i = 0; i < size; i++) // Получаем все предметы которые зарегистрированы через RegisterItem  
    {  
        ArrayGetString(ItemName, i, name, 31)  
        cost = ArrayGetCell(ItemCost, i)  
        if(cs_get_user_money(id) >= cost) // Создаем условие если деньги игрока больше либо равны стоимости наших предметов то выводим их в меню  
        {  
            formatex(FormatItem, 63, "%s \y%d", name, cost)   
            menu_additem(menu, FormatItem)  
        }  
    }  
    menu_display(id, menu, 0) // Выводим созданное меню игроку   
    return PLUGIN_HANDLED  
}  
  
public menu_func(id, menu, item)  
{  
    ExecuteForward(g_item_selected, result, id, item) // Сообщаем другому плагину что игрок id выбрал предмет item  
    return PLUGIN_HANDLED  
}  
  
public plugin_natives()  
{  
    register_native("RegisterItem", "NativeRegisterItem", 1)  
}  
  
public NativeRegisterItem(const Name[], cost) // Name[] = имя предмета , cost = стоимость предмета   
{  
    param_convert(1) // Конвертируем наше название предмета  
   
    ArrayPushString(ItemName, Name) // Устанавливаем наше имя созданному нами выше Array'ю  
    ArrayPushCell(ItemCost, cost) // Устанавливаем стоимость для нашего предмета  
  
    return ArraySize(ItemName) - 1 // Возвращаем последний зарегистрированный предмет  
}
```
  
  
Ну какой же магазин без предметов , Создадим их   
Но как это сделать :?  
Нам сначала нужно создать файл с расширение .inc (к примеру shop.inc)  
Записать туда нам нужно всего две строки   
Это наш **RegisterItem**  
native RegisterItem(const Name[], cost)  
и наш форвард **ItemSelected**  
forward ItemSelected(id, item) // Ид игрока который выбрал предмет , item предмет который выбрал игрок  
  
В конечном итоге нам инклюд shop.inc должен выглядеть так   
```
native RegisterItem(const Name[], cost)  
forward ItemSelected(id, item)
```
  
  
Создание предметов для нашего магазина   
пример :  
```
#include <amxmodx>  
#include <shop> // Созданный нами инклюд  
#include <fun>  
  
new health // Сокращенное имя нашего предмета   
  
public plugin_init()  
{  
 health = RegisterItem("Здоровье", 5000) // Название нашего предмета Здоровье , его стоимость 5000 , Внимание предмет будет показываться в том случае если у вас (игрока) денег больше чем 5000 ну или равно :)  
}  
  
public ItemSelected(id, item)  
{  
 if(item == health) // Проверяем выбранный игроком предмет , Если это наш созданный предмет то выполняем следующее  
 {  
  set_user_health(id, 150) // Устанавливаем игроку 150 здоровья   
 }  
}
```
  
  
Ну вот и все компилируем наш плагин устанавливаем на сервер   
Перезагружаем сервер и вызываем наш магазин командой **say /shop**  
Все магазин готов   
Примечание :  
Если хотите чтобы один плагин создавал несколько предметов нужно создать его через armor = RegisterItem("Броня", 1500) и создать условие в ItemSelected следующее   
Вместо ```
 if(item == health)  
 {  
  set_user_health(id, 150)  
 }  

```
Сделать так :  
```
  
if(item == health)  
 {  
  set_user_health(id, 150)  
 }else if(item == armor)  
 {  
  set_user_armor(id, 150)  
 }
```

