# Half-Life и Adrenaline Gamer форум


## [[TUT] Entity attaching (to unique model bone)](https://aghlru.ds-servers.com/forum/viewtopic.php?f=39&t=731)
Категории: [Туториал](https://aghlru.ds-servers.com/forum/search.php?keywords=%2B%D0%A2%D1%83%D1%82%D0%BE%D1%80%D0%B8%D0%B0%D0%BB&terms=all&fid\[\]=19&sc=1&sf=catonly&sr=topics)
Модератор: [KORD_12.7](https://aghlru.ds-servers.com/forum/memberlist.php?mode=viewprofile&u=67)
  
1) Открываем модель к которой хотите приаттачить энтитю  
2) Открываем вкладку "render"  
3) Ставим галочки напротив: Attachments + Bones  
4) Находим единственную красную точку - ориджин модели  
  
Тут возникает не большая не стыковка, если к примеру взять привязку класса beam, то pev_body - будет отвечать за искажение луча, если же взять точечный обьект к примеру env_sprite, то pev_body - будет отвечать за определение точки привязки (об этом следующий пункт)  
  
5) Находим желательную точку привязки - точки обозначены зеленым цветом  
6) Начинаем считать вектора(оранжевые линии) связывающие синие точки от ориджина модели до точки привязки, на примере ниже 11-13(т.к. 3 точки привязки подряд) таких векторов (Player), на 2м примере (Turret) 2 вариации 1) Можно привязать к дулу пулемета 2) К его крыше  
Вложение: [![faq_2.jpg](https://aghlru.ds-servers.com/forum/download/file.php?id=888&t=1)](https://aghlru.ds-servers.com/forum/download/file.php?id=888&mode=view)  
faq_2.jpg [ 141.45 КБ | Просмотров: 1053 ]   
  
7) Подставляем получившиеся значения в алгоритм  
set_pev(ent, pev_aiment, target) // target - индекс энтити для аттача (стартовой)  
set_pev(ent, pev_skin, target | (1 << X)) // Где Х - число векторов(смещений), можно получившееся значение (1 << X) перевести в hex, к примеру при 13 смещениях значение будет иметь вид - 0x2000  
  
При аттаче точечного обьекта нужно задать верный body  
set_pev(ent, pev_body, Y) // где Y - порядковый номер точки привязки (нумерация начинается с 1) относительно ориджина (у игрока последняя точка привязки при 13 векторах = 3)  
  
И в заключении пример привязки спрайта к рукам игрока  
**[▼](https://aghlru.ds-servers.com/forum/viewtopic.php?f=39&t=731) Код** **Код:** 
```
#include<amxmodx>  
#include<fakemeta_util>  
#include<hamsandwich>  
  
#define PLUGIN "Sprite_Test"  
#define AUTHOR "Turanga_Leela"  
#define VERSION "0.1"// 29.03.2012  
  
new g_client_orb[32]  
#define_Client_ent(%1) g_client_orb[%1-1]  
  
public plugin_precache()  
{  
   precache_model("sprites/flare3.spr")  
}  
  
public plugin_cfg()  
{  
   register_plugin(PLUGIN, VERSION, AUTHOR)  
RegisterHam(Ham_Spawn,"player","Client_Spawn_Post",1)  
}  
  
publicClient_Spawn_Post(id)  
{  
if(!_Client_ent(id)&& pev_valid(id))  
{  
static g_cache  
new ent  
  
if((g_cache ||(g_cache = engfunc(EngFunc_AllocString,"env_sprite")))&& pev_valid((ent = engfunc(EngFunc_CreateNamedEntity, g_cache))))  
{  
_Client_ent(id)= ent  
  
#define hex_Offset    0x1000// 1 << 12 - смещаем на кол-во пройденных векторов  
  
         engfunc(EngFunc_SetModel, ent,"sprites/flare3.spr")  
  
/*  
         * На примере класса [b]beam[/b], можно отметить что присвоение модели идет иным способом  
  
         * set_pev(beam, pev_model, "sprites/laserbeam.spr")  
         * set_pev(beam, pev_modelindex, g_beam_cache) // g_beam_cache = precache_model("sprites/laserbeam.spr")  
         */  
  
set_pev(ent, pev_body,2)// у beam - это искажение луча  
set_pev(ent, pev_movetype, MOVETYPE_FOLLOW)  
set_pev(ent, pev_aiment, id)  
set_pev(ent, pev_skin, id | hex_Offset)  
set_pev(ent, pev_scale,1.0)  
  
set_pev(ent, pev_solid, SOLID_NOT)  
         fm_set_rendering(ent, kRenderFxNone, random(256), random(256), random(256), kRenderTransAdd,128)  
         dllfunc(DLLFunc_Spawn, ent)  
}  
}  
}  

```
Хотелось бы так же продемонстрировать метод используемый в HLSDK, принцип его действия изменится лишь в том случае если мы решим изменить существующее значение. При создании же нового обьекта он совершенно не отличается от метода указанного выше. В чем явный смысл такого переприсвоения с запросом текущего статуса - лично мне на момент написания статьи не понятен, т.к. можно просто переназначить аттач ... а не извращаться, но время покажет, для чего собственно это делалось -_-  
**Код:** 
```
#define hex_Offset 0x2000// или (1 << _dec)  
#define _dec 13// колличество пройденных векторов - есть прямая зависимость - (1 << 13) / 0x2000  
#define _max 0x10000// или (1 << 16) или 65536 - значение соответствующие модели игрока, почему именно это значение не знаю, не смог найти зависимостей, мб это правило действительно для всех энтитей ... хз  
  
set_pev(ent, pev_skin,(target | hex_Offset)|((pev(target, pev_skin)&(_max - hex_Offset))<< _dec))  
  
/*  
Тестировал на hl_laser_beam - где применяется метод из HLSDK, заменил своим методом и ничего не изменилось - все прекрасно работает без запроса - pev_skin(target), мб он = 0, хз не проверял.   
  
Кстати именно в этом единственное отличие методов - при создании нового обьекта его "pev_skin" = 0, -> все манипуляции со скинами дадут "0" - что в свою очередь не изменить картины в целом :D  
  
set_pev(ent, pev_skin, (target | hex_Offset) | 0) // Нет эффекта  
*/  

```
  
PS  
Во время тестинга точечного env_beam при попытке привязки к статичной энтите (на типо "monster_turret", при привязке к игроку глюков не обнаружилось) возникал стабильный глюк. Примерно в процентном соотношении - 50/50 спрайт не аттачился к модельке, причину пока установить не удалось. Менял мув тайп модельке, менял movetype ent - follow/noclip, пробывал создавать с задержкой и менять класс env_beam - info_target, но улучшений не наблюдалось ... ![:\(](https://aghlru.ds-servers.com/forum/images/smilies/sad.gif)   
