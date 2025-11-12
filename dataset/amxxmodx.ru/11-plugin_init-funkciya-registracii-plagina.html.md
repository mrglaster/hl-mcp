# plugin_init Функция вызывается при старте сервера,смене карты или рестарте сервера
[Ядро AMXx](http://amxxmodx.ru/core/) [amxmodx.inc](http://amxxmodx.ru/core/amxmodxinc/)
**plugin_init**  
А так же в ней регистрируются команды,квары,ResetHUD и другое.  
Вызывается всегда при старте/перезагрузке сервера,а так же при смене карты.  
  
Инфо из **amxmodx.inc:**  
```
/* Function is called just after server activation.  
* Good place for configuration loading, commands and cvars registration. */  
forward plugin_init();
```
  
  
**Синтаксис:**  
```
public  plugin_init ( )
```
  
[code=php]for()[/code]  
  
**Пример:**  
```
#include <amxmodx>  
#include <amxmisc>  
#include <fun>  
  
#define PLUGIN "Plugin name"  
#define VERSION "1.0"  
#define AUTHOR "Author plagin"  
  
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
    register_clcmd("say /test","test")  
}  
public test(id){  
    // Add your code here...  
}  

```
  
  
Данный пример зарегистрирует плагин, добавит информацию о плагине, его авторе и версии.  
Так же он зарегистрирует команду **say /test** в консоле или же прямо в чате сказать **/test**
