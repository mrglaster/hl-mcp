# fread_raw Функция чтения блока данных в формате raw
[Ядро AMXx](http://amxxmodx.ru/core/) [file.inc](http://amxxmodx.ru/core/fileinc/)
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
native fread_raw(file, stream[], blocksize, blocks);  

```
  
  
**Синтаксис:**  

fread_raw(file, stream[], blocksize, blocks)
  

    * **file** - Идентификатор открытого файла  

    * **stream[]** - Массив для данных  

    * **blocksize** - Размер блоков  

    * **blocks** - Номера блоков??  

  
  
**Тип функции:**  
Native  
  
**Пример:**  
--  
  
**Описание:**  
--
