# Tags (Scripting)
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Tags_\(Scripting\)#mw-head), [search](https://wiki.alliedmods.net/Tags_\(Scripting\)#p-search)
## Contents
  * [1 Introduction](https://wiki.alliedmods.net/Tags_\(Scripting\)#Introduction)
    * [1.1 Usage](https://wiki.alliedmods.net/Tags_\(Scripting\)#Usage)
    * [1.2 Mismatches and Coalescence](https://wiki.alliedmods.net/Tags_\(Scripting\)#Mismatches_and_Coalescence)
  * [2 Built-in Tags](https://wiki.alliedmods.net/Tags_\(Scripting\)#Built-in_Tags)
    * [2.1 Boolean](https://wiki.alliedmods.net/Tags_\(Scripting\)#Boolean)
    * [2.2 Float](https://wiki.alliedmods.net/Tags_\(Scripting\)#Float)
  * [3 SourceMod Specific](https://wiki.alliedmods.net/Tags_\(Scripting\)#SourceMod_Specific)
    * [3.1 New Magic Tags](https://wiki.alliedmods.net/Tags_\(Scripting\)#New_Magic_Tags)
    * [3.2 Function Enumerations](https://wiki.alliedmods.net/Tags_\(Scripting\)#Function_Enumerations)
    * [3.3 New General Tags](https://wiki.alliedmods.net/Tags_\(Scripting\)#New_General_Tags)
  * [4 AMX Mod X Specific](https://wiki.alliedmods.net/Tags_\(Scripting\)#AMX_Mod_X_Specific)


# Introduction
Tags are a concept in the original Small/Pawn language that work around the inherent lack of data types present. For example, Java/C would declare variables like so: 
```
double dNumber = 5.0;
int iNumber = 5;
char cLetter = 'a';
```

In Java, the sizes of these types respectively are eight bytes, four bytes, and two bytes. However, Pawn is only capable of one data type size. In SourcePawn, that's 32bit (four bytes). Therefore, tags serve two purposes: 
  * Allow overloads and restrictions of basic math operators
  * Introduce weak typing and coalescence


An example of this is: 
```
new Float:fNum = 5.0;
new iNum = 5;
new char = 'A';
```

In this example, all of the variables are the same _type_ , the `cell`, which is four bytes. But the `fNum` variable is _tagged_ as a `Float`, and so it uses a set of overloaded operators for floating point math. The `iNum` and `char` variables are both integers. Even though `char` is only holding one byte of data (an ASCII character), it is still a 32bit data type. 
## Usage
Tags are identified by prefixing the tag name and a colon to a variable name. Note that you still need the `new` declaration, as tags aren't a declaration in and of themselves. Example: 
```
//this is valid
new ValidTag:crab = something;
//this is not
InvalidTag:tag = something;
```

Tags can be used for enumerations. For example, the following defines a list of constant symbols which are each tagged as the enumeration name. 
```
enum Clam
{
   Oyster = 0,  /* Oyster has the Clam tag */
   Quahog = 1,  /* Quahog has the Clam tag */
};
```

## Mismatches and Coalescence
If you attempt to mix tags in an expression, you will get the infamous (213) "Tag mismatch" warning from the compiler. Although it is only a warning, it _can_ be a serious error, and it is important that your plugins do not carry this warning (or, if they do, it is carefully understood to be safe). 
An example of a tag mismatch, using the above enumeration, might be: 
```
stock GetClamNumber()
{
   return Oyster;
}
 
stock Clam:GetOyster()
{
   return 0;
}
```

Both of these functions will generate tag mismatch warnings by the compiler. This is because 0 is not inherently an Oyster, and Oyster is a `Clam`, not a raw number. 
Luckily in Pawn, you can 'coalesce' tags. This means you can convert one tag to another. This is usually a bad idea, however, it can be important for converting a bitstring to another bitstring, or a raw integer. The generic, or "empty" tag is `_`, and this symbol will effectively strip a tag from a tagged variable. For example: 
```
stock GetClamNumber()
{
   return _:Oyster;
}
 
stock Clam:GetOyster()
{
   return Clam:0;
}
```

This forces the tags to be correct. _Note that the second function could simply return` Oyster`. This mistake was for example purposes only._
# Built-in Tags
Pawn has two built-in tags by default. These are **bool** and **Float**. 
## Boolean
The `bool` tag (note case sensitivity) can be set to two values: 
  * **true** - 1
  * **false** - 0


Again, it is not faster or slower than an integer 1 or 0, because the data type is the same. This tag simply provides better looking code. 
## Float
The `Float` tag (note case sensitivity) is used for floating point math. If the compiler detects a number to have a decimal point, it is automatically tagged as Float. Floats have the following operators defined. Note that these operators are not intrinsic to the compiler, and are written in `float.inc`. 
  * **Math**
    * **Binary** +, -, /, * (at least one side must be a Float)
    * **Unary** ++, --
    * **Unary** -
  * **Comparison**
    * **Binary** ==, != (at least one side must be a Float)
    * **Binary** >=, >, <, <= (at least one side must be a Float)
    * **Unary** !


  

# SourceMod Specific
## New Magic Tags
In SourceMod, the rules for tags change in two cases, as there are a few 'magic' tags. These magic tags are: 
  * **Function** : This is the tag returned when using a function without a call. For example: ```
stock Function() { }
new Function:fCall = Function;
```

  * **String** : This is a "magic" tag similar to `Float`. It is inherent to literal strings. Unlike `Float`, it secretly changes the storage method -- this makes it a true data type internally, unlike any other tag. Any array tagged as a String is stored in _bytes_ , not _cells_. Observe the example: ```
new String:hello[] = "Hello";
new hello2[] = "Hello";
new hello3[] = {'H', 'e', 'l', 'l', 'o', 0};
```

In this example, `hello` is a valid string array. To the scripter, this appears normal. Internally, it is roughly 6 bytes. This is specifically to make C++ coding of Pawn very fast and easy, in order to avoid cell to string conversion. `hello2` is an invalid declaration, as it is a tag mismatch. `hello3` is a valid declaration, but uses one cell for each character, rather than one byte. Thus, it will be incompatible with natives that use Strings. _This is a good example of why tag coalescence is often dangerous._ If you attempt to manually rewrite tags for strings, the result will be very unexpected, and may even crash. 
Note, however, that is still possible to do assignments like this: 
```
new String:string[20]
new letter = 'a'
string[3] = 'a'
string[a] = letter
```
These assignments work because the `String` tag is a true type underneath, and will correctly cast other tags when necessary.


## Function Enumerations
SourceMod features "function enumerations," which are normal enums, except they define function prototypes rather than constants. Each of the prototypes is given a unique sub-tag that only matches a `Function` of that prototype. These will be explained more in the future, as they are not used yet. 
## New General Tags
SourceMod introduces one important general tag. 
  * **Handle** : Used for the [Handle System](https://wiki.alliedmods.net/Handles_\(SourceMod_Scripting\) "Handles \(SourceMod Scripting\)").


  

# AMX Mod X Specific
AMX Mod X has literally a plethora of tags, but has no new "magic" tags. Some of these tags are: 
  * **Sql** : An SQL index for the DBI system.
  * **Result** : An SQL Result index for the DBI system.
  * **Handle** : An SQL Handle (precursor to SourceMod's `Handle`) for the SQLX system.
  * **Vault** : An index for a vault opened with the nVault module.


