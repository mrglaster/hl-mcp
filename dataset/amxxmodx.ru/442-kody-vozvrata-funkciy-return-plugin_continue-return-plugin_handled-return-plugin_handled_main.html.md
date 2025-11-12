# Коды возврата функций return PLUGIN_CONTINUE, return PLUGIN_HANDLED, return PLUGIN_HANDLED_MAIN
[Ядро AMXx](http://amxxmodx.ru/core/)
В AMX Mod X существует 3 константы возврата функций:```
//Plugin passes through operation.  Whatever called it continues.  
#define PLUGIN_CONTINUE        0  
//Plugin halts continued operation (plugins following in the plugins.ini won't be called).  
//Whatever called it will eventually supercede.  
#define PLUGIN_HANDLED        1  
//Continue calling plugins but halt the operation  
#define PLUGIN_HANDLED_MAIN    2
```

    * **PLUGIN_CONTINUE** - Плагин продолжает работать.  

    * **PLUGIN_HANDLED** - Плагин останавливает операцию и плагины следующих ниже в plugins.ini не будут вызваны.  

    * **PLUGIN_HANDLED_MAIN** - Останавливает функцию, но остальные плагины будут вызваны  

  
**Разберемся на примере двух простых плагинов:**  
**Плагин 1:**  
```
#include <amxmodx>  
#include <amxmisc>  
  
#define PLUGIN "[http://amxxmodx.ru] return Pl1"  
//                    PLUGIN_HANDLED_MAIN                              
//                    PLUGIN_HANDLED_MAIN  
//                    PLUGIN_CONTINUE  
  
#define VERSION "1.0"  
#define AUTHOR "Admin"  
  
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
      
    register_clcmd("say hand","FUNC_PLUGIN_HANDLED")  
    register_clcmd("say handm","FUNC_PLUGIN_HANDLED_MAIN")  
    register_clcmd("say cont","FUNC_PLUGIN_CONTINUE")  
  
}  
public FUNC_PLUGIN_HANDLED(id){  
      
    client_print(id,print_chat,"1 plugin - handled")  
      
    return PLUGIN_HANDLED  
      
}  
public FUNC_PLUGIN_HANDLED_MAIN(id){  
      
    client_print(id,print_chat,"1 plugin - handled_main")  
      
    return PLUGIN_HANDLED_MAIN  
      
}  
public FUNC_PLUGIN_CONTINUE(id){  
      
    client_print(id,print_chat,"1 plugin - continue")  
      
    return PLUGIN_CONTINUE  
      
}
```
  
  
**Плагин 2:**  
```
#include <amxmodx>  
#include <amxmisc>  
  
#define PLUGIN "[http://amxxmodx.ru] return Pl2"  
//                    PLUGIN_HANDLED_MAIN                              
//                    PLUGIN_HANDLED_MAIN  
//                    PLUGIN_CONTINUE  
  
#define VERSION "1.0"  
#define AUTHOR "Admin"  
  
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
      
    register_clcmd("say hand","FUNC_PLUGIN_HANDLED")  
    register_clcmd("say handm","FUNC_PLUGIN_HANDLED_MAIN")  
    register_clcmd("say cont","FUNC_PLUGIN_CONTINUE")  
  
}  
public FUNC_PLUGIN_HANDLED(id){  
      
    client_print(id,print_chat,"2 plugin - handled")  
      
    return PLUGIN_HANDLED  
      
}  
public FUNC_PLUGIN_HANDLED_MAIN(id){  
      
    client_print(id,print_chat,"2 plugin - handled_main")  
      
    return PLUGIN_HANDLED_MAIN  
      
}  
public FUNC_PLUGIN_CONTINUE(id){  
      
    client_print(id,print_chat,"2 plugin - continue")  
      
    return PLUGIN_CONTINUE  
      
}
```
  
  
**Описание:**  
Самые внимательные заметили что плагины отличаются всего лишь парой знаков, но именно эти знаки дадут понимание происходящего.  
В обоих плагинах зарегистрированы 3 команды, они одинаковые _это важно_.  
При вводе команды **say hand** будет вызвана функция **public FUNC_PLUGIN_HANDLED(id)** в обоих плагинах (ключевое тут что одна и та же функция будет вызвана, название может быть любым, главное что вызываются от одного и того же.) Аналогично и для двух других команд **say handm** и **say cont** , как вы уже догадались это сокращения от имен констант возвратов.  
  
Если не ставить ни каких возвратов или **PLUGIN_CONTINUE** , то в обоих плагинах выполнится весь код и в чате будет такая картина:  

1 plugin - continue  
2 plugin - continue  
Admin : cont
  
Как видно прошло и сообщение в чат и выполнились полностью функции в каждом из плагинов.  
  
Теперь **PLUGIN_HANDLED** , команда **say handm** , результат такой:  

1 plugin - handle
  
Как видно нет ни самго сообщения в чат ни сообщения из второго плагина, хотя оно там есть - проверьте сами.  
Это потому что PLUGIN_HANDLED блокирует не только операцию, но вызов плагинов следующих после него в списке plugins.ini  
  
И наконец редко встречающийся **PLUGIN_HANDLED_MAIN** , команда **say handm** :  

1 plugin - handled_main  
2 plugin - handled_main  

  
Как видите нету сообщения в чат **handm** , но зато выполнились все функции остальных плагинов.  
  
Надеюсь теперь вам понятны различия данных возвратов.  
  
  

