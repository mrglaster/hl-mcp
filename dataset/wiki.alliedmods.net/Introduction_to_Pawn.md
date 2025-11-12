# Introduction to Pawn
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Introduction_to_Pawn#mw-head), [search](https://wiki.alliedmods.net/Introduction_to_Pawn#p-search)
# Introduction
This guide is designed to give you a very basic overview to fundamentals of scripting in Pawn. [Pawn](https://wiki.alliedmods.net/Pawn "Pawn") is a "scripting" language used to embed functionality in other programs. There are two kinds of languages. The first is a language like C or C++, a "compiled" language which outputs executable binaries. The other is "interpreted" which is run through a virtual machine that runs code on the fly. [AMX](https://wiki.alliedmods.net/index.php?title=AMX&action=edit&redlink=1 "AMX \(page does not exist\)")/Pawn is a mixture of the two: You compile it, but the binaries are interpreted. 
There a few important constructs you should know before you begin to script. The first is a "[variable](https://wiki.alliedmods.net/index.php?title=Variable&action=edit&redlink=1 "Variable \(page does not exist\)")". A variable is a symbol, or marker, that holds data. For example, the variable "a" could hold the number "2", "16", "0", et cetera. Variables are created for storage space throughout a program. It is your responsibility to declare the names of variables you will be using before you use them. Variables are assigned data with the equal sign: 
```
new a,b,c,d

a=5
b=16
c=0
d=500
```

The next important concept is [functions](https://wiki.alliedmods.net/index.php?title=Functions&action=edit&redlink=1 "Functions \(page does not exist\)"). Functions are symbols or markers that do something when called. That means when you activate them, they carry out actions on the data you supply to them. There are a few types of functions, but every function is activated the same way. For example, say the "show" function prints a number to the screen: 
```
show(56)   //Activates "show" function, and gives the number 56 to it
show()     //Activates "show" function with no data, blank
show(a)    //Activates "show" function, gives a variable's contents as data

```

Note any text that appears after a "//" is considered a "comment" and is not actual code. For every piece of data you pass to a function, it is called a "[parameter](https://wiki.alliedmods.net/index.php?title=Parameter&action=edit&redlink=1 "Parameter \(page does not exist\)")". A function can have any number of parameters, and you need to make sure the data you give each parameter is correct. If a function takes in two numbers, you cannot give it words. Functions may also return data, like so: 
```
new b
b = add(5, 7)
```

In this case, if "add" is a function that adds the first parameter to the second and returns the answer, the variable "b" will be assigned the number 12. 
The next concept is block coding. You can group code into "blocks" separated by { and }. This effectively makes one large block of code act as one piece. For example: 
```
{
   here
   is
   some
   code
}
```

It is a common practice to always use block coding when possible, and to indent the code in between the block delimiters. 
This should give you a VERY brief necessary background to learning Pawn. 
