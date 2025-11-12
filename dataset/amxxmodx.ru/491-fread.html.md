# fread
[Ядро AMXx](http://amxxmodx.ru/core/) [file.inc](http://amxxmodx.ru/core/fileinc/)
Инфо из **file.inc:**  
```
//The following functions work as such:  
// RAW - means the array you pass is a raw bytestream, for experts only  
// BLOCK - means you are passing in an array where each element will be written  
// NORMAL - means you are writing only one element  
// RAW and BLOCK return the number of blocks acted upon successfully  
// NORMAL returns 1 on success  
  
native fread(file, &data, mode);
```
  
  
**Синтаксис:**  

fread(file, &data, mode)
  

    * **file** - идентификатор открытого файла  

    * **& data** -   

    * **mode** - тип обращения:  

      * ```
// RAW - means the array you pass is a raw bytestream, for experts only  
// BLOCK - means you are passing in an array where each element will be written  
// NORMAL - means you are writing only one element  
// RAW and BLOCK return the number of blocks acted upon successfully  
// NORMAL returns 1 on success
```
  

  

  
  
**Тип функции:**  
Native  
  
**Пример:**  
--  
  
**Описание:**  
--
