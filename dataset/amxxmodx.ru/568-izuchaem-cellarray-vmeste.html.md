# Изучаем CellArray вместе
[Присланное](http://amxxmodx.ru/other/)
Если его (инклюда cellarray.inc) нету в папке addons/amxmodx/scripting/include   
Вы не можете скачивать файлы с нашего сервера  
  
Скачали :? Отлично   
Теперь перейдём к изучению   
  
```
  
/**  
 * Создаёт Array  
 * используется для Array{Get,Set,Push}  
 *  
 * @параметр cellsize        Размер Array 32 = строка , 1 = число  
 * @параметр reserved        Сколько пустых записей создаются сразу же после создания массива.  
 * @return             Handle to the array.  
 */  
native Array:ArrayCreate(cellsize=1, reserved=32);  

```
  
  
Натив создает Array  
Пример :  
```
  
#include <amxmodx> // Инклюд cellarray.inc вписан в amxmodx.inc   
  
new Array:MyArray // Наш Array  
  
public plugin_init()  
{  
 MyArray = ArrayCreate(32, 1) // Создали наш Array, 32 = значит Array будет строкой , если хотим чтобы было число вместо 32 ставим 1  
}  

```
  
  
```
  
/**  
 * Возвращает сколько всего было зарегистрировано Array  
 *  
 * @параметр which        Array для проверки  
 * @return                Число   
 */  
native ArraySize(Array:which);  

```
  
  
Возвращает размер Array  
Пример :  
```
  
#include <amxmodx> // Инклюд cellarray.inc вписан в amxmodx.inc   
  
new Array:MyArray // Наш Array  
  
public plugin_init()  
{  
 MyArray = ArrayCreate(32, 1) // Создали наш Array, 32 = значит Array будет строкой , если хотим чтобы было число вместо 32 ставим 1  
 new size = ArraySize(MyArray)  
 server_print("Array = %i", size)  
}  

```
  
  
```
  
/**  
 * Возвращает число полученное из Array.    
 * Используется если cellsize = 1!  
 *  
 * @параметр which        Array для получения  
 * @параметр item            Номер Array  
 * @return                Число   
 */  
native any:ArrayGetCell(Array:which, item);  

```
  
  
Получает число из Array  
пример :  
```
  
#include <amxmodx> // Инклюд cellarray.inc вписан в amxmodx.inc   
  
new Array:MyArray // Наш Array  
  
public plugin_init()  
{  
 MyArray = ArrayCreate(1, 1) // Создали наш Array, 32 = значит Array будет строкой , если хотим чтобы было число вместо 32 ставим 1  
 new size = ArraySize(MyArray)  
 server_print("Array = %i", size)  
 for(new i = 0; i < size; i++)   
 {  
  new MyArrayCell = ArrayGetCell(MyArray, i)  
  server_print("Array = %i", MyArrayCell) // Выводиться ничего небудет так как мы еще не записывали ничего в MyArray  
 }  
}  

```
  
  
```
  
/**  
 * Возвращает строку полученную из Array.  
 *  
 * @параметр which            Array для получения строки  
 * @параметр item            Номер Array  
 * @параметр output        Массив для записи строки  
 * @параметр size            Размер массива  
 */  
native ArrayGetString(Array:which, item, output[], size);  

```
  
  
Возвращает строку полученную из Array  
Пример :  
```
  
#include <amxmodx> // Инклюд cellarray.inc вписан в amxmodx.inc   
  
new Array:MyArray // Наш Array  
  
public plugin_init()  
{  
 MyArray = ArrayCreate(32, 1) // Создали наш Array, 32 = значит Array будет строкой , если хотим чтобы было число вместо 32 ставим 1  
 new size = ArraySize(MyArray)  
 server_print("Array = %i", size)  
 for(new i = 0; i < size; i++)   
 {  
  new MyArrayString[32]  
  ArrayGetCell(MyArray, i, MyArrayString, 31)  
  server_print("Array = %s", MyArrayString) // Выводиться ничего небудет так как мы еще не записывали ничего в MyArray  
 }  
}  

```
  
  
```
  
/**  
 * Устанавливает число Array использовать только если cellsize = 1!  
 *  
 * @параметр which            Array для установки числа   
 * @параметр input            Число для установки   
 */  
native ArrayPushCell(Array:which, any:input);  

```
  
  
Устанавливает число для Array  
Пример :  
```
  
#include <amxmodx> // Инклюд cellarray.inc вписан в amxmodx.inc   
#include <amxmisc>  
  
new Array:MyArray // Наш Array  
  
public plugin_init()  
{  
 MyArray = ArrayCreate(1, 1) // Создали наш Array, 32 = значит Array будет строкой , если хотим чтобы было число вместо 32 ставим 1  
 register_clcmd("set_array_cell", "set_cell")  
}  
  
public set_cell(id)  
{  
 new Cell[15] // Массив куда будет записана строка с числом   
 read_argv(1, Cell, 31) // Читаем строку  
   
 if(strlen(Cell))  
 {  
  new MyCell = str_to_num(Cell) // Преобразуем строку в число  
  ArrayPushCell(MyArray, MyCell) // Устанавливаем MyArray число MyCell  
  server_print("MyArray = %i", MyCell) // Выводим в консоле сервера число которое было установлено  
 }  
}  

```
  
  
```
  
/**  
 * Устанавливает Array строку.    
 * @параметр which            Array для записи строки  
 * @параметр input            Строка для записи   
 */  
native ArrayPushString(Array:which, const input[]);  

```
  
  
Устанавливает строку в Array  
Пример :  
```
  
#include <amxmodx> // Инклюд cellarray.inc вписан в amxmodx.inc   
#include <amxmisc>  
  
new Array:MyArray // Наш Array  
  
public plugin_init()  
{  
 MyArray = ArrayCreate(32, 1) // Создали наш Array, 32 = значит Array будет строкой , если хотим чтобы было число вместо 32 ставим 1  
 register_clcmd("set_array_string", "set_string")  
}  
  
public set_string(id)  
{  
 new Cell[15] // Массив куда будет записана строка с числом   
 read_argv(1, Cell, 31) // Читаем строку  
   
 if(strlen(Cell))  
 {  
  ArrayPushString(MyArray, MyCell) // Устанавливаем MyArray строку Cell  
  server_print("MyArray = %s", Cell) // Выводим в консоле сервера число которое было установлено  
 }  
}  

```
  
  
```
  
/**  
 * Уничтожает созданные Array  
 *  
 * @параметр which            Array для уничтожения   
 */  
native ArrayDestroy(&Array:which);  

```
  
  
Уничтожает Array  
Пример :  
```
  
#include <amxmodx> // Инклюд cellarray.inc вписан в amxmodx.inc   
#include <amxmisc>  
  
new Array:MyArray // Наш Array  
  
public plugin_init()  
{  
 MyArray = ArrayCreate(32, 1) // Создали наш Array, 32 = значит Array будет строкой , если хотим чтобы было число вместо 32 ставим 1  
 register_clcmd("set_array_string", "set_string")  
}  
  
public set_string(id)  
{  
 new Cell[15] // Массив куда будет записана строка с числом   
 read_argv(1, Cell, 31) // Читаем строку  
   
 if(strlen(Cell))  
 {  
  ArrayPushString(MyArray, MyCell) // Устанавливаем MyArray строку Cell  
  server_print("MyArray = %s", Cell) // Выводим в консоле сервера строку которая была установлена  
 }  
}  
  
public destroy()  
{  
 ArrayDestroy(MyArray)  
}  

```
  
  
Ну вот немного разобрались  
Здесь описаны не все нативы которые есть в cellarray.inc  
Но можно сказать что они основные которые пригодятся вам   
Обычно инклюд используется для создания магазинов и т.д.   
примером для нас служит Zombie Mod, в моде все модели , звуки , спрайты записаны в Array
