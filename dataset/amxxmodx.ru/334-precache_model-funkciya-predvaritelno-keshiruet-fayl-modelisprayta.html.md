# precache_model Функция предварительно кэширует файл модели,спрайта.
[Ядро AMXx](http://amxxmodx.ru/core/) [amxmodx.inc](http://amxxmodx.ru/core/amxmodxinc/)
Функция необходима для предварительного кеширвоания не стандартных фалов моделей, спрайтов, что бы игроки у которых нет этих файлов видели ту красоты которую вы создали.  
  
Инфо из **amxmodx.inc:**  
```
/* Precache model. Can be used only in plugin_precache() function.*/  
native precache_model(const name[]);
```
  
  
**Синтаксис:**  

precache_model(const name[])
  

    * **const name[]** - Имя файла с путем к нему (если не в корневой папке)  

  
  
**Тип функции:**  
Native  
  
**Описание:**  
Функция аналогичная функции **precache_sound** , пример и описание смотрите там.
