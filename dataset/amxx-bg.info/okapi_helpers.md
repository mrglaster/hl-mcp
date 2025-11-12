# okapi_helpers.inc
```
//
// AMX Mod X, based on AMX Mod by Aleksander Naszko ("OLO").
// Copyright (C) The AMX Mod X Development Team.
//
// This software is licensed under the GNU General Public License, version 3 or higher.
// Additional exceptions apply. For full license details, see LICENSE.txt or visit:
//     https://alliedmods.net/amxmodx-license

//
// Okapi Helpers Include
//

#if defined _okapi_helpers_included
	#endinput
#endif
#define _okapi_helpers_included

#include <okapi_extra>
#include <okapi_memory>


// To get library address
// ------------------------------------------------------------------
//      okapi_get_mod_ptr             okapi_get_engine_ptr
//
// To get library length
// ------------------------------------------------------------------
//      okapi_get_mod_size            okapi_get_engine_size
//
// To find signature and symbol
// ------------------------------------------------------------------
//      okapi_mod_find_sig_at         okapi_engine_find_sig_at
//      okapi_mod_find_sig            okapi_engine_find_sig
//      okapi_mod_find_symbol         okapi_engine_find_symbol
//
// To replace value in memory
// ------------------------------------------------------------------
//      okapi_mod_replace_string      okapi_engine_replace_string
//      okapi_mod_replace_array       okapi_engine_replace_array
//      okapi_mod_replace_int         okapi_engine_replace_int
//      okapi_mod_replace_float       okapi_engine_replace_float
//
// To find value in memory
// ------------------------------------------------------------------
//      okapi_mod_find_string_at      okapi_engine_find_string_at
//      okapi_mod_find_string         okapi_engine_find_string
//      okapi_mod_find_array_at       okapi_engine_find_array_at
//      okapi_mod_find_array          okapi_engine_find_array
//      okapi_mod_find_int_at         okapi_engine_find_int_at
//      okapi_mod_find_int            okapi_engine_find_int
//      okapi_mod_find_float_at       okapi_engine_find_float_at
//      okapi_mod_find_float          okapi_engine_find_float
//      okapi_mod_find_byte_at        okapi_engine_find_byte_at
//      okapi_mod_find_byte           okapi_engine_find_byte
//
// To get/set value in memory
// --------------------------
//      okapi_get_ptr_ent             okapi_set_ptr_ent
//      okapi_get_ptr_edict           okapi_set_ptr_edict
//      okapi_get_ptr_cbase           okapi_set_ptr_cbase
//      okapi_get_ptr_int             okapi_set_ptr_int
//      okapi_get_ptr_float           okapi_set_ptr_byte
//      okapi_get_ptr_byte            okapi_set_ptr_float
//      okapi_get_ptr_array           okapi_set_ptr_array
//      okapi_get_ptr_strning         okapi_set_ptr_string
//
// To convert address <-> offset
// ------------------------------------------------------------------
//      okapi_mod_get_offset_ptr      okapi_engine_get_offset_ptr
//      okapi_mod_get_ptr_offset      okapi_engine_get_ptr_offset


// To get library address
// ----------------------

	/**
	 * Gets the base address of where the mod library is allocated in memory.
	 *
	 * @return          Base address on success, 0 otherwise.
	 *
	 */
	stock okapi_get_mod_ptr()
	{
		static address;

		if (!address)
		{
			address = okapi_get_library_ptr("mod");
		}

		return address;
	}

	/**
	 * Gets the base address of where the engine library is allocated in memory.
	 *
	 * @return          Base address on success, 0 otherwise.
	 */
	stock okapi_get_engine_ptr()
	{
		static address;

		if (!address)
		{
			address = okapi_get_library_ptr("engine");
		}

		return address;
	}


// To get library length
// ---------------------

	/**
	 * Gets the length of the mod library
	 *
	 * @return          Number of bytes on succes, otherwise 0.
	 */
	stock okapi_get_mod_size()
	{
		static size;

		if (!size)
		{
			size = okapi_get_library_size("mod");
		}

		return size;
	}

	/**
	 * Gets the length of the mod library.
	 *
	 * @return          Number of bytes on succes, otherwise 0.
	 */
	stock okapi_get_engine_size()
	{
		static size;

		if (!size)
		{
			size = okapi_get_library_size("engine");
		}

		return size;
	}


// To find signature and symbol
// ----------------------------

	/**
	 * Searches for a signature in the mod library from a given address.
	 *
	 * @param start_address     Start address
	 * @param signature[]       Signature to find
	 * @param count             Size of the signature
	 *
	 * @return                  Address where the sig was first found, 0 otherwise
	 */
	stock okapi_mod_find_sig_at(start_address, const signature[], count = sizeof signature)
	{
		return okapi_find_sig(start_address, start_address + (okapi_get_mod_size() - (start_address - okapi_get_mod_ptr())), signature, count);
	}

	/**
	 * Searches for a signature in the mod library.
	 *
	 * @param signature[]       Signature to find
	 * @param count             Size of the signature
	 *
	 * @return                  Address where the sig was first found, 0 otherwise
	 */
	stock okapi_mod_find_sig(const signature[], count = sizeof signature)
	{
		return okapi_find_sig(okapi_get_mod_ptr(), okapi_get_mod_size(), signature, count);
	}

	/**
	 * Searches for a signature in the engine library from a given address.
	 *
	 * @param start_address     Start address
	 * @param signature[]       Signature to find
	 * @param count             Size of the signature
	 *
	 * @return                  Address where the sig was first found, 0 otherwise
	 */
	stock okapi_engine_find_sig_at(start_address, const signature[], count = sizeof signature)
	{
		return okapi_find_sig(okapi_get_engine_ptr(), start_address + (okapi_engine_mod_size() - (start_address - okapi_engine_mod_address())), signature, count);
	}

	/**
	 * Searches for a signature in the engine library.
	 *
	 * @param signature[]       Signature to find
	 * @param count             Size of the signature
	 *
	 * @return                  Address where the sig was first found, 0 otherwise
	 */
	stock okapi_engine_find_sig(const signature[], count = sizeof signature)
	{
		return okapi_engine_find_sig_at(okapi_get_engine_ptr(), okapi_get_engine_size(), signature, count);
	}

	/**
	 * Gets the address of a function located in mod library, given it's symbolic name.
	 *
	 * @param symbol        Symbolic name of a function
	 *
	 * @return              Address of the function on success, 0 otherwise
	 */
	stock okapi_mod_find_symbol(const symbol[])
	{
		return okapi_find_symbol(okapi_get_mod_ptr(), symbol);
	}

	/**
	 * Gets the address of a function located in engine library, given it's symbolic name.
	 *
	 * @param symbol        Symbolic name of a function
	 *
	 * @return              Address of the function on success, 0 otherwise
	 */
	stock okapi_engine_find_symbol(const symbol[])
	{
		return okapi_find_symbol(okapi_get_engine_ptr(), symbol);
	}


// To replace value in memory
// --------------------------

	/**
	 * Replaces every string that occurs in the mod library with another one.
	 *
	 * @note The replacement string should be of equal or shorter size than the original.
	 *       If you know what you are doing and want to skip this check, make force to 1.
	 *
	 * @param str_orig[]        Original string
	 * @param str_replace[]     Replacement string
	 * @param force             Setting to 1 will skip the restrition of the string replacement size
	 *
	 * @return                  Number of replacements ocurred on success, 0 otherwise.
	 * @error                   Invalid replacement string length
	 */
	stock okapi_mod_replace_string(const str_orig[], const str_replace[], force = 0)
	{
		return okapi_mem_replace(okapi_get_mod_ptr(), okapi_get_mod_size(), okapi_mem_string, str_orig, str_replace, force);
	}

	/**
	 * Replaces every ocurrence of the sequence of bytes given, in the mod library, with other sequence.
	 *
	 * @param arr_orig[]        Original array
	 * @param arr_replace[]     Replacement array
	 * @param arr_len           Number of bytes to replace
	 *
	 * @return                  Number of replacements ocurred on success, 0 otherwise.
	 */
	stock okapi_mod_replace_array(any:arr_orig[], any:arr_replace[], arr_len)
	{
		return okapi_mem_replace(okapi_get_mod_ptr(), okapi_get_mod_size(), okapi_mem_array, arr_orig, arr_replace, arr_len);
	}

	/**
	 * Replaces every ocurrence of the integer given, in the mod library, with other integer.
	 *
	 * @param val_search        Original value
	 * @param val_replace       Replacement value
	 *
	 * @return                  Number of replacements ocurred on success, 0 otherwise.
	 */
	stock okapi_mod_replace_int(any:val_search, any:val_replace)
	{
		return okapi_mem_replace(okapi_get_mod_ptr(), okapi_get_mod_size(), okapi_mem_int, val_search, val_replace);
	}

	/**
	 * Replaces every ocurrence of the float given, in the mod library, with other float.
	 *
	 * @param val_search        Original value
	 * @param val_replace       Replacement value
	 *
	 * @return                  Number of replacements ocurred on success, 0 otherwise.
	 */
	stock okapi_mod_replace_float(Float:val_search,Float:val_replace)
	{
		return okapi_mem_replace(okapi_get_mod_ptr(), okapi_get_mod_size(), okapi_mem_float, val_search, val_replace);
	}

	/**
	 * Replaces every string that occurs in the engine library with another one.
	 *
	 * @note The replacement string should be of equal or shorter size than the original.
	 *       If you know what you are doing and want to skip this check, make force to 1.
	 *
	 * @param str_orig[]        Original string
	 * @param str_replace[]     Replacement string
	 * @param force             Setting to 1 will skip the restrition of the string replacement size
	 *
	 * @return                  Number of replacements ocurred on success, 0 otherwise.
	 * @error                   Invalid replacement string length
	 */
	stock okapi_engine_replace_string(const str_orig[], const str_replace[], force = 0)
	{
		return okapi_mem_replace(okapi_get_engine_ptr(), okapi_get_engine_size(), okapi_mem_string, str_orig, str_replace, force);
	}

	/**
	 * Replaces every ocurrence of the sequence of bytes given, in the engine library, with other sequence.
	 *
	 * @param arr_orig[]        Original array
	 * @param arr_replace[]     Replacement array
	 * @param arr_len           Number of bytes to replace
	 *
	 * @return                  Number of replacements ocurred on success, 0 otherwise.
	 */
	stock okapi_engine_replace_array(any:arr_orig[], any:arr_replace[], arr_len)
	{
		return okapi_mem_replace(okapi_get_engine_ptr(), okapi_get_engine_size(), okapi_mem_array, str_orig, str_replace, arr_len);
	}

	/**
	 * Replaces every ocurrence of the integer given, in the engine library, with other integer.
	 *
	 * @param val_search        Original value
	 * @param val_replace       Replacement value
	 *
	 * @return                  Number of replacements ocurred on success, 0 otherwise.
	 */
	stock okapi_engine_replace_int(any:val_search, any:val_replace)
	{
		return okapi_mem_replace(okapi_get_engine_ptr(), okapi_get_engine_size(), okapi_mem_int, val_search, val_replace);
	}

	/**
	 * Replaces every ocurrence of the float given, in the engine library, with other float.
	 *
	 * @param val_search        Original value
	 * @param val_replace       Replacement value
	 *
	 * @return                  Number of replacements ocurred on success, 0 otherwise.
	 */
	stock okapi_engine_replace_float(Float:val_search,Float:val_replace)
	{
		return okapi_mem_replace(okapi_get_engine_ptr(), okapi_get_engine_size(), okapi_mem_float, val_search, val_replace);
	}


// To find value in memory
// -----------------------

	/**
	 * Searches for a string in the mod library, starting from a given address.
	 *
	 * @param ptr               Start address
	 * @param str[]             String to find
	 *
	 * @return                  Address where the first string was found, 0 otherwise.
	 */
	stock okapi_mod_find_string_at(ptr, const str[])
	{
		return okapi_mem_find(ptr, ptr + (okapi_get_mod_size() - (ptr - okapi_get_mod_ptr())), mem_type_string, str);
	}

		/**
		 * Searches for a string in the mod library.
		 *
		 * @param str[]             String to find
		 *
		 * @return                  Address where the first string was found, 0 otherwise.
		 */
		stock okapi_mod_find_string(const str[])
		{
			return okapi_mod_find_string_at(okapi_mod_get_base_ptr(), str);
		}

	/**
	 * Searches for an array of bytes in the mod library, starting from a given address.
	 *
	 * @param ptr               Start address
	 * @param array_            Array to find
	 * @param count             Number of bytes
	 *
	 * @return                  Address where the first array was found, 0 otherwise.
	 */
	stock okapi_mod_find_array_at(ptr, any:array[], count)
	{
		return okapi_mem_find(ptr, ptr + (okapi_get_mod_size() - (ptr - okapi_get_mod_ptr())), mem_type_array, array_, count);
	}

		/**
		 * Searches for an array of bytes in the mod library.
		 *
		 * @param array_            Array to find
		 * @param count             Number of bytes
		 *
		 * @return                  Address where the first array was found, 0 otherwise.
		 */
		stock okapi_mod_find_array(any:array[], count)
		{
			return okapi_mod_find_string_at(okapi_mod_get_base_ptr(), array_, count);
		}

	/**
	 * Searches for an integer in the mod library, starting from a given address.
	 *
	 * @param ptr               Start address
	 * @param val               Integer to find
	 *
	 * @return                  Address where the first integer was found, 0 otherwise.
	 */
	stock okapi_mod_find_int_at(ptr, any:val)
	{
		return okapi_mem_find(ptr, ptr + (okapi_get_mod_size() - (ptr - okapi_get_mod_ptr())), mem_type_int, val);
	}

		/**
		 * Searches for a integer in the mod library.
		 *
		 * @param val               Integer to find
		 *
		 * @return                  Address where the first integer was found, 0 otherwise.
		 */
		stock okapi_mod_find_int(any:val)
		{
			return okapi_mod_find_int_at(okapi_mod_get_base_ptr(), val);
		}

	/**
	 * Searches for a float in the mod library, starting from a given address.
	 *
	 * @param ptr               Start address
	 * @param val               Float to find
	 *
	 * @return                  Address where the first float was found, 0 otherwise.
	 */
	stock okapi_mod_find_float_at(ptr, Float:value)
	{
		return okapi_mem_find(ptr, ptr + (okapi_get_mod_size() - (ptr - okapi_get_mod_ptr())), mem_type_float, value);
	}

		/**
		 * Searches for a flaot in the mod library.
		 *
		 * @param val               Float to find
		 *
		 * @return                  Address where the first float was found, 0 otherwise.
		 */
		stock okapi_mod_find_float(Float:value)
		{
			return okapi_mod_find_float_at(okapi_mod_get_base_ptr(), value);
		}

	/**
	 * Searches for a byte in the mod library, starting from a given address.
	 *
	 * @param ptr               Start address
	 * @param val               Byte to find
	 *
	 * @return                  Address where the first byte was found, 0 otherwise.
	 */
	stock okapi_mod_find_byte_at(ptr, any:value)
	{
		return okapi_mem_find(ptr, ptr + (okapi_get_mod_size() - (ptr - okapi_get_mod_ptr())), mem_type_byte, value);
	}

		/**
		 * Searches for a byte in the mod library.
		 *
		 * @param val               Byte to find
		 *
		 * @return                  Address where the first byte was found, 0 otherwise.
		 */
		stock okapi_mod_find_byte(any:value)
		{
			return okapi_mod_find_byte_at(okapi_mod_get_base_ptr(), value);
		}

	/**
	 * Searches for a string in the engine library, starting from a given address.
	 *
	 * @param ptr               Start address
	 * @param str[]             String to find
	 *
	 * @return                  Address where the first string was found, 0 otherwise.
	 */
	stock okapi_engine_find_string_at(ptr, const str[])
	{
		return okapi_mem_find(ptr, ptr + (okapi_get_engine_size() - (ptr - okapi_get_engine_ptr())), mem_type_string, str);
	}

		/**
		 * Searches for a string in the engine library.
		 *
		 * @param str[]             String to find
		 *
		 * @return                  Address where the first string was found, 0 otherwise.
		 */
		stock okapi_engine_find_string(const str[])
		{
			return okapi_engine_find_string_at(okapi_engine_get_base_ptr(), str);
		}

	/**
	 * Searches for an array of bytes in the engine library, starting from a given address.
	 *
	 * @param ptr               Start address
	 * @param array_            Array to find
	 * @param count             Number of bytes
	 *
	 * @return                  Address where the first array was found, 0 otherwise.
	 */
	stock okapi_engine_find_array_at(ptr, any:array[], count)
	{
		return okapi_mem_find(ptr, ptr + (okapi_get_engine_size() - (ptr - okapi_get_engine_ptr())), mem_type_array, array_, count);
	}

		/**
		 * Searches for an array of bytes in the engine library.
		 *
		 * @param array_            Array to find
		 * @param count             Number of bytes
		 *
		 * @return                  Address where the first array was found, 0 otherwise.
		 */
		stock okapi_engine_find_array(any:array[], count)
		{
			return okapi_engine_find_string_at(okapi_engine_get_base_ptr(), array_, count);
		}

	/**
	 * Searches for an integer in the engine library, starting from a given address.
	 *
	 * @param ptr               Start address
	 * @param val               Integer to find
	 *
	 * @return                  Address where the first integer was found, 0 otherwise.
	 */
	stock okapi_engine_find_int_at(ptr, any:val)
	{
		return okapi_mem_find(ptr, ptr + (okapi_get_engine_size() - (ptr - okapi_get_engine_ptr())), mem_type_int, val);
	}

		/**
		 * Searches for a integer in the engine library.
		 *
		 * @param val               Integer to find
		 *
		 * @return                  Address where the first integer was found, 0 otherwise.
		 */
		stock okapi_engine_find_int(any:val)
		{
			return okapi_engine_find_int_at(okapi_engine_get_base_ptr(), val);
		}

	/**
	 * Searches for a float in the engine library, starting from a given address.
	 *
	 * @param ptr               Start address
	 * @param val               Float to find
	 *
	 * @return                  Address where the first float was found, 0 otherwise.
	 */
	stock okapi_engine_find_float_at(ptr, Float:value)
	{
		return okapi_mem_find(ptr, ptr + (okapi_get_engine_size() - (ptr - okapi_get_engine_ptr())), mem_type_float, value);
	}

		/**
		 * Searches for a flaot in the engine library.
		 *
		 * @param val               Float to find
		 *
		 * @return                  Address where the first float was found, 0 otherwise.
		 */
		stock okapi_engine_find_float(Float:value)
		{
			return okapi_mod_find_float_at(okapi_engine_get_base_ptr(), value);
		}

	/**
	 * Searches for a byte in the engine library, starting from a given address.
	 *
	 * @param ptr               Start address
	 * @param val               Byte to find
	 *
	 * @return                  Address where the first byte was found, 0 otherwise.
	 */
	stock okapi_engine_find_byte_at(ptr, any:value)
	{
		return okapi_mem_find(ptr, ptr + (okapi_get_engine_size() - (ptr - okapi_get_engine_ptr())), mem_type_byte, value);
	}

		/**
		 * Searches for a byte in the engine library.
		 *
		 * @param val               Byte to find
		 *
		 * @return                  Address where the first byte was found, 0 otherwise.
		 */
		stock okapi_engine_find_byte(any:value)
		{
			return okapi_engine_find_byte_at(okapi_engine_get_base_ptr(), value);
		}


// To get/set value in memory
// --------------------------

	/**
	 * Sets the value of the location pointed by the address with the entvars relative to an entity represented by id.
	 *
	 * @param ptr           Address where is located the value
	 * @param id            Entity index
	 */
	stock okapi_set_ptr_ent(ptr, id)
	{
		return okapi_mem_set(ptr, mem_type_entvars, id);
	}

	/**
	 * Retrieves the entvars located in an address as an entity index.
	 *
	 * @param ptr           Address where is located the value
	 * @return              Entity index
	 */
	stock okapi_get_ptr_ent(ptr)
	{
		return okapi_mem_get(ptr, mem_type_entvars);
	}

	/**
	 * Sets the value of the location pointed by the address with the edict relative to an entity represented by id.
	 *
	 * @param ptr           Address where is located the value
	 * @param id            Entity index to set
	 */
	stock okapi_set_ptr_edict(ptr, id)
	{
		return okapi_mem_set(ptr, mem_type_edict, id);
	}

	/**
	 * Retrieves the edict located in an address as an entity id.
	 *
	 * @param ptr           Address where is located the value
	 * @return              Entity index
	 */
	stock okapi_get_ptr_edict(ptr)
	{
		return okapi_mem_get(ptr, mem_type_edict);
	}

	/**
	 * Sets the value of the location pointed by the address with the cbase relative to an entity represented by id.
	 *
	 * @param ptr           Address where is located the value
	 * @param id            Entity index to set
	 */
	stock okapi_set_ptr_cbase(ptr, id)
	{
		return okapi_mem_set(ptr, mem_type_cbase, id);
	}

	/**
	 * Retrieves the cbase located in an address as an entity id.
	 *
	 * @param ptr           Address where is located the value
	 * @return              Entity index
	 */
	stock okapi_get_ptr_cbase(ptr)
	{
		return okapi_mem_get(ptr, mem_type_cbase);
	}

	/**
	 * Writes an integer value at the location pointed by the address.
	 *
	 * @param ptr           Address where is located the value
	 * @param value         Value to set
	 */
	stock okapi_set_ptr_int(ptr, value)
	{
		return okapi_mem_set(ptr, mem_type_int, value);
	}

	/**
	 * Retrieves an integer value in the location pointed by the address.
	 *
	 * @param ptr           Address where is located the value
	 * @return              Integer value
	 */
	stock okapi_get_ptr_int(ptr)
	{
		return okapi_mem_get(ptr, mem_type_int);
	}

	/**
	 * Writes a byte value at the location pointed by the address.
	 *
	 * @param ptr           Address where is located the value
	 * @param value         Value to set
	 */
	stock okapi_set_ptr_byte(ptr, value)
	{
		return okapi_mem_set(ptr, mem_type_byte, value);
	}

	/**
	 * Retrieves a byte value in the location pointed by the address.
	 *
	 * @param ptr           Address where is located the value
	 * @return              Byte value
	 */
	stock okapi_get_ptr_byte(ptr)
	{
		return okapi_mem_get(ptr, mem_type_byte);
	}

	/**
	 * Writes a float value at the location pointed by the address.
	 *
	 * @param ptr           Address where is located the value
	 * @param value         Value to set
	 */
	stock okapi_set_ptr_float(ptr, Float:value)
	{
		return okapi_mem_set(ptr, mem_type_float, value);
	}

	/**
	 * Retrieves a float value in the location pointed to by the address.
	 *
	 * @param ptr           Address where is located the value
	 * @return              Float value
	 */
	stock Float:okapi_get_ptr_float(ptr)
	{
		return okapi_mem_get(ptr, mem_type_float);
	}

	/**
	 * Writes an array of bytes to the location pointed to by the address.
	 *
	 * @param ptr           Address where is located the value
	 * @param holder        Array with the bytes to write
	 * @param count         Number of bytes to write
	 */
	stock okapi_set_ptr_array(ptr, holder[], count)
	{
		return okapi_mem_set(ptr, mem_type_array, holder, count);
	}

	/**
	 * Retrieves an array of bytes in the location pointed to by the address
	 *
	 * @param ptr           Address where is located the value
	 * @param holder        Array where the bytes will be stored
	 * @param count         Number of bytes to retrieve
	 */
	stock okapi_get_ptr_array(ptr, holder[], count)
	{
		return okapi_mem_get(ptr, mem_type_array, holder, count);
	}

	/**
	 * Writes a vector to the location pointed to by the address.
	 *
	 * @param ptr           Address where is located the value
	 * @param vec           Variable where the vector will be retrieved from
	 */
	stock okapi_set_ptr_vec(ptr, Float:vec[3])
	{
		return okapi_mem_set(ptr, mem_type_vector, vec);
	}

	/**
	 * Retrieves an array of bytes in the location pointed to by the address.
	 *
	 * @param ptr           Address where is located the value
	 * @param vec           Variable where the vector will be wrote to
	 */
	stock okapi_get_ptr_vec(ptr, Float:vec[3])
	{
		return okapi_mem_get(ptr, mem_type_vector, vec);
	}

	/**
	 * Writes a string to the location pointed to by the address.
	 *
	 * @param ptr           Address where is located the value
	 * @param str           String to write
	 */
	stock okapi_set_ptr_string(ptr, const str[])
	{
		return okapi_mem_set(ptr, mem_type_string, str);
	}

	/**
	 * Retrieves an string from the location pointed to by the address.
	 *
	 * @param ptr           Address where is located the value
	 * @param str[]         Variable where the string will be stored
	 * @param len           Limit of chars to retrieve
	 *
	 * @return              Number of chars retrieved
	 */
	stock okapi_get_ptr_string(ptr, str[], len)
	{
		return okapi_mem_get(ptr, mem_type_string, str, len);
	}


// To convert address <-> offset
// -----------------------------

	/**
	 * Gets the address of an offset relative to mod library.
	 *
	 * @param ptr       Offset to convert
	 *
	 * @return          Address of the offset in the mod library on success, 0 otherwise.
	 */
	stock okapi_mod_get_offset_ptr(offset)
	{
		if (offset >= 0 && offset < okapi_get_mod_size())
		{
			return okapi_get_mod_ptr() + offset;
		}

		return 0;
	}

	/**
	 * Gets the address of an offset relative to engine library.
	 *
	 * @param ptr       Offset to convert
	 *
	 * @return          Address of the offset in the engine library on success, 0 otherwise.
	 */
	stock okapi_engine_get_offset_ptr(offset)
	{
		if (offset >= 0 && offset < okapi_get_engine_size())
		{
			return okapi_get_engine_ptr() + offset;
		}

		return 0;
	}

	/**
	 * Gets the offset of an address relative to mod library.
	 *
	 * @param ptr       Address to convert
	 *
	 * @return          Offset of the address in the engine library on success, 0 otherwise.
	 */
	stock okapi_mod_get_ptr_offset(ptr)
	{
		new offset = ptr - okapi_get_mod_ptr();

		if (offset >= 0 && offset < okapi_get_mod_size())
		{
			return offset;
		}

		return 0;
	}

	/**
	 * Gets the offset of an address relative to engine library.
	 *
	 * @param ptr       Address to convert
	 *
	 * @return          Offset of the address in the engine library on success, 0 otherwise.
	 */
	stock okapi_engine_get_ptr_offset(ptr)
	{
		new offset = ptr - okapi_get_engine_ptr();

		if (offset >= 0 && offset < okapi_get_engine_size())
		{
			return offset;
		}

		return 0;
	}


// To keep backward compatibility
// ------------------------------

	#define okapi_mod_get_size               okapi_get_mod_size
	#define okapi_engine_get_size            okapi_get_engine_size

	#define okapi_mod_get_base_ptr           okapi_get_mod_ptr
	#define okapi_engine_get_base_ptr        okapi_get_engine_ptr

	#define okapi_mod_ptr_find_string_at     okapi_mod_find_string_at
	#define okapi_mod_ptr_find_array_at      okapi_mod_find_array_at
	#define okapi_mod_ptr_find_int_at        okapi_mod_find_int_at
	#define okapi_mod_ptr_find_float_at      okapi_mod_find_float_at
	#define okapi_mod_ptr_find_byte_at       okapi_mod_find_byte_at

	#define okapi_engine_ptr_find_string_at  okapi_engine_find_string_at
	#define okapi_engine_ptr_find_array_at   okapi_engine_find_array_at
	#define okapi_engine_ptr_find_int_at     okapi_engine_find_int_at
	#define okapi_engine_ptr_find_float_at   okapi_engine_find_float_at
	#define okapi_engine_ptr_find_byte_at    okapi_engine_find_byte_at

	#define okapi_mod_get_symbol_ptr         okapi_mod_find_symbol
	#define okapi_engine_get_symbol_ptr      okapi_engine_find_symbol

```


This code is a part of okapi_helpers.inc. To use this code you should include okapi_helpers.inc as ```#include <okapi_helpers>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.