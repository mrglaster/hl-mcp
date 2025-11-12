# md5_file - вычисляет MD5 хеш файла
[Ядро AMXx](http://amxxmodx.ru/core/) [amxmodx.inc](http://amxxmodx.ru/core/amxmodxinc/)
```
/**  
 * Вычисляет MD5 хеш файла.  
 *  
 * @param file      путь к файлу, хеш которого будет вычислен  
 * @param md5buffer строка-буффер, в который будет скопирован хеш  
 *  
 * @return          количество ячеек записанных в строку-буффер  
 *                 (всегда 32)  
 * @error           если файл невозможно открыть, то будет выдано  
 *                  сообщение об ошибке.  
 */  
  
native md5_file(const file[], md5buffer[34]);
```
  
  
**Пример** :  
```
#include <amxmodx>  
  
#define PLUGIN  "MD5 file"  
#define VERSION "1.0"  
#define AUTHOR  "amxxmodx.ru"  
  
#define FULL_FILENAME "addons/amxmodx/configs/users.ini"  
  
public plugin_init()  
{  
  register_plugin(PLUGIN, VERSION, AUTHOR);  
    
  new md5buffer[34];  
  md5_file(FULL_FILENAME, md5buffer);  
    
  log_amx("File: '%s', md5 hash: '%s'", FULL_FILENAME, md5buffer);  
}
```
  
  
**Заметки:**  

    * С помощью функции можно проверить редактировался файл или нет.  

