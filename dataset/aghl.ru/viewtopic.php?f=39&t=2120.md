# Half-Life и Adrenaline Gamer форум
Всё об игре в Халф-Лайф и АГ  


## [[TUT] Pawn, константы, определенные препроцессором](https://aghlru.ds-servers.com/forum/viewtopic.php?f=39&t=2120)
Категории: [Туториал](https://aghlru.ds-servers.com/forum/search.php?keywords=%2B%D0%A2%D1%83%D1%82%D0%BE%D1%80%D0%B8%D0%B0%D0%BB&terms=all&fid\[\]=19&sc=1&sf=catonly&sr=topics)
Модератор: [KORD_12.7](https://aghlru.ds-servers.com/forum/memberlist.php?mode=viewprofile&u=67)
  
  
**PAWN, константы, определенные препроцессором**  
**Навеяно постом by KliPPy отсюда:** (_<http://forums.alliedmods.net/showthread.php?t=252477>_)  
  
Препроцессор _PAWN_ самостоятельно определяет несколько полезных констант:  

**__DATE__** - дата компиляции,  
**__TIME__** - время компиляции,  
**cellbits** - размер ячейки в битах,  
**cellmax** - максимальное значение, которое может храниться в ячейке,  
**cellmin** - минимальное значение, которое может храниться в ячейке,  
**__Pawn** - версия _PAWN_ в целочисленном значении,  
**debug** - уровень дебага.
  
Также, начиная с версии _AMXX 1.8.3_ , были добавлены еще три константы:  

**__LINE__** - номер текущей строки исходного текста плагина,  
**__BINARY_PATH__** - путь к скомпилированному файлу плагина,  
**__BINARY_NAME__** - имя скомпилированного файла плагина.
  
Если эти константы встречаются в тексте скрита, то заменяются на соответствующие строки или числа. Плагин ниже выводит значения предопределенных препроцессором констант в консоль сервера:  
**Код:** 
```
#include <amxmodx>  
  
public plugin_init()  
{  
   server_print("Constants:");  
   server_print("__DATE__: %s", __DATE__);  
   server_print("__TIME__: %s", __TIME__);  
   server_print("cellbits: %d", cellbits);  
   server_print("cellmax: %d", cellmax);  
   server_print("cellmin: %d", cellmin);  
   server_print("__Pawn: %d", __Pawn);  
   server_print("debug: %d", debug);  
     
   #if AMXX_VERSION_NUM > 182  
     
   server_print("__LINE__: %d", __LINE__);  
   server_print("__BINARY_PATH__: %s", __BINARY_PATH__);  
   server_print("__BINARY_NAME__: %s", __BINARY_NAME__);  
     
   #endif  
}  

```
