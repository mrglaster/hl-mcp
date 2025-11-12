# okapi_const.inc
```
//
// AMX Mod X, based on AMX Mod by Aleksander Naszko ("OLO").
// Copyright (C) The AMX Mod X Development Team.
//
// This software is licensed under the GNU General Public License, version 3 or higher.
// Additional exceptions apply. For full license details, see LICENSE.txt or visit:
//     https://alliedmods.net/amxmodx-license

//
// Okapi Constants Include
//

#if defined _okapi_const_included
	#endinput
#endif
#define _okapi_const_included

/**
 * Argument and return types
 */
enum okapi_arg
{
	arg_void,
	arg_int,
	arg_cbase,
	arg_float,
	arg_vec,
	arg_entvars,
	arg_string,
	arg_edict,
	arg_vec_ptr
};

/**
 * Memory data types
 */
enum okapi_mem_type
{
	mem_type_int,
	mem_type_byte,
	mem_type_foat,
	mem_type_entvars,
	mem_type_edict,
	mem_type_cbase,
	mem_type_array,
	mem_type_string,
	mem_type_vector,
};

/**
 * Memory protection codes
 */
enum okapi_mem_protect
{
	PAGE_READ  = 1,
	PAGE_WRITE = 2,
	PAGE_EXEC  = 4,
};

/**
 * Return codes
 */
enum okapi_ret
{
	okapi_ret_ignore,
	okapi_ret_override,
	okapi_ret_supercede
};

```


This code is a part of okapi_const.inc. To use this code you should include okapi_const.inc as ```#include <okapi_const>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.