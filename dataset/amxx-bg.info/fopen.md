# fopen
#### Syntax
```
native fopen(const filename[], const mode[], bool:use_valve_fs = false, const valve_path_id[] = "GAME");
```

#### Usage
filename | ```File to open```
---|---
mode | ```Open mode```
use_valve_fs | ```If true, the Valve file system will be used instead This can be used to finred files existing in valve search paths, rather than solely files existing directly in the gamedir.```
valve_path_id | ```If use_valve_fs, a search path from gameinfo or NULL_STRING for all search paths```
#### Description
```
Opens or creates a file, returning a file handle on success. File handles
should be closed with fclose().
```

#### Note
```
The open mode may be one of the following strings:
  "r": Open an existing file for reading.
  "w": Create a file for writing, or truncate (delete the contents of) an
       existing file and then open it for writing.
  "a": Create a file for writing, or open an existing file such that writes
       will be appended to the end.
 "r+": Open an existing file for both reading and writing.
 "w+": Create a file for reading and writing, or truncate an existing file
       and then open it for reading and writing.
 "a+": Create a file for both reading and writing, or open an existing file
       such that writes will be appended to the end.
```

#### Note
```
The open mode may also contain an additional character after "r", "w", or "a",
but before any "+" sign. This character may be "b" (indicating binary mode) or
"t" (indicating text mode). By default, "text" mode is implied. On Linux and
Mac, this has no distinction from binary mode. On Windows, it causes the '\n'
character (0xA) to be written as "\r\n" (0xD, 0xA).

Example: "rb" opens a binary file for writing; "at" opens a text file for
appending.
```

#### Note
```
Registered paths ID are (in priority order) :
  GAME           All paths related to current mod, including fallback
                 Depending settings, it includes: <gamedir>_lv/_addon/_<language>/_hd
                 and <gamedir> itself
  GAMECONFIG     The default writable directory (<gamedir>)
  GAMEDOWNLOAD   The download directory (<gamedir>_download)
  GAME_FALLBACK  All paths related to fallback game, same as GAME
  DEFAULTGAME    All paths related to the default game which is "valve", same as GAME
  BASE           The base path where server is installed

  Note that some paths are non-writable. It includes all <gamedir>_* (expect _download)
  and DEFAULTGAME. Any file inside a non-writable path will be ignored if you try to open
  it in writing mode.
```

#### Return
```
A file handle, or null if the file could not be opened.
```


This code is a part of file.inc. To use this code you should include file.inc as ```#include <file>```


  
  

