# Оглавление модуля "The Fun Module"
[The Fun Module](http://amxxmodx.ru/fun/)
Цель модуля заключается в обеспечении набора функций "обмана", которыми не обеспечивает Ядро, функции данного модуля изменяют такие характеристики игрока как здоровье, броня и другие.  
  
**The Fun module** имеет один include:  

    * [fun.inc](http://amxxmodx.ru/fun/funinc/) (Дополнительные функции для модификации геймплея)  

**Функции:**  

    * [**get_client_listen**](http://amxxmodx.ru/fun/funinc/) проверяет слышит ли игрок другого игрока или нет  

    * [**get_user_footsteps**](http://amxxmodx.ru/fun/funinc/150-get_user_footsteps-funkciya-vozvraschaet-kak-peredvigaetsya-igrok-besshumno-ili-ego-shagi-slyshny.html) возвращает как передвигается игрок, бесшумно или его шаги слышны  

    * [**get_user_godmode**](http://amxxmodx.ru/fun/funinc/151-get_user_godmode-funkciya-vozraschaet-bessmertnyy-igrok-ili-inet.html) возращает бессмертный игрок или инет  

    * [**get_user_gravity**](http://amxxmodx.ru/fun/funinc/41-get_user_gravity-funkciya-vozvraschaet-gravitaciyu-igroka.html) возвращает гравитацию игрока  

    * [**get_user_hitzones**](http://amxxmodx.ru/fun/funinc/158-get_user_hitzones-funkciya-poluchaet-znachenie-zon-popadaniya-igroka.html) получает значение зон попадания игрока  

    * [**get_user_maxspeed**](http://amxxmodx.ru/fun/funinc/152-get_user_maxspeed-funkciya-vozvraschaet-maksimalnuyu-skorost-igroka.html) возвращает максимальную скорость игрока  

    * [**get_user_noclip**](http://amxxmodx.ru/fun/funinc/153-get_user_noclip-funkciya-poluchaet-vklyuchen-li-rezhim-noclip-u-igroka.html) получает включен ли режим noclip у игрока  

    * [**give_item**](http://amxxmodx.ru/fun/funinc/155-give_item-funkciya-vydaet-opredelennomu-igroku-oruzhiepredmety.html) выдает определенному игроку оружие/предметы  

    * [**set_client_listen**](http://amxxmodx.ru/fun/funinc/156-set_client_listen-funkciya-ustanavlivaet-kto-kogo-mozhet-slyshat.html) устанавливает кто кого может слышать  

    * [**set_user_armor**](http://amxxmodx.ru/fun/funinc/83-set_user_armor-funkciya-ustanavlivaet-kolichestvo-broni-igroku.html) устанавливает количество брони игроку  

    * [**set_user_footsteps**](http://amxxmodx.ru/fun/funinc/20-set_user_footsteps-besshumnye-shagi.html) устанавливает бесшумные шаги игроку  

    * [**set_user_frags**](http://amxxmodx.ru/fun/funinc/17-set_user_frags-funkciya-ustanovki-kolichestva-fragov-igroku.html) установки количества фрагов игроку  

    * [**set_user_godmode**](http://amxxmodx.ru/fun/funinc/18-set_user_godmode-rezhim-boga.html) устанавливает режим бога игроку  

    * [**set_user_gravity**](http://amxxmodx.ru/fun/funinc/21-set_user_gravity-funkciya-izmeneniya-gravitacii-igroka.html) изменения гравитации игрока  

    * [**set_user_health**](http://amxxmodx.ru/fun/funinc/19-set_user_health-funkciya-ustanavlivaet-zdorove-igroka.html) устанавливает здоровье игрока  

    * [**set_user_hitzones**](http://amxxmodx.ru/fun/funinc/157-set_user_hitzones-funkciya-zadaet-tochki-popadaniya-tulovischa-holostye-patrony.html) задает точки попадания туловища (холостые патроны)  

    * [**set_user_maxspeed**](http://amxxmodx.ru/fun/funinc/23-set_user_maxspeed-skorost-igroka.html) задает скорость игроку  

    * [**set_user_noclip**](http://amxxmodx.ru/fun/funinc/22-set_user_noclip.html)   

    * [**set_user_origin**](http://amxxmodx.ru/fun/funinc/77-set_user_origin.html) перемещает игрока в заданную точку  

    * [**set_user_rendering**](http://amxxmodx.ru/fun/funinc/24-set_user_rendering.html)  

    * [**spawn**](http://amxxmodx.ru/fun/funinc/154-spawn-funkciya-vozrazhdaet-igroka-respawn.html) возрождает игрока (respawn)  

    * [**strip_user_weapons**](http://amxxmodx.ru/fun/funinc/8-strip_user_weapons.html) Отбирает все оружие  

  
**У Fun модуля есть только несколько констант:**  

    * **Hitzone Constants:** - грубо говоря части тела( точки попаданий)  

      * HIT_GENERIC 0  

      * HIT_HEAD 1  

      * HIT_CHEST 2  

      * HIT_STOMACH 3  

      * HIT_LEFTARM 4  

      * HIT_RIGHTARM 5  

      * HIT_LEFTLEG 6  

      * HIT_RIGHTLEG 7  

  

    * **Render Constants:**  
```
enum {      
    kRenderNormal = 0,        /* src */  
    kRenderTransColor,        /* c*a+dest*(1-a) */  
    kRenderTransTexture,        /* src*a+dest*(1-a) */  
    kRenderGlow,            /* src*a+dest -- No Z buffer checks */  
    kRenderTransAlpha,        /* src*srca+dest*(1-srca) */  
    kRenderTransAdd,        /* src*a+dest */  
}
```
  

    * **FX Constants:**  
```
enum {      
    kRenderFxNone = 0,   
    kRenderFxPulseSlow,   
    kRenderFxPulseFast,   
    kRenderFxPulseSlowWide,   
    kRenderFxPulseFastWide,   
    kRenderFxFadeSlow,   
    kRenderFxFadeFast,   
    kRenderFxSolidSlow,   
    kRenderFxSolidFast,          
    kRenderFxStrobeSlow,   
    kRenderFxStrobeFast,   
    kRenderFxStrobeFaster,   
    kRenderFxFlickerSlow,   
    kRenderFxFlickerFast,  
    kRenderFxNoDissipation,  
    kRenderFxDistort,        /* Distort/scale/translate flicker */  
    kRenderFxHologram,        /* kRenderFxDistort + distance fade */  
    kRenderFxDeadPlayer,        /* kRenderAmt is the player index */  
    kRenderFxExplode,        /* Scale up really big! */  
    kRenderFxGlowShell,        /* Glowing Shell */  
    kRenderFxClampMinScale,        /* Keep this sprite from getting very small (SPRITES only!) */  
}
```
  

