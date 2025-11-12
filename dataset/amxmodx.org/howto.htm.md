. Basic Module Layout
Sections:
  1. [Natives/Parameters](http://127.0.0.1:8000/content/howto.htm#natives)
  2. [Forwards/Callbacks](http://127.0.0.1:8000/content/howto.htm#callbacks)
  3. [Compiling](http://127.0.0.1:8000/content/howto.htm#compiling)
  4. [Debugging](http://127.0.0.1:8000/content/howto.htm#debug)

**1. Natives/Parameters**   
  
A native is a C or C++ function that can be used in Small scripts. They are one of the two ways to glue Small to your module. Take this sample native:  
  
```
//my native
static cell AMX_NATIVE_CALL my_native(AMX *amx, cell *params)
{
	return 1;
}

```
  
This native simply returns 1 - it does nothing else. Let's analyze it. 
  * static - You should know the static keyword.
  * cell - This is the base type for Small plugins. It is either a 4byte or 8byte unsigned integer depending on the architecture.
  * AMX_NATIVE_CALL - a macro for the calling convention (__cdecl).
  * AMX *amx - a pointer to the AMX structure for a plugin. This structure contains the virtual machine bytecode and state information - you rarely need to use this directly.
  * cell *params - an array of parameters that the plugin passed to your native. params[0] is the number of bytes following in the array, so *params/sizeof(cell) will be equal to the number of parameters. Then params[1] is the first parameter and so on.
  * return 1; - AMX functions should always return a value.

So, how do extract parameters? Let's say we wanted to make a simple math function that found the product of two numbers passed.  
  
```
static cell AMX_NATIVE_CALL amx_biproduct(AMX *amx, cell *params)
{
	return params[1] * params[2];
}

```
  
Simple enough, right? Well, it gets more complicated. Small plugins follow a certain calling convention.  
  
Integers and floats are passed by value. Arrays (including strings) are passed by reference. And lastly, variable arguments are always passed by reference. For example:  
  
```
native sample_native(a, b, ...);
```
Everything after b will be by reference.   
  
```
//native prototype: amx_product(...);
static cell AMX_NATIVE_CALL amx_product(AMX *amx, cell *params)
{
	int i = 0;
	int sum = 1;
	cell *addr = NULL;
	int numParams = *params/sizeof(cell);
	for (i=1; i<=numParams; i++)
	{
		addr = MF_GetAmxAddr(amx, params[i]);
		sum *= (int)(*addr);
	}
	return sum;
}

```
  
MF_GetAmxAddr is the first module function we will deal with. It takes two parameters, an AMX virtual machine and a by-reference offset in the machine. It will return the actual address where the data is stored. So here, we retrieve the cell address at which the parameter is stored and add it to our product.   
  
What about floats? Let's say you want to make a function that multiplies two floats together.  
  
```
//amx_fProduct(Float:a1, Float:a2)
static cell AMX_NATIVE_CALL amx_fProduct(AMX *amx, cell *params)
{
	REAL product;

	product = amx_ctof(params[1]) * amx_ctof(params[2]);

	return amx_ftoc(product);
}

```
  
Here we have the next two module functions. The AMX virtual machine has only one data type - the cell. So we have two natives to convert a cell to a float and vice versa. Because cells differ from platform to platform, we use REAL which is a float or a double depending on the cellsize. amx_ctof convers a cell to a REAL and amx_ftoc converts a REAL to a cell. Note we have to return the result as a cell, not a REAL.   
  
Here is the variadic version using multiple parameters:   
  
```
//native prototype: Float:amx_fProduct({Float}:...);
static cell AMX_NATIVE_CALL amx_product(AMX *amx, cell *params)
{
	int i = 0;
	REAL sum = 1;
	cell *addr = NULL;
	int numParams = *params/sizeof(cell);
	for (i=1; i<=numParams; i++)
	{
		addr = MF_GetAmxAddr(amx, params[i]);
		sum *= amx_ctof(*addr);
	}

	return amx_ftoc(sum);
}

```
  
Now, what about strings? There are two issues with strings. Strings are basically arrays, which means each character is a 32bit cell, not a char. To help convert there is a function called MF_GetAmxString:  
  
```
char *MF_GetAmxString(AMX *amx, cell addr, int bufferId, int *length);
```
  
Buffer IDs are from 0 to 3. They copy the string to a static, non-reentrant buffer. This means you can only use this function with 4 string parameters, and that it is not thread safe!  
  
Next, you can "set" strings using MF_SetAmxString. Let's wrap this section up with a super-example. This function will take in a vector (Float:vec[3]), a string, then multiply the vector by the integer value in the string, then set the result as a string and return a float:  
  
```
//Float:amx_weird(Float:vec[3], const str[], result[], maxlen)
static cell AMX_NATIVE_CALL amx_weird(AMX *amx, cell *params)
{
	int len = 0;
	cell *vec = MF_GetAmxAddr(amx, params[1]);
	char *str = MF_GetAmxString(amx, params[2], 0, &len);
	REAL prod = amx_ctof(vec[0]) * amx_ctof(vec[1]) * amx_ctof(vec[2]);
	prod *= atoi(str);
	char buf[20];
	itoa((int)prod, buf, 10);
	//amx, dest addr, source, max length
	MF_SetAmxString(amx, params[3], buf, params[4]);
	return amx_ftoc(prod);
}

```
  
So how do you glue your natives to small scripts? This is a two step process.   
First, go to moduleconfig.h and uncomment this line:  
  
```
	// #define FN_AMXX_ATTACH OnAmxxAttach
```
  
Then add this somewhere into your module's main file (let's call it mymodule.cpp):   
  
```
AMX_NATIVE_INFO my_Natives[] = 
{
	{"amx_fproduct",	amx_fProduct},
	{"amx_weird",		amx_weird},
	{NULL,			NULL},
};

```
  
This creates a list describing what natives you want to add to Small plugins. The list is formatted as Name, Function, Name, Function, etc. Terminate the list with NULLs. Now create this function:  
  
```
void OnAmxxAttach()
{
	MF_AddNatives(my_Natives);
}

```
  
Now your functions are available to plugins! The last step is to actually make an include file. Example mymodule.inc:  
  
```
#if defined _mymodule_included
   #endinput
#endif
#define _mymodule_included

//Multiply all the float parameters passed and return the result.
native Float:amx_fproduct({Float}:...);

//This function is just weird!
native Float:amx_weird(Float:vec[3], const numStr[], retstr[], maxLen);

```
  
You're done!   
  
  
**2. Forwards/Callbacks**   
  
The second way to glue your module to plugins is to make callbacks, or forwards.   
  
For example, let's say you want your module to have two new forwards for plugins: one so they can hook every time something is touched, another so they can hook every time an entity is created by name - but only if they register the call beforehand. The first example is a global forward. In an include, it would look like this:  
  
```
forward mymodule_Touch(entToucher, entTouched);
```
  
To make a global forward is pretty simple. These examples will require Metamod activation in your module. Find these lines in moduleconfig.h and uncomment them:   
  
```
// #define USE_METAMOD
// #define FN_AMXX_PLUGINSLOADED OnPluginsLoaded
// #define FN_CreateNamedEntity CreateNamedEntity
// #define FN_DispatchTouch DispatchTouch

```
  
In your module header file (mymodule.h) add something like:   
  
```
#include "CString.h"	//copy this file from AMX Mod X core
#include "CVector.h"	//copy this file from AMX Mod X core
#include "amxxmodule.h" //this is the SDK file

struct CreateForward    //We will use this to store some info
{
	int forwardID;
	String name;
};

extern int TouchForward;
extern CVector<CreateForward> CreateForwards;

```
  
In mymodule.cpp, you can now do:  
  
```
int TouchForward = -1;	//-1 is an invalid forward so initiate this to that
CVector<CreateForward> CreateForwards;

void OnPluginsLoaded()
{
   //mymodule_Touch - the forward name
   //ET_IGNORE - means PLUGIN_HANDLED will be ignored (other option is ET_STOP)
   //FP_CELL - first parameter is a normal cell
   //FP_CELL - second parameter is a normal cell
   //FP_DONE - that's the end of the parameter descriptions
   TouchForward = MF_RegisterForward("mymodule_Touch", ET_IGNORE, FP_CELL, FP_CELL, FP_DONE);	
}

void DispatchTouch(edict_t *pfnToucher, edict_t *pfnTouched)
{
   if (TouchForward > -1)
   {
      MF_ExecuteForward(TouchForward, ENTINDEX(pfnToucher), ENTINDEX(pfnTouched));
   }

   //ignore metamod return value
   RETURN_META(MRES_IGNORED);
}

```
  
Now your module will call the forward in every plugin, every time two entities touch. The next part is trickier, we want a native that will register forwards, for example:   
  
```
public plugin_info()
	register_create("createWeaponBox", "weaponbox")

public createWeaponBox(classname[], entId)
{
	//A weaponbox has been created!
}

```
This is a non-global, or Single Plugin forward. Here is an example of how to make one:  
  
```
//register_native(func[], classname[])
static cell AMX_NATIVE_CALL register_create(AMX *amx, cell *params)
{
   int len = 0;
   //get function name
   char *func = MF_GetAmxString(amx, params[1], 0, &len);
   //get desired classname
   char *classname = MF_GetAmxString(amx, params[2], 1, &len);

   //new forward storage
   CreateForward sForward;
   //set the classname
   sForward.name.assign(classname);
   //note this time there is no ET_ value.  Also, FP_STRING is a special format option.
   //only use FP_STRING for valid char * zero terminated string pointers.
   //If you need to push an array, you must use FP_ARRAY and MF_PrepareCellArrray
   sForward.forwardID = MF_RegisterSPForwardByName(func, FP_STRING, FP_CELL, FP_DONE);

   if (sForward.forwardID == -1)
   {
      MF_LogError(amx, AMX_ERR_NOTFOUND, "Function \"%s\" was not found!", func);
      return 0;
   }

   //add this information to the main list
   CreateForwards.push_back(sForward);
   return 1;
}

//This is the MetaMod hook for catching when an entity is made.
edict_t *CreateNamedEntity(int iszClassname)
{
   //go through our list of forwards.  do any of the classes match?
   //STRING converts an HL engine isz string to an sz string
   const char *classname = STRING(iszClassname);
   int i = 0;
   edict_t *e = CREATENAMEDENTITY(iszClassname);
   for (i=0; i<CreateForwards.size(); i++)
   {
      if (CreateForwards[i].forwardID != -1)
      {
         if (CreateForwards[i].name.compare(classname) == 0)
         {
            MF_ExecuteForward(CreateForwards[i].forwardID, classname, ENTINDEX(e));
         }
      }
   }
   RETURN_META_VALUE(MRES_SUPERCEDE, e);
}

```
  
There! We've now made global and local forwards.   
  
  
**3. Compiling**   
  
Lastly, you must compile your module. For Windows, this is fairly easy. Microsoft makes some of the best development environments known - so we have some directions for Microsoft Visual C++ 6.0 and 7.0 (and gcc for Linux users)  
  
**Microsoft Visual C++ 6.0**
  1. Create a new project from the File menu.
  2. Select Win32 Dynamic-Link Library.
  3. On the next page, select "An empty DLL project".
  4. Go to Projet, Add to Project, Files.
  5. Add amxxmodule.cpp, amxxmodule.h, moduleconfig.h, and the other files you have for your module.
  6. Go to Project, Settings. Change these settings for both Win32 Debug and Win32 Release options.
  7. Under C++ / Code Generation, it is recommended you do not make Multi-Threaded builds.
  8. Under Link, you should change the module name to conform to AMX Mod X standards: <modulename>_amxx.dll.
  9. Once you're done, go to Tools, Options, Directories.
  10. Make sure you have Metamod and HLSDK source code installed.
  11. Add the following directories above the already included ones:
     * in hlsdk/SourceCode or hlsdk/multiplayer/ folder: pm_shared, engine, common, dlls.
     * Metamod's source folder.
     * AMX Mod X's source folder if you include AMXXSTL files with #include <>.
  12. You're ready to build your module from the Build menu. Use Set Active Configuration to switch between Debug and Release.

**Microsoft Visual C++ 7.0**
  1. Go to File, New, Project.
  2. Select Visual C++ Projects, Win32 Application.
  3. Select Application Settings, DLL, Empty Project.
  4. Go to Project, Properties. For both Debug and Release, change these:
     * Linker->General should conform to AMX Mod X's naming scheme, _amxx.dll
     * C/C++->Code Generation->Runtime Library should never be Multi-Threaded (unless special circumstances need it).
  5. Lastly, in the Tools, Options, Projects, VC++ Directories, Include Files menu, make sure to include the same directories as shown above for VC++ 6.0

**Linux (GNU C Compiler 2.95 and 3.30)**
  1. AMX Mod X is distributed with perl Makefiles to assist you in building your modules. They are fairly easy to edit - you can just change the array containing the source files. For 32bit machines, you can use a GCC line like this: ```
gcc -march=i386 -O3 -fomit-frame-pointer -s -Wall -fno-rtti    \
    -fno-exceptions -fPIC <list of source files> -ldl -shared  \
    -lm -o_i386.so

```
  
For 64bit, it becomes:  
```
gcc -m64 -DSMALL_CELL_SIZE=64 -DHAVE_I64 -O3 -fomit-frame-pointer \
    -s -Wall -fno-rtti -fno-exceptions -fPIC <list of source files> \
    -ldl -shared -lm -o<modulename>_amd64.so

```

  2. If you use the Standard C++ Library, you may need to include -lstdc++, just be aware that not everyone may have your version of stdc++.
  3. To test if your module will load on linux, you can use the "dlsym" or "dlsym64" program that comes with AMX Mod X for Linux. It will either return an error message or success notification: ```
cd amxmodx/scripting
./dlsym ~/mymodule/mymodule_i386.so

```


  
  
**4. Debugging (crashes)**   
  
I'm not going to go into how to debug too in depth, as it's a complicated subject best learned by practice. But I will go over how to start and see a debugger and a call stack trace (showing what happened prior to the crash). Since MSVC 7.0's debugger is much easier to use than 6's, I will not cover 6's.   
  
**Microsoft Visual C++ 7.0**
  1. Compile your module in debug mode. You may also want to compile and upload debug versionso of AMX Mod X and Metamod, incase the bug ends up being there.
  2. Start HLDS with -dev 1. This gives metamod a 10 second pause so you can attach to the HLDS process. You could also just use HLDS GUI and attach before you click "Start". 
  3. In MSVC, go to Tools, Debug Process. Attach to the HLDS process.
  4. Cause your module to crash or hit a breakpoint.
  5. In MSVC, go to Debug, Windows, Call Stack.

**Linux (GNU Debugger)**
  1. Compile your module with only the following optimization flags:  
```
  -ggdb3
   (or for AMD64:)
  -ggdb3 -DSMALL_CELL_SIZE=64 -DHAVE_I64

```

  2. Cd into the directory where hlds_run is located. Type the following line into your shell/command line: ```
export LD_LIBRARY_PATH=".:$LD_LIBRARY_PATH"
```

  3. Make sure you have GDB (GNU Debugger installed). Enter the debugger: ```
gdb hlds_i686
  (or on AMD64)
gdb hlds_amd64

```

  4. Load HLDS: ```
run +maxplayers 16 +map de_dust -game cstrike -debug
```

  5. Cause your module to crash, or hit a previously specified breakpoint.
  6. Now you can use the GNU Debugger to view a call stack with any of these commands: ```
bt
where
backtrace

```

  7. Or if you want a more advanced diagnostic: ```
info all-registers
```


For both debuggers, there are many more options for powerful debugging. It is best to consult the manuals to see how to use them.
