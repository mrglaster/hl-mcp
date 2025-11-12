# cs_set_user_model Функция замены модели игроку
[CStrike](http://amxxmodx.ru/cstrike/)
Есть такие плагины, где нужно сменить модель игрока.Так вот именно функция **cs_set_user_model** поможет сменить модель.  
  
Инфо из **cstrike.inc:**  
```
/* Set user model*/  
native cs_set_user_model(index, const model[]);
```
  
  
**Синтаксис:**  

cs_set_user_model ( index, const model[] )
  

    * **index** - id игрока кому меняем модель (от 1 до 32)  

    * **const model[]** - Имя модели  

  
**Внимание:** Работает только для Counter_strike.  
  
**Пример:**  
```
#include <amxmodx>  
#include <amxmisc>  
#include <cstrike>  
   
#define PLUGIN "Set user model"  
#define VERSION "1.0"  
#define AUTHOR "Maf1a"  
   
public plugin_init() {  
        register_plugin(PLUGIN, VERSION, AUTHOR)  
       
        register_clcmd("say /model","user_model")  
}  
public plugin_precache() {  
        precache_model("models/player/gign.mdl")  
}  
public user_model(id)  
{  
        cs_set_user_model(id, "gign")  
}  

```
  
  
**Описание:**  
И так,нам нужно сменить модель игрока,для этого мы зарегистрировали команду **say /model** ,которая выполняет функцию **user_model** ,внутри этой функции мы меняем модель игроку.  
  
**gign** - модель игрока,можно указывать любую.  
**Внимание:** в функции нужно указывать модель без **.mdl** только название  
```
сs_set_user_model(id, "gign")
```
  
Иначе работать не будет.  
  
Кеширвоание файла модели, если вы используете не стандартную модель, что бы она закачалась игроку при коннекте к серверу.  
```
public plugin_precache() {  
        precache_model("models/player/gign.mdl")  
}
```
Меняйте модели на здоровье!
