# get_players Функция получает индексы всех игроков
[Ядро AMXx](http://amxxmodx.ru/core/) [amxmodx.inc](http://amxxmodx.ru/core/amxmodxinc/)
Предположим что вам необходимо в конце раунда всем живым игрокам дать какой то бонус, как это сделать?  
Один из вариантов сделать цикл по всем игрокам и проверять жив ли игрок или нет, но можно воспользоваться функцией **get_players** , которая возвращает индексы игроков, при этом в функции есть возможность сортировки по флагам.  
  
Инфо из **amxmodx.inc:**  
```
/* Sets indexes of players.  
* Flags:  
* "a" - don't collect dead players.  
* "b" - don't collect alive players.  
* "c" - skip bots.  
* "d" - skip real players.  
* "e" - match with team.  
* "f" - match with part of name.  
* "g" - ignore case sensitivity.  
* "h" - skip HLTV.  
* Example: Get all alive CTs: get_players(players,num,"ae","CT") */  
native get_players(players[32], &num ,const flags[]="", const team[]="");
```
  
  
**Синтаксис:**  

get_players ( players[32], &num, const flags = )
  

    1. **players[32]** - массив для индексов игроков  

    2. &**num** - переменная для общего числа игроков  

    3. **const flags =** - Какого типа игроков не считаем  

  
**Флаги:**  

    * **a** - Не считать мертвых  

    * **b** - Не считать живых  

    * **c** - Не считать ботов  

    * **d** - Не считать реальных игроков  

    * **e** - Соответствие с командой  

    * **f** - Соответствие с частью имени ( клантегом например)  

    * **g** - Игнорирование регистра  

    * **h** - Не считать HLTV  

  
  
**Пример:**  
```
#include <amxmodx>  
#include <amxmisc>  
  
#define PLUGIN "Get Players"  
#define VERSION "1.0"  
#define AUTHOR "Admin"  
  
  
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
      
    register_clcmd("get_players","player_list")  
}  
public player_list(id){  
      
    //Регистрируем необходимые массивы  
    // Куда зпишем иднексы игроков  
    new Players[32]   
    // Всего игроков,счетчик для цикла,для id в цикле,  
    //что бы не писать грамоздкую конструкцию Players[i]  
    new Count, i, player   
      
    //Для наглядности плагина, массивы под имя и ip игроков  
    new name[32],ip[32]  
      
    //получаем индексы игроков и их количество, игнорируем HLTV  
    get_players(Players, Count, "h")   
      
    //Цикл, пробегает до последнего игрока  
    for (i=0; i<Count; i++) {  
        //в цикле id игрока получается Players[i], но мы его преобразовываем в player  
        player = Players[i]  
          
        //Получаем имя и ip игрока  
        get_user_name(player,name,31)  
        get_user_ip(player,ip,16,1)  
          
        //Выводим информацию в консоль  
        console_print(id,"Nick: %s, ip: %s",name,ip)  
    }  
      
}
```
  
**Описание:**  
Выполнив в консоле команды **get_players** , вы получите список имен игроков и их ip адреса.  
Наглядный пример как работает функция, а заодно и цикл **for**.  
  
Обратите внимание, что сами разработчики мода, не особо довольны данной функцией.  
Но не отчаивайтесь, есть и другие способы получить необходимых нам игроков, и они не намного сложнее, просто в место нескольких флагов данной функции, придется разобраться с парочкой других функций, которые вам все равно пришлось бы изучать.
