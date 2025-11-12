# get_plugin Функция получает информацию о плагине
[Ядро AMXx](http://amxxmodx.ru/core/) [amxmodx.inc](http://amxxmodx.ru/core/amxmodxinc/)
Функция получения информации о плагине используется крайне редко.  
Я ее встречал только в плагине admincmd, для получения списка загруженных плагинов.  
Если вы не собираетесь его переписывать, то она на вряд ли будет полезна.  
  
Инфо из **amxmodx.inc:**  
```
/* Gets info about plugin by given index.  
 * Function returns -1 if plugin doesn't exist with given index.   
 * Note: the [...] portion should not be used, and is only for backward compatibility.  
 * Use index of -1 to use the calling plugin's ID.  
 */  
native get_plugin(index,filename[]="",len1=0,name[]="",len2=0,version[]="",len3=0,author[]="",len4=0,status[]="",len5=0,...);
```
  
  
**Синтаксис:**  

get_plugin(index, filename[] = "", len1 = 0, name[] = "", len2 = 0, version[] = "", len3 = 0, author[] = "", len4 = 0, status[] = "", len5 = 0)
  

    * **index** - id плагина  

    * **filename** - Массив под имя файла плагина  

    * **len1** - Максимальный размер для имени файла плагна  

    * **name** - Название плагина  

    * **len2** - Максимальный размер для имени плагина  

    * **version** - Массив для записи версии плагина  

    * **len3** - Максимальный размер для версии плагина  

    * **author** - Массив для записи автора плагина  

    * **len4** - Максимальный размер массива для автора плагина  

    * **status** - Массив для статуса плагина  

    * **len5** - Максимальная длина для массива статуса плагина  

  
  
**Тип функции:**  
Native   
  
**Пример:**  
```
public cmdPlugins(id, level, cid)  
{  
    if (!cmd_access(id, level, cid, 1))  
        return PLUGIN_HANDLED  
          
    if (id==0) // If server executes redirect this to "amxx plugins" for more in depth output  
    {  
        server_cmd("amxx plugins");  
        server_exec();  
        return PLUGIN_HANDLED;  
    }  
  
    new name[32], version[32], author[32], filename[32], status[32]  
    new lName[32], lVersion[32], lAuthor[32], lFile[32], lStatus[32]  
  
    format(lName, 31, "%L", id, "NAME")  
    format(lVersion, 31, "%L", id, "VERSION")  
    format(lAuthor, 31, "%L", id, "AUTHOR")  
    format(lFile, 31, "%L", id, "FILE")  
    format(lStatus, 31, "%L", id, "STATUS")  
  
    new StartPLID=0;  
    new EndPLID;  
  
    new Temp[96]  
  
    new num = get_pluginsnum()  
      
    if (read_argc() > 1)  
    {  
        read_argv(1,Temp,sizeof(Temp)-1);  
        StartPLID=str_to_num(Temp)-1; // zero-based  
    }  
  
    EndPLID=min(StartPLID + 10, num);  
      
    new running = 0  
      
    console_print(id, "----- %L -----", id, "LOADED_PLUGINS")  
    console_print(id, "%-18.17s %-11.10s %-17.16s %-16.15s %-9.8s", lName, lVersion, lAuthor, lFile, lStatus)  
  
    new i=StartPLID;  
    while (i <EndPLID)  
    {  
        get_plugin(i++, filename, 31, name, 31, version, 31, author, 31, status, 31)  
        console_print(id, "%-18.17s %-11.10s %-17.16s %-16.15s %-9.8s", name, version, author, filename, status)  
          
        if (status[0]=='d' || status[0]=='r') // "debug" or "running"  
            running++  
    }  
    console_print(id, "%L", id, "PLUGINS_RUN", EndPLID-StartPLID, running)  
    console_print(id, "----- %L -----",id,"HELP_ENTRIES",StartPLID + 1,EndPLID,num);  
      
    if (EndPLID < num)  
    {  
        formatex(Temp,sizeof(Temp)-1,"----- %L -----",id,"HELP_USE_MORE", EndPLID + 1);  
        replace_all(Temp,sizeof(Temp)-1,"amx_help","amx_plugins");  
        console_print(id,"%s",Temp);  
    }  
    else  
    {  
        formatex(Temp,sizeof(Temp)-1,"----- %L -----",id,"HELP_USE_BEGIN");  
        replace_all(Temp,sizeof(Temp)-1,"amx_help","amx_plugins");  
        console_print(id,"%s",Temp);  
    }  
  
    return PLUGIN_HANDLED  
}
```
  
  
**Описание:**  
Данный пример взят из плагина admincmd, так как не вижу смысла придумывать велосипед.  
Думаю тем кому необходима данная функция, сам более детально сможет разобраться с данным кодом.  
Я же лучше займусь более важными и часто используемым функциями.
