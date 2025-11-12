# get_user_weapons - функция для получения списка оружия игрока.
[Ядро AMXx](http://amxxmodx.ru/core/) [amxmodx.inc](http://amxxmodx.ru/core/amxmodxinc/)
Функция для получения списка оружия игрока.  
  
Инфо из **amxmodx.inc:**  
```
/**  
* Извлекает все оружие в инвентаре игрока, сохраняет их в массиве, и  
* возвращает в виде суммы битов.  
*  
* @note: Убедитесь, что переменная num имеет начальное значение 0, иначе  
* функция будет работать неправильно.  
*  
* @param index   индекс игрока  
* @param weapons массив для хранения индексов оружия  
* @param num     переменная для хранения количества оружия в инвентаре  
*  
* @return        сумма битов индексов оружия, 0 если игрок не подключен  
* @error         если индекс игрока находится за пределами диапазона от 1 до  
*                MaxClients, будет выдано сообщение об ошибке.  
*/  
  
native get_user_weapons(index, weapons[32], &num);
```
  
  
**Пример:**  
```
  
#include <amxmodx>  
  
#define PLUGIN  "Print user weapons list"  
#define VERSION "1.0"  
#define AUTHOR  "amxxmodx.ru"  
  
const MAX_WEAPONS   = 32;  
const CLASSNAME_LEN = 32;  
  
public plugin_init()  
{  
  register_plugin(PLUGIN, VERSION, AUTHOR);  
  register_concmd("weapon_list", "concmd_weapon_list");  
}  
  
public concmd_weapon_list(id)  
{  
  static weapons[MAX_WEAPONS], weapon_classname[CLASSNAME_LEN];  
  
  // Учитываем замечание в описании функции,  
  // чтобы получить корректный результат  
  new num;  
    
  // Получаем список оружия  
  get_user_weapons(id, weapons, num);  
    
  for (new i; i < num; i++) {  
    // Получаем classname оружия по его CSW идентификатору  
    get_weaponname(weapons[i], weapon_classname, charsmax(weapon_classname));  
      
    // Распечатываем в консоль игроку classname оружия  
    console_print(id, weapon_classname);  
  }  
}
```

