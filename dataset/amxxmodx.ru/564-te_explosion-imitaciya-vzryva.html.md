# TE_EXPLOSION - Имитация взрыва
[Ядро AMXx](http://amxxmodx.ru/core/) [message_const.inc](http://amxxmodx.ru/core/message_constinc/)
**TE_EXPLOSION** - Это сообщение поможет вам создать взрыв.  
  
```
#define    TE_EXPLOSION                3        // Additive sprite, 2 dynamic lights, flickering particles, explosion sound, move vertically 8 pps  
// write_byte(TE_EXPLOSION)  
// write_coord(position.x)  
// write_coord(position.y)  
// write_coord(position.z)  
// write_short(sprite index)  
// write_byte(scale in 0.1's)  
// write_byte(framerate)  
// write_byte(flags)  
//  
// The Explosion effect has some flags to control performance/aesthetic features:  
#define TE_EXPLFLAG_NONE            0        // All flags clear makes default Half-Life explosion  
#define TE_EXPLFLAG_NOADDITIVE      1        // Sprite will be drawn opaque (ensure that the sprite you send is a non-additive sprite)  
#define TE_EXPLFLAG_NODLIGHTS       2        // Do not render dynamic lights  
#define TE_EXPLFLAG_NOSOUND         4        // Do not play client explosion sound  
#define TE_EXPLFLAG_NOPARTICLES     8        // Do not draw particles
```
  
  
**Синтаксис:**  
Для того что бы создать сообщения нужно объявить по началу message_begin, а по окончанию message_end и между ними вставить данные.  
  
**Пример:**  
```
/*  
    #define TE_EXPLFLAG_NONE            0        // Все Флаги по умолчанию  
    #define TE_EXPLFLAG_NOADDITIVE      1        // Спрайт будет не прозрачным(указывается при создании спрайта)  
    #define TE_EXPLFLAG_NODLIGHTS       2        // Не создовать подсветку   
    #define TE_EXPLFLAG_NOSOUND         4        // Не проигрывать звук взрыва  
    #define TE_EXPLFLAG_NOPARTICLES     8        // Не создовать частиц  
*/  
  
#include <amxmodx>  
#include <engine>  
  
#pragma semicolon            1  
#pragma tabsize             0  
  
#define PLUGIN "[MSG][SVC_TEMPENTITY] -> TE_EXPLOSION"  
#define VERSION "0.1"  
#define AUTHOR "Mon[str]"  
  
  
new _:g_iSpiteExlplosion;  
  
new _:g_cvar_ExplScall;  
new _:g_cvar_ExplSpeed;  
new _:g_cvar_ExplFlag;  
  
  
public plugin_precache()  
{  
    /* Функция precache_model возвращает индекс который нам нужен */  
    g_iSpiteExlplosion = precache_model("sprites/dexplo.spr");  
}  
  
public plugin_init()   
{  
    register_plugin(PLUGIN, VERSION, AUTHOR);  
      
    /* Регистрируем саму команду вызова сообщения */  
    register_concmd("Explosion", "_Explosion");  
      
    /* Регистрируем и записываем в переменные квары */  
    g_cvar_ExplScall = register_cvar("[TE_EXPLOSION] -> Cvars -> Scall", "10");  
    g_cvar_ExplSpeed = register_cvar("[TE_EXPLOSION] -> Cvars -> Speed", "10");  
    g_cvar_ExplFlag = register_cvar("[TE_EXPLOSION] -> Cvars -> Flag", "0");  
      
      
    /* Приглушаем свет */  
    set_lights("c");  
}  
  
public _Explosion(id)  
{  
    new _:iAimOrigin[3];  
      
    /* Берем аим координаты */  
    get_user_origin(id, iAimOrigin, 3);  
      
    /* Немного поднимаем координату вверх */  
    iAimOrigin[2] += 25.0;  
      
    /* Само сообщение */  
    message_begin(MSG_BROADCAST, SVC_TEMPENTITY);     // Начало  
      
        write_byte(TE_EXPLOSION);             // Индекс сообщения (message_const.inc)  
      
        /* Координаты */  
        write_coord(iAimOrigin[0]);             // x  
        write_coord(iAimOrigin[1]);            // y  
        write_coord(iAimOrigin[2]);            // z  
              
        write_short(g_iSpiteExlplosion);        // Тот самый индекс  
          
        write_byte(get_pcvar_num(g_cvar_ExplScall));    // Размер спрайта указывать в десятых(0.1)  
        write_byte(get_pcvar_num(g_cvar_ExplSpeed));    // Скорость проигрывания анимации  
        write_byte(get_pcvar_num(g_cvar_ExplFlag));    // Флаги  
      
    message_end();                     // Конец  
      
    return PLUGIN_HANDLED;  
}
```
  
  
**Видео:**  

