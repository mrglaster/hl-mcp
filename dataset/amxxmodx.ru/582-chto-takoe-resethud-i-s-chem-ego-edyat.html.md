# Что такое ResetHUD и с чем его едят
[Присланное](http://amxxmodx.ru/other/)
В этом уроке я хочу рассказать что такое на самом деле ResetHUD  
Как все уже знают ResetHUD это событие которое происходит при начале/старте раунда как многие думали,я же отвечу что это не так,для начала я расскажу вам что такое HUD - худ это не 1 и не 2 обьекта HUD это целая графическая система,а именно,я лучше приведу пример на моем скриншоте  

[![Что такое ResetHUD и с чем его едят](http://amxxmodx.ru/uploads/posts/2014-03/thumbs/1394352779_image.png)](http://amxxmodx.ru/uploads/posts/2014-03/1394352779_image.png)
  
,на скриншоте я отчетливо показал что HUD это те же самые деньги,HP,AP,Радар,всякие иконки закупки,фанарика и прочее прочее прочее,это всё вместе называют HUD,так вот теперь когда вы знаете что такое HUD я расскажу про само событие ResetHUD - событие которое вызывается когда игрок зайдя на сервер выбирает команду,он возраждается,и у него появляется HUD,теперь я разберу ошибки многих скриптеров и скажу вам что стоит делать с ResetHUD а что нет,смотрим код  
  
```
  
#include <amxmodx>  
#include <amxmisc>  
#unclude <cstrike>  
#include <fun>  
#include <engine>  
#include <hamsandwich>  
#include <fakemeta>  
  
#define PLUGIN "ResetHUD test"  
#define VERSION "1.0"  
#define AUTHOR "True_Hacker"  
  
  
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
    register_event("ResetHUD","hud_show","be","1=1")  
}  
  
public hud_show(id)  
{  
    set_user_health(id, 200)  
    set_user_armor(id, 200)  
}  

```
  
  
Вот она,та самая ошибка всех скриптеров,после появления HUD у игрока скриптеры не осознавая этого загружают HUD под завязку и тем самым может упасть сервер,или клиент у игрока,а теперь пора вам рассказать как засунуть чтото в ResetHUD и чтобы это не нагружало сервер! смотрим код  
```
  
#include <amxmodx>  
#include <amxmisc>  
#include <cstrike>  
#include <fun>  
#include <engine>  
#include <hamsandwich>  
#include <fakemeta>  
  
#define PLUGIN "ResetHUD test"  
#define VERSION "1.0"  
#define AUTHOR "True_Hacker"  
  
  
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
    register_event("ResetHUD","hud_show","be","1=1")  
}  
  
public hud_show(id)  
{  
    set_task(3.0,"armor_and_hp",1,_,_,_,1)  
}  
  
public armor_and_hp(id)  
{  
    set_user_health(id, 200)  
    set_user_armor(id, 200)  
}  

```
  
  
Да,да ! тот самый set_task,благодаря ему сервер не будет нагружаться,просто ставим задержку во времени и всё,спасибо за внимание надеюсь статью не зря писал,не забываем говорить спасибо ![fellow](http://amxxmodx.ru/engine/data/emoticons/fellow.gif)  
_Новость отредактировал**Admin** - 8-03-2014, 21:24_
Причина: Коллеги, давайте расскажем автору о его ошибках в комментариях.
