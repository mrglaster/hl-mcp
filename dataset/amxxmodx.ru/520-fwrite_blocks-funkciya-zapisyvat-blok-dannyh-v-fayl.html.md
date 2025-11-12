# fwrite_blocks Функция записывает блок данных в файл.
[Ядро AMXx](http://amxxmodx.ru/core/) [file.inc](http://amxxmodx.ru/core/fileinc/)
Данная функция предназначена для записи блока данных в файл. Запись блока данных в file из массив данных data. blocks - размер массива.  
  
Инфо из **file.inc:**  
```
#define BLOCK_INT    4  
#define BLOCK_SHORT    2  
#define BLOCK_CHAR    1  
#define BLOCK_BYTE    1  
  
//The following functions work as such:  
// RAW - means the array you pass is a raw bytestream, for experts only  
// BLOCK - means you are passing in an array where each element will be written  
// NORMAL - means you are writing only one element  
// RAW and BLOCK return the number of blocks acted upon successfully  
// NORMAL returns 1 on success  
native fwrite_raw(file, const stream[], blocksize, mode);
```
  
  
**Синтаксис:**  

fwrite_blocks(file, const data[], blocks, mode) 
  

    * **file** - Идентификатор файла  

    * **const data[]** - Массив данных  

    * **blocks** - Размер массива  

    * **mode** - Режимы:  

      * BLOCK_INT - для записи любого числа или символов  

      * BLOCK_SHORT - для записи символов и значений в пределах -32767 - 32767  

      * BLOCK_CHAR - для записи символов и значений в пределах -127 - 127  

      * BLOCK_BYTE - похоже на BLOCK_CHAR  

  

  
  
Возвращает число успешно записанных блоков.  
  
**Тип функции:**  
Native  
  
**Пример:**  
--  
  
**Описание:**  
--
