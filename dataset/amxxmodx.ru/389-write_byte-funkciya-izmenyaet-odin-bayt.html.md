# write_byte Функция изменяет один бит
[Ядро AMXx](http://amxxmodx.ru/core/) [messages.inc ](http://amxxmodx.ru/core/messagesinc/)
Функция write_byte используется только совместно с функцией [**message_begin**](http://amxxmodx.ru/core/messagesinc/312-message_begin-funkciya-geniriruet-klientskie-soobscheniya.html), для изменения значений одному биту в клиентском сообщении.  
  
Инфо из **messages.inc:**  
```
native write_byte(x);
```
  
  
**Синтаксис:**  

write_byte ( x )
  

    * **Х** - Переменная содержащая число или число  

  
  
**Тип функции:**  
Native  
  
**Пример:**  
```
  
...  
//Функция создающая спрайт  
public my_first_sprite(arg[0]){  
       
    //Получаем координаты для спрайта  
    new origin[3]  
    get_user_origin(arg[0],origin,0)  
    origin[1] += 100  
       
    //Говорим что хотим создать временный объект и показать одному игроку  
    message_begin(MSG_ONE,SVC_TEMPENTITY,origin,arg[0])  
    write_byte(TE_SPRITE)//говорим что хотим создать, в данном случае спрайт  
    write_coord(origin[0])//х - координата  
    write_coord(origin[1])//у - координата  
    write_coord(origin[2])//z - координата  
    write_short(sprite)// id спрайта  
    write_byte(5) //масштаб  
    write_byte(100)//яркость  
    message_end()  
       
}
```
  
  
**Описание:**  
Полный пример и описание смотрите в функции [**message_begin**](http://amxxmodx.ru/core/messagesinc/312-message_begin-funkciya-geniriruet-klientskie-soobscheniya.html)  
 _Новость отредактировал**Admin** - 31-03-2014, 18:46_
Причина: байт -> бит (Артист)
