# Некоторые функции, особенно нагружающие сервер
[Присланное](http://amxxmodx.ru/other/)
Внимание! 'Статья' - это по сути комментарий, который не уместился. Раскрыто от силы 5% материала. Вопросы, пожелания и предложения в комментариях приветствуются.  
  
  

sibas
Если можно, хорошо было бы составить список команд, функций, форвардов которые нагружают сервер.
  
**sibas** , ага) А вторую сразу же - с наиболее распространёнными примерами, когда можно обойтись без дикой нагрузки xD Жаль, нет времени.  
  
Всё в той или иной степени нагружает сервер) Главное вот что: ощутимую нагрузку создаёт то, что выполняется в плагине многократно за секунду.  
  
Особенно нагрузочные форварды из комплекта AMXX:  
```
// engine  
client_PostThink()  
client_PreThink()  
server_frame()  
client_cmdStart()  
  
// fakemeta  
FM_PlayerPreThink  
FM_PlayerPostThink  
FM_CmdStart  
FM_CmdEnd  
FM_AddToFullPack  
FM_UpdateClientData  
  
// ham sandwich  
Ham_Player_PreThink  
Ham_Player_PostThink
```
  
Лидирует в этом списке, безусловно, _FM_AddToFullPack_ - этот форвард выполняется просто с космической скоростью: порядка 10000 раз в секунду. Затем идёт _server_frame()_ - число вызовов равно FPS сервера, остальные перечисленные форварды выполняются порядка 50-100 раз в секунду.  
  
Есть простой способ определить число выполнений функции:  
```
// algorithm by Asdmodai  
  
// инклуды  
  
#define INTERVAL 1    // how frequently print info; in seconds  
  
new giCounter  
   
public plugin_init() {  
    // регим форвард, если нужно  
    // <> TargetForward <>  
  
    set_task( INTERVAL.0, "PrintRate", .flags = "b" )  
}  
  
public TargetForward() {  
    giCounter++  
}  
  
public PrintRate() {  
    server_print( "Current rate: %d", giCounter / INTERVAL )  
    giCounter = 0  
}
```
  
На примере форварда _server_frame_ :  
```
#include <amxmodx>  
#include <engine>  
  
#define INTERVAL 1    // how frequently print info in seconds  
  
new giCounter  
   
public plugin_init() {  
    set_task( INTERVAL.0, "PrintRate", .flags = "b" )  
}  
  
public server_frame() {  
    giCounter++  
}  
  
public PrintRate() {  
    server_print( "Current server_frame() rate: %d", giCounter / INTERVAL )  
    giCounter = 0  
}
```
  
Интервал показаний 1 с (sys_ticrate 100):  

Current forward rate: 102  
Current forward rate: 102  
Current forward rate: 91  
Current forward rate: 102  
Current forward rate: 92  
Current forward rate: 100  
Current forward rate: 89  
Current forward rate: 100  
Current forward rate: 101  
Current forward rate: 91  
Current forward rate: 100  
Current forward rate: 100  
Current forward rate: 90  
Current forward rate: 100
  
Интервал 5 с даёт усреднённые значения:  

Current forward rate: 100  
Current forward rate: 98  
Current forward rate: 99  
Current forward rate: 98  
Current forward rate: 97  
Current forward rate: 98
(и не спрашивайте, почему именно такие средние значения: эти данные выдал сервер xD)  
  
Таким макаром и выясняйте для себя частоту выполнения той или иной функции.
