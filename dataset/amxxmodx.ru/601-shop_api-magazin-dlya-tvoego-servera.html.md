# shop_api Магазин для твоего сервера
[Присланное](http://amxxmodx.ru/other/)
**Автор** : Nesquik  
**Версия** : 1.0 специально для http://amxxmodx.ru/  
**О плагине** : Магазин имеющий свой внутренний API через который можно добавлять предметы  
  
[![shop_api Магазин для твоего сервера](http://amxxmodx.ru/uploads/posts/2014-06/thumbs/1402158941_cs_militia0001.jpg)](http://amxxmodx.ru/uploads/posts/2014-06/1402158941_cs_militia0001.jpg)  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
**Требования :**  
Модуль Amxx  
Модуль Cstrike  
  
**Содержание shop_api.inc**  
```
// Команда для которой будет предмет  
#define TEAM_ALL    0 // Для всех  
#define TEAM_T 1 // Только для Террористов  
#define TEAM_CT    2 // Только для ментов  
  
#define SHOP_ITEM_DISABLED 97 // Возвращаем в UserChooseItem что бы заблокировать выбор предмета  
  
// Вызывается когда игрок выбирает предмет   
// @param id     Индекс игрока  
// @param item Индекс предмета  
forward UserChooseItem(id, item)  
  
// Вызывается когда игрок открывает магазин  
forward UserOpenMenu(id)  
  
// Используется для того что бы игроку открыть меню на определенной странице  
// @param id   Индекс игрока  
// @param page    Страница  
native OpenShopMenu(const id, const page)  
  
// Регистрирует новый предмет для магазина  
// @param Name         Имя предмета  
// @param cost           Стоимость предмета  
// @param team          Для какой команды предмет  
// @return                  Возвращает ид данного предмета  
native RegisterItem(Name[], cost, team)  

```
  
  
**Основные квары:**  
**amxx_cvar_enable_round_shop = 0**  
Если квар равен нулю то в любом раунде можно открыть меню   
Если равен 3 то только после 3 раунда можно будет открывать меню  
  
**amxx_cvar_buy_max_items = 10**  
Сколько можно предметов купить за раунд  
  
**Исходный код:**  
```
#include <amxmodx>  
#include <cstrike>  
  
#define TEAM_ALL    0  
#define SHOP_ITEM_DISABLED    97  
  
enum _:EXEC_FORWARD  
{  
    ForwardItemChoose=0,  
    ForwardMenuOpen  
}  
  
new Array:ItemName, Array:ItemCost, Array:ItemTeam  
new pCvarRoundEnable, pCvarBuyMaxItems  
new RoundNumber, szResult  
new gForward[EXEC_FORWARD]  
new szBuyItems[33]  
  
new szButtonName[][] = {"MENU_EXIT", "MENU_NEXT", "MENU_BACK"}  
new szButtonIndex[] = {MPROP_EXITNAME, MPROP_NEXTNAME, MPROP_BACKNAME}  
  
public plugin_init()  
{  
    register_plugin("Shop Api for amxxmodx.ru", "1.0", "Nesquik")  
      
    register_clcmd("say /shop", "ShowShopMenu")  
    register_clcmd("say_team /shop", "ShowShopMenu")  
  
    pCvarRoundEnable = register_cvar("amxx_cvar_enable_round_shop", "0")  
    pCvarBuyMaxItems = register_cvar("amxx_cvar_buy_max_items", "10")  
      
    gForward[ForwardItemChoose] = CreateMultiForward("UserChooseItem", ET_CONTINUE, FP_CELL, FP_CELL)  
    gForward[ForwardMenuOpen] = CreateMultiForward("UserOpenMenu", ET_CONTINUE, FP_CELL)  
      
    register_event("HLTV", "EventHLTV", "a", "1=0", "2=0")  
    register_event("TextMsg", "EventTextMsg", "a", "2=#Game_Commencing", "2=#Game_will_restart_in")  
      
    register_dictionary("shop_api.txt")  
}  
  
public ShowShopMenu(id)  
    return ShopMenuSub(id, 0)  
  
public ShopMenuSub(id, page)  
{  
    new cvar[2]  
    cvar[0] = get_pcvar_num(pCvarRoundEnable)  
    cvar[1] = get_pcvar_num(pCvarBuyMaxItems)  
      
    if(cvar[0] && (cvar[0] > RoundNumber))  
    {  
        client_print(id, print_chat, "%L", LANG_PLAYER, "CANT_BUY_IN_ROUND", cvar[0])  
        return 0  
    }  
      
    if(cvar[1] && (szBuyItems[id] >= cvar[1]))  
    {  
        client_print(id, print_chat, "%L", LANG_PLAYER, "YOU_BUY_MAX_ITEMS_IN_ROUND", cvar[1])  
        return 0  
    }  
          
    new szMenu[96], szName[64], szHostName[64], szKey[3]  
    new szCreateMenuShop, szBackMenuShop, szCost, szTeam  
    new szSize = ArraySize(ItemName), szUserTeam = get_user_team(id), szMoney = cs_get_user_money(id)  
      
    get_cvar_string("hostname", szHostName, charsmax(szHostName))  
    ExecuteForward(gForward[ForwardMenuOpen], szResult, id)  
      
    format(szMenu, charsmax(szMenu), "%L", LANG_PLAYER, "SHOP_TITLE", szHostName)  
    szCreateMenuShop = menu_create(szMenu, "MenuFuncShop")  
    szBackMenuShop = menu_makecallback("MenuBackShop")  
      
    for(new i = 0; i < szSize; i++)  
    {  
        num_to_str(i, szKey, charsmax(szKey))  
      
        ArrayGetString(ItemName, i, szName, charsmax(szName))  
        szCost = ArrayGetCell(ItemCost, i)  
        szTeam = ArrayGetCell(ItemTeam, i)  
          
        if(szTeam == szUserTeam || szTeam == TEAM_ALL)  
        {  
            if(szMoney >= szCost)  
                formatex(szMenu, charsmax(szMenu), "%L", LANG_PLAYER, "INFO_ITEM", szName, szCost)  
            else  
                formatex(szMenu, charsmax(szMenu), "%L", LANG_PLAYER, "NO_MONEY", szName, szCost - szMoney)  
        }  
          
        menu_additem(szCreateMenuShop, szMenu, szKey, 0, szBackMenuShop)  
    }  
      
    for(new i = 0; i < sizeof szButtonName; i++)  
    {  
        formatex(szMenu, charsmax(szMenu), "%L", LANG_PLAYER, szButtonName[i])  
        menu_setprop(szCreateMenuShop, szButtonIndex[i], szMenu)  
    }  
      
    if(szSize)  
        return menu_display(id, szCreateMenuShop, page)  
    else  
        client_print(id, print_chat, "%L", LANG_PLAYER, "NO_ITEM_IN_MENU")  
      
    return 0  
}  
  
public MenuFuncShop(id, szMenu, szItem)  
{  
    if(szItem == MENU_EXIT)  
        return menu_destroy(szMenu)  
      
    new szData[3]  
    new szDummy  
    new szCost, szMoney = cs_get_user_money(id)  
      
    menu_item_getinfo(szMenu, szItem, szDummy, szData, charsmax(szData), _, _, szDummy)  
    szItem = str_to_num(szData)  
      
    szCost = ArrayGetCell(ItemCost, szItem)  
    cs_set_user_money(id, szMoney - szCost, 1)  
      
    ExecuteForward(gForward[ForwardItemChoose], szResult, id, szItem)  
      
    if(szResult == SHOP_ITEM_DISABLED)  
        cs_set_user_money(id, szMoney, 1)  
      
    return 1  
}  
  
public MenuBackShop(id, szMenu, szItem)  
{  
    new szData[3]  
    new szDummy  
    new szMoney = cs_get_user_money(id)  
      
    menu_item_getinfo(szMenu, szItem, szDummy, szData, charsmax(szData), _, _, szDummy)  
    szItem = str_to_num(szData)  
      
    if(szMoney < ArrayGetCell(ItemCost, szItem))  
        return ITEM_DISABLED  
      
    return ITEM_ENABLED  
}  
  
public EventHLTV()  
{  
    arrayset(szBuyItems, 0, 33)  
    RoundNumber++  
}  
  
public EventTextMsg()  
{  
    arrayset(szBuyItems, 0, 33)  
    RoundNumber=0  
}  
  
public plugin_precache()  
{  
    ItemName = ArrayCreate(64, 1)  
    ItemCost = ArrayCreate(1, 1)  
    ItemTeam = ArrayCreate(1, 1)  
}  
  
public plugin_natives()  
{  
    register_native("RegisterItem", "NativeRegisterItem", 1)  
    register_native("OpenShopMenu", "NativeOpenShopMenu", 1)  
}  
  
public NativeRegisterItem(const Name[], const Cost, const Team)  
{  
    param_convert(1)  
      
    ArrayPushString(ItemName, Name)  
    ArrayPushCell(ItemCost, Cost)  
    ArrayPushCell(ItemTeam, Team)  
      
    return (ArraySize(ItemName) - 1)  
}  
  
public NativeOpenShopMenu(id, page)  
    return ShopMenuSub(id, page)
```
  
  
Магазин вызывается командой **say /shop**  
  
**Как добавить предмет:**  
```
#include <amxmodx>  
#include <shop_api> // Инклюд магазина  
#include <fun>  
  
new ItemId // Будет хранить ид нашего предмета  
  
public plugin_precache()  
 ItemId = RegisterItem("He граната", 500, TEAM_ALL) // Мы создаем предмет с именем He граната , стоимостью 500 $ , для всех команд  
  
public UserChooseItem(id, item)  
{  
    if(item == ItemId) // Проверяем ид выбранного предмета и нами созданного   
    {  
        if(!user_has_weapon(id, CSW_HEGRENADE)) // Если у игрока нет He гранаты  
            give_item(id, "weapon_hegrenade") // Выдаем He гранату  
        else  
            return SHOP_ITEM_DISABLED // Возвращаем деньги игроку если у него есть He граната  
    }  
      
    return 1  
}
```
  
  
Так же плагин полностью **мультиязычный**  
Вы не можете скачивать файлы с нашего сервера  
  
Если есть какие либо пожелания / критика   
Выслушаю и приму к сведению  
 _Новость отредактировал**Admin** - 23-10-2014, 00:23_
Причина: Плагин администрацией не проверялся.
