# Модуль CSX
[The CSX Module](http://amxxmodx.ru/csx/)
Модуль Counter-Strike (CSX) был разработан SidLuke, изначально портированным из модуля более раннего модуля AMX Mod. У модуля CSX есть две основных части, native функции для Couter-Strike и статистические. Так же работающие для Condition-Zero  
  
**Две основные части модуля:**
    * [**csx.inc**](http://amxxmodx.ru/csx/csxinc/) (Counter-Strike and Condition-Zero natives)  

    * [**csstats.inc**](http://amxxmodx.ru/csx/csstatsinc/) (Counter-Strike and Condition-Zero statistical natives)  

  
  
**Функции csx.inc:**  
[**client_damage**](http://amxxmodx.ru/csx/csxinc/391-client_damage-funkciya-vyzyvaetsya-kogd-aodin-igrok-nanosit-uron-drugomu.html) вызывается когда один игрок наносит урон другому  
[**client_death**](http://amxxmodx.ru/csx/csxinc/393-client_death-funkciya-vyzyvaetsya-kogda-igrok-umiraet.html) вызывается когда игрок умирает  
grenade_throw  
[**bomb_planting**](http://amxxmodx.ru/csx/csxinc/91-bomb_planting-funkciya-vyzyvaetsya-v-moment-ustanovki-momby-ili-otlov-sobytiya-ustanovki-bomby.html) вызывается в момент установки бомбы или отлов события установки бомбы  
[**bomb_planted**](http://amxxmodx.ru/csx/csxinc/93-bomb_planted-funkciya-vyzyvaetsya-posle-ustanovki-bomby-ili-otlov-sobytiya-ustanovki-bomby.html) вызывается после установки бомбы или отлов события установки бомбы  
[**bomb_explode**](http://amxxmodx.ru/csx/csxinc/94-bomb_explode-funkciya-vyzyvaetsya-pri-vzryve-bomby-ili-otlov-sobytiya-vzryva-bomby.html) вызывается при взрыве бомбы или отлов события взрыва бомбы  
[**bomb_defusing**](http://amxxmodx.ru/csx/csxinc/95-bomb_defusing-funkciya-vyzyvaetsya-v-moment-razminirovaniya-bomby-ili-otlov-sobytiya-nachala-razminirovaniya-bomby.html) вызывается в момент разминирования бомбы или отлов события начала разминирования бомбы  
[**bomb_defused**](http://amxxmodx.ru/csx/csxinc/96-bomb_defused-funkciya-vyzyvaetsya-v-moment-razminirovaniya-bomby.html) вызывается в момент разминирования бомбы  
custom_weapon_dmg  
custom_weapon_shot  
xmod_is_melee_wpn  
xmod_get_wpnname  
xmod_get_wpnlogname  
xmod_get_maxweapons  
xmod_get_stats_size  
  
**Функции csstats.inc:**  
get_user_wstats  
get_user_wrstats  
[**get_user_stats**](http://amxxmodx.ru/csx/csstatsinc/98-get_user_stats-funkciya-poluchaet-statistiku-igroka-iz-statsdat.html) получает статистику игрока  
get_user_rstats  
get_user_vstats  
get_user_astats  
reset_user_wstats  
[**get_stats**](http://amxxmodx.ru/csx/csstatsinc/97-get_stats-funkciya-poluchaet-stroku-iz-standartnoy-statistiki.html) получает строку из стандартной статистики  
[**get_statsnum**](http://amxxmodx.ru/csx/csstatsinc/92-get_statsnum-funkciya-poluchaet-kolichestvo-igrokov-v-statitike.html) получает количество игроков в статитике  
get_user_stats2  
get_stats2
