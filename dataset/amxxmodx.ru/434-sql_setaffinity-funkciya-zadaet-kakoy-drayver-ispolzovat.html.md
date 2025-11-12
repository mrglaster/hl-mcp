# SQL_SetAffinity Функция задает какой драйвер использовать
[SQLx](http://amxxmodx.ru/sqlx/)
С помощью функции **SQL_SetAffinity** возможно задать необходимый драйвер для использования модулем.  
  
Инфо из **sql.inc:**  
```
/**  
 * Sets driver affinity.  You can use this to force a particular   
 *  driver implementation.  This will automatically change all SQL  
 *  natives in your plugin to be "bound" to the module in question.  
 * If no such module is found, it will return 0.  This isn't necessarily bad -   
 *  the user might have typed the wrong driver.  Unless your plugin is built  
 *  to handle different driver types at once, you should let this error pass.  
 * Note, that using this while you have open handles to another database   
 *  type will cause problems.  I.e., you cannot open a handle, switch  
 *  affinity, then close the handle with a different driver.  
 * Switching affinity is an O(n*m) operation, where n is the number of  
 *  SQL natives and m is the number of used natives in total.  
 * Intuitive programmers will note that this causes problems for threaded queries.  
 *  You will have to either force your script to work under one affinity, or to   
 *  pack the affinity type into the query data, check it against the current, then  
 *  set the new affinity if necessary.  Then, restore the old for safety.  
 */  
native SQL_SetAffinity(const driver[]);
```
  
  
**Синтаксис:**  

SQL_SetAffinity(const driver[])
  

    * **const driver[]** - Название драйвера или массив с названием  

  
  
**Тип функции:**  
Native  
  
**Пример:**  
```
SQL_SetAffinity("sqlite")
```
  
  
**Описание:**  
--
