# Новая система меню AMXX и все ее функции.
[Ядро AMXx](http://amxxmodx.ru/core/) [amxmodx.inc](http://amxxmodx.ru/core/amxmodxinc/) [newmenus.inc](http://amxxmodx.ru/core/amxmodxinc/newmenusinc/)
В большинстве случаев первым что хочется сделать новичку сриптеру это игровое меню, так как это очень наглядно. С помощью новой системы меню можно создавать очень гибкую систему различных менюшек, главное разобраться с небольшим количеством функций и обладать логическим мышлением, что бы придумывать собственные алгоритмы работы плагинов использую данный набор функций.  
  
**Парочка советов:**  

    1. Если ваше меню не динамическое (пункты меню не меняются при каждом открытии) то его лучше создавать глобальным (не пересоздавать каждый раз при открытии, это сэкономит ресурсы сервера)  

    2. Если в создаваемом меню нет пунктов - оно не будет показано  

    3. Что бы закрыть меню( убрать его с экрана игрока ) воспользуйтесь следующей функцией:  
```
show_menu(id, 0, "^n", 1)
```
( показ пустого меню старой системой )  

    4. Если необходимо выровнять текст в меню по правому краю, то используйте \R.  

  
  
**Функции новой системы меню:**
    * [**menu_create**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2NvcmUvYW14bW9keGluYy9uZXdtZW51c2luYy8yMzEtbWVudV9jcmVhdGUtZnVua2NpeWEtc296ZGFuaXlhLW5vdm9nby1tZW55dS5odG1s) - создает новое меню  

    * [**menu_makecallback**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2NvcmUvYW14bW9keGluYy9uZXdtZW51c2luYy8yMzMtbWVudV9tYWtlY2FsbGJhY2stZnVua2NpeWEtc296ZGFldC1vYnJhYm90Y2hpay1vYnJhdG5vZ28tdnl6b3ZhLXB1bmt0YS1tZW55dS5odG1s) - создает функцию обработчик обратного вызова пункта меню ( сделать пункт меню не активным )  

    * [**menu_additem**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2NvcmUvYW14bW9keGluYy9uZXdtZW51c2luYy8yMzItbWVudV9hZGRpdGVtLWZ1bmtjaXlhLWRvYmF2bHlhZXQtcHVua3Qtdi1tZW55dS5odG1s) - добавляет пункт в меню  

    * [**menu_pages**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2NvcmUvYW14bW9keGluYy9uZXdtZW51c2luYy8yNjEtbWVudV9wYWdlcy1mdW5rY2l5YS1wb2x1Y2hhZXQta29saWNoZXN0dm8tc3RyYW5pYy12LW1lbnl1Lmh0bWw%3D) - получает количество страниц в меню  

    * [**menu_items**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2NvcmUvYW14bW9keGluYy9uZXdtZW51c2luYy8yNjItbWVudV9pdGVtcy1mdW5rY2l5YS1wb2x1Y2hhZXQta29saWNoZXN0dm8tZWxlbWVudG92LW1lbnl1Lmh0bWw%3D) - получает количество элементов меню  

    * [**menu_display**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2NvcmUvYW14bW9keGluYy9uZXdtZW51c2luYy8yMzQtbWVudV9kaXNwbGF5LWZ1bmtjaXlhLXBva2F6eXZhZXQtbWVueXUtaWdyb2t1Lmh0bWw%3D) - показывает меню игроку  

    * [**menu_find_id**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2NvcmUvYW14bW9keGluYy9uZXdtZW51c2luYy8zMTctbWVudV9maW5kX2lkLWZ1bmtjaXlhLW5haG9kaXQtaWQtcHVua3RhLWl6LW1lbnl1LXBvLXVrYXphbml5dS1zdHJhbmljeS1pLW5vbWVyYS5odG1s) - находит id пункта из меню по указанию страницы и номера.  

    * [**menu_item_getinfo**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2NvcmUvYW14bW9keGluYy9uZXdtZW51c2luYy8zMTgtbWVudV9pdGVtX2dldGluZm8tZnVua2NpeWEtcG9sdWNoYWV0LWRhbm55ZS1vLXZ5YnJhbm5vbS1wdW5rdGUtbWVueXUuaHRtbA%3D%3D) - получает данные о выбранном пункте меню  

    * [**menu_item_setname**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2NvcmUvYW14bW9keGluYy9uZXdtZW51c2luYy8yNTUtbWVudV9pdGVtX3NldG5hbWUtZnVua2NpeWEtaXptZW55YWV0LW90b2JyYXpoYWVtb2UtaW15YS1wdW5rdGEtdi1tZW55dS5odG1s) - изменяет отображаемое имя пункта в меню.  

    * **menu_item_setcmd** -  

    * [**menu_item_setcall**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2NvcmUvYW14bW9keGluYy9uZXdtZW51c2luYy8yNjMtbWVudV9pdGVtX3NldGNhbGwtZnVua2NpeWEtaXptZW55YWV0LWNhbGxiYWNrLWZ1bmtjaXl1LWstcHVua3R1LW1lbnl1Lmh0bWw%3D) - изменяет callback функцию к пункту меню  

    * [**menu_destroy**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2NvcmUvYW14bW9keGluYy9uZXdtZW51c2luYy8yNTYtbWVudV9kZXN0cm95LWZ1bmtjaXlhLXVuaWNodG96aGFldC1yYW5lZS1zb3pkYW5ub2UtbWVueXUuaHRtbA%3D%3D) - уничтожает ранее созданное меню  

    * [**player_menu_info**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2NvcmUvYW14bW9keGluYy9uZXdtZW51c2luYy8yNTQtcGxheWVyX21lbnVfaW5mby1mdW5rY2l5YS1wcnZvZXJ5YWV0LXZpZGV0LWxpLWlncm9rLW1lbnl1LWlsaS1uZXQuaHRtbA%3D%3D) - проверяет видит ли игрок меню или нет.  

    * [**menu_addblank**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2NvcmUvYW14bW9keGluYy9uZXdtZW51c2luYy8yNDYtbWVudV9hZGRibGFuay1mdW5rY2l5YS1kb2Jhdmx5YWV0LXB1c3R1eXUtc3Ryb2t1LXYtbWVueXUuaHRtbA%3D%3D) - добавляет пустую строку в меню  

    * [**menu_addtext**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2NvcmUvYW14bW9keGluYy9uZXdtZW51c2luYy8yNDctbWVudV9hZGR0ZXh0LWZ1bmtjaXlhLWRvYmF2bHlhZXQtdGVrc3QtbWV6aGR1LXB1bmt0YW1pLW1lbnl1Lmh0bWw%3D) - добавляет текст между пунктами меню  

    * [**menu_setprop**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2NvcmUvYW14bW9keGluYy9uZXdtZW51c2luYy8yNTItbWVudV9zZXRwcm9wLWZ1bmtjaXlhLXVzdGFuYXZsaXZhZXQtc3ZveXN0dmEtbWVueXUuaHRtbA%3D%3D) - устанавливает свойства меню  

    * [**menu_cancel**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2NvcmUvYW14bW9keGluYy9uZXdtZW51c2luYy8yNTMtbWVudV9jYW5jZWwtZnVua2NpeWEtb3RtZW55YWV0LW1lbnl1LWRseWEtcG9sem92YXRlbHlhLXZ5YmlyYWV0LWV4aXQtbmUtdnlrbHl1Y2hheWEtbWVueXUuaHRtbA%3D%3D) - отменяет меню для пользователя (выбирает exit не выключая меню)  

    * Бонус:[**Оформление и свойства меню ( кнопки выход/вход, цета и т.д.)**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2NvcmUvYW14bW9keGluYy9uZXdtZW51c2luYy8yODgtc3ZveXN0dmEtaS1vZm9ybWxlbmllLW1lbnl1a2FrLWl6bWVudC1jdmV0LW1lbnl1LWl6bWVuaXQta25vcGtpLWV4aXQtbmEtdnlob2QtaS1kcnVnb2UuaHRtbA%3D%3D)  

  
  
**Еще одна маленькая подсказка:**  
Не забывайте о том, что игроку все равно дважды или трижды было пересоздано меню, он их не отличит.Зато вы этим можете воспользоваться ( например сделать таймер в меню )
