# Список pvPrivateData оффсетов OFFSET_*
[The Fakemeta Module](http://amxxmodx.ru/fakemeta/)
**pvPrivateData** - это свойство, описанное в структуре edict_s (см. HLSDK, файл edict.h). Содержит блок памяти, в котором находятся дополнительные свойства объекта, относящиеся к конкретному моду (mod-related). Доступ к нему осуществляется посредством модификации памяти - по смещению. Чтобы узнать структуру этого блока памяти, необходимы исходники мода. А так как у вас их нет и вряд ли будут (речь о CS/CZ), то информацию о типе и назначении групп ячеек памяти можно получить исследовательским методом (а-ля хакинг). Т.е. вы определяете для себя область данных, которую будете исследовать, запоминаете значения, потом выполняете действия, смотрите - изменилось ли что - и т.о. делаете вывод (если повезет) о назначении этого участка памяти.   
  
Т.к. это колоссальный и утомительный труд, то информация по ячейкам памяти бесценна. К сожалению, полученная информация не может со 100% гарантией распространяться на родственные моды (CS/CZ) и даже на различные версии одного и того же мода.   
  
Итак, что же содержится в pvPrivateData?   
  

Процитирую VEN'a: "Player's Money, BackPackAmmo, Defuse/Plant skill, Deaths, Weapon's Type, Ammo и многое-многое другое". Не путайте эти свойства со свойствами PEV структуры. Они друг друга дополняют. 
  
  
**Как работать с ними?**   
  
Для этого в fakemeta.inc есть следующие функции:   
```
get_pdata_<type> 
```
[](http://amxxmodx.ru/fakemeta/fakemetainc/358-get_pdata_int-funkciya-poluchaet-pvprivatedata-dannye-offset_.html)  
```
 set_pdata_<type> 
```
[](http://amxxmodx.ru/fakemeta/fakemetainc/359-get_pdata_int-funkciya-ustanavlivaet-znacheniya-pvprivatedata-dannym-offsetam.html)  
где  может быть int, float ,string.   
  
Т.к. вы напрямую работаете с памятью, то делать это надо очень и **очень акуратно** , особенно если используете set_pdata_string/get_pdata_string.  
  
Данные оффсеты касаются только игрока:  

75 - m_LastHitGroup   
76 - m_bitsDamageType   
83 - m_flNextAttack   
89 - m_bloodColor   
96 - random_seed   
122 - last switched trigger_camera (cbase)   
123 - fGametime of next trigger_camera view   
205 - iMenuCode   
209 - IsTerroristEscaped / IsVIPRescued (1<<0), IsPlayerVIP (1<<8)   
211 - fOriginX   
212 - fOriginY   
213 - fOriginZ   
219 - bIsPrimaryFireAllowed (note: disallow in prePlayerPostThink)   
232 - IsDefusing (1<<8)   
243 - m_flFlashLightTime   
244 - m_iFlashBattery   
245 - m_afButtonLast ?   
246 - m_afButtonPressed ?   
247 - m_afButtonReleased ?   
251 - m_flFallVelocity   
334 - m_lastDamageAmount   
338 - iGeiger   
345 - m_idrowndmg ?   
346 - m_idrownrestored ?   
347 - m_bitsHUDDamage ?   
356 - m_fLongJump   
359 - m_iClientHealth   
360 - m_iClientBattery   
363 - m_iFOV   
364 - m_iClientFOV   
368 - last gained primary (cbase)   
369 - last gained secondary (cbase)   
370 - last gained knife (cbase)   
371 - last gained grenade (cbase)   
372 - last gained c4 (cbase)   
373 - m_pActiveItem (cbase)   
374 - m_pClientActiveItem (cbase)   
375 - m_pLastItem (cbase)   
446 - iStatusValue1   
447 - iStatusValue2   
448 - iStatusValue3   
486 - m_flNextDecalTime   
500 - activity-related (kill 0, default 1, walk/duck 3, run 4, longjump 5, jump 6)   
509 - bAutoWepSwitch   
510 - setinfo _vgui_menus (1<<0), _ah (1<<8), uses_shield (1<<16), has_shield (1<<24)   
514 - fGametime flashed until ?   
515 - fGametime flashed at ?   
516 - fHoldTimeInSeconds of ScreenFade   
517 - fDurationInSeconds of ScreenFade   
518 - iAlpha of ScreenFade   
605 - fGametime of StatusBar 0%   
606 - fGametime of StatusBar 100%
  
  
**weaponbox**  

73 - iBPAmmo
  
  
**weapon_***  

41 - m_pPlayer (cbase)   
49 - m_iPrimaryAmmoType   
54 - m_fInReload
  
  
armoury_entity  

35 - iCount
  
[**Автор: slogic**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteG1vZHgudWNvei5ydS9mb3J1bS85LTY3LTE%3D)  
  
Список оффсетов которые я встречал в плагинах:  
```
OFFSET_PAINSHOCK = 108 // ConnorMcLeod  
OFFSET_CSTEAMS = 114  
OFFSET_CSMONEY = 115  
OFFSET_FLASHLIGHT_BATTERY = 244  
OFFSET_CSDEATHS = 444  
OFFSET_MODELINDEX = 491 // Orangutanz  
  
OFFSET_ACTIVE_ITEM = 373  
OFFSET_WEAPONOWNER = 41  
  
OFFSET_LINUX = 5 // offsets 5 higher in Linux builds  
OFFSET_LINUX_WEAPONS = 4 // weapon offsets are only 4 steps higher on Linux  
OFFSET_CLIPAMMO        51  
OFFSET_LINUX_WEAPONS    4  
OFFSET_LINUX            5  
EXTRAOFFSET_WEAPONS        4   
ACTUAL_EXTRA_OFFSET        20  
  
OFFSET_ARMORTYPE        112  
OFFSET_TEAM            114  
OFFSET_MONEY            115  
OFFSET_INTERNALMODEL        126  
OFFSET_AWP_AMMO            377   
OFFSET_SCOUT_AMMO        378  
OFFSET_PARA_AMMO        379  
OFFSET_FAMAS_AMMO        380  
OFFSET_M3_AMMO            381  
OFFSET_USP_AMMO            382  
OFFSET_FIVESEVEN_AMMO        383  
OFFSET_DEAGLE_AMMO        384  
OFFSET_P228_AMMO        385  
OFFSET_GLOCK_AMMO        386  
OFFSET_FLASHBANG_AMMO        387  
OFFSET_HEGRENADE_AMMO        388  
OFFSET_SMOKEGRENADE_AMMO    389  
OFFSET_C4_AMMO            390  
OFFSET_CSMONEY    115 //win  
OFFSET_CSMONEY    140 //lin  
OFFSET_LINUX    5  
OFFSET_TEAM 114 //win  
OFFSET_TEAM 139 //lin
```
  
  
Если вы знаете какие то другие оффсеты - пишите в комментариях - дополню статью.
