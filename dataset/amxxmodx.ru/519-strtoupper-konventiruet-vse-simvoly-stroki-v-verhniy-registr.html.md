# strtoupper Конвентирует все символы строки в верхний регистр
[Ядро AMXx](http://amxxmodx.ru/core/) [string.inc](http://amxxmodx.ru/core/stringinc/)
strtoupper Конвентирует все символы строки в верхний регистр  
  
Данная функция аналогична функции [strtolower](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2NvcmUvc3RyaW5naW5jLzUxOC1zdHJ0b2xvd2VyLWtvbnZlbnRpcnVldC12c2Utc2ltdm9seS1zdHJva2ktdi1uaXpobml5LXJlZ2lzdHIuaHRtbA%3D%3D), только эта конвентирует все символы строки в верхний регистр.  
  
Инфо из **string.inc**  
```
/* Converts all chars in string to upper case. */  
native strtoupper(string[]);
```
  
  
**Параметры:**  

string[]
  
**string[]** - строка  
  
**Пример:**  
```
#include <amxmodx>  
  
#define PLUGIN "[string.inc] strtoupper  
#define VERSION "1.0"  
#define AUTHOR "Awake"  
  
public plugin_init()  
{  
    register_clcmd("say /test", "Test")  
}  
  
public Test(id)  
{  
    new szText[] = "amxmodx.ru" // создаём переменную szText и записываем в неё строку amxxmodx.ru  
    strtoupper(szText) // конвентируем строку в верхний регистр  
      
    client_print(id, print_chat, "%s", szText) // выводим нашу строку в верхнем регистре, то есть "AMXXMODX.RU"  
}
```

