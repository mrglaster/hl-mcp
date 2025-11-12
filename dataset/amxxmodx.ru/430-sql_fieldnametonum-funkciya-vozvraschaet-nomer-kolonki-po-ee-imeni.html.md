# SQL_FieldNameToNum Функция возвращает номер колонки по ее имени
[SQLx](http://amxxmodx.ru/sqlx/)
Функция SQL_FieldNameToNum вернет номер колонки по ее имени.  
  
Инфо из **sqlx.inc:**  
```
/**  
 * Returns the number of a named column, or -1 if not found.  
 */  
native SQL_FieldNameToNum(Handle:query, const name[]);
```
  
  
**Синтаксис:**  

SQL_FieldNameToNum(Handle:query, const name[])
  

    * **Handle:query** - Идентификатор запроса  

    * **const name[]** - Имя колонки базы данных  

Функция вернет номер колонки в противном случае -1  
  
**Тип функции:**  
Native  
  
**Пример:**  
--  
  
**Описание:**  
--
