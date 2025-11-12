# Pawn Tutorial
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Pawn_Tutorial#mw-head), [search](https://wiki.alliedmods.net/Pawn_Tutorial#p-search)
`**Note:** This guide is rather hardcoded to AMX Mod X[](https://wiki.alliedmods.net/AMX_Mod_X "AMX Mod X").  It needs to be mode generic.`
This guide is designed to give you a more in-depth overview of the basics of programming in [Pawn](https://wiki.alliedmods.net/Pawn "Pawn"). 
## Contents
[hide] 
  * [1 Introduction](https://wiki.alliedmods.net/Pawn_Tutorial#Introduction)
    * [1.1 Language Paradigms](https://wiki.alliedmods.net/Pawn_Tutorial#Language_Paradigms)
    * [1.2 Implementation Features](https://wiki.alliedmods.net/Pawn_Tutorial#Implementation_Features)
    * [1.3 License](https://wiki.alliedmods.net/Pawn_Tutorial#License)
  * [2 Variables](https://wiki.alliedmods.net/Pawn_Tutorial#Variables)
    * [2.1 Types](https://wiki.alliedmods.net/Pawn_Tutorial#Types)
      * [2.1.1 Integers](https://wiki.alliedmods.net/Pawn_Tutorial#Integers)
      * [2.1.2 Floats](https://wiki.alliedmods.net/Pawn_Tutorial#Floats)
      * [2.1.3 Booleans](https://wiki.alliedmods.net/Pawn_Tutorial#Booleans)
  * [3 Arrays](https://wiki.alliedmods.net/Pawn_Tutorial#Arrays)
  * [4 Strings](https://wiki.alliedmods.net/Pawn_Tutorial#Strings)
  * [5 Functions](https://wiki.alliedmods.net/Pawn_Tutorial#Functions)
  * [6 Expressions](https://wiki.alliedmods.net/Pawn_Tutorial#Expressions)
  * [7 Conditionals](https://wiki.alliedmods.net/Pawn_Tutorial#Conditionals)
    * [7.1 If Statements](https://wiki.alliedmods.net/Pawn_Tutorial#If_Statements)
    * [7.2 Switch Statements](https://wiki.alliedmods.net/Pawn_Tutorial#Switch_Statements)
  * [8 Looping](https://wiki.alliedmods.net/Pawn_Tutorial#Looping)
    * [8.1 For Loops](https://wiki.alliedmods.net/Pawn_Tutorial#For_Loops)
    * [8.2 While Loops](https://wiki.alliedmods.net/Pawn_Tutorial#While_Loops)
    * [8.3 Two Dimensional Arrays](https://wiki.alliedmods.net/Pawn_Tutorial#Two_Dimensional_Arrays)
  * [9 Compiler Pre-processor Directives](https://wiki.alliedmods.net/Pawn_Tutorial#Compiler_Pre-processor_Directives)
  * [10 Conclusion](https://wiki.alliedmods.net/Pawn_Tutorial#Conclusion)
  * [11 External Links](https://wiki.alliedmods.net/Pawn_Tutorial#External_Links)


# Introduction
Pawn is an embeddable, (almost) typeless, easy to use scripting language that is compiled for a virtual machine. [AMX Mod X](https://wiki.alliedmods.net/AMX_Mod_X "AMX Mod X") uses Pawn to route scripting functions to the Half-Life engine, using the Pawn [Virtual Machine](https://wiki.alliedmods.net/index.php?title=Virtual_Machine&action=edit&redlink=1 "Virtual Machine \(page does not exist\)") and [Metamod](https://wiki.alliedmods.net/Metamod "Metamod") ([Pawn](https://wiki.alliedmods.net/Pawn "Pawn") is written in C, Metamod is written in C++). While you write Pawn scripts in a text editor, the scripts must be compiled with a "Compiler", which produces a binary for AMX Mod X. The AMX Mod X team distributes a specially modified Pawn compiler. 
Programming scripts in Pawn is relatively easy, and does not have concepts in other languages that are unnecessary for general use, such as pointers, vectors, structs, classes, allocation, et cetera. 
## Language Paradigms
Pawn was originally named "[Small](https://wiki.alliedmods.net/Small "Small")" to emphasize the size of the language specification. The language sacrifices many features found in modern languages to achieve simplicity and speed, which are required for embedded uses. 
  * No typing 
    * Pawn only has one data type -- the "[cell](https://wiki.alliedmods.net/index.php?title=Cell_\(Pawn\)&action=edit&redlink=1 "Cell \(Pawn\) \(page does not exist\)")". It is the size of the processor's integral pointer (4 bytes for 32bit processor, 8 bytes for 64bit processors). This has two major implications - Pawn bytecode is processor specific, and pointers can fit inside a cell.
    * [Tagging](https://wiki.alliedmods.net/index.php?title=Tagging_\(Pawn\)&action=edit&redlink=1 "Tagging \(Pawn\) \(page does not exist\)") - Pawn lets you create weakly statically typed "tags", which can be associated with variables for primitive operator overloading. For example, Pawn has no concept of floating point numbers (only integers). Instead, operators are overloaded with the Float: tag to redirect computation to new functions. Tag-checking is only enforced as a warning. If you're using SourcePawn (for SourceMod), there is actually a second type: String. In a String, letters are stored as separate bytes... essentially having 4 characters stored in every cell.
    * Since Pawn only has one datatype, it does not support structs, records, objects, or anything else.
    * Pawn _does_ support arrays of cells, which leads to C-style arrays for strings.
  * No garbage collection 
    * Pawn has no "heap" allocation built-in. All variables are stored on the stack or in the data section. Therefore, no garbage collection is necessary and memory leaks are not possible from the language specification alone.
  * Procedural 
    * Pawn is entirely comprised of single, non-nested subroutines. There are no lambda functions, member functions, constructors, et cetera. Functions can either be internal (within the script) or public (exposed to the VM by name, like C's "extern").
  * No thread-safety 
    * Pawn is targetted toward single-thread instances.


## Implementation Features
  * Cross-platform compatible compiler, which outputs bytecode and debug browsing information.
  * Cross-platform compatible Virtual Machine (VM), with support for debug browsing, halting/stopping execution, and interacting with scripts from C/C++ libraries.
  * IA32 JIT Compiler for vastly increasing script execution time.


Because the footprints of the VM and JIT are so small, Pawn is ideal inside games which need a simple and highly fast event system, embedded devices or applications, and realtime systems. 
## License
Pawn is licensed under the [ZLib/libpng_License](https://wiki.alliedmods.net/ZLib/libpng_License "ZLib/libpng License") license. 
# Variables
Variables are simple structures for holding data throughout a period of time in your script. 
## Types
Small has just three data types for declaring variables. The default variable type is a regular whole number, or integer. A variable name, for backwards compatibility, should be 19 characters or less, and MUST start with a letter. It can contain the symbols A-Z, a-z, 0-9, and the underscore ("_"). It is important to note that variable names are case sensitive - "myvar", "MyVaR", and "MYVAR" are three separate symbols. 
### Integers
The simplest data type in Pawn is an "integer". Integers are whole numbers. To declare a new integer variable, use the "new" operator like so: 
```
new a            //Declare empty variable "a"
new b=5          //Declare variable "b" and set it to 5.
new c=5.0        //This is invalid, technically not a whole number!
new d="hello"    //"hello" is not a number either, this is invalid.
 
//You can also declare multiple variables on one line:
new e,f,g,h
new x=7, y=3
new z = 1_000_000 // Pawn supports numbers like this. So big values are easier to read.
```

### Floats
You can also declare a variable as a "Float", which means it can store numbers with decimal places. These are called "floating point" numbers: 
```
new Float:a            //Declare empty floating point variable "a"
new Float:b=5.3        //This will declare a new variable "b" and assign 5.3 to it.
new Float:c=5          //This is valid, but the compiler will give you a warning.
new Float:d="hello"    //This is invalid, "hello" is not a decimal number.
```

You can also do the following: 
```
//float(n) is a function that takes a number n and makes it a
// floating point number.
new Float:var = float(5)
new Float:var2 = 5.0     
new Float:var3 = 1.0*5
new var4 = floatround(5.0)     
//Note: floatround(n) is a function that takes a number n and rounds it to a whole number.
//  this makes the assignment to a regular integer variable valid.
```

Note - Spacing does generally not matter, as long as the compiler can tell symbols apart from each other. If your spacing is REALLY bad, you will get errors or maybe even warnings. For example, "new var = 5" and "new var=5" are the same, but "newvar=5" is totally wrong. 
### Booleans
The last variable type is "boolean". It is very simple - it is either "true", or "false". Both "true" and "false" are predefined data structures. 
```
new bool:IsItOn        //Declares a new variable "IsItOn" which is automatically false
new bool:xyz=true      //Declares a new variable "xyz" set to true
```

  

# Arrays
Pawn features basic "arrays". An array is a simple type of aggregate data. This means you can store multiple values in one variable! An array follows the same rules as a regular variable, and it has the same types. It simply can contain multiple values. You define an array with brackets, and how many values it can hold. For example: 
```
//This will declare a variable called "Players" which holds 32 numbers. 
new Players[32]
 
//You can now store values in any of the 32 "slots" this array has.  
// The slots are numbered from 0 to n-1, or in this case, 0 to 31.
//Every slot starts off as 0.
 
//Set slot 0 to 5
Players[0] = 5
 
//Set slot 1 to whatever is in slot 0, in this case, the number 5
Players[1] = Players[0]
 
//This is invalid! 
//Although there are 32 slots, they are numbered from 0 to 31.
//Doing this results in AMX Native Error 4 - AMX_ERR_BOUNDS
// or, it simply won't compile!
Players[32] = 15
 
//This is also totally invalid           
Players[-1] = 6
 
new a = 3
//This is also totally invalid.  
//a must be a constant number.
new BadArray[a]
 
//So this is valid:
const b = 3
new GoodArray[b]
 
//You can also use Compiler Directives (See last section)
 
#define ARRAY_SIZE 3
new Array[ARRAY_SIZE]
```

Arrays can also be declared with groups of data default, such as: 
```
new Numbers[4] = {0,1,2,3}
//Note: it is important that you make sure the amount of numbers
// you pass and the size of the array match
```

  
You can also use any data type with arrays: 
```
//Array of floating points:
new Float:Numbers[4] = {0.0, 1.2, 2.4, 3.8}
//Array of booleans.  Note this sets every slot to true.
new bool:playerHasGun[33] = {true, ...}
```

# Strings
You have probably noticed that an important data type is missing - characters (letters and symbols). These are called "strings", and in Pawn, they are technically numbers! A string is an array of numbers that translate to ASCII (character) symbols. For example: 
```
//This will declare a number array "myString" that contains the data "Hello".  
//It will have 6 slots, because there are 5 characters.  
//The last slot is reserved for the number 0, which tells the Pawn engine that it is a string.
new myString[] = "Hello"
// If you're using SourcePawn, do this instead:
new String:myString[] = "Hello"
```

Note: anything in between /* and */ is also a comment. You cannot use /* */ inside a /* */. The following set of commands achieves the same purpose, however, it is longer and not recommended. This works because each character of the string "Hello" is stored in a slot in the array. 
```
new myString[6]
myString[0] = 'H'
myString[1] = 'e'
myString[2] = 'l'
myString[3] = 'l'
myString[4] = 'o'
myString[5] = 0
```

`**Note:** Arrays that are meant to be strings must end in a 0, or the null character.  This is so you know where the string ends.`
You CANNOT do this! While it may compile, it is highly dangerous as it might cause overflow errors: 
```
new myString[6]
myString = "Hello"     //INVALID!
myString[0] = "Hello"  //INVALID!
//To add data to a string, you can do this:
new goodString[7]
copy(goodString, 6, "Hello")
```

`**Note:** In SourcePawn, copy was renamed to strcopy and avoids the issue with copy noted below.`
Note that we copied 6 cells of the array into an array that can hold 7. If we were to copy 7 bytes into this array, copy() could potentially copy an extra byte for the Null character, overflowing the array. This is called a [buffer overflow](https://wiki.alliedmods.net/index.php?title=Buffer_overflow&action=edit&redlink=1 "Buffer overflow \(page does not exist\)") and must be carefully avoided. 
More examples: 
```
//Copy is a function that takes three parameters:
copy(destination[], length, source[])
//It copies the string inside the source array and places 
// it into the destination array, but only copies up to length characters.
 
//Lastly, to prove that a string is really an array of numbers, this is completely valid:
new weird[6]
weird[0] = 68
weird[1] = 65
weird[2] = 73
weird[3] = 86
weird[4] = 68
weird[5] = 0
//This will set the variable "weird" to the string "DAVID".
//To see how letters and symbols translate into numbers, visit www.asciitable.com
```

# Functions
Pawn allows you to define your own functions. This comes in handy for removing code that is used in multiple places. Note that all functions should return a value. To do this, you use the "return" command, which immediately halts the function and returns the value of the expression passed to it. No code is executed in a function once the return is found. Here are some examples: 
```
//This is a function that takes no parameters and returns 1.
//When activated, it uses the (non-existant) print function.
show()
{
   print("Hello!")
 
   return 1   //End, return 1
}
 
//Activate like this:
show()
```

You can also declare functions to take parameters. 
```
//This declares a function called "add_two_numbers", which takes two numbers and returns the sum.
add_two_numbers(first, second)
{
   new sum = first + second
 
   return sum  //Return the sum
}
//Then you can use your new function like this:
 
new a,b
a = 5
b = 12
new c = add_two_numbers(a,b)
//c will now be equal to 17.
```

You are not limited by what types of data parameters can accept. When you give parameters to a function, it is called "passing". You can pass either data or a variable to a function. 
```
//This defines a new function called "add_two_floats"
// which takes two floating points and returns the sum
Float:add_two_floats(Float:first, Float:second)
{
   new Float:sum = first + second
 
   return sum
}
 
new Float:a
new Float:b
a = 5.0
b = 6.3
new Float:c
c = add_two_floats( a+b )
//c is now equal to 11.3
```

You can even pass arrays! You do not have to specify the size of the array. If you do, you must make sure you are calling the function with an array of equal size and type. 
```
add_two_from_array(array[], a, b)
{
   new first = array[a]
   new second = array[b]
   new sum = add_two_numbers(first, second)   //use our function from earlier
 
   return sum
}
```

Note, that when you pass arrays through a function they are passed through what is called "by reference". When a normal variable is passed to a function, it is copied in memory, and the copy is sent and then deleted afterwards. This is not the case with an array. Because arrays can be very large, the array is "referenced" instead of copied. This means if you change the array, afterwards it will stay changed. For example: 
```
//This function will switch slots a and b inside any array passed to this function.
swap_slots(array[], a, b)
{
   //Note, you need to temporarily hold one of the slots before swapping them
   //Otherwise, you can't swap both values! This is a classic problem.
   //If you have a and b, setting b equal to a eliminates the original value in b.
   new temp
 
   temp = array[b]
   array[b] = array[a]
   array[a] = temp
}
 
new myArray[2]
myArray[0] = 5
myArray[1] = 6
swap_slots(myArray, 0, 1)
//myArray[0] is 6, myArray[1] is 5
```

You can prevent arrays from being modified by declaring them "constant", like so: 
```
add_two_from_array(const array[], a, b)
{
   new first = array[a]
   new second = array[b]
   new sum = add_two_from_array(first, second)
   return sum
}
//Note, now when you use the function, you are guaranteed that the array will not be modified.
```

This function modifies an array passed as a constant. It will not work. 
```
bad_function(const array[])
{
   array[0] = 0
}
```

# Expressions
Expressions are just what they sound like from mathematics. They are groupings of symbols that return one piece of data. Expressions are normally comprised of parenthetical expressions, and are evaluated in a certain order (from innermost to outermost, parenthesis first, then multiplication, division, addition, subtraction, et cetera). You can put expressions anywhere. You can set variables equal to them or pass them to functions. 
```
//This is the simplest expression.  It returns the number zero.
0
//However, to make it easier to read, this is also valid:
(0)
```

If an expression is not zero or it is not false, it not only returns a value, it also returns "true". Otherwise, it will return 0, which is also "false". 
```
//Here are more mathematical expressions.  The mathematical operators are
// + for addition
// - for subtraction
// * for multiplication
// / for division
// % for modulus (finding the remainder of one number divided by another (5%2 is 1)
(5+6)                       //returns 11
((5*6)+3)                   //returns 33
((((5+3)/2)*4)-9)           //returns 7
((5*6) % 7)                 //returns 2
//Here are other expressions:
(true)                      //returns true
(5.0 + 2.3)                 //returns 7.3 as a floating point
```

There are also extensions of these operators for direct use on variables. 
```
new a = 5
new b = 6
//The first are the post/pre increment and decrement operators.
a++          //returns a+1, or 6.  This is a post increment.
++a          //also returns a+1, or 6.  This is a pre increment.
```

The difference between the two is subtle but important. a++ is evaluated LAST in an expression, while ++a is evaluated FIRST. This differences comes in handy with code that uses loops in certain ways. It is also important to know that the increment/decrement operators will not only return a+1, but set the variable a to a+1. 
```
a--          //returns 4, post decrement
--a          //returns 4, pre decrement
```

Note that a++ essentially trims down this code: 
```
a = a + 1
```

However, there is another way to write lines of code of this form: 
```
a = a OP y
```

Where OP is a math operator. It can be shortened to: 
```
a OP= x
```

Observe: 
```
a += 1       //This sets a to a + 1
a -= b       //This sets a to a - b
a *= 0       //This multiplies a by 0
a /= 2       //This divides a by 2.
```

However, mathematical operators are not the only operators you are given. There are boolean operators to help you with logical circuits or logical decisions. 
The and operator takes in the left expression and right expression. If both are "true", then it returns true. 
```
//This is false, because 1 returns true and 0 returns false.  
//Since both are not true, && returns false.
(1 && 0)
(1 && 2)                    //Both numbers are "true", therefore the expression is true.
(true && false)             //false
(false && false)            //false
(true && true)              //true
```

The other important operator is "or". It returns true if one of two expressions are true. 
```
(1 || 0)                    //true, since one of the values is true.
(1 || 2)                    //true
(true || false)             //true
(false || false)            //false
(true || true)              //true
```

There are other operators as well, that you may not use as often. The "bitwise and" operator returns whether a binary bit sequence is contained in another sequence. In the technical terms, it does an "and (&&)" operation on each of the bits in both numbers. For example, say you have the number "9", which is "1001" in binary. If you want to know if that sequence contains the number "8" (1000), you can do: 
```
//This will return 8, which means 8 is indeed a bit in 9.
(9 & 8)
//4 (00100) is not a bit inside 16 (10000) and this will return 0.
(16 & 4)
//The next operator is "bitwise or" 
//which does an "or (||)' operation on each of the bits in both numbers.
//This will take 9 (1001) and match it with 3 (0011), resulting in 1011, or 11.
(9 | 3)
```

These two operators are also important, but not used often. They are the bitwise shift operators, << is a left shift and >> is a right shift. They shift the bits in a number to one direction. 
```
//This takes the number 3 (00011) and shifts it three places to binary (11000), or 24.
(3 << 3)
//This takes the number 24 (11000) and shifts it three places to binary (00011), or 3.
(24 >> 3)
```

The last operator is "bitwise not". It returns the exact opposite of whatever is given to it. When used on a number, it will return each of the bits flipped (1 to 0, 0 to 1). 
```
//This returns false
(!true)
//This returns true
(!false)
//This takes 9 (binary 1001) and makes it 6 (binary 0110).
//This is the "bitwise complement" operator, which performs a !(not) on each bit.
(~(9))
```

# Conditionals
Conditionals allow you to test if an expression meets a standard, and to execute code based on that decision. 
## If Statements
The most important conditional is called "if ... then". If evaluates whether a given expression is true or false. It if is true, it executes a block of code. If not, it executes a different block of code. For example: 
This is an example of the most basic if ... then statement. The first line checks to see if the expression is true. In this case, if the variable a is equal to 5, then the if statement will execute the block of code underneath it, which sets a to 6. 
```
if (a == 5)
{
   a = 6
}
```

However, what happens if a does not equal 5? Then the code will not be executed. However, you can tell it to execute code if the conditions are not met. Now, if a is equal to 5, a will be set to 6. Otherwise, it will be set to 7. 
```
if (a == 5)
{
   a = 6
} else {
   a = 7
}
```

There are many different operators you can use inside the if () statement. In fact, you can use any [expression](https://wiki.alliedmods.net/Pawn_Tutorial#Expressions) that evaluates to true (not zero) or false (zero). 
```
//This will return true if a does not equal 5
if (a != 5) {}
//Returns true if a is greater than 5
if (a > 5) {}
//Returns true if a is less than 5
if (a < 5) {}
//Returns true if a is greater than or equal to 5
if (a >= 5) {}
//Returns true if a is less than or equal to 5
if (a <= 5) {}
//Returns true because 11 is true
if (5+6) {}
//Returns true of both a and b are true
if (a && b) {}
//Returns true if 7.5 is greater than c
if ( ((5*3)/2) > c) {}
//Always returns true no matter what
if (true) {}
//Never returns true
if (false) {}
```

Note that array comparisons have restrictions. This is invalid: 
```
my arrayOne[3]
my arrayTwo[3]
if (arrayOne == arrayTwo) {
```

You must do: 
```
if ((arrayOne[0] == arrayTwo[0]) && 
    (arrayOne[1] == arrayTwo[1]) && 
    (arrayOne[2] == arrayTwo[2])) {
```

Obviously, this would get very tedious with large arrays. You will see later on how to easily compare strings and arrays. 
The if...then model of conditional switching can be brought up to another level. Pawn provides a way for you to provide multiple levels of true and false expressions. 
```
//Example of "if...else if"
if (a == 5) {
   //This code will be run if a is 5.
} else if (a < 6) {
   //This code will be run if a is less than 6
} else if (a == 7) {
   //This code will be run if a is 7.
} else {
   //If none of the above conditions are met, this code will be run.
}
```

  
It is important to note that in the above example, each code block is not "fall through". That means each of the conditions will be checked in order, and if one is true, the code will be executed and the if statement is done. It will not execute multiple true conditions. 
## Switch Statements
Lastly, there is one last type of conditional statement. It is called a "switch" statement, and it allows you to make a nicely ordered list of conditions similar to, but not as powerful as, "if...else if". 
```
//Example of a switch statement
switch (a)
{
    case 5:
    {
       //This code will run if a is equal to 5
    }
 
    case 6:
    {
       //This code will run if a is equal to 6
    }
 
    case 7:
    {
       //This code will run if a is equal to 7
    }
 
    default:
    {
       //This code will run if all other cases fail
    }
}
```

Multiple conditions are also possible in pawn: 
```
//Example of an multiple switch statement
switch (a)
{
    case 1, 2, 3:
    {
       //This code will run if a is equal to 1 or 2 or 3
    }
 
    case 4, 5, 6:
    {
       //This code will run if a is equal to 4 or 5 or6
    }
 
    case 7, 8, 9:
    {
       //This code will run if a is equal to 7 or 8 or 9
    }
 
    default:
    {
       //This code will run if all other cases fail
    }
}
```

Note that switch cases do not "fall-through." If a case is true, no other cases are evaluated. 
# Looping
Looping is essential for any language. It allows you to perform the same block of code over and over, by constructing conditions on which code should be repeated. 
## For Loops
The first and most widely used loop is called a "for loop". It takes an initial value, a condition upon which it should stop, and an incremental step. Then it executes code until it the conditions are no longer true. This lets you repeat the same block of code any number of times. Example: 
```
/*A for loop has three parameters:
  for (initial; condition; increment)
  {
    //your code here
  }
 
  Before the first loop executes, it runs your initial condition.
  Then it begins looping your code with these steps:
  1.  Check if the condition is true.  If so, continue.  If not, stop.
  2.  Run the code.
  3.  Run the "increment" parameter.
  4.  Go to step 1.
*/
 
//Example of a for loop
new i
new sum
for (i=1; i<=10; i++)
{
   sum += i
}
```

Explanation: 
  1. The first parameter, i=1, sets the i variable to one. This happens before the looping starts.
  2. Next, the "increment" parameter is checked. This parameter is a post-increment operator, so 1 will be added to i after the entire code block is evaluated.
  3. Then the condition is checked. Is i<=10? It is currently 1, so it is indeed less than or equal to 10.
  4. Since the condition is true, sum+=i is executed. This means i is added into sum.
  5. The code block has finished, and i++ increments i to 2.
  6. Now it repeats.
  7. Is i<=10? Yes, it is 2. Now sum+=i runs again, and now sum is equal to 3.
  8. The code block has finished, and i now increments to 3.
  9. This happens until...
  10. The increment parameter sets i to 11. The condition is no longer true, and the for loop is finished.
  11. The sum variable now holds the number 55, which is the sum of 1 through 10.


This provides a nice way of managing arrays! 
```
//Note: this provides a nice way to loop through arrays!  Observe this function below.
sum_of_array(myArray[], size)
{
   //Note: Make sure the user passes the size of the array, so we don't overflow it.
   new i, sum
 
   //This loop will start at 0 and stop right before size is reached.
   //If the user passes the correct size of the array, 
   // the loop will be going from 0 to size-1
   // This correctly matches the numbers of slots in the array.
   for  (i=0; i<size; i++)
   {
      //For every time this loop executes, 
      // i will be a number from 0 to size-1
      //Add the value of the slot (i) in the array to sum.
      //Once this is finished, sum will contain 
      // the sum of all slots in the array.
      sum += myArray[i]
   }
 
   return sum
}
 
new NumberArray[4]
NumberArray[0] = 3
NumberArray[1] = 1
NumberArray[2] = 4
NumberArray[3] = 1
 
new answer = sum_of_array(NumberArray, 4)
//answer will be 3+1+4+1, or 9
 
//Here is a function to compare if one array is equal to another (i.e. a string)
bool:compare_arrays(array1[], array2[], size)
{
   new i
   for (i=0; i<size; i++)
   {
      //If a slot does not match, halt the function and return false.
      if (array1[i] != array2[i])
      {
         return false
      }
   }
 
   //If the function got to this point without returning false, return true.
   return true
}
```

## While Loops
The next kind of loop is also very important, and is simpler than a for loop. Called a "while" loop, it only takes one parameter: a condition. As long as the condition is true, it keeps executing code. See the above examples rewritten with while loops. 
```
//Basic loop
new i=0
new sum
 
while (++i <= 10)
{
   sum+=i
}
 
sum_of_array(array[], size)
{
   new i=0, sum
 
   //Do this loop while i is less than the size.
   //i is incremented at the end of every loop.
   while (i++ < size)
   {
      sum += array[i]
   }
 
   return sum
}
 
bool:compare_arrays(array1[], array2[], size)
{
   new i
   while (i++ < size)
   {
      if (array1[i] != array2[i])
      {
         return false
      }
   }
 
   return true
}
```

  

## Two Dimensional Arrays
In Pawn it is possible to have arrays where each slot is another array. This is very useful for storing a table of data, where the first section of slots is a row and the second section of slots is a column. Two dimensional arrays are declared like so: 
```
//This declares an array with 50 rows and 50 columns.
new BigArray[50][50]
//this declares a floating point array with 25 rows and 10 columns.
new Float:BigArray[25][10]
```

Each slot in the first subset of the array becomes its own array. 
```
new BigArray[3][3]
BigArray[0][0] = 10
BigArray[0][1] = 20
BigArray[0][2] = 30
BigArray[1][0] = 40
BigArray[1][1] = 50
BigArray[1][2] = 60
BigArray[2][0] = 70
BigArray[2][1] = 80
BigArray[2][2] = 90
```

Will result in BigArray looking like this:       BigArray  | 0  | 1  | 2   
---|---|---|---  
0  | 10  | 20  | 30   
1  | 40  | 50  | 60   
2  | 70  | 80  | 90   
Note that our old sum_of_array() function can still work! We can do: 
```
new sum = sum_of_array(BigArray[2], 3)
```

Because BigArray[2] contains a second, single dimensional array, containing {7,8,9}. However, let's write a 2D sum of array function. 
```
//This function will tally up a two dimensional array.
sum_of_table(array[][], rows, cols)
{
   new i, j, sum
 
   //Note, there is a loop inside the loop.  
   //This lets you go through each array inside the   
   // bigger array. 
   for (i=0; i<rows; i++)
   {
      for (j=0; j<cols; j++)
      {
         sum += array[i][j]
      }
   }
 
   return sum
}
```

Note, it is also possible to store an array of strings using two dimensional arrays. 
```
new StringList[3][] = {"Hello", "my", "friend"}
/*
  StringList[0][0] through [0][5] contains "Hello"
  StringList[1][0] through [1][2] contains "my"
  StringList[2][0] through [2][6] contains "friend"
*/
```

The table for StringList will look like: StringList 0 1 2 3 4 5 6 0 H e l l o \0 1 m y \0 2 f r i e n d \0 
Comparing strings in multidimensional arrays is also similar: 
```
if (StringList[0] == "Hello")       //INVALID
if (StringList[0][0] == "Hello")    //INVALID
if (equali(StringList[0], "Hello")) //Valid
```

# Compiler Pre-processor Directives
Compiler directives allow you to change how your code is read. This is rather advanced and will only be run over briefly. 
```
//To bind a symbol to a value, you can do this:
#define SYMBOL VALUE
//for example:
 
#define MAX_STRING 250
new String[MAX_STRING]
 
#define HELLO "Hello.  This is a generic greeting."
new Hello[MAX_STRING] = HELLO
```

You can also use #defines to change the flow of code the compiler makes. 
```
#if defined LINUX
   //This portion will be compiled if #define LINUX exists
   execute_command("ls -l")
#else
   //This portion will be compiled if #define LINUX does not exist
   execute_command("dir")
#endif
```

You can also change how much memory your script uses. 
```
#pragma dynamic 4096
//This creates a 16K stack of memory (default).
//It is measured in blocks of 4 byte cells.
```

You can also specify whether semicolon usage is required to terminate a line of code (by default it is not required). 
```
#pragma semicolon 1
```

You can also change the control character( amxx std: '^' ) 
```
#pragma ctrlchar '\'
//this sets the control character to backslash( c/c++/c#/java/... std )
// now you have to use the \ instead of ^
// e.g. "this is ^":D^" " must be now " this is \":D\" "
```

# Conclusion
This guide should have given you a VERY brief introduction to basic Pawn programming. It is by no means comprehensive and it should not constitute the entirety of one's knowledge of Pawn. To read the official Pawn documentation and language guide, go this website: <https://github.com/compuphase/pawn/blob/master/doc/Pawn_Language_Guide.pdf> (Note, this guide is very long and should be used as a reference. You may want to try the Small forums or the AMX Mod X forums). Continue to the next Section to see how to apply Small programming to the Half-Life and AMX Mod X engine! 
# External Links
  * [Pawn Language Reference](https://github.com/compuphase/pawn/blob/master/doc/Pawn_Language_Guide.pdf)
  * [Pawn Homepage](http://www.compuphase.com/pawn/pawn.htm)
  * [ITB CompuPhase](http://www.compuphase.com/)


