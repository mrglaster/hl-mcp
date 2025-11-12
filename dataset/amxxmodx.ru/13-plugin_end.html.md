# plugin_end Функция вызывается в перед сменой карты или выключением сервера.
[Ядро AMXx](http://amxxmodx.ru/core/) [amxmodx.inc](http://amxxmodx.ru/core/amxmodxinc/)
**plugin_end** - Данная функция вызывается при смене карты или выключении сервера.  
Обычно используется зля завершения соединения с базами данных и сохранение других важных данных, которые могут потребоваться в дальнейшем.  
  
Инфо из **amxmodx.inc**  
```
/* Function called before plugin unloading (server deactivation) */  
forward plugin_end();
```
  
  
**Синтаксис:**  

plugin_end ( )
  
  
**Пример:**  
```
public plugin_end(){  
     SQL_FreeHandle (SQL_Connection) // Закрытие соединения с БД  
}
```
  
Данный пример не является готовым плагином.
