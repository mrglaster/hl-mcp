# is_string_category
#### Syntax
```
native bool:is_string_category(const input[], input_size, flags, &output_size = 0);
```

#### Usage
input | ```The string to check```
---|---
input_size | ```Size of the string, use 1 to check one character regardless its size```
flags | ```Requested category, see UTF8C_* flags```
output_size | ```Number of bytes in the input that conform to the specified category flags```
#### Description
```
Checks if the input string conforms to the category specified by the flags.
```

#### Note
```
This function can be used to check if the code points in a string are part
of a category. Valid flags are part of the UTF8C_* list of defines.
The category for a code point is defined as part of the entry in
UnicodeData.txt, the data file for the Unicode code point database.
```

#### Note
```
Flags parameter must be a combination of UTF8C_* flags or a single UTF8C_IS* flag.
In order to main backwards compatibility with POSIX functions like `isdigit`
and `isspace`, compatibility flags have been provided. Note, however, that
the result is only guaranteed to be correct for code points in the Basic
Latin range, between U+0000 and 0+007F. Combining a compatibility flag with
a regular category flag will result in undefined behavior.
```

#### Note
```
The function is greedy. This means it will try to match as many code
points with the matching category flags as possible and return the offset in
the input in bytes.
```

#### Return
```
True if the whole input of `input_size` conforms to the specified
category flags, false otherwise
```


This code is a part of string.inc. To use this code you should include string.inc as ```#include <string>```


  
  

