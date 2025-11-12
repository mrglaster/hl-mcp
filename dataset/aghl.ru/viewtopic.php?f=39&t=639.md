# Half-Life и Adrenaline Gamer форум


## [[TUT] User Icon Status - Иконка статуса](https://aghlru.ds-servers.com/forum/viewtopic.php?f=39&t=639)
Категории: [Туториал](https://aghlru.ds-servers.com/forum/search.php?keywords=%2B%D0%A2%D1%83%D1%82%D0%BE%D1%80%D0%B8%D0%B0%D0%BB&terms=all&fid\[\]=19&sc=1&sf=catonly&sr=topics)
Модератор: [KORD_12.7](https://aghlru.ds-servers.com/forum/memberlist.php?mode=viewprofile&u=67)
  
  
Иконка статуса - это HUD иконка, которая располагается на экране игрока и используется в определенных случаях для определения статуса игрока. В данной статье мы рассмотрим способ создания такой иконки. За данную иконку отвечает сообщение с названием **StatusIcon**. Показать можно любой спрайт, который объявлен у клиента в **sprites/hud.txt.** Одновременно можно отобразить четыре иконки.  
  
Структура данного сообщения:  
**Цитата:** _Status_ - _byte_ - Статус сообщения  
 _SpriteName_ - _string_ - Название спрайта  
 _ColorR_ - _byte_ - Цвет R (красный)  
_ColorG_ - _byte_ - Цвет G (зеленый)  
_ColorB_ - _byte_ - Цвет B (синий)   

Статус сообщения может быть следующим:  

  * 0 - спрятать иконку
  * 1 - показать иконку
  * 2 - обновить иконку

  
Если статус равен 0, то посылать цвет не нужно.  
  
Итак, начнем:  
1. Прежде всего нам необходимо создать глобальную переменную для хранения ID сообщения, которое отвечает за такого рода иконку:  
**Код:** 
```
new g_msgStatusIcon
```

2. По умолчанию, в Half-Life (в отличии от Counter-Strike) сообщение **StatusIcon** на сервере не зарегистрировано, поэтому в plugin_precache нам необходимо его зарегистрировать и получить ID. (В [Bugfixed and improved HL release](http://aghl.ru/forum/viewtopic.php?f=32&t=686) данное собщение регистрируется, поэтому надо сначала попробовать получить его ID, и если оно 0, то тогда зарегистрировать самим):  
**Код:** 
```
public plugin_precache()   
{  
   g_msgStatusIcon = get_user_msgid("StatusIcon")  
   if (!g_msgStatusIcon)  
      g_msgStatusIcon = engfunc(EngFunc_RegUserMsg,"StatusIcon",-1)  
}
```

3. Для того чтобы отобразить иконку статуса, нам необходимо создать сообщение следующим образом:  
**Код:** 
```
engfunc(EngFunc_MessageBegin, MSG_ONE_UNRELIABLE, g_msgStatusIcon, {0.0, 0.0, 0.0}, iPlayer)
```
4. Дальше нам необходимо передать байт, отвечающий за статус сообщения:  
**Код:** 
```
write_byte(1) // 1 - означает показ иконки.
```
5. Затем необходимо передать название спрайта:  
**Код:** 
```
write_string("имя спрайта")
```
6. Теперь нам нужно передать цвет иконки:  
**Код:** 
```
write_byte(r)  
write_byte(g)  
write_byte(b)
```
7. Завершаем сообщение следующим образом:  
**Код:** 
```
message_end()
```
  
Примерный плагин:  
**Код:** 
```
#include <amxmodx>  
#include <fakemeta>  
  
public plugin_precache()   
{  
   g_msgStatusIcon = engfunc(EngFunc_RegUserMsg, "StatusIcon", -1)  
  
   register_clcmd("say /show_icon", "ShowStatusIcon")  
   register_clcmd("say /hide_icon", "HideStatusIcon");  
}  
  
public ShowStatusIcon(iPlayer)  
{  
   engfunc(EngFunc_MessageBegin, MSG_ONE_UNRELIABLE, g_msgStatusIcon, {0.0, 0.0, 0.0}, iPlayer)  
   write_byte(1)  
   write_string("item_longjump")  
   write_byte(0);  
   write_byte(255);   
   write_byte(0);  
   message_end  
}  
  
public HideStatusIcon(iPlayer)  
{  
   engfunc(EngFunc_MessageBegin, MSG_ONE_UNRELIABLE, g_msgStatusIcon, {0.0, 0.0, 0.0}, iPlayer)  
   write_byte(0)  
   write_string("item_longjump")  
   message_end  
}
```
  
**Список стандартно доступных спрайтов**   
bucket1  
bucket2   
bucket3   
bucket4   
bucket5   
bucket0   
  
dmg_bio  
dmg_poison  
dmg_chem  
dmg_cold  
dmg_drown  
dmg_heat  
dmg_gas  
dmg_rad  
dmg_shock  
  
number_0  
number_1  
number_2  
number_3  
number_4  
number_5  
number_6  
number_7  
number_8  
number_9  
  
divider  
  
cross  
  
suit_full  
suit_empty  
  
flash_full  
flash_empty  
flash_beam  
  
train_back  
train_stop  
train_forward1  
train_forward2  
train_forward3  
  
autoaim_c  
  
title_half  
title_life  
  
d_crowbar  
d_9mmhandgun  
d_357  
d_9mmAR  
d_shotgun  
d_bolt  
d_crossbow  
d_rpg_rocket  
d_gauss  
d_egon  
d_hornet  
d_grenade  
d_satchel  
d_tripmine  
d_snark  
d_skull  
d_tracktrain  
  
item_battery  
item_healthkit  
item_longjump  
  
grenade   
