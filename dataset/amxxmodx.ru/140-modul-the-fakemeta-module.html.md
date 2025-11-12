# Модуль Fakemeta
[The Fakemeta Module](http://amxxmodx.ru/fakemeta/)
Модуль **Fakemeta** - это мощная альтернатива модулю Engine. Он позволяет взаимодействовать почти со всем движком **HL** , вызывая функции DLL ,Engine функции,создание функций вызываемых при определенных события и другие возможности. Данный модуль может получить любые данные о игроке.  
  
У модуля есть 3 инклюда включающие в себя функции и константы для получения/изменения любых данных о игроке.  

    * [**fakemeta.inc**](http://amxxmodx.ru/fakemeta/fakemetainc/) Основные функции модуля  

    * [**fakemeta_const.inc**](http://amxxmodx.ru/fakemeta/fakemeta_constinc/) Константы ( работа с константами)  

    * [**fakemeta_stocks.inc**](http://amxxmodx.ru/fakemeta/fakemeta_stocksinc/) Stock функции модуля  

    * [**fakemeta_util.inc**](http://amxxmodx.ru/fakemeta/fakemeta_utilinc/) Бонус, дополнительные сток функции на основе модуля Fakemeta  

Инклюд fakemeta_const.inc не содержит функций, он содержит только константы для работы с модулем.  
Обратите внимание, что модуль работает с самим движком и если вы допустите ошибку, то сервер может "упасть"  
Будьте предельно внимательны и аккуратны при работе с данным модулем.  
  

## Функции **Fakemeta**
  
[**pev**](http://amxxmodx.ru/fakemeta/fakemetainc/184-pev-funkciya-poluchaet-bolshinstvo-dannyh-ob-igroke-ili-obekte.html) получает большинство данных об игроке или объекте  
[**set_pev**](http://amxxmodx.ru/fakemeta/fakemetainc/185-set_pev-funkciya-ustanavlivaet-razlichnye-svoystva-igroku-ili-obektu.html) устанавливает различные свойства игроку или объекту  
**set_pev_string**  
[**pev_valid**](http://amxxmodx.ru/fakemeta/fakemetainc/159-pev_valid-funkciya-prvoeryaet-suschestvuet-li-obekt.html) проверяет существует ли объект  
**pev_serial**  
**global_get**  
[**get_pdata_int**](http://amxxmodx.ru/fakemeta/fakemetainc/358-get_pdata_int-funkciya-poluchaet-pvprivatedata-dannye-offset_.html) получает pvPrivateData данные ( OFFSET_*)  
[**set_pdata_int**](http://amxxmodx.ru/fakemeta/fakemetainc/359-get_pdata_int-funkciya-ustanavlivaet-znacheniya-pvprivatedata-dannym-offsetam.html) устанавливает значения pvPrivateData данным (OFFSET`ам)  
**get_pdata_float**  
**set_pdata_float**  
**get_pdata_ent**  
[**register_forward**](http://amxxmodx.ru/fakemeta/fakemetainc/201-register_forward-funkciya-registriruet-sobytiya-vnturi-dvizhka-hl-otlov-sobytiy.html) регистрирует события происходящие внутри движка HL (отлов событий)  
**unregister_forward**  
**forward_return**  
**get_orig_retval**  
[**engfunc**](http://amxxmodx.ru/fakemeta/fakemetainc/269-engfunc-funkciya-vyzyvaet-funkcii-dvizhka-half-life.html) вызывает функции движка Half-Life  
[**dllfunc**](http://amxxmodx.ru/fakemeta/fakemetainc/270-dllfunc-funkciya-vyzyvaet-funkcii-dvizhka-half-life.html) вызывает функции движка Half-Life  
**get_tr**  
**set_tr**  
**get_tr2**  
**set_tr2**  
**create_tr2**  
**free_tr2**  
**get_kvd**  
**set_kvd**  
**get_cd**  
**set_cd**  
[**get_es**](http://amxxmodx.ru/fakemeta/fakemetainc/418-get_es-funkciya-poluchaet-sostoyanie-obektov.html) получает состояние объектов  
[**set_es**](http://amxxmodx.ru/fakemeta/fakemetainc/400-set_es-funkciya-izmenyaet-sostoyanie-obektov.html) изменяет состояние объектов  
**get_uc**  
**set_uc**  
**get_pdata_string**  
**set_pdata_string**  
**copy_infokey_buffer**  
**lookup_sequence**  
**set_controller**  
  

## Модуль Fakemeta содержит следующие наборы констант
  

    * [**Return Type Constants**](http://amxxmodx.ru/fakemeta/fakemeta_constinc/142-return-type-constants-vozvrat-tipa-konstanty-forvarda.html) Возврат типа константы форварда  

    * [**Return Value Constants**](http://amxxmodx.ru/fakemeta/fakemeta_constinc/141-return-value-constants.html) Константы возвращаемого значения  

    * **Engine Function Constants**  

    * **DLL Function Constants**  

    * **Pev Constants**  

    * **Global Constants**  

    * **Forward Function Constants**  

    * **TraceResult Constants**  

    * **KeyValueData Constants**  

    * **ClientData Constants**  

    * **EntityState Constants**  

    * **UserCmd Constants**  

    * **AlertType Constants**  

[**Список pvPrivateData оффсетов OFFSET_***](http://amxxmodx.ru/fakemeta/366-spisok-pvprivatedata-offsetov-offset_.html)  
  
 **Return Type Constants**  
```
#define FMV_STRING        1  
#define FMV_FLOAT        2  
#define FMV_CELL        3
```
  
  
**Return Value Constants**  
```
#define FMRES_HANDLED    2  
#define FMRES_SUPERCEDE    4  
#define FMRES_IGNORED    1  
#define FMRES_OVERRIDE    3
```
  
  
**Engine Function Constants**  
```
enum {  
    EngFunc_PrecacheModel,        // int  )        (char* s);  
    EngFunc_PrecacheSound,        // int  )        (char* s);  
    EngFunc_SetModel,        // void )        (edict_t *e, const char *m);  
    EngFunc_ModelIndex,        // int  )        (const char *m);  
    EngFunc_ModelFrames,        // int  )        (int modelIndex);  
    EngFunc_SetSize,        // void )        (edict_t *e, const float *rgflMin, const float *rgflMax);  
    EngFunc_ChangeLevel,        // void )        (char* s1, char* s2);  
    EngFunc_VecToYaw,        // float)        (const float *rgflVector);  
    EngFunc_VecToAngles,        // void )        (const float *rgflVectorIn, float *rgflVectorOut);  
    EngFunc_MoveToOrigin,        // void )        (edict_t *ent, const float *pflGoal, float dist, int iMoveType);  
    EngFunc_ChangeYaw,        // void )        (edict_t* ent);  
    EngFunc_ChangePitch,        // void )        (edict_t* ent);  
    EngFunc_FindEntityByString,    // edict)        (edict_t *pEdictStartSearchAfter, const char *pszField, const char *pszValue);  
    EngFunc_GetEntityIllum,        // int  )        (edict_t* pEnt);  
    EngFunc_FindEntityInSphere,    // edict)        (edict_t *pEdictStartSearchAfter, const float *org, float rad);  
    EngFunc_FindClientInPVS,    // edict)        (edict_t *pEdict);  
    EngFunc_EntitiesInPVS,        // edict)        (edict_t *pplayer);  
    EngFunc_MakeVectors,        // void )        (const float *rgflVector);  
    EngFunc_AngleVectors,        // void )        (const float *rgflVector, float *forward, float *right, float *up);  
    EngFunc_CreateEntity,        // edict)        (void);  
    EngFunc_RemoveEntity,        // void )        (edict_t* e);  
    EngFunc_CreateNamedEntity,    // edict)        (int className);  
    EngFunc_MakeStatic,        // void )        (edict_t *ent);  
    EngFunc_EntIsOnFloor,        // int  )        (edict_t *e);  
    EngFunc_DropToFloor,        // int  )        (edict_t* e);  
    EngFunc_WalkMove,        // int  )        (edict_t *ent, float yaw, float dist, int iMode);  
    EngFunc_SetOrigin,        // void )        (edict_t *e, const float *rgflOrigin);  
    EngFunc_EmitSound,        // void )        (edict_t *entity, int channel, const char *sample, /*int*/float volume, float attenuation, int fFlags, int pitch);  
    EngFunc_EmitAmbientSound,    // void )        (edict_t *entity, float *pos, const char *samp, float vol, float attenuation, int fFlags, int pitch);  
    EngFunc_TraceLine,        // void )        (const float *v1, const float *v2, int fNoMonsters, edict_t *pentToSkip, TraceResult *ptr);  
    EngFunc_TraceToss,        // void )        (edict_t* pent, edict_t* pentToIgnore, TraceResult *ptr);  
    EngFunc_TraceMonsterHull,    // int  )        (edict_t *pEdict, const float *v1, const float *v2, int fNoMonsters, edict_t *pentToSkip, TraceResult *ptr);  
    EngFunc_TraceHull,        // void )        (const float *v1, const float *v2, int fNoMonsters, int hullNumber, edict_t *pentToSkip, TraceResult *ptr);  
    EngFunc_TraceModel,        // void )        (const float *v1, const float *v2, int hullNumber, edict_t *pent, TraceResult *ptr);  
    EngFunc_TraceTexture,        // const char *)    (edict_t *pTextureEntity, const float *v1, const float *v2);  
    EngFunc_TraceSphere,        // void )        (const float *v1, const float *v2, int fNoMonsters, float radius, edict_t *pentToSkip, TraceResult *ptr);  
    EngFunc_GetAimVector,        // void )        (edict_t* ent, float speed, float *rgflReturn);  
    EngFunc_ParticleEffect,        // void )        (const float *org, const float *dir, float color, float count);  
    EngFunc_LightStyle,        // void )        (int style, char* val);  
    EngFunc_DecalIndex,        // int  )        (const char *name);  
    EngFunc_PointContents,        // int  )        (const float *rgflVector);  
    EngFunc_FreeEntPrivateData,    // void )        (edict_t *pEdict);  
    EngFunc_SzFromIndex,        // const char * )    (int iString);  
    EngFunc_AllocString,        // int  )        (const char *szValue);  
    EngFunc_RegUserMsg,        // int    )        (const char *pszName, int iSize);  
    EngFunc_AnimationAutomove,    // void )        (const edict_t* pEdict, float flTime);  
    EngFunc_GetBonePosition,    // void )        (const edict_t* pEdict, int iBone, float *rgflOrigin, float *rgflAngles);  
    EngFunc_GetAttachment,        // void    )        (const edict_t *pEdict, int iAttachment, float *rgflOrigin, float *rgflAngles);  
    EngFunc_SetView,        // void )        (const edict_t *pClient, const edict_t *pViewent);  
    EngFunc_Time,            // float)        (void);  
    EngFunc_CrosshairAngle,        // void )        (const edict_t *pClient, float pitch, float yaw);  
    EngFunc_FadeClientVolume,    // void )        (const edict_t *pEdict, int fadePercent, int fadeOutSeconds, int holdTime, int fadeInSeconds);  
    EngFunc_SetClientMaxspeed,    // void )        (const edict_t *pEdict, float fNewMaxspeed);  
    EngFunc_CreateFakeClient,    // edict)        (const char *netname);    // returns NULL if fake client can't be created  
    EngFunc_RunPlayerMove,        // void )        (edict_t *fakeclient, const float *viewangles, float forwardmove, float sidemove, float upmove, unsigned short buttons, byte impulse, byte msec);  
    EngFunc_NumberOfEntities,    // int  )        (void);  
    EngFunc_StaticDecal,        // void )        ( const float *origin, int decalIndex, int entityIndex, int modelIndex);  
    EngFunc_PrecacheGeneric,    // int  )        (char* s);  
    EngFunc_BuildSoundMsg,        // void )        (edict_t *entity, int channel, const char *sample, /*int*/float volume, float attenuation, int fFlags, int pitch, int msg_dest, int msg_type, const float *pOrigin, edict_t *ed);  
    EngFunc_GetPhysicsKeyValue,    // const char* )    (const edict_t *pClient, const char *key);  
    EngFunc_SetPhysicsKeyValue,    // void )        (const edict_t *pClient, const char *key, const char *value);  
    EngFunc_GetPhysicsInfoString,    // const char* )    (const edict_t *pClient);  
    EngFunc_PrecacheEvent,        // unsigned short )    (int type, const char*psz);  
    EngFunc_PlaybackEvent,        // void )        (int flags, const edict_t *pInvoker, unsigned short eventindex, float delay, float *origin, float *angles, float fparam1, float fparam2, int iparam1, int iparam2, int bparam1, int bparam2);  
    EngFunc_CheckVisibility,    //)            (const edict_t *entity, unsigned char *pset);  
    EngFunc_GetCurrentPlayer,    //)            (void);  
    EngFunc_CanSkipPlayer,        //)            (const edict_t *player);  
    EngFunc_SetGroupMask,        //)            (int mask, int op);  
    EngFunc_GetClientListening,    // bool            (int iReceiver, int iSender)  
    EngFunc_SetClientListening,    // bool            (int iReceiver, int iSender, bool Listen)  
    EngFunc_MessageBegin,        // void            (int msg_dest, int msg_type, const float *pOrigin, edict_t *ed)  
    EngFunc_WriteCoord,        // void            (float)  
    EngFunc_WriteAngle,        // void            (float)  
    EngFunc_InfoKeyValue,        // char*)        (char *infobuffer, char *key);  
    EngFunc_SetKeyValue,        // void )        (char *infobuffer, char *key, char *value);  
    EngFunc_SetClientKeyValue,    // void )        (int clientIndex, char *infobuffer, char *key, char *value);  
    EngFunc_CreateInstBaseline,    // int  )        (int classname, struct entity_state_s *baseline);  
  
    // Returns pointer to info buffer that can be used with the infobuffer param of InfoKeyValue, SetKeyValue, and SetClientKeyValue  
    EngFunc_GetInfoKeyBuffer,    // char*)        (edict_t *e);  
    EngFunc_AlertMessage,        // void )        (ALERT_TYPE atype, char *szFmt, ...);  
    EngFunc_ClientPrintf        // void )        (edict_t* pEdict, PRINT_TYPE ptype, const char *szMsg);  
};
```
  
  
**DLL Function Constants**  
```
enum  
{  
    DLLFunc_GameInit,        // void )    (void);                  
    DLLFunc_Spawn,            // int  )    (edict_t *pent);  
    DLLFunc_Think,            // void )    (edict_t *pent);  
    DLLFunc_Use,            // void )    (edict_t *pentUsed, edict_t *pentOther );  
    DLLFunc_Touch,            // void )    (edict_t *pentTouched, edict_t *pentOther );  
    DLLFunc_Blocked,        // void )    (edict_t *pentBlocked, edict_t *pentOther );  
    DLLFunc_KeyValue,        // void )    (edict_t *pentKeyvalue, KeyValueData *pkvd );  
    DLLFunc_SetAbsBox,        // void )    (edict_t *pent );  
  
    DLLFunc_ClientConnect,        // bool )    (edict_t *pEntity, const char *pszName, const char *pszAddress, char szRejectReason[ 128 ] );  
      
    DLLFunc_ClientDisconnect,    // void )    (edict_t *pEntity);  
    DLLFunc_ClientKill,        // void )    (edict_t *pEntity);  
    DLLFunc_ClientPutInServer,    // void )    (edict_t *pEntity);  
    DLLFunc_ClientCommand,        // void )    (edict_t *pEntity);  
  
    DLLFunc_ServerDeactivate,    // void )    (void);  
  
    DLLFunc_PlayerPreThink,        // void )    (edict_t *pEntity);  
    DLLFunc_PlayerPostThink,    // void )    (edict_t *pEntity);  
  
    DLLFunc_StartFrame,        // void )    (void);  
    DLLFunc_ParmsNewLevel,        // void )    (void);  
    DLLFunc_ParmsChangeLevel,    // void )    (void);  
  
     // Returns string describing current .dll.  E.g., TeamFotrress 2, Half-Life  
    DLLFunc_GetGameDescription,    // const char * )(void);       
  
    // Spectator funcs  
    DLLFunc_SpectatorConnect,    // void )    (edict_t *pEntity);  
    DLLFunc_SpectatorDisconnect,    // void )    (edict_t *pEntity);  
    DLLFunc_SpectatorThink,        // void )    (edict_t *pEntity);  
  
    // Notify game .dll that engine is going to shut down.  Allows mod authors to set a breakpoint.  
    DLLFunc_Sys_Error,        // void )    (const char *error_string);  
  
    DLLFunc_PM_FindTextureType,    // char )    (char *name);  
    DLLFunc_RegisterEncoders,    // void )    (void);  
  
    // Enumerates player hulls.  Returns 0 if the hull number doesn't exist, 1 otherwise  
    DLLFunc_GetHullBounds,        // int  )    (int hullnumber, float *mins, float *maxs);  
  
    // Create baselines for certain "unplaced" items.  
    DLLFunc_CreateInstancedBaseline,    // void )    (void);  
    DLLFunc_pfnAllowLagCompensation,    // int  )    (void);  
    // I know this does not fit with DLLFUNC(), but I dont want another native just for it.  
    MetaFunc_CallGameEntity,        // bool        (plid_t plid, const char *entStr,entvars_t *pev);  
    DLLFunc_ClientUserInfoChanged,        // void        (idplayer);  
    // You can pass in 0 for global cd handle or another cd handle here  
    DLLFunc_UpdateClientData,        // void )    (const struct edict_s *ent, int sendweapons, struct clientdata_s *cd);  
    // You can pass in 0 for global entity state handle or another entity state handle here  
    DLLFunc_AddToFullPack,            // int  )    (struct entity_state_s *state, int e, edict_t *ent, edict_t *host, int hostflags, int player, unsigned char *pSet);  
    // You can pass in 0 for global usercmd handle or another usercmd handle here  
    DLLFunc_CmdStart,            // void )    (const edict_t *player, const struct usercmd_s *cmd, unsigned int random_seed);  
    DLLFunc_CmdEnd,                // void )    (const edict_t *player);  
    DLLFunc_CreateBaseline            // void )    (int player, int eindex, struct entity_state_s *baseline, struct edict_s *entity, int playermodelindex, vec3_t player_mins, vec3_t player_maxs);  
};
```
  
  
**Pev Constants**  
```
enum {  
    pev_string_start = 0,  
    pev_classname,  
    pev_globalname,  
    pev_model,  
    pev_target,  
    pev_targetname,  
    pev_netname,  
    pev_message,  
    pev_noise,  
    pev_noise1,  
    pev_noise2,  
    pev_noise3,  
    pev_string_end,  
    pev_edict_start,  
    pev_chain,  
    pev_dmg_inflictor,  
    pev_enemy,  
    pev_aiment,  
    pev_owner,  
    pev_groundentity,  
    pev_euser1,  
    pev_euser2,  
    pev_euser3,  
    pev_euser4,  
    pev_edict_end,  
    pev_float_start,  
    pev_impacttime,  
    pev_starttime,  
    pev_idealpitch,  
    pev_ideal_yaw,  
    pev_pitch_speed,  
    pev_yaw_speed,  
    pev_ltime,  
    pev_nextthink,  
    pev_gravity,  
    pev_friction,  
    pev_frame,  
    pev_animtime,  
    pev_framerate,  
    pev_scale,  
    pev_renderamt,  
    pev_health,  
    pev_frags,  
    pev_takedamage,  
    pev_max_health,  
    pev_teleport_time,  
    pev_armortype,  
    pev_armorvalue,  
    pev_dmg_take,  
    pev_dmg_save,  
    pev_dmg,  
    pev_dmgtime,  
    pev_speed,  
    pev_air_finished,  
    pev_pain_finished,  
    pev_radsuit_finished,  
    pev_maxspeed,  
    pev_fov,  
    pev_flFallVelocity,  
    pev_fuser1,  
    pev_fuser2,  
    pev_fuser3,  
    pev_fuser4,  
    pev_float_end,  
    pev_int_start,  
    pev_fixangle,  
    pev_modelindex,  
    pev_viewmodel,  
    pev_weaponmodel,  
    pev_movetype,  
    pev_solid,  
    pev_skin,  
    pev_body,  
    pev_effects,  
    pev_light_level,  
    pev_sequence,  
    pev_gaitsequence,  
    pev_rendermode,  
    pev_renderfx,  
    pev_weapons,  
    pev_deadflag,  
    pev_button,  
    pev_impulse,  
    pev_spawnflags,  
    pev_flags,  
    pev_colormap,  
    pev_team,  
    pev_waterlevel,  
    pev_watertype,  
    pev_playerclass,  
    pev_weaponanim,  
    pev_pushmsec,  
    pev_bInDuck,  
    pev_flTimeStepSound,  
    pev_flSwimTime,  
    pev_flDuckTime,  
    pev_iStepLeft,  
    pev_gamestate,  
    pev_oldbuttons,  
    pev_groupinfo,  
    pev_iuser1,  
    pev_iuser2,  
    pev_iuser3,  
    pev_iuser4,  
    pev_int_end,  
    pev_byte_start,  
    pev_controller_0,  
    pev_controller_1,  
    pev_controller_2,  
    pev_controller_3,  
    pev_blending_0,  
    pev_blending_1,  
    pev_byte_end,  
    pev_bytearray_start,  
    pev_controller,  
    pev_blending,  
    pev_bytearray_end,  
    pev_vecarray_start,  
    pev_origin,  
    pev_oldorigin,  
    pev_velocity,  
    pev_basevelocity,  
    pev_clbasevelocity,  
    pev_movedir,  
    pev_angles,  
    pev_avelocity,  
    pev_v_angle,  
    pev_endpos,  
    pev_startpos,  
    pev_absmin,  
    pev_absmax,  
    pev_mins,  
    pev_maxs,  
    pev_size,  
    pev_rendercolor,  
    pev_view_ofs,  
    pev_vuser1,  
    pev_vuser2,  
    pev_vuser3,  
    pev_vuser4,  
    pev_punchangle,  
    pev_vecarray_end,  
    pev_string2_begin,    // anything after here are string corrections  
    pev_weaponmodel2,  
    pev_viewmodel2,  
    pev_absolute_end  
};
```
  
  
**Global Constants**  
```
enum {  
    glb_start_int = 0,   
    glb_trace_hitgroup,   
    glb_trace_flags,   
    glb_msg_entity,   
    glb_cdAudioTrack,   
    glb_maxClients,   
    glb_maxEntities,   
    glb_end_int,   
    glb_start_float,   
    glb_time,   
    glb_frametime,   
    glb_force_retouch,   
    glb_deathmatch,   
    glb_coop,   
    glb_teamplay,   
    glb_serverflags,   
    glb_found_secrets,   
    glb_trace_allsolid,   
    glb_trace_startsolid,   
    glb_trace_fraction,   
    glb_trace_plane_dist,   
    glb_trace_inopen,   
    glb_trace_inwater,   
    glb_end_float,   
    glb_start_edict,   
    glb_trace_ent,   
    glb_end_edict,   
    glb_start_vector,   
    glb_v_forward,   
    glb_v_up,   
    glb_v_right,   
    glb_trace_endpos,   
    glb_trace_plane_normal,   
    glb_vecLandmarkOffset,  
    glb_end_vector,  
    glb_start_string,   
    glb_mapname,   
    glb_startspot,   
    glb_end_string,   
    glb_start_pchar,   
    glb_pStringBase,   
    glb_end_pchar  
};
```
  
  
**Forward Function Constants**  
```
enum {  
    FM_PrecacheModel = 1,        // int )    (const szModel[])  
    FM_PrecacheSound,        // int )    (const szSound[])  
    FM_SetModel,            // void )    (ent, const szModel[])  
    FM_ModelIndex,            // int )    (const szModel[])  
    FM_ModelFrames,            // int )    (iModelIndex)  
    FM_SetSize,            // void )    (ent, const Float:fMins[3], const Float:fMaxs[3])  
    FM_ChangeLevel,            // void )    (szMap[], szSomething[])  
    FM_VecToYaw,            // float )    (const Float:fVector[3])  
    FM_VecToAngles,            // void )    (const Float:fVectorIn[3], Float:fVectorOut[3])  
    FM_MoveToOrigin,        // void )    (ent, const Float:fGoal[3], Float:fDistance, iMoveType)  
    FM_ChangeYaw,            // void )    (ent)  
    FM_ChangePitch,            // void )    (ent)  
    FM_FindEntityByString,        // edict )    (entStartSearchAfter, const szField[], const szValue[])  
    FM_GetEntityIllum,        // int )    (ent)  
    FM_FindEntityInSphere,        // edict )    (ent, const Float:fVector[3], Float:fRadius)  
    FM_FindClientInPVS,        // edict )    (id)  
    FM_EntitiesInPVS,        // edict )    (ent)  
    FM_MakeVectors,            // void )    (const Float:fVector[3])  
    FM_AngleVectors,        // void )    (const Float:fVec[3], Float:fForward[3], Float:fRight[3], Float:fUp[3])  
    FM_CreateEntity,        // edict )    ()  
    FM_RemoveEntity,        // void )    (ent)  
    FM_CreateNamedEntity,        // edict )    (iClassname)  
    FM_MakeStatic,            // void )    (ent)  
    FM_EntIsOnFloor,        // int )    (ent)  
    FM_DropToFloor,            // int )    (ent)  
    FM_WalkMove,            // int  )    (ent, Float:fYaw, Float:fDist, iMode)  
    FM_SetOrigin,            // void )    (ent, const Float:fOrigin[3])  
    FM_EmitSound,            // void )    (ent, iChannel, const szSample[], Float:fVolume, Float:fAttenuation, iFlags, iPitch)  
    FM_EmitAmbientSound,        // void )    (ent, Float:fOrigin[3], const szSample[], Float:fVolume, Float:fAttenuation, iFlags, iPitch)  
    FM_TraceLine,            // void )    (const Float:fV1[3], const Float:fV2[3], iNoMonsters, entToSkip, tr)  
    FM_TraceToss,            // void )    (ent, entToIgnore, tr)  
    FM_TraceMonsterHull,        // int )    (ent, const Float:fV1, const Float:fV2, iNoMonsters, entToSkip, tr)  
    FM_TraceHull,            // void )    (const Float:fV1[3], const Float:fV2[3], iNoMonsters, iHullNumber, entToSkip, tr)  
    FM_TraceModel,            // void )    (const Float:fV1[3], const Float:fV2[3], iHullNumber, ent, tr)  
    FM_TraceTexture,        // char )    (entTexture, const Float:fV1[3], const Float:fV2[3])  
    FM_TraceSphere,            // void )    (const Float:fV1[3], const Float:fV2[3], iNoMonsters, Float:fRadius, entToSkip, tr)  
    FM_GetAimVector,        // void )    (ent, Float:fSpeed, Float:fReturn[3])  
    FM_ParticleEffect,        // void )    (const Float:fOrigin[3], const Float:fDir[3], Float:fColor, Float:fCount)  
    FM_LightStyle,            // void )    (iStyle, szVal[])  
    FM_DecalIndex,            // int )    (const szName[])  
    FM_PointContents,        // int )    (const Float:fOrigin[3])  
    FM_MessageBegin,        // void )    (iMsg_Dest, iMsg_Type, const Float:fOrigin[3], ent)  
    FM_MessageEnd,            // void )    ()  
    FM_WriteByte,            // void )    (iValue)  
    FM_WriteChar,            // void )    (iValue)  
    FM_WriteShort,            // void )    (iValue)  
    FM_WriteLong,            // void )    (iValue)  
    FM_WriteAngle,            // void )    (Float:fValue)  
    FM_WriteCoord,            // void )    (Float:fValue)  
    FM_WriteString,            // void )    (const szValue[])  
    FM_WriteEntity,            // void )    (iValue)  
    FM_CVarGetFloat,        // float )    (const szCvar[])  
    FM_CVarGetString,        // char )    (const szCvar[])  
    FM_CVarSetFloat,        // void )    (const szCvar[], Float:fValue)  
    FM_CVarSetString,        // void )    (const szCvar[], szValue[])  
    FM_FreeEntPrivateData,        // void )    (ent)  
    FM_SzFromIndex,            // char )    (iString)  
    FM_AllocString,            // int )    (const szValue[])  
    FM_RegUserMsg,            // int )    (szName[], iSize)  
    FM_AnimationAutomove,        // void )    (const ent, Float:fTime)  
    FM_GetBonePosition,        // void )    (const ent, iBone, Float:fOrigin[3], Float:fAngle[3])  
    FM_GetAttachment,        // void    )    (const ent, iAttachment, Float:fOrigin[3], Float:fAngle[3])  
    FM_SetView,            // void )    (const ent, const entView)  
    FM_Time,            // float )    ()  
    FM_CrosshairAngle,        // void )    (const ent, Float:fPitch, Float:fYaw)  
    FM_FadeClientVolume,        // void )    (const ent, iFadePercent, iFadeOutSeconds, iHoldTime, iFadeInSeconds)  
    FM_SetClientMaxspeed,        // void )    (const ent, Float:fMaxSpeed)  
    FM_CreateFakeClient,        // edict )    (const szNetName[])  
    FM_RunPlayerMove,        // void )    (const entFakeClient, Float:fViewAngles[3], Float:fForwardmove, Float:fSidemove, Float:fUpmove, iButtons, iImpulse, i_mSec)  
    FM_NumberOfEntities,        // int )     ()  
    FM_StaticDecal,            // void )    (const Float:fOrigin[3], iDecalIndex, iEntityIndex, iModelIndex)  
    FM_PrecacheGeneric,        // int )    (szString[])  
    FM_BuildSoundMsg,        // void )    (ent, iChannel, const szSample[], Float:fVolume, Float:fAttenuation, iFlags, iPitch, iMsg_Dest, iMsg_Type, const Float:fOrigin[3], ent)  
    FM_GetPhysicsKeyValue,        // char )    (const ent, const szKey[])  
    FM_SetPhysicsKeyValue,        // void )    (const ent, const szKey[], const szValue[])  
    FM_GetPhysicsInfoString,    // char )    (const ent)  
    FM_PrecacheEvent,        // int )    (iType, const szEvent[])  
    FM_PlaybackEvent,        // void )    (iFlags, const entInvoker, iEventIndex, Float:fDelay, Float:fOrigin[3], Float:fAngles[3], Float:fParam1, Float:fParam2, iParam1, iParam2, bool:bParam1, bool:bParam2)  
    FM_CheckVisibility,        // int )    (const ent, iSet)  
    FM_GetCurrentPlayer,        // int )    ()  
    FM_CanSkipPlayer,        // int )    (const ent)  
    FM_SetGroupMask,        // void )    (iMask, iOp)  
    FM_Voice_GetClientListening,    // bool )    (iReceiver, iSender)  
    FM_Voice_SetClientListening,    // bool )    (iReceiver, iSender, bool:bListen)  
    FM_InfoKeyValue,        // char )    (szInfoBuffer[], szKey[])  
    FM_SetKeyValue,            // void )    (szInfoBuffer[], szKey[], szValue[])  
    FM_SetClientKeyValue,        // void )    (iClientIndex, szInfoBuffer[], szKey[], szValue[])  
    FM_GetPlayerAuthId,        // char )    (ent)  
    FM_GetPlayerWONId,        // char )    (ent)  
    FM_IsMapValid,            // int )    (szFileName[])  
  
  
    FM_Spawn,            // int )    (ent)  
    FM_Think,            // void )    (ent)  
    FM_Use,                // void )    (entUsed, entOther)  
    FM_Touch,            // void )    (entTouched, entOther)  
    FM_Blocked,            // void )    (entBlocked, entOther)  
    FM_KeyValue,            // void )    (keyvalue, kvd_id)  
    FM_SetAbsBox,            // void )    (ent)  
    FM_ClientConnect,        // bool )    (ent, const szName[], const szAddress[], const szRejectReason[128])  
      
    FM_ClientDisconnect,        // void )    (ent)  
    FM_ClientKill,            // void )    (ent)  
    FM_ClientPutInServer,        // void )    (ent)  
    FM_ClientCommand,        // void )    (ent)  
  
    FM_ServerDeactivate,        // void )    ()  
  
    FM_PlayerPreThink,        // void )    (ent)  
    FM_PlayerPostThink,        // void )    (ent)  
  
    FM_StartFrame,            // void )    ()  
    FM_ParmsNewLevel,        // void )    ()  
    FM_ParmsChangeLevel,        // void )    ()  
  
     // Returns string describing current .dll.  E.g., TeamFotrress 2, Half-Life  
    FM_GetGameDescription,         // char )    ()  
  
    // Spectator funcs  
    FM_SpectatorConnect,        // void )    (ent)  
    FM_SpectatorDisconnect,        // void )    (ent)  
    FM_SpectatorThink,        // void )    (ent)  
  
    // Notify game .dll that engine is going to shut down.  Allows mod authors to set a breakpoint.  
    FM_Sys_Error,            // void )    (const szError[])  
  
    FM_PM_FindTextureType,        // char )    (szType[])  
    FM_RegisterEncoders,        // void )    ()  
  
    // Enumerates player hulls.  Returns 0 if the hull number doesn't exist, 1 otherwise  
  
    // Create baselines for certain "unplaced" items.  
    FM_CreateInstancedBaseline,    // void )    ()  
    FM_AllowLagCompensation,    // int )    ()  
      
    FM_AlertMessage,        // void )    (AlertType:aType, szBuffer[])  
  
    // NEW_DLL_FUNCTIONS:  
    FM_OnFreeEntPrivateData,    // void )    (ent)  
    FM_GameShutdown,        // unknown )    ()  
    FM_ShouldCollide,        // unknown )    (entTouched, entOther)  
  
    // LATE ADDITIONS (v1.71)  
    FM_ClientUserInfoChanged,    // void )    (ent, szInfo[])  
      
    // LATE ADDITIONS (v1.75)  
    FM_UpdateClientData,        // void )    (const ent, iSendWeapons, cd_handle)  
    FM_AddToFullPack,        // int )    (entState, e, ent, host, iHostFlags, iPlayer, pSet)  
    FM_CmdStart,            // void )    (const ent, uc_handle, seed)  
    FM_CmdEnd,            // void )    (const ent)  
    FM_CreateInstBaseline,        // int )    (classname, baseline)  
    FM_CreateBaseline,        // void )    (iPlayer, i_eIndex, baseline, ent, iPlayerModelIndex, Float:fMins[3], Float:fMaxs[3])  
    FM_GetInfoKeyBuffer,        // char )    (ent)  
    FM_ClientPrintf         // void )    (ent, type, const szMsg[])  
  
    // LATE ADDITIONS (v1.80)  
    FM_ServerPrint            // void )    (const szMsg[])  
};
```
  
  
**TraceResult Constants**  
```
enum {  
    TR_AllSolid,  
    TR_StartSolid,  
    TR_InOpen,  
    TR_InWater,  
    TR_flFraction,  
    TR_vecEndPos,  
    TR_flPlaneDist,  
    TR_vecPlaneNormal,  
    TR_pHit,  
    TR_iHitgroup,  
};
```
  
  
**KeyValueData Constants**  
```
enum {  
    KV_ClassName,  
    KV_KeyName,  
    KV_Value,  
    KV_fHandled  
};
```
  
  
**ClientData Constants**  
```
enum {  
    CD_Origin,        // float array[3]  
    CD_Velocity,        // float array[3]  
    CD_ViewModel,        // int  
    CD_PunchAngle,        // float array[3]  
    CD_Flags,        // int  
    CD_WaterLevel,        // int  
    CD_WaterType,        // int  
    CD_ViewOfs,        //
```

