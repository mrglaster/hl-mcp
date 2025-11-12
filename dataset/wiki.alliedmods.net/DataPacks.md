# DataPacks
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/DataPacks#mw-head), [search](https://wiki.alliedmods.net/DataPacks#p-search)
DataPacks are a way to store and move around various types of data in [SourceMod Scripting](https://wiki.alliedmods.net/Category:SourceMod_Scripting "Category:SourceMod Scripting"). Since some things are not possible in SourcePawn, such as a function consuming a String, DataPacks help us get these Strings and other items where they need to go. 
## Contents
  * [1 Example of using a DataPack](https://wiki.alliedmods.net/DataPacks#Example_of_using_a_DataPack)
  * [2 Creating a DataPack](https://wiki.alliedmods.net/DataPacks#Creating_a_DataPack)
  * [3 DataPack Functions](https://wiki.alliedmods.net/DataPacks#DataPack_Functions)
    * [3.1 WritePackCell](https://wiki.alliedmods.net/DataPacks#WritePackCell)
    * [3.2 WritePackFloat](https://wiki.alliedmods.net/DataPacks#WritePackFloat)
    * [3.3 WritePackString](https://wiki.alliedmods.net/DataPacks#WritePackString)
    * [3.4 ReadPackCell](https://wiki.alliedmods.net/DataPacks#ReadPackCell)
    * [3.5 ReadPackFloat](https://wiki.alliedmods.net/DataPacks#ReadPackFloat)
    * [3.6 ReadPackString](https://wiki.alliedmods.net/DataPacks#ReadPackString)
    * [3.7 ResetPack](https://wiki.alliedmods.net/DataPacks#ResetPack)
    * [3.8 GetPackPosition](https://wiki.alliedmods.net/DataPacks#GetPackPosition)
    * [3.9 SetPackPosition](https://wiki.alliedmods.net/DataPacks#SetPackPosition)
  * [4 Disposing of a DataPack](https://wiki.alliedmods.net/DataPacks#Disposing_of_a_DataPack)


# Example of using a DataPack
Syntax: 
```
//writing
DataPack pack = new DataPack();
pack.WriteCell(23);
pack.WriteString("I'm a little teapot.");
 
//reading
pack.Reset(); //resets the index to the beginning, necessary for read.
int cellValue = pack.ReadCell();
char buffer[1024];
pack.ReadString(buffer, 1024);
```

# Creating a DataPack
Creating a DataPack is very simple; all you need is a Handle to write to. 
```
Datapack dataPackHandle = new DataPack();
```

For more information on using Handles, see [Handle API (SourceMod)](https://wiki.alliedmods.net/Handle_API_\(SourceMod\) "Handle API \(SourceMod\)"). 
# DataPack Functions
On you have created your DataPack, you can use a variety of functions to manage the DataPack. 
## WritePackCell
Syntax: 
```
native void WritePackCell(Handle pack, any cell);
```

## WritePackFloat
This function can be used to write a Float to a DataPack. 
Syntax: 
```
native void WritePackFloat(Handle pack, float val);
```

## WritePackString
This function can be used to write a String to a DataPack. 
Syntax: 
```
native void WritePackString(Handle pack, const char[] str);
```

## ReadPackCell
Syntax: 
```
native any ReadPackCell(Handle pack);
```

## ReadPackFloat
This function can be used to read a Float from a DataPack. 
Syntax: 
```
native float ReadPackFloat(Handle pack);
```

## ReadPackString
This function can be used to read a String from a DataPack. 
Syntax: 
```
native void ReadPackString(Handle pack, char[] buffer, maxlen);
```

## ResetPack
This function resets your position in the DataPack. 
Syntax: 
```
native void ResetPack(Handle pack, bool clear=false);
```

## GetPackPosition
This function gets your current position in the DataPack. 
Syntax: 
```
native int GetPackPosition(Handle pack);
```

## SetPackPosition
This function sets your current position in the DataPack. 
Syntax: 
```
native void SetPackPosition(Handle pack, int position);
```

# Disposing of a DataPack
To dispose of a DataPack, all you have to do is close its Handle. 
Example: 
```
CloseHandle(dataPackHandle);
```

