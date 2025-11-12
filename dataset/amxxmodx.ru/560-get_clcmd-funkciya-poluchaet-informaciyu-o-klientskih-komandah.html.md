# get_clcmd Функция получает информацию о клиентских командах.
[Ядро AMXx](http://amxxmodx.ru/core/) [amxmodx.inc](http://amxxmodx.ru/core/amxmodxinc/)
Инфо из **amxmodx.inc:**  
```
/* Gets info about client command. */  
native get_clcmd(index, command[], len1, &flags, info[], len2, flag);
```
  
  
**Синтаксис:**  

get_clcmd(index, command[], len1, &flags, info[], len2, flag)
  

    * **index** - Индекс команды  

    * **command[]** - Команда  

    * **len1** - Длина для массива  

    * **& flags** -   

    * **info[]** -   

    * **len2** -   

    * **flag** -   

  
  
**Тип функции:**  
Native  
  
**Пример:**  
```
  
stock bool:get_clcmd_flags(const search_command[], &flags)  
{  
    new count = get_clcmdsnum(-1);  
    static cmd[128];  
    static info[1];  
    new _flags;  
  
    for (new i = 0; i < count; i++)  
    {  
        get_clcmd(i, cmd, charsmax(cmd), _flags, info, charsmax(info), -1);  
  
        if (strcmp(cmd, search_command) == 0)  
        {  
            flags = _flags;  
            return true;  
        }  
    }  
  
    return false;  
}  

```
  
  
**Описание:**  
Пример использования смотрите в плагине menufront.sma.
