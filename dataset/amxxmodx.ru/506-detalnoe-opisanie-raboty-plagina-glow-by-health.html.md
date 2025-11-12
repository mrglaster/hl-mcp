# Детальное описание работы плагина Glow by Health
[Готовые скрипты](http://amxxmodx.ru/scripts/)
В этой статье рассказано как работают разные функции на примере плагина **Glow by Health(** Изменяет подсветку игрока в зависимости от здоровья).Скриптерам,которые уже знают азы программирования думаю будет не интересно.  
**И так** ,вот код плагина о котором шла речь.  
```
#include <amxmod>   
#include <fun>  
  
public plugin_init(){   
  register_plugin("[http://amxxmodx.ru]Glow by Health","1.1","Freecode")   
  register_event("Damage","event_damage","b")   
  register_event("ResetHUD","spawn","be","1=1")    
  register_cvar("amx_healthglow","1")   
}   
  
public spawn(id){   
  if (get_cvar_num("amx_healthglow")!=1) return PLUGIN_HANDLED   
  
  new health = get_user_health(id)   
  new Float:Red = ((1.0 - (float(health) / 100.0)) * 255.0)   
  new Float:Green = ((float(health) / 100.0) * 255.0)   
  set_user_rendering(0, kRenderFxGlowShell,0,255,0, kRenderNormal, 40)   
  set_user_rendering(id, kRenderFxGlowShell, floatround(Red), floatround(Green), 0, kRenderNormal, 40)    
  return PLUGIN_HANDLED   
}   
  
  
public event_damage(id){   
  if (get_cvar_num("amx_healthglow")!=1) return PLUGIN_HANDLED  
  new health = get_user_health(id)   
  new Float:Red = ((1.0 - (float(health) / 100.0)) * 255.0)   
  new Float:Green = ((float(health) / 100.0) * 255.0)   
  set_user_rendering(id, kRenderFxGlowShell, floatround(Red), floatround(Green), 0, kRenderNormal, 40)  
  return PLUGIN_HANDLED   
}   
  

```
  
Теперь подробно о каждом кусочке плагина:  
Функция **plugin_init()  
**  
**1.**```
register_plugin("[http://amxxmodx.ru]Glow by Health","1.1","Freecode") 
```
  
Указывает Название,Версию,Автора данного плагина.  
**2.**```
register_event("Damage","event_damage","b")
```
  
Регистрирует событие получения\нанесения урона  
**3.**```
register_event("ResetHUD","spawn","be","1=1")
```
  
Регистрирует событие спавна игрока.   
**4.**```
register_cvar("amx_healthglow","1") 
```
  
Регистрирует Квар.  
О этих функциях подробно можете почитать на данном сайте.  
Функция **spawn(id)**  
**1.**```
  if (get_cvar_num("amx_healthglow")!=1) return PLUGIN_HANDLED 
```
  
Проверка на активацию квара.Если квар **amx_healthglow** не равен 1,то последующий код не активируем.  
**2.**```
  new health = get_user_health(id)   
  new Float:Red = ((1.0 - (float(health) / 100.0)) * 255.0)   
  new Float:Green = ((float(health) / 100.0) * 255.0) 
```
  
Переменной health присваиваем жизни игрока.  
Далее,переменной **Red** и **Green** устанавливаем значения цвета в зависимости от того,сколько у игрока **HP**.  
**3.**```
  set_user_rendering(0, kRenderFxGlowShell,0,255,0, kRenderNormal, 40)
```
  
Честно говоря не вижу смысла в этой строке,она устанавливает всем игрокам зеленое свечение.  
**4.**```
  set_user_rendering(id, kRenderFxGlowShell, floatround(Red), floatround(Green), 0, kRenderNormal, 40)  
```
  
А вот тут уже устанавливаем свечение в соответствии с жизнями игрока.  
**5.**```
  return PLUGIN_HANDLED 
```
  
Что-бы компилятор не ругался,**возвращаем PLUGIN_HANDLED**  
В функции **event_damage(id)** код аналогичен,думаю нет смысла его описывать.  
**Описание:**  
При нанесении урона, проверяется квар,получается здоровье игрока,генерируется случайный цвет Red,green и устанавливается свечение.  
На этом мое небольшое описание плагина заканчиваю.  
Если вам была полезна статья,пишите в комментариях,буду писать еще.  
Если есть вопросы тоже просьба писать в комментарии.
