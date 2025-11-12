# rage_const.inc
```
#if defined _rage_const_included
	#endinput
#endif
#define _rage_const_included

#if AMXX_VERSION_NUM >= 175
 #pragma reqlib rage
 #if !defined AMXMODX_NOAUTOLOAD
  #pragma loadlib rage
 #endif
#else
 #pragma library rage
#endif

const RageFunc:RageFuncInvalid = RageFunc:-1

enum RageHookPhase
{
	RageHookPre,
	RageHookPost
}

enum RageHookReturn
{
	RageHookIgnored,
	RageHookHandled,
	RageHookOverride,
	RageHookSupercede
}

```


This code is a part of rage_const.inc. To use this code you should include rage_const.inc as ```#include <rage_const>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.