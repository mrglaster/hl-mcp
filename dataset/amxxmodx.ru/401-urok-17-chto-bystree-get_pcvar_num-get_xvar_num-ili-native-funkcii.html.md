# Урок 17. Что быстрее get_pcvar_num, get_xvar_num или native функции.
[Уроки по скриптингу для начинающих](http://amxxmodx.ru/lessons-on-pawn/)
Честно говоря, я сам не особо задавался данным вопросом, так как у меня ни когда не было особых ограничений в использовании ресурсов физических серверов, так как они у меня стоят на собственных "машинах". Но когда искал информацию для описания очередной функции **xvar_exists** , наткнулся на результаты одного эксперимента, и разумеется решил и вам рассказать о его результатах.  
  
Основной вопрос эксперимента:  
_Что быстрее get_pcvar_num, get_xvar_num или native функции?_  
  
Для эксперимента было написано два коротеньких плагина (плагины представлены в оригинале):  
**Первый плагин:**  
```
#include <amxmodx>   
  
#define VERSION "0.0.1"   
#define PLUGIN "xvar profile 1"   
  
public xvar1 = 10   
  
public plugin_init()   
{   
    register_plugin(PLUGIN, VERSION, "ConnorMcLeod")   
    register_cvar("amx_cvar_test", "1337")   
}   
  
public plugin_natives()   
{   
    register_native("get_variable_test", "get_variable_test")   
}   
  
public get_variable_test()   
{   
    return xvar1   
} 
```
  
В нем регистрируется натив и переменная для эксперимента.  
  
**Второй плагин:**  
```
#include <amxmodx>   
  
#define VERSION "0.0.1"   
#define PLUGIN "xvar profile 2"   
  
native get_variable_test()   
  
public plugin_init()   
{   
    register_plugin(PLUGIN, VERSION, "ConnorMcLeod")   
}   
  
public plugin_cfg()   
{   
    new pcvar = get_cvar_pointer("amx_cvar_test")   
    new xvar = get_xvar_id("xvar1")   
  
    for(new i; i<1000; i++)   
    {   
        get_pcvar_num(pcvar)   
        get_xvar_num(xvar)   
        get_variable_test()   
    }   
} 
```
  
В нем с помощью цикла вызываются 3 изучаемые функции.  
  
И теперь самое главное, результаты:```
  
date: Fri Sep 24 19:18:23 2010 map: de_aztec  
type |             name |  calls | time / min / max  
-------------------------------------------------------------------  
   n |  register_plugin |      1 | 0.000001 / 0.000001 / 0.000001  
   n | get_cvar_pointer |      1 | 0.000001 / 0.000001 / 0.000001  
   n |      get_xvar_id |      1 | 0.000001 / 0.000001 / 0.000001  
   n |    get_pcvar_num |   1000 | 0.000180 / 0.000000 / 0.000000  
   n |     get_xvar_num |   1000 | 0.000179 / 0.000000 / 0.000000  
   n |get_variable_test |   1000 | 0.000245 / 0.000000 / 0.000001  
   p |       plugin_cfg |      1 | 0.000561 / 0.000561 / 0.000561  
   p |      plugin_init |      1 | 0.000001 / 0.000001 / 0.000001  
0 natives, 0 public callbacks, 2 function calls were not executed.
```
  
  
Обратите внимание на эти 3 строки:  

type | name | calls | time / min / max  
-------------------------------------------------------------------  
n | get_pcvar_num | 1000 | 0.000180 / 0.000000 / 0.000000  
n | get_xvar_num | 1000 | 0.000179 / 0.000000 / 0.000000  
n |get_variable_test | 1000 | 0.000245 / 0.000000 / 0.000001
  
  
Точнее на столбец time это время выполнения для каждой из функций выборка берется для 1000 раз, думаю и так видно, что работает быстрее, но все же расставим по местам:  

    * Первое место занимает **get_xvar_num**  

    * Второе место **get_pcvar_num**  

    * Третье место **get_variable_test**  

Между первым и вторым местом разница не значительная, но как факт есть.  
По этому если вам нужно передать переменную из плагина в плагин, то луче использовать **xvar**  
  
**Источник:[forums.alliedmods.net](http://amxxmodx.ru/engine/go.php?url=aHR0cHM6Ly9mb3J1bXMuYWxsaWVkbW9kcy5uZXQvc2hvd3Bvc3QucGhwP3A9MTMwNzU3NSZhbXA7cG9zdGNvdW50PTg%3D)**
