# md5 - вычисляет MD5 хеш строки
[Ядро AMXx](http://amxxmodx.ru/core/) [amxmodx.inc](http://amxxmodx.ru/core/amxmodxinc/)
```
/**  
 * Вычисляет MD5 хеш строки.  
 *  
 * @param szString  строка, хеш которой будет вычислен  
 * @param md5buffer строка-буффер, в который будет скопирован хеш  
 *  
 * @return          количество ячеек записанных в строку-буффер  
 *                 (всегда 32)  
 */  
  
native md5_file(const szString[], md5buffer[34]);
```
  
  
**Пример** :  
```
#include <amxmodx>  
  
#define PLUGIN  "MD5 string"  
#define VERSION "1.0"  
#define AUTHOR  "amxxmodx.ru"  
  
#define TEST_STRING "AMX Mod X в примерах"  
  
public plugin_init()  
{  
  register_plugin(PLUGIN, VERSION, AUTHOR);  
    
  new md5buffer[34];  
  md5_file(TEST_STRING, md5buffer);  
    
  log_amx("String: '%s', md5 hash: '%s'", TEST_STRING, md5buffer);  
}
```
  
  
**Заметки:**  

    * Ограничений на размер строки нет (разве что системных).  

