. Porting AMX Mod Modules
Sections:
  1. [New Include/Base Structure](http://127.0.0.1:8000/content/porting.htm#base)
  2. [New API](http://127.0.0.1:8000/content/porting.htm#api)
  3. [New Forward/Callback System](http://127.0.0.1:8000/content/porting.htm#forwards)

**1. New Include/Base Structure**   
  
Instead of including <modules.h>, you should now include <amxxmodule.h> and add the M/SDK to your project (get the MDK from CVS or the packaged source code).   
  
Then you should make the necessary moduleconfig.h configuration changes listed in the module writing guide to enable Metamod hooks, Native hooks, and your module's "personal" information struct.   
  
You should remove any .def files, and also remove any Metamod or AMX Mod hooks, such as Meta_Attach() or Amx_Attach(). Instead, uncomment the appropriate hooks in moduleconfig.h - such as OnAmxxAttach for natives and OnPluginsLoaded for forwards. For Metamod, remove all of the engine hook sets and uncomment the appropriate hooks in moduleconfig.h. For example, if your old AMX Mod module had this:  
  
```
C_DLLEXPORT int AMX_Attach(pfnamx_engine_g* amxeng,pfnmodule_engine_g* meng) {
   g_engAmxFunc = amxeng;
   g_engModuleFunc = meng;
	
   if(!gpMetaGlobals) REPORT_ERROR(1, "[AMX] fun is not attached to metamod (module \"%s\")\n", LOGTAG);
	
   ADD_AMXNATIVES(&module_info, fun_Exports);
	
   return(1);
}

```
  
This would simply become:  
  
```
void OnAmxxAttach()
{
	MF_AddNatives(fun_Exports);
}

```
  
Likewise:  
  
```
enginefuncs_t meta_engfuncs;
C_DLLEXPORT int GetEngineFunctions(enginefuncs_t *pengfuncsFromEngine, int interfaceVersion ) {
   meta_engfuncs.pfnTraceLine = TraceLine;
   memcpy(pengfuncsFromEngine, &meta_engfuncs, sizeof(enginefuncs_t));
   return(TRUE);
}

```
  
Is simply deleted, and #define FM_TraceLine is uncommented from moduleconfig.h.   
  
Easy, huh? Other things, like global/external pointers used for MM/AMX should be removed. These are handled by the M/SDK.  
  
**2. Natives/Parameters**   
  
You should familiarize yourself with the new module functions available.  
  
Here are some quick changes. The parameter count is listed as well. A * indicates the parameters changed.  
  

  * ADD_AMXNATIVES(2) -> [MF_AddNatives](http://127.0.0.1:8000/content/funcs.htm#mf_addnatives)(1*)
  * AMX_RAISEERROR(2) -> [MF_RaiseAmxError](http://127.0.0.1:8000/content/funcs.htm#mf_raiseamxerror)(2) or [MF_LogError](http://127.0.0.1:8000/content/funcs.htm#mf_logerror)(...*)
  * GET_AMXADDR(2) -> [MF_GetAmxAddr](http://127.0.0.1:8000/content/funcs.htm#mf_getamxaddr)(2)
  * SET_AMXSTRING(4) -> [MF_SetAmxString](http://127.0.0.1:8000/content/funcs.htm#mf_setamxstring)(4)
  * GET_AMXSTRING(4) -> [MF_GetAmxString](http://127.0.0.1:8000/content/funcs.htm#mf_getamxstring)(4*)

**3. New Forward/Callback System**   
  
AMX Mod modules are responsible for handling forwards their own way - in AMX Mod X the core does it for you.  
  
Take this example from VexD, the way to manage a forward was:  
  
```
struct AmxCall {
   plugin_t *pPlugin;
   int iFunctionIdx;
};

std::vector<AmxCall> vTouchCallList;

//Registering the forward:
   if (AMX_FINDPUBLIC(&pCurrent->amx, "vexd_pfntouch", &iFunctionIndex) == AMX_ERR_NONE) {
      AmxCall sNewCall;
      sNewCall.pPlugin = pCurrent;
      sNewCall.iFunctionIdx = iFunctionIndex;
      vTouchCallList.push_back(sNewCall);
   //...		}

//Calling the forward:
   for(std::vector<AmxCall>::iterator i = vTouchCallList.begin(); i != vTouchCallList.end(); i++) {
      cell iRetVal = 0;
      AMX_EXEC(&i->pPlugin->amx, &iRetVal, i->iFunctionIdx, 2, ENTINDEX(pToucher), ENTINDEX(pTouched));
   }

```
  
Rather than using the new API functions (MF_AmxFindPublic, MF_AmxExec), let's try using the new Forward system.  
  
```
int TouchForward = -1;

//Registering the forward:
   TouchForward = MF_RegisterForward("vexd_pfntouch", ET_IGNORE, FP_CELL, FP_CELL, FP_DONE);

//Calling the forward:
   MF_ExecuteForward(TouchForward, ENTINDEX(pToucher), ENTINDEX(pTouched));

```
  
Simple, clean, efficient. Have fun!
