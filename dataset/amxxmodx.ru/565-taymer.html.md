# Таймер
[Присланное](http://amxxmodx.ru/other/)
```
  
#include <amxmodx>  
#include <hamsandwich>  
  
new szTime[33] // регистрация переменной времени  
  
public plugin_init()  
{  
 register_clcmd("say /time","show_timer") // Регистрируем нашу команду вызова Таймера  
}  
  
public show_timer(id)  
{  
 szTime[id] = 5 // szTime[id] ранее наша зарегистрированая переменная , 5 время в  
 //секундах  
 show_second_timer(id) // здесь вызываем наш таймер  
}  
  
public show_second_timer(id)  
{  
if(szTime[id] > 0) // Если время больше 0 то показываем сообшение   
{  
set_hudmessage(255, 0, 0, 0.28, 0.69, 0, 6.0, 12.0)  
show_hudmessage(id, "До вашего воскрешения осталось %d сек",szTime[id]) //сообщение  
szTime[id] -- // Отнимаем время от нашего таймера  
set_task(1.0,"show_second_timer",id,_,_,"b) // Время через которое будет -1 сек от нашего таймера  
}else{ // Если время истекло воскрешаем игрока  
ExecuteHamB(Ham_CS_RoundRespawn, id)   
}  

```
  
  
Вот собственно все спасибо за внимание !!!  
  
Дополнение от **igas**  
```
#include <amxmodx>  
#include <hamsandwich>  
   
new szTime[33] = 0    // регистрация массива времени  
   
public plugin_init()  
{  
    register_clcmd("say /time","show_timer")   // Регистрируем нашу команду вызова Таймера  
}  
    
public show_timer(id)  
{  
    if(task_exists(id))   // Проверка на выполнения Task, если выполняется Task  
    {  
        remove_task(id)   // Останавливаем его (Task)  
    }  
       
    szTime[id] = 15   // szTime[id] ранее наш зарегистрированный массив, 15 время в секундах  
    // Запускаем таймер  
    set_task(1.0, "show_second_timer", id, _, _, "b")   // Время через которое будет -1 сек от нашего таймера  
}  
    
public show_second_timer(id)  
{  
    // Если время больше или равна 1 то показываем сообщение (таймер исчезнет после 1 последней секунды, если 0, будет показана 0 секунда)  
    if(szTime[id] >= 1)  
    {  
        szTime[id] --   // Отнимаем время от нашего таймера  
        set_hudmessage(255, 0, 0, 0.28, 0.69, 0, 6.0, 12.0)   // Устанавливаем цвет, координаты, эффекты сообщения  
        show_hudmessage(id, "До вашего воскрешения осталось %d сек",szTime[id])   //сообщение  
           
    }  
    else   // Если время истекло   
    {   
        remove_task(id)   // Останавливаем (Task)  
        ExecuteHamB(Ham_CS_RoundRespawn, id)   // Воскрешаем игрока  
    }  
}
```
  
_Новость отредактировал**Admin** - 22-09-2013, 18:12_
Причина: Добавление от igas
