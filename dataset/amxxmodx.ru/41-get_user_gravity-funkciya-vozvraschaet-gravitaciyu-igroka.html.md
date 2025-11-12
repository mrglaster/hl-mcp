# get_user_gravity Функция возвращает гравитацию игрока
[The Fun Module](http://amxxmodx.ru/fun/) [fun.inc](http://amxxmodx.ru/fun/funinc/)
**get_user_gravity** - Простенькая функция для получения гравитация игрока.  
  
Иноф из **fun.inc:**  
```
/* Returns users gravity. */  
native Float:get_user_gravity(index);
```
  
  
**Синтаксис:**  

Float: get_user_gravity ( index )
  
**index** - id игрока  
 _Получаемое число дробное_  
  
**Пример:**  
```
#include <amxmodx>  
#include <amxmisc>  
#include <fun>  
   
#define PLUGIN "Get user gravity"  
#define VERSION "1.0"  
#define AUTHOR "Admin"  
   
   
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
       
    register_clcmd("say /get-user-gravity","get_gravity")  
}  
public get_gravity(id){  
       
    new Float:user_gravity[32]  
    user_gravity[id] = get_user_gravity(id)   
    client_print(id,print_center,"You gravity is %.2f",user_gravity[id])  
    client_print(id,print_chat,"You gravity is %.2f",user_gravity[id])  
   
}
```
  
  
**Описание:**  
наша единственная команда **say /get-user-gravity** , вызовет функцию **get_gravity** , в которой мы получим гравитацию игрока и выведем ее в центр экрана, обратите внимание на вывод дробного числа **%.2f** f - значет что число дробное, а 2 сколько нулей будет после запятой.  
  
_Внимание!_ - функция возвращает не число которому равна гравитация игрока, а коэффициент от серверной, вот пример:  
Если на сервере гравтация 800 и функция вернула:  
а) 1 - то гравитация игрока 800  
б) 0.5 - гравитация 400  
в) 2 - гравитация 1600  
Если же вы хотите сразу получить число, то нужно сначала получить установленную на сервере гравитацию и потом умножить полученный нами коэффициент на гравитацию сервера.
