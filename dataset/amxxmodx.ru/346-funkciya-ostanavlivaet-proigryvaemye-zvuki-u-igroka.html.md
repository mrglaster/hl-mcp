# StopSound Функция останавливает проигрываемые звуки у игрока
[Полезные функции Amx Mod X](http://amxxmodx.ru/poleznye_funkcii/)
За последнее время несколько раз слышал вопрос о том как заблокировать или остановить звуки, ответ нашелся на форуме, что бы функция не затерялась выкладываю ее сдесь.  
  
**Исходный код функции:**  
```
#define STOP_SOUND_WAV  0  
#define STOP_SOUND_MP3  1  
#define STOP_SOUND_ALL  2  
   
stock StopSound(pId, iType = STOP_SOUND_ALL)  
{  
        switch (iType)  
        {  
                case STOP_SOUND_WAV: client_cmd(pId, "stopsound");  
                case STOP_SOUND_MP3: client_cmd(pId, "mp3 stop");  
                case STOP_SOUND_ALL: client_cmd(pId, "stopsound;mp3 stop");  
        }  
          
        return 1;  
  
}
```
Автор:[**PRoSToTeM@**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteC14LnJ1L3ZpZXd0b3BpYy5waHA%2FcD0zOTQ1MSNwMzk0NTE%3D)  
  
**Синтаксис:**  

StopSound(pId, iType = STOP_SOUND_ALL)
  

    * **pId** - id игрока  

    * **iType = STOP_SOUND_ALL** - какой тип звуков останавливать:```
#define STOP_SOUND_WAV  0  
#define STOP_SOUND_MP3  1  
#define STOP_SOUND_ALL  2
```
  

  
  
**Тип функции:**  
stock  
  
**Пример:**  
```
#include <amxmodx>  
#include <amxmisc>  
   
#define PLUGIN "[stock function] Stop"  
#define VERSION "1.0"  
#define AUTHOR "Admin"  
  
#define STOP_SOUND_WAV  0  
#define STOP_SOUND_MP3  1  
#define STOP_SOUND_ALL  2  
   
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
    //Все три события вызывают одну функцию stop_sd  
    register_event("SendAudio", "stop_sd", "a", "2&%!MRAD_terwin")  
    register_event("SendAudio", "stop_sd", "a", "2&%!MRAD_ctwin")   
    register_event("SendAudio", "stop_sd", "a", "2&%!MRAD_rounddraw")   
}  
  
public stop_sd(){  
      
    new Players[32]   
    new playerCount, i, id   
    get_players(Players, playerCount, "ch")   
      
    for (i=0; i<playerCount; i++) {  
        id = Players[i]  
        //Вызов функции блокировки звука  
        StopSound(id,2)  
    }  
      
}  
stock StopSound(pId, iType = STOP_SOUND_ALL)  
{  
        switch (iType)  
        {  
                case STOP_SOUND_WAV: client_cmd(pId, "stopsound");  
                case STOP_SOUND_MP3: client_cmd(pId, "mp3 stop");  
                case STOP_SOUND_ALL: client_cmd(pId, "stopsound;mp3 stop");  
        }  
          
        return 1;  
}
```
  
  
**Описание:**  
Приведенный пример блокирует звуки при победе контров, терроров и ничьей.  
Не забывайте что в отлове этих событий нет id игроков и по этому приходится применять цикл
