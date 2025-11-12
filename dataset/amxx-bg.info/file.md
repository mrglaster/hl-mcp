# Functions in file.inc
Function | Description  
---|---  
[read_dir](https://amxx-bg.info/api/file/read_dir) | ```
Reads content from directory
```
  
[read_file](https://amxx-bg.info/api/file/read_file) | ```
Reads line from file.
```
  
[write_file](https://amxx-bg.info/api/file/write_file) | ```
Writes text to file.
```
  
[delete_file](https://amxx-bg.info/api/file/delete_file) | ```
Deletes a file.
```
  
[file_exists](https://amxx-bg.info/api/file/file_exists) | ```
Checks if a file exists.
```
  
[rename_file](https://amxx-bg.info/api/file/rename_file) | ```
Renames a file.
```
  
[dir_exists](https://amxx-bg.info/api/file/dir_exists) | ```
Checks if a directory exists.
```
  
[file_size](https://amxx-bg.info/api/file/file_size) | ```
Get the file size in bytes.
```
  
[fopen](https://amxx-bg.info/api/file/fopen) | ```
Opens or creates a file, returning a file handle on success. File handles
should be closed with fclose().
```
  
[fclose](https://amxx-bg.info/api/file/fclose) | ```
Closes a file handle.
```
  
[fread](https://amxx-bg.info/api/file/fread) | ```
Reads a single binary data from a file.
```
  
[fread_blocks](https://amxx-bg.info/api/file/fread_blocks) | ```
Reads binary data from a file.
```
  
[fread_raw](https://amxx-bg.info/api/file/fread_raw) | ```
Reads raw binary data from a file.
```
  
[fwrite](https://amxx-bg.info/api/file/fwrite) | ```
Writes a single binary data to a file.
```
  
[fwrite_blocks](https://amxx-bg.info/api/file/fwrite_blocks) | ```
Writes binary data to a file.
```
  
[fwrite_raw](https://amxx-bg.info/api/file/fwrite_raw) | ```
Writes raw binary data to a file.
```
  
[feof](https://amxx-bg.info/api/file/feof) | ```
Tests if the end of file has been reached.
```
  
[fgets](https://amxx-bg.info/api/file/fgets) | ```
Reads a line from a text file.
```
  
[fputs](https://amxx-bg.info/api/file/fputs) | ```
Writes a line of text to a text file.
```
  
[fprintf](https://amxx-bg.info/api/file/fprintf) | ```
Writes a line of formatted text to a text file.
```
  
[fseek](https://amxx-bg.info/api/file/fseek) | ```
Sets the file position indicator.
```
  
[ftell](https://amxx-bg.info/api/file/ftell) | ```
Gets current position in the file.
```
  
[fgetc](https://amxx-bg.info/api/file/fgetc) | ```
Gets character from file.
```
  
[fputc](https://amxx-bg.info/api/file/fputc) | ```
Writes character to file
```
  
[fungetc](https://amxx-bg.info/api/file/fungetc) | ```
Ungets character from file.
```
  
[fflush](https://amxx-bg.info/api/file/fflush) | ```
Flushes a buffered output stream.
```
  
[filesize](https://amxx-bg.info/api/file/filesize) | ```
Gets the formatted file size in bytes.
```
  
[rmdir](https://amxx-bg.info/api/file/rmdir) | ```
Removes a directory.
```
  
[mkdir](https://amxx-bg.info/api/file/mkdir) | ```
Creates a directory.
```
  
[unlink](https://amxx-bg.info/api/file/unlink) | ```
Deletes a file (delete_file macro)
```
  
[open_dir](https://amxx-bg.info/api/file/open_dir) | ```
Opens a directory/folder for contents enumeration.
```
  
[next_file](https://amxx-bg.info/api/file/next_file) | ```
Reads the next directory entry as a local filename.
```
  
[close_dir](https://amxx-bg.info/api/file/close_dir) | ```
Closes the directory.
```
  
[LoadFileForMe](https://amxx-bg.info/api/file/LoadFileForMe) | ```
Loads a file using the LoadFileForMe engine function.

The data is truncated if there is not enough space.  No null-terminator
is applied; the data is the raw contents of the file.
```
  
[GetFileTime](https://amxx-bg.info/api/file/GetFileTime) | ```
Returns a file timestamp as a unix timestamp.
```
  
[SetFilePermissions](https://amxx-bg.info/api/file/SetFilePermissions) | ```
Changes a file or directories permissions.
```
  
[FileReadInt8](https://amxx-bg.info/api/file/FileReadInt8) | ```
Reads a single int8 (byte) from a file. The returned value is sign-
extended to an int32.
```
  
[FileReadUint8](https://amxx-bg.info/api/file/FileReadUint8) | ```
Reads a single uint8 (unsigned byte) from a file. The returned value is
zero-extended to an int32.
```
  
[FileReadInt16](https://amxx-bg.info/api/file/FileReadInt16) | ```
Reads a single int16 (short) from a file. The value is sign-extended to
an int32.
```
  
[FileReadUint16](https://amxx-bg.info/api/file/FileReadUint16) | ```
Reads a single unt16 (unsigned short) from a file. The value is zero-
extended to an int32.
```
  
[FileReadInt32](https://amxx-bg.info/api/file/FileReadInt32) | ```
Reads a single int32 (int/cell) from a file.
```
  
[FileWriteInt8](https://amxx-bg.info/api/file/FileWriteInt8) | ```
Writes a single int8 (byte) to a file.
```
  
[FileWriteInt16](https://amxx-bg.info/api/file/FileWriteInt16) | ```
Writes a single int16 (short) to a file.
```
  
[FileWriteInt32](https://amxx-bg.info/api/file/FileWriteInt32) | ```
Writes a single int32 (int/cell) to a file.
```
  

This code is a part of file.inc. To use this code you should include file.inc as ```#include <file>```


  
  

