# Урок 27. Enum Struct в Amxx и их практическое применение на основе "Shop Menu"
[Уроки по скриптингу для начинающих](http://amxxmodx.ru/lessons-on-pawn/)
Здравствуйте, я увидел несколько реализаций Shop магазинов, и решил(тоже) поделиться своим подходом к этой задачи. ![laughing](http://amxxmodx.ru/engine/data/emoticons/laughing.gif)   
  
**enum** — Перечисления. В основном используют в качестве "структуризации" данных.  
Они позволяют:  

    * создать блок данных и установить разные значения в него.  

    * создавать свои константы с автоматическим инкрементом.  

    * создавать свои значения для переменных.  

  
например:  
Довольно все знают **boo l** значения...  
```
  
enum bool {  
    false = 0,  
    true  
}  

```
  
Более подробное объяснение можно найти на [оленях](http://amxxmodx.ru/engine/go.php?url=aHR0cHM6Ly9mb3J1bXMuYWxsaWVkbW9kcy5uZXQvc2hvd3RocmVhZC5waHA%2FdD0xNDAxMDM%3D)  
  

    * В самом низу темы будут приложены Исходники, которые мы здесь рассмотрим.  

  
  
На данный момент мы рассмотрим "Блок Данных".  
_блок данных_ — в других языках семейства Си, С++ это структура данных(struct).  
**Структура** — некое объединение различных переменных, которых связывает что-то общее. Например:  
```
  
enum _:Игрок {  
    Имя[32],  
    Кол-во Жизней,  
    Кол-во Брони  
// этот список можно увеличивать и увеличивать, но мы остановимся на этом.  
}  

```
  
у нас теперь есть Общее понятие о Игроке мы его можем представить как Объект. Этот Объект можно использовать как обычную переменную, создать из неё массив т.д.  
  
  
Вот ещё один "маленький" пример структуры:  
Мы же все люди, верно?(знаю, есть коты которые сидят пока хозяев нет)  
представим структуру "Человек".  
```
  
enum _:Человек {  
    Инициалы,  
    возраст,  
    Пол,  
    Цвет Кожи,  
    // и другие... дальше углубляться не буду, а то пойдёт наследование, полиморфизм...  
    // это уже ближе к C++  :D  
}  

```
  
  
  
  
И так. Давайте, перейдём к примерам.  

    * _пример_ **№1** (Примеры сделаны лишь для понимание работы с enum массивами, к примерам не будут прилагаться исходные коды, потому что написаны от руки в теме)
  
```
  
enum _:Test_A {  
    A_one,  
    A_two[32]  
}  
new Ab[Test_A];// так мы создали нашу "структуру"  
// Использование:  
public plugin_init() {  
    // ....  
    Ab[A_One] = 12;  
    if(Ab[i][A_One] == 12) Ab[A_two] = "amxxmodx.ru";  
// Этот код написан лишь для примера.  
}  

```
  

    * _пример_ **№2** (создадим Массив на 100 элементов)
  
```
  
enum _:Test_A {  
    A_one,  
    A_two[32]  
}  
new Ab[100][Test_A];// так мы создали фиксированный массив наших "структур"  
// Использование:  
public plugin_init() {  
    // ....  
    for(new i = 0; i < 100; i++) {  
        Ab[i][A_One] = 12;  
        if(Ab[i][A_One] == 12) Ab[i][A_two] = "amxxmodx.ru";  
// Этот код написан лишь для примера.  
    }  
}  

```
  

    * _пример_ **№3** (Будем Использовать Array)
  
```
  
enum _:Test_A {  
    A_one,  
    A_two[32]  
}  
new Array:Ab;  
// Использование:  
public plugin_init() {  
    // ....  
    Ab = ArrayCreate(Test_A);// указываем Enum который будем хранить в каждой ячейке списка  
    for(new i = 0; i < 100; i++) {  
    new tmp[Test_A];  
    tmp[A_One] = 12;  
    tmp[A_two] = "amxxmodx.ru";  
    ArrayPushArray(Ab, tmp);// добавляем tmp к нашему массиву  
  
    // Получаем элемент  
        new tmp_get[Test_A];  
    ArrayGetArray(Ab, i, tmp_get);  
    tmp_get[A_One] = 13;  
    }  
}  

```
  
  
  
Как и сказано в теме мы будем писать Shop Menu.  
Мы напишем обычный Shop Menu с некоторыми уточнениями:  

    * При регистрации Item мы будем указывать имя функции _CallBack_.  
эта функция как раз и будет нашим обработчиком на выбор Item в меню, и функция будет должна вернуть какое-то значение Главному плагину для дальнейшей обработки.  
  

    * Меню не будет пересоздаватся для каждого отдельно(ну поверьте, это тупо постоянно листать циклом создавая одну и туже менюху ![wassat](http://amxxmodx.ru/engine/data/emoticons/wassat.gif) )  
  

    * Меню будет закрываться когда игрок Умер, или же кончился раунд (когда вы будете допиливать систему, или меня заставите, на разбитие команды, то это вам понадобится что бы **TR** не мог купить **CT** вещи или наоборот)  
  

    * Ну, последним моментом это будет Наиболее Оптимизация кода(если это потребуется)  
Если я не смогу проделать Оптимизацию в коде по причине что я не знаю, или ещё что-то... Я с удовольствием выслушаю, и приму меры(если потребуются).  

  
  
Начнём мы с _*.inc_ файла. А назовём мы его : _my_shop_menu.inc_ (Вы можете назвать по своему)  
```
  
#include <cstrike>  
  
#define SIZE 32  
// Для начала подумаем что нужно для того что бы добавить новый предмет?  
enum _:MyMenuItem {  
    ItemName[SIZE],// имя предмета  
    ItemCost,// стоимость  
    ItemForwardHandle// индекс форварда.  
}// Этот список можно увеличивать и увеличивать, но для примера этого хватит с головой  
  
  
// А теперь подумаем, если вдруг, Sub плагин которому отправили что пользователь выбрал  
//этот Item. Он не хочет отрабатывать это, нам главному плагину это нужно как то знать...  
//Вернуть какое-то значение от форварда (например, нет денег для покупки предмета).  
enum _:ShopReturns {  
    Shop_OK = 1,// операция прошла успешно  
    ShopNotEnoughMoney = 2,// нет денег на предмет  
    Shop_False = 0  
}  
  
/* натив регистрации */  
native shop_register_item(item_name[SIZE], item_cost = 0, callback_function[SIZE] = "shop_buy_item");  
// про значения по default, думаю, будет понятно, что если не указывать значение (указав знак  _ ) то параметр будет присвоен тому что указано в прототипу функции.  
  
/* можно ли купить предмет */  
stock check_try_buy(id, iCost) {  
    new new_money = cs_get_user_money(id) - iCost;  
    if(new_money < 0) return false;  
    cs_set_user_money(id, new_money, 1);  
    return true;  
}  

```
  
  
У нас есть заготовка, теперь мы можем приступить к Главному Плагину.  
  
```
  
#include <amxmodx>  
#include <cstrike>  
#include "my_shop_menu.inc"  
  
new Array:ShopItems;  
new HandleMenu = -1;  
  
// звук который будет воспроизводится когда пользователь купил предмет  
new const SoundBuy[] = "items/9mmclip1.wav";  
public plugin_precache() precache_sound(SoundBuy);  
  
public plugin_init() {  
    register_plugin("[amxxmodx.ru] Shop Menu", "1.2e", "Gavrilyuc");  
    register_clcmd("shop", "ShowShopMenu")  
    register_clcmd("say shop", "ShowShopMenu")  
    register_clcmd("say_team shop", "ShowShopMenu")  
    register_event("HLTV", "HLTV_New_Round", "a", "1=0", "2=0");  
    register_event("DeathMsg", "PlayerDeath", "a");  
}  
  
public ShowShopMenu(id) {  
    if(is_user_alive(id)) menu_display(id, HandleMenu);  
}  
  
/* начало раунда */  
public HLTV_New_Round() {  
    new iPlayers[32], z;  
    get_players(iPlayers, z, "a");  
    for(new i; i < z; i++) CheckMenuClose(iPlayers[i]);  
}  
/* Смерть игрока */  
public PlayerDeath() {  
    static id; id = read_data(2);  
    if(!is_user_connected(id)) return;  
    CheckMenuClose(id);  
}  
  
/* проверяем закрытое ли меню? если нет то закрывает */  
CheckMenuClose(id) {  
    new iCrap, iMenuId;  
    player_menu_info(id, iCrap, iMenuId)  
    if(iMenuId > -1 && (iMenuId == HandleMenu)) menu_cancel(id);  
}  
  
public plugin_natives() {  
    register_native("shop_register_item", "RegisterItem");  
}  
  
public RegisterItem(iPlugin) {  
    new mDatas[MyMenuItem], szCallBack[SIZE];  
    get_string(3, szCallBack, charsmax(szCallBack));  
    mDatas[ItemForwardHandle] = CreateOneForward(iPlugin, szCallBack, FP_CELL);  
    if((mDatas[ItemCost] = get_param(2)) > 0) {  
        get_string(1, mDatas[ItemName], charsmax(mDatas[ItemName]))  
        AddItemToMenu(mDatas);  
    }  
    return mDatas[ItemForwardHandle];  
}  
  
/* добавить в Shop Menu */  
AddItemToMenu(mDatas[MyMenuItem]) {  
    if(ShopItems == Invalid_Array) ShopItems = ArrayCreate(MyMenuItem);  
    if(HandleMenu == -1) {  
        HandleMenu = menu_create("\r[amxxmodx.ru] Shop Menu", "ShopMenu_Handler");  
        menu_setprop(HandleMenu, MPROP_NUMBER_COLOR, "\y");  
    }  
    ArrayPushArray(ShopItems, mDatas);  
    new szItemInformation[SIZE + SIZE];  
    formatex(szItemInformation, charsmax(szItemInformation), "\w%s\R\y$%d", mDatas[ItemName], mDatas[ItemCost]);  
    menu_additem(HandleMenu, szItemInformation);  
}  
  
/* Handler CallBack главного меню. */  
public ShopMenu_Handler(id, menu, item) {  
    if(item > MENU_MORE && is_user_alive(id)) {  
        new mDatas[MyMenuItem];  
        ArrayGetArray(Array:ShopItems, item, mDatas);  
        GetReturnForward(mDatas, id);  
    }  
}  
  
/* Обработчик результатов от Sub плагинов */  
GetReturnForward(mDatas[MyMenuItem], id) {  
    new returned;  
    ExecuteForward(mDatas[ItemForwardHandle], returned, id);  
    switch(returned) {  
        case Shop_OK: {  
            emit_sound(id, CHAN_ITEM, SoundBuy, VOL_NORM, ATTN_NORM, 0, PITCH_NORM);  
            return 1;  
        }  
        case ShopNotEnoughMoney: {  
            client_print(id, print_center, "НЕТ ДЕНЕГ!");  
        }  
    }  
    return 0;  
}  

```
  
  
и Так давайте рассмотрим этот код с более логической цепочки.  
Мы Создали   
```
 new Array:ShopItems; 
```
  
это и будет нашем _хранилищем_ всех предметов в магазине.  
  
Теперь давайте разберём:  
```
  
public plugin_natives() {  
    register_native("shop_register_item", "RegisterItem");  
}  
  
public RegisterItem(iPlugin) {  
    new mDatas[MyMenuItem], szCallBack[SIZE];  
    get_string(3, szCallBack, charsmax(szCallBack));  
    mDatas[ItemForwardHandle] = CreateOneForward(iPlugin, szCallBack, FP_CELL);  
    if((mDatas[ItemCost] = get_param(2)) > 0) {  
        get_string(1, mDatas[ItemName], charsmax(mDatas[ItemName]))  
        AddItemToMenu(mDatas);  
    }  
    return mDatas[ItemForwardHandle];  
}  

```
  
да, тут то мы и делаем _CallBack_ функцию в другой плагин (это Образно говоря, на самом деле просто создаём форвард).  
  
Теперь давайте рассмотрим функцию :  
```
  
/* добавить в Shop Menu */  
AddItemToMenu(mDatas[MyMenuItem]) {  
    if(ShopItems == Invalid_Array) ShopItems = ArrayCreate(MyMenuItem);  
    if(HandleMenu == -1) {  
        HandleMenu = menu_create("\r[amxxmodx.ru] Shop Menu", "ShopMenu_Handler");  
        menu_setprop(HandleMenu, MPROP_NUMBER_COLOR, "\y");  
    }  
    ArrayPushArray(ShopItems, mDatas);  
    new szItemInformation[SIZE + SIZE];  
    formatex(szItemInformation, charsmax(szItemInformation), "\w%s\R\y$%d", mDatas[ItemName], mDatas[ItemCost]);  
    menu_additem(HandleMenu, szItemInformation);  
}  

```
  
Когда приходит событие на добавление элемента в меню мы проверяем:  

    1. существует ли список предметов? если нет то создаём список.  

    2. существует ли меню? если нет создаём.  

    3. добавляем в Массив, предмет который пришел.  

    4. Добавляем пункт в меню.  

  
  
Теперь Обработчик Меню:  
```
  
/* Handler CallBack главного меню. */  
public ShopMenu_Handler(id, menu, item) {  
    if(item > MENU_MORE && is_user_alive(id)) {  
        new mDatas[MyMenuItem];  
        ArrayGetArray(Array:ShopItems, item, mDatas);  
        GetReturnForward(mDatas, id);  
    }  
}  

```
  
возможно, не заметили вы. Но я использую ArrayGetArray(...); что же это за функция?  
  
Могу лишь сказать что она относится к [Cell Array](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L290aGVyLzU2OC1penVjaGFlbS1jZWxsYXJyYXktdm1lc3RlLmh0bWw%3D)  
ну, так как про неё там не описано, можно гуглануть и найти на   
[amx-x.ru](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteC14LnJ1L3ZpZXd0b3BpYy5waHA%2FZj05JmFtcDt0PTI3NjQ%3D) там есть описание для нашей и для других функций такого рода.  
  
"GetReturnForward" это уже более конкретнее:  
```
  
/* Обработчик результатов от Sub плагинов */  
GetReturnForward(mDatas[MyMenuItem], id) {  
    new returned;  
    ExecuteForward(mDatas[ItemForwardHandle], returned, id);  
    switch(returned) {  
        case Shop_OK: {  
            emit_sound(id, CHAN_ITEM, SoundBuy, VOL_NORM, ATTN_NORM, 0, PITCH_NORM);  
            return 1;  
        }  
        case ShopNotEnoughMoney: {  
            client_print(id, print_center, "НЕТ ДЕНЕГ!");  
        }  
    }  
    return 0;  
}  

```
  
вызываем форвард, получая от него результат.  
Потом проверяем что вернули наши подписчики и обрабатываем.  
  
Ну что ж... Весь Фундамент готов, теперь нужно писать(искать) клёвые предметы для магазина...  

    * Для примера я напишу Sub плагин
  
```
  
#include <amxmodx>  
#include <fun>  
#include "my_shop_menu.inc"  
  
#define COST_HP 50  
#define COST_GRENADE 100  
  
public plugin_init() {  
    register_plugin("[amxxmodx.ru] Items for Shop Menu", "1.0", "Gavrilyuc");  
    shop_register_item("Хочу +100 хп", COST_HP, "callback_function");  
    shop_register_item("Хочу Гранату", COST_GRENADE, "callback_function_1");  
}  
  
public callback_function(id) {  
    if(!is_user_alive(id)) return Shop_False;  
    if(check_try_buy(id, 50)) {  
        set_user_health(id, get_user_health(id) + 100);  
        return Shop_OK;  
    }  
    return ShopNotEnoughMoney;  
}  
  
public callback_function_1(id) {  
    if(!is_user_alive(id)) return Shop_False;  
    if(check_try_buy(id, COST_GRENADE)) {  
        give_item(id,"weapon_hegrenade");  
        return Shop_OK;  
    }  
    return ShopNotEnoughMoney;  
}  

```
  
В одном плагине сразу два предмета.  
Что бы посмотреть в действии, хватит лишь залить два плагина на сервер и вызвать "say shop"  
  
  
  
  
Как я и Обещал: Вы не можете скачивать файлы с нашего сервера  
  
Если появятся вопросы по теме, по возможности отвечу.  
Если нашли опечатку, ошибку в плагине, пишем, я исправляю.
