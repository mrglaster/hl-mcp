# orpheu_const.inc
```
#if defined _orpheu_const_included
	#endinput
#endif
#define _orpheu_const_included

#if AMXX_VERSION_NUM >= 175
 #pragma reqlib orpheu
 #if !defined AMXMODX_NOAUTOLOAD
  #pragma loadlib orpheu
 #endif
#else
 #pragma library orpheu
#endif

const OrpheuFunction:OrpheuInvalidFunction = OrpheuFunction:0

enum OrpheuHookReturn
{
	OrpheuIgnored,
	OrpheuOverride,
	OrpheuSupercede
}

enum OrpheuHookPhase
{
	OrpheuHookPre,
	OrpheuHookPost
}

enum OrpheuStructType
{
	OrpheuStructMovevars,
	OrpheuStructUsercmd,
	OrpheuStructMonsterEvent,
	OrpheuStructDLL_FUNCTIONS,
	OrpheuStructPlayerMove,
	OrpheuStructEngineFuncs,
	OrpheuStructTraceResult,
	OrpheuStructPhysent,
	OrpheuStructPmplane,
	OrpheuStructPmtrace,
	OrpheuStructWeaponData,
	OrpheuStructAmmoInfo,
	OrpheuStructItemInfo,
	OrpheuStructTask,
	OrpheuStructSchedule,
	OrpheuStructKeyValueData
}

```


This code is a part of orpheu_const.inc. To use this code you should include orpheu_const.inc as ```#include <orpheu_const>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. Orpheu is outdated and not recommended for use, so use Include at your own risk. 