# strtolower Конвентирует все символы строки в нижний регистр
[Ядро AMXx](http://amxxmodx.ru/core/) [string.inc](http://amxxmodx.ru/core/stringinc/)
Данная функция конвентирует все символы строки в нижний регистр. Она редко встречается в плагинах, но, думаю, вы найдёте ей применение.  
  
Инфо из **string.inc**  
```
/* Converts all chars in string to lower case. */  
native strtolower(string[]);
```
  
Параметры:  

string[] - строка
  
  
**Пример:**  
  
```
#include <amxmodx>  
  
#define PLUGIN "[string.inc] strtolower  
#define VERSION "1.0"  
#define AUTHOR "Awake"  
  
public plugin_init()  
{  
    register_clcmd("say /test", "Test")  
}  
  
public Test(id)  
{  
    new szText[] = "AMXXMODX.RU" // создаём переменную szText и записываем в неё строку AMXXMODX.RU  
    strtolower(szText) // конвентируем строку в нижний регистр  
      
    client_print(id, print_chat, "%s", szText) // выводим нашу строку в нижнем регистре, то есть - "amxxmodx.ru"  
}
```
  
Как видите, функция очень проста и не должна вызывать трудностей. Спасибо за внимание! :)
