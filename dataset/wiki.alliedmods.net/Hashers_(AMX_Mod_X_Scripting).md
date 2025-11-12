# Hashers (AMX Mod X Scripting)
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Hashers_\(AMX_Mod_X_Scripting\)#mw-head), [search](https://wiki.alliedmods.net/Hashers_\(AMX_Mod_X_Scripting\)#p-search)
**Language:** |  **English** [français](https://wiki.alliedmods.net/Hashers_\(AMX_Mod_X_Scripting\)/fr "Hashers \(AMX Mod X Scripting\)/fr")  
---|---  
  

## Contents
  * [1 About](https://wiki.alliedmods.net/Hashers_\(AMX_Mod_X_Scripting\)#About)
  * [2 Usage](https://wiki.alliedmods.net/Hashers_\(AMX_Mod_X_Scripting\)#Usage)
    * [2.1 Hashes](https://wiki.alliedmods.net/Hashers_\(AMX_Mod_X_Scripting\)#Hashes)
    * [2.2 Natives](https://wiki.alliedmods.net/Hashers_\(AMX_Mod_X_Scripting\)#Natives)


## About
Hashers provide a way to generate a hash value from a string or file content, available in [amxmodx.inc](https://github.com/alliedmodders/amxmodx/tree/master/plugins/include#L2472-L2495). 
**Note:** The following API deprecates `md5` and `md5_file` natives.
## Usage
### Hashes
The available [`HashType` constants](https://github.com/alliedmodders/amxmodx/blob/master/plugins/include/amxconst.inc#L432-L452) are:       `Hash_Crc32` |  Provides CRC32 hashing   
---|---  
`Hash_Md5` |  Provides MD5 hashing   
`Hash_Sha1` |  Provides SHA1 hashing   
`Hash_Sha256` |  Provides SHA256 hashing   
`Hash_Sha3_224` |  Provides SHA3 224 bit hashing   
`Hash_Sha3_256` |  Provides SHA3 256 bit hashing   
`Hash_Sha3_384` |  Provides SHA3 384 bit hashing   
`Hash_Sha3_512` |  Provides SHA3 512 bit hashing   
`Hash_Keccak_224` |  Provides Keccak 224 bit hashing   
`Hash_Keccak_256` |  Provides Keccak 256 bit hashing   
`Hash_Keccak_384` |  Provides Keccak 384 bit hashing   
`Hash_Keccak_512` |  Provides Keccak 512 bit hashing   
### Natives
`hash_string(const string[], const HashType:type, output[], const outputSize)`     Generates a hash value (message digest).      `string` |  String to be hashed.   
---|---  
`type` |  Type of selected hashing algorithm. See `Hash_*` constants above.   
`output` |  Output string to store hash in.   
`outputSize` |  The maximum size of the output string to store hash in.        
**Return:** Number of written bytes.     
**Example:**`new hash[32];  
new const message[] = "Hello World!";  
new const length = hash_string(message, Hash_Md5, hash, charsmax(hash));`
`hash_file(const fileName[], const HashType:type, output[], const outputSize)`     Generates a hash value using the contents of a given file.      `fileName` |  Path of file to be hashed.   
---|---  
`type` |  Type of selected hashing algorithm. See `Hash_*` constants above.   
`output` |  Output string to store hash in.   
`outputSize` |  The maximum size of the output string to store hash in.        
**Return:** Number of written bytes.     
**Note:** Path of file is relative to `$mod/` directory.     
**Example:**`new hash[32];  
new const fileName[] = "server.cfg";  
new const length = hash_file(message, Hash_Md5, hash, charsmax(hash));`
