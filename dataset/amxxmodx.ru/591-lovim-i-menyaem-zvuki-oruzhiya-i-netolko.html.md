# Ловим и Меняем звуки (оружия и нетолько)
[Присланное](http://amxxmodx.ru/other/)
Всем привет и сегодня в этой статье мы будем ловить нужные нам звуки и заменять на нужные нам,способ очень лёгкий по сравнению с другими возможными,отлов звуков будет вестись через форвард **FM_EmitSound**  
  
Приведу пример кода и всё распишу в комментариях  
  
```
  
#include <amxmodx>  
#include <amxmisc>  
#include <fakemeta>  
  
#define PLUGIN "Sound Replace Plugin"  
#define VERSION "1.0"  
#define AUTHOR "True_Hacker"  
  
  
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
    register_forward(FM_EmitSound, "fw_emit_sound") // регестрируем форвард который будет работать как фильтр звуков  
}  
  
public plugin_precache()  
{  
    precache_sound("player/sprayer2.wav") // кэшируем звук на который будем менять  
}  
  
public fw_emit_sound(id,channel,const sound[])  
{  
    if(equal(sound,"player/sprayer.wav")) // проверяем,тот ли звук мы поймали  
    {  
        emit_sound(id,channel,"player/sprayer2.wav",1.0,1.0,0,100) // проигрываем нужный нам  
        return FMRES_SUPERCEDE;  
    }  
}  

```
  
  
Как видим ```
fw_emit_sound(id,channel,const sound[])
```
Принимает три параментра,**id** - ид игрока у которого проигрывается звук,**channel** - канал по каторому должен был проиграться старый звук,константа **sound** будет содержать в себе путь к звуку который проигрывается в данный момент  
  
В итоге что мы получили:  
был стандартный звук нанесения спрэя,мы перехватили его и заменили на sprayer2.wav и так можно делать с любым звуком в игре,или при желании можно вовсе его выключить ![smile](http://amxxmodx.ru/engine/data/emoticons/smile.gif)
