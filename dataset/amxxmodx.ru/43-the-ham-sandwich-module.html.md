# The Ham Sandwich Module
[Ham Sandwich](http://amxxmodx.ru/hamsandwich/)
Модуль **Ham Sandwich** , невероятно нужный, а иногда и незаменимый модуль. Он значительно упрощает отлов различных событий связанных с игровым миром Counter-Strike, в некоторых же случаях он просто незаменим, так как имеет функционал, которого нет в других модулях. Но если и есть - то эти методы будут очень сильно нагружать сервер, что не принесет удовольствия от игры, на сервере где установлен плагин через мерно нагружающий сервер.  
  
У модуля есть 2 инклюда включающие в себя функции и константы:  

    * [**hamsandwich.inc**](http://amxxmodx.ru/hamsandwich/hamsandwichinc/) - Содержит native функции   

    * [**ham_const.inc**](http://amxxmodx.ru/hamsandwich/ham_constinc/) - Содержит константы, связанные с собственными функциями  

  
  

## Функции Ham Sandwich 
[**HamHook:RegisterHam**](http://amxxmodx.ru/hamsandwich/hamsandwichinc/419-hamhookregisterham-funkciya-dlya-scepleniya-virualnyh-funkciy-i-obektov-otlov-sobytiy.html) для сцепления виртуальных функций и объектов по классу  
[**HamHook:RegisterHamFromEntity**](http://amxxmodx.ru/hamsandwich/hamsandwichinc/420-hamhookregisterhamfromentity-funkciya-dlya-scepleniya-virualnyh-funkciy-i-obektov-po-entityid-otlov-sobytiy.html) для сцепления виртуальных функций и объектов по EntityId  
[**DisableHamForward**](http://amxxmodx.ru/hamsandwich/hamsandwichinc/296-disablehamforward-funkciya-prekraschaet-rabotu-zaregistrirovannogo-ham-forvarda.html) прекращает работу зарегистрированного ham форварда  
[**EnableHamForward**](http://amxxmodx.ru/hamsandwich/hamsandwichinc/421-enablehamforward-funkciya-vozobnovlyaet-rabotu-ham-forvarda.html) возобновляет работу ham форварда.  
[**ExecuteHam**](http://amxxmodx.ru/hamsandwich/hamsandwichinc/278-executeham-vypolnyaet-virtualnuyu-funkciyu-na-igroke-obekte.html) выполняет виртуальную функцию на игроке (объекте)  
[**ExecuteHamB**](http://amxxmodx.ru/hamsandwich/hamsandwichinc/353-executehamb-vypolnyaet-virtualnuyu-funkciyu-na-igroke-obekte.html) выполняет виртуальную функцию на игроке  
[**GetHamReturnStatus**](http://amxxmodx.ru/hamsandwich/hamsandwichinc/422-gethamreturnstatus-funkciya-poluchaet-status-vozvrata-ispolnyaemogo-forvarda.html) получает статус возврата исполняемого форварда  
**GetHamReturnInteger**  
**GetHamReturnFloat**  
**GetHamReturnVector**  
**GetHamReturnEntity**  
**GetHamReturnString**  
**GetOrigHamReturnInteger**  
**GetOrigHamReturnFloat**  
**GetOrigHamReturnVector**  
**GetOrigHamReturnEntity**  
**GetOrigHamReturnString**  
**SetHamReturnInteger**  
**SetHamReturnFloat**  
**SetHamReturnVector**  
**SetHamReturnEntity**  
**SetHamReturnString**  
[**SetHamParamInteger**](http://amxxmodx.ru/hamsandwich/hamsandwichinc/390-sethamparaminteger-funkcya-izmenyaet-parametry-otlovlennyh-sobytiy-celoe-znachenie.html) изменяет параметры отловленных событий  
[**SetHamParamFloat**](http://amxxmodx.ru/hamsandwich/hamsandwichinc/295-sethamparamfloat-funkcya-izmenyaet-parametry-otlovlennyh-sobytiy-drobnye-znacheniya.html) изменяет параметры отловленных событий (дробные значения)  
**SetHamParamVector**  
**SetHamParamEntity**  
**SetHamParamString**  
**SetHamParamTraceResult**  
**bool:IsHamValid**  
**get_pdata_cbase**  
**set_pdata_cbase**  
**get_pdata_cbase_safe**  
**__fatal_ham_error**  
  

## Константы виртуальных функций
[**Ham_Spawn**](http://amxxmodx.ru/hamsandwich/ham_constinc/44-ham_spawn-sobytie-respauna-igroka.html) респаун игрока  
**Ham_Precache**  
**Ham_Keyvalue**  
**Ham_ObjectCaps**  
**Ham_Activate**  
**Ham_SetObjectCollisionBox**  
**Ham_Classify**  
**Ham_DeathNotice**  
**Ham_TraceAttack**  
[**Ham_TakeDamage**](http://amxxmodx.ru/hamsandwich/ham_constinc/45-ham_takedamage-sobytie-poluchenya-urona.html) при получении урона  
**Ham_TakeHealth**  
[**Ham_Killed**](http://amxxmodx.ru/hamsandwich/ham_constinc/47-ham_killed-otlov-sobytiya-ubiystva-igroka-obekta.html) отлов события убийства игрока (объекта)  
**Ham_BloodColor**  
**Ham_TraceBleed**  
**Ham_IsTriggered**  
**Ham_MyMonsterPointer**  
**Ham_MySquadMonsterPointer**  
**Ham_GetToggleState**  
**Ham_AddPoints**  
**Ham_AddPointsToTeam**  
**Ham_AddPlayerItem**  
[**Ham_RemovePlayerItem**](http://amxxmodx.ru/hamsandwich/ham_constinc/279-ham_removeplayeritem-udalyaet-predmet-iz-inventarya-igroka.html) удаляет предмет из инвентаря игрока.  
[**Ham_GiveAmmo**](http://amxxmodx.ru/hamsandwich/ham_constinc/613-ham_giveammo-dobavlyaet-boepripasy.html) Ham_GiveAmmo Добавляет боеприпасы  
**Ham_GetDelay**  
**Ham_IsMoving**  
**Ham_OverrideReset**  
**Ham_DamageDecal**  
**Ham_SetToggleState**  
**Ham_StartSneaking**  
**Ham_StopSneaking**  
**Ham_OnControls**  
**Ham_IsSneaking**  
**Ham_IsAlive**  
**Ham_IsBSPModel**  
**Ham_ReflectGauss**  
**Ham_HasTarget**  
**Ham_IsInWorld**  
[**Ham_IsPlayer**](http://amxxmodx.ru/hamsandwich/ham_constinc/614-ham_isplayer-proverka-na-igrok-li.html) Проверка на "игрок ли?"  
**Ham_IsNetClient**  
**Ham_TeamId**  
**Ham_GetNextTarget**  
**Ham_Think**  
[**Ham_Touch**](http://amxxmodx.ru/hamsandwich/ham_constinc/329-ham_touch-vyzyvaetsya-kogda-obekty-soprikasayutsya-kogda-igrok-kasaetsya-oruzhiya-ili-drugogo-predmeta.html) вызывается когда объекты соприкасаются  
[**Ham_Use**](http://amxxmodx.ru/hamsandwich/ham_constinc/277-ham_use-vyzyvaetsya-kogda-ispolzuetsya-kakoy-to-obekt-igrok-nazhal-na-knopku.html) вызывается когда используется какой то объект (игрок нажал на кнопку)  
**Ham_Blocked**  
**Ham_Respawn**  
**Ham_UpdateOwner**  
**Ham_FBecomeProne**  
**Ham_Center**  
**Ham_EyePosition**  
**Ham_EarPosition**  
**Ham_BodyTarget**  
**Ham_Illumination**  
**Ham_FVisible**  
**Ham_FVecVisible**  
[**Ham_Player_Jump**](http://amxxmodx.ru/hamsandwich/ham_constinc/395-ham_player_jump.html)  
[**Ham_Player_Duck**](http://amxxmodx.ru/hamsandwich/ham_constinc/394-ham_player_duck.html)  
**Ham_Player_PreThink**  
**Ham_Player_PostThink**  
**Ham_Player_GetGunPosition**  
**Ham_Player_ShouldFadeOnDeath**  
**Ham_Player_ImpulseCommands**  
**Ham_Player_UpdateClientData**  
[**Ham_Item_AddToPlayer**](http://amxxmodx.ru/hamsandwich/ham_constinc/427-ham_item_addtoplayer.html) вызывается при получении оружия игроком  
**Ham_Item_AddDuplicate**  
**Ham_Item_CanDeploy**  
**Ham_Item_Deploy**  
**Ham_Item_CanHolster**  
**Ham_Item_Holster**  
**Ham_Item_UpdateItemInfo**  
**Ham_Item_PreFrame**  
**Ham_Item_PostFrame**  
**Ham_Item_Drop**  
**Ham_Item_Kill**  
**Ham_Item_AttachToPlayer**  
**Ham_Item_PrimaryAmmoIndex**  
**Ham_Item_SecondaryAmmoIndex**  
**Ham_Item_UpdateClientData**  
**Ham_Item_GetWeaponPtr**  
**Ham_Item_ItemSlot**  
**Ham_Weapon_ExtractAmmo**  
**Ham_Weapon_ExtractClipAmmo**  
**Ham_Weapon_AddWeapon**  
**Ham_Weapon_PlayEmptySound**  
**Ham_Weapon_ResetEmptySound**  
**Ham_Weapon_SendWeaponAnim**  
**Ham_Weapon_IsUsable**  
[**Ham_Weapon_PrimaryAttack**](http://amxxmodx.ru/hamsandwich/ham_constinc/324-ham_weapon_primaryattack-vyzyvaetsya-pri-atake-osnovnym-opredelennym-oruzhiem.html) вызывается при основной атаке определенным оружием  
[**Ham_Weapon_SecondaryAttack**](http://amxxmodx.ru/hamsandwich/ham_constinc/325-ham_weapon_secondaryattack-vyzyvaetsya-pri-alternativnoy-atake-opredelennym-oruzhiem.html) вызывается при альтернативной атаке определенным оружием  
[**Ham_Weapon_Reload**](http://amxxmodx.ru/hamsandwich/ham_constinc/281-ham_weapon_reload.html) вызывается каждый раз когда перезаряжается оружие.  
**Ham_Weapon_WeaponIdle**  
[**Ham_Weapon_RetireWeapon**](http://amxxmodx.ru/hamsandwich/ham_constinc/285-ham_weapon_retireweapon-pereklyuchaet-na-sleduyuschie-oruzhie-sleduyuschee-luchshee-oruzhie.html) переключает на следующие оружие (следующее лучшее оружие)  
**Ham_Weapon_ShouldWeaponIdle**  
**Ham_Weapon_UseDecrement**  
**Ham_CS_Restart**  
**Ham_CS_RoundRespawn**  
**Ham_CS_Item_CanDrop**  
**Ham_CS_Item_GetMaxSpeed**  
  
**Ham Return Types** - Возвращаемые константы  
```
#define HAM_IGNORED        1    /**< Calls target function, returns normal value */  
#define HAM_HANDLED        2    /**< Tells the module you did something, still calls target function and returns normal value */  
#define HAM_OVERRIDE    3    /**< Still calls the target function, but returns whatever is set with SetHamReturn*() */  
#define HAM_SUPERCEDE    4    /**< Block the target call, and use your return value (if applicable) (Set with SetHamReturn*()) */
```
  
  
**Ham Errors Types**  
```
enum HamError  
{  
    HAM_OK = 0,  
      
    HAM_INVALID_FUNC,            // The function is not valid  
    HAM_FUNC_NOT_CONFIGURED,    // This function is not configured in hamdata.ini  
      
    HAM_ERR_END  
};
```
  
  
**Список объектов:**  
[![The Ham Sandwich Module](http://amxxmodx.ru/uploads/posts/2012-10/thumbs/1350152009_1331813087_entity.png)](http://amxxmodx.ru/uploads/posts/2012-10/1350152009_1331813087_entity.png)
