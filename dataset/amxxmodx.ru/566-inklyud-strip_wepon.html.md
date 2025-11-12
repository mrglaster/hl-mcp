# инклюд strip_wepon
[Присланное](http://amxxmodx.ru/other/)
Вы хотели когда-нибудь сделать так что бы у игрока отобралось только определенное оружие , с этим инклюдом это станет реальностью .   
Собственно инклюд вытащил из Зомби мода   
  
из strip_weapon.inc  
```
  
stock strip_weapons(id,stripwhat)  

```
  
strip_weapons(id,stripwhat)  
id - ид игрока которому нужно выбросить оружие  
stripwhat - Какое оружие выбрасываем  
  
Небольшой пример   
```
  
#include <amxmodx>  
#include <strip_weapon> // Подгружаем наш инклюд  
  
#define AUTHOR "Nesquik"  
#define PLUGIN "Strip Weapons for http://amxxmodx.ru"  
#define VERSION "1.0a"  
  
public plugin_init()  
{  
 register_plugin(PLUGIN,VERSION,AUTHOR)  
 register_clcmd("say /pistols","strip_pistols")  
 register_clcmd("say /weapons","strip_guns")  
 register_clcmd("say /grenade","strip_grenade")  
}  
  
public strip_pisrols(id)  
{  
 strip_weapons(id,SECONDARY_ONLY) // Выбрасываем только пистолеты  
 client_print(id,print_chat,"У тебя отобрали все пистолеты")  
}  
  
public strip_guns(id)  
{  
 strip_weapons(id,PRIMARY_ONLY) // Отбираем только основное оружие  
 client_print(id,print_chat,"У тебя отоброны все оружия")  
}  
  
public strip_grenade(id)  
{  
 strip_weapons(id,GRENADES_ONLY)  
 client_print(id,print_chat,"У тебя отобраны все гранаты")  
}  

```
  
  
Тоесть если выполнить команду **say /pistols** то у игрока будут выброшены все пистолеты , если выполнить команду **say /weapons** то у игрока будут отобраны все основные оружия , если выполнить команду **say /grenade** то у игрока будут отобраны все гранаты  
Надеюсь объяснил понятно   
Если нет пишите в комментах поясню  
  
Вы не можете скачивать файлы с нашего сервера  
 _Новость отредактировал**Admin** - 18-05-2013, 18:00_
Причина: Это инклуд с функциями, сам инклуд ничего не делает. Так же в инклуде есть другие функции.
