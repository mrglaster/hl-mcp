# SQL_FreeHandle Функция освобождения дескриптора
[SQLx](http://amxxmodx.ru/sqlx/)
**SQL_FreeHandle** - Освобождает дескриптор SQL (кортеж, соединение, запрос, результаты, и т.д.).   
Если Вы освобождаете соединение с базой данных, то соединение закрывается  
  
Инфо из **sqlx.inc** :  
```
/**  
 * Frees an SQL handle.  
 * The handle can be to anything (tuple, connection, query, results, etc).  
 * If you free a database connection, it closes the connection as well.  
 */  
native SQL_FreeHandle(Handle:h);
```
  
  
**Синтаксис:**  

SQL_FreeHandle ( Handle:h )
  
  
**Пример:**  
```
public plugin_end(){  
     SQL_FreeHandle (SQL_Connection) // Закрытие соединения с БД  
}  

```
  
Примечание:Данный пример не является готовым плагином.
