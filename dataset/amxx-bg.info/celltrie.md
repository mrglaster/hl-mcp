# Functions in celltrie.inc
Function | Description  
---|---  
[TrieCreate](https://amxx-bg.info/api/celltrie/TrieCreate) | ```
Creates a hash map. A hash map is a container that maps strings (called keys)
to arbitrary values (cells, arrays or strings).
```
  
[TrieClear](https://amxx-bg.info/api/celltrie/TrieClear) | ```
Clears all entries from a Map.
```
  
[TrieSetCell](https://amxx-bg.info/api/celltrie/TrieSetCell) | ```
Sets a cell value in a hash map, either inserting a new entry or replacing
an old one.
```
  
[TrieSetString](https://amxx-bg.info/api/celltrie/TrieSetString) | ```
Sets a string value in a hash map, either inserting a new entry or replacing
an old one.
```
  
[TrieSetArray](https://amxx-bg.info/api/celltrie/TrieSetArray) | ```
Sets an array value in a hash map, either inserting a new entry or replacing
an old one.
```
  
[TrieGetCell](https://amxx-bg.info/api/celltrie/TrieGetCell) | ```
Retrieves a cell value from a hash map.
```
  
[TrieGetString](https://amxx-bg.info/api/celltrie/TrieGetString) | ```
Retrieves a string from a hash map.
```
  
[TrieGetArray](https://amxx-bg.info/api/celltrie/TrieGetArray) | ```
Retrieves a string from a hash map.
```
  
[TrieDeleteKey](https://amxx-bg.info/api/celltrie/TrieDeleteKey) | ```
Removes an entry from a hash map.
```
  
[TrieKeyExists](https://amxx-bg.info/api/celltrie/TrieKeyExists) | ```
Checks a hash map for the existence of an entry.
```
  
[TrieDestroy](https://amxx-bg.info/api/celltrie/TrieDestroy) | ```
Destroys a hash map and frees its memory.
```
  
[TrieGetSize](https://amxx-bg.info/api/celltrie/TrieGetSize) | ```
Returns the number of entries in a hash map.
```
  
[TrieSnapshotCreate](https://amxx-bg.info/api/celltrie/TrieSnapshotCreate) | ```
Creates a snapshot of all keys in a hash map. If the map is changed
afterwards,  the changes are not reflected in the snapshot.
Keys are not sorted.
```
  
[TrieSnapshotLength](https://amxx-bg.info/api/celltrie/TrieSnapshotLength) | ```
Returns the number of keys in a map snapshot. Note that this may be
different from the size of the map, since the map can change after the
snapshot of its keys was taken.
```
  
[TrieSnapshotKeyBufferSize](https://amxx-bg.info/api/celltrie/TrieSnapshotKeyBufferSize) | ```
Returns the buffer size required to store a given key. That is, it returns
the length of the key plus one.
```
  
[TrieSnapshotGetKey](https://amxx-bg.info/api/celltrie/TrieSnapshotGetKey) | ```
Retrieves the key string of a given key in a map snapshot.
```
  
[TrieSnapshotDestroy](https://amxx-bg.info/api/celltrie/TrieSnapshotDestroy) | ```
Destroys a map snapshot and frees its memory.
```
  
[TrieIterCreate](https://amxx-bg.info/api/celltrie/TrieIterCreate) | ```
Creates an iterator for a map. It provides iterative read-only access to the
maps contents.
```
  
[TrieIterEnded](https://amxx-bg.info/api/celltrie/TrieIterEnded) | ```
Returns if the iterator has reached its end and no more data can be read.
```
  
[TrieIterNext](https://amxx-bg.info/api/celltrie/TrieIterNext) | ```
Advances the iterator to the next key/value pair if one is available.
```
  
[TrieIterGetKey](https://amxx-bg.info/api/celltrie/TrieIterGetKey) | ```
Retrieves the key the iterator currently points to.
```
  
[TrieIterGetSize](https://amxx-bg.info/api/celltrie/TrieIterGetSize) | ```
Retrieves the number of elements in the underlying map.
```
  
[TrieIterGetCell](https://amxx-bg.info/api/celltrie/TrieIterGetCell) | ```
Retrieves a value at the current position of the iterator.
```
  
[TrieIterGetString](https://amxx-bg.info/api/celltrie/TrieIterGetString) | ```
Retrieves a string at the current position of the iterator.
```
  
[TrieIterGetArray](https://amxx-bg.info/api/celltrie/TrieIterGetArray) | ```
Retrieves an array at the current position of the iterator.
```
  
[TrieIterDestroy](https://amxx-bg.info/api/celltrie/TrieIterDestroy) | ```
Destroys an iterator handle.
```
  

This code is a part of celltrie.inc. To use this code you should include celltrie.inc as ```#include <celltrie>```


  
  

