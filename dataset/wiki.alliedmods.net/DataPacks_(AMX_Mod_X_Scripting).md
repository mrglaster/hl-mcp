# DataPacks (AMX Mod X Scripting)
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/DataPacks_\(AMX_Mod_X_Scripting\)#mw-head), [search](https://wiki.alliedmods.net/DataPacks_\(AMX_Mod_X_Scripting\)#p-search)
**Language:** |  **English**  
---|---  
  

## Contents
  * [1 About](https://wiki.alliedmods.net/DataPacks_\(AMX_Mod_X_Scripting\)#About)
  * [2 Usage](https://wiki.alliedmods.net/DataPacks_\(AMX_Mod_X_Scripting\)#Usage)
    * [2.1 Creating & Disposing](https://wiki.alliedmods.net/DataPacks_\(AMX_Mod_X_Scripting\)#Creating_.26_Disposing)
    * [2.2 Resetting](https://wiki.alliedmods.net/DataPacks_\(AMX_Mod_X_Scripting\)#Resetting)
    * [2.3 Writing data](https://wiki.alliedmods.net/DataPacks_\(AMX_Mod_X_Scripting\)#Writing_data)
    * [2.4 Reading data](https://wiki.alliedmods.net/DataPacks_\(AMX_Mod_X_Scripting\)#Reading_data)
    * [2.5 Managing position](https://wiki.alliedmods.net/DataPacks_\(AMX_Mod_X_Scripting\)#Managing_position)
  * [3 Example](https://wiki.alliedmods.net/DataPacks_\(AMX_Mod_X_Scripting\)#Example)


## About
Datapacks provide a way to store and move around arbitrary amounts (and types) of data in AMX Mox X, available from [datapack.inc](https://github.com/alliedmodders/amxmodx/blob/master/plugins/include/datapack.inc).   
Data is packed into a single cell value - the `DataPack` handle. This handle can be passed around more easily, can be returned by functions and can simulate advanced concepts like string consummation. 
## Usage
### Creating & Disposing
`DataPack:CreateDataPack()`     Creates a new datapack.     
**Return:** New datapack handle, which must be freed via `DestroyDataPack`.     
**Important:** Plugins are responsible for freeing all datapack handles they acquire. Failing to free handles will result in the plugin and AMXX leaking memory.     
**Example:**`new const DataPack:handle = CreateDataPack();`
`DestroyDataPack(&DataPack:pack)`     Destroys the datapack and frees its memory.      `pack` |  Datapack handle to free.   
---|---       
**Note:**`pack` will be reset to 0.     
**Example:**`DestroyDataPack(pack);`
### Resetting
`ResetPack(DataPack:pack, bool:clear = false)`     Resets the datapack read/write position to the start.      `clear` |  If true, clears the contained data.   
---|---       
**Attention:** You need to reset the datapack before reading data.     
**Example:**`ResetPack(pack);`
### Writing data
`WritePackCell(DataPack:pack, any:cell)`     Packs a cell value into a datapack.     
**Example:**`WritePackCell(pack, 42);`
`WritePackFloat(DataPack:pack, Float:val)`     Packs a float value into a datapack.     
**Example:**`WritePackFloat(pack, 13.36);`
`WritePackString(DataPack:pack, const str[])`     Packs a string value into a datapack.     
**Return:** Length of copied string.     
**Example:**`new const length = WritePackString(pack, "Hello world!");`
### Reading data
`bool:IsPackEnded(DataPack:pack)`     Returns if the datapack has reached its end and no more data can be read.     
**Return:** True if datapack has reached the end, false otherwise.     
**Example:**`if (IsPackEnded(pack)) {}`
`any:ReadPackCell(DataPack:pack)`     Reads a cell from a Datapack.     
**Attention:** You need to reset the datapack before reading data.     
**Return:** Cell value.     
**Example:**`new value = ReadPackCell(pack);`
`Float:ReadPackFloat(DataPack:pack)`     Reads a float from a Datapack.     
**Attention:** You need to reset the datapack before reading data.     
**Return:** Float value.     
**Example:**`new Float:value = ReadPackFloat(pack);`     
`ReadPackString(DataPack:pack, buffer[], maxlen)`     Reads a string from a Datapack.     
**Attention:** You need to reset the datapack before reading data.     
**Return:** Number of cells written to buffer.     
**Example:**`new buffer[32];  
new const length = ReadPackString(pack, buffer, charsmax(buffer));`
### Managing position
`DataPackPos:GetPackPosition(DataPack:pack)`     Returns the datapack read/write position.     
**Return:** Position in the datapack, only usable with calls to `SetPackPosition`.     
**Example:**`new const DataPackPos:position = GetPackPosition(pack);`
`SetPackPosition(DataPack:pack, DataPackPos:position)`     Sets the datapack read/write position.     
**Attention:** This should only ever be used with (known to be valid) positions returned by `GetPackPosition`. It is not possible for plugins to safely compute datapack positions.     
**Example:**`SetPackPosition(pack, position);`
## Example
```
foo()
{
    // Creating
    new const DataPack:pack = CreateDataPack();
 
    // Writing
    WritePackCell(pack, refCell);
    WritePackFloat(pack, refFloat);
    WritePackString(pack, refString);
 
    // Reset before reading
    ResetPack(pack);
    server_print("Datapack is readable: %s", !IsPackEnded(pack) ? "yes" : "no");
 
    // Reading
    new cellValue = ReadPackCell(pack);
    new Float:floatValue = ReadPackFloat(pack);
    new buffer[32];
    ReadPackString(pack, buffer, charsmax(buffer));
    server_print("cellValue = %d, floatValue = %f, buffer = %s", cellValue, floatValue, buffer)
    server_print("Datapack is no more readable: %s", IsPackEnded(pack) ? "yes" : "no");
 
    // Clear all data
    ResetPack(pack, .clear = true);
    server_print("Datapack is empty: %s", IsPackEnded(pack) ? "yes" : "no");
 
    // Disposing
    DestroyDataPack(pack);
}
```

