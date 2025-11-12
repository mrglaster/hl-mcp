# cs_set_weapon_burst Функция устанавливает burst режим ( по три патрона)
[CStrike](http://amxxmodx.ru/cstrike/)
Не вижу особого смысла в использовании данной функции, так как она работает только для glock и famas.  
Но раз уж она есть, и мало ли вам понадобится, то пару слов о ней все же скажу.  
  
Инфо из **cstrike.inc:**  
```
/* If burstmode = 1, weapon will be changed to burst mode, 0 and non-burst mode (semiautomatic/automatic) will be activated.  
 * Only GLOCK and FAMAS can enter/leave burst mode.  
 */  
native cs_set_weapon_burst(index, burstmode = 1);
```
  
  
**Синтаксис:**  

cs_set_weapon_burst ( index, [ burstmode = 1 ] )
  

    * **index** - id игрока  

    * **[ burstmode = 1 ]** - 1 включить / 0 выключить  

  
  
**Тип функции:**  
Native  
  
**Описание:**  
Использование данной команды аналогично [**cs_set_weapon_silen**](http://amxxmodx.ru/cstrike/145-cs_set_weapon_silen-funkciya-odevaet-glushitel-na-oruzhie.html).  
По этому позволю себе не писать аналогичный пример.
