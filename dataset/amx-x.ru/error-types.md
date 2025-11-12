### [Решение ошибок при компиляции](https://amx-x.ru/viewtopic.php?f=9&t=10#p21)

Список ошибок:  

    `  
/*001*/  "expected token: \"%s\", but found \"%s\"\n",  
/*002*/  "only a single statement (or expression) can follow each \"case\"\n",  
/*003*/  "declaration of a local variable must appear in a compound block\n",  
/*004*/  "function \"%s\" is not implemented\n",  
/*005*/  "function may not have arguments\n",  
/*006*/  "must be assigned to an array\n",  
/*007*/  "operator cannot be redefined\n",  
/*008*/  "must be a constant expression; assumed zero\n",  
/*009*/  "invalid array size (negative or zero)\n",  
/*010*/  "invalid function or declaration\n",  
/*011*/  "invalid outside functions\n",  
/*012*/  "invalid function call, not a valid address\n",  
/*013*/  "no entry point (no public functions)\n",  
/*014*/  "invalid statement; not in switch\n",  
/*015*/  "\"default\" case must be the last case in switch statement\n",  
/*016*/  "multiple defaults in \"switch\"\n",  
/*017*/  "undefined symbol \"%s\"\n",  
/*018*/  "initialization data exceeds declared size\n",  
/*019*/  "not a label: \"%s\"\n",  
/*020*/  "invalid symbol name \"%s\"\n",  
/*021*/  "symbol already defined: \"%s\"\n",  
/*022*/  "must be lvalue (non-constant)\n",  
/*023*/  "array assignment must be simple assignment\n",  
/*024*/  "\"break\" or \"continue\" is out of context\n",  
/*025*/  "function heading differs from prototype\n",  
/*026*/  "no matching \"#if...\"\n",  
/*027*/  "invalid character constant\n",  
/*028*/  "invalid subscript (not an array or too many subscripts): \"%s\"\n",  
/*029*/  "invalid expression, assumed zero\n",  
/*030*/  "compound statement not closed at the end of file\n",  
/*031*/  "unknown directive\n",  
/*032*/  "array index out of bounds (variable \"%s\")\n",  
/*033*/  "array must be indexed (variable \"%s\")\n",  
/*034*/  "argument does not have a default value (argument %d)\n",  
/*035*/  "argument type mismatch (argument %d)\n",  
/*036*/  "empty statement\n",  
/*037*/  "invalid string (possibly non-terminated string)\n",  
/*038*/  "extra characters on line\n",  
/*039*/  "constant symbol has no size\n",  
/*040*/  "duplicate \"case\" label (value %d)\n",  
/*041*/  "invalid ellipsis, array size is not known\n",  
/*042*/  "invalid combination of class specifiers\n",  
/*043*/  "character constant exceeds range for packed string\n",  
/*044*/  "positional parameters must precede all named parameters\n",  
/*045*/  "too many function arguments\n",  
/*046*/  "unknown array size (variable \"%s\")\n",  
/*047*/  "array sizes do not match, or destination array is too small\n",  
/*048*/  "array dimensions do not match\n",  
/*049*/  "invalid line continuation\n",  
/*050*/  "invalid range\n",  
/*051*/  "invalid subscript, use \"[ ]\" operators on major dimensions\n",  
/*052*/  "multi-dimensional arrays must be fully initialized\n",  
/*053*/  "exceeding maximum number of dimensions\n",  
/*054*/  "unmatched closing brace\n",  
/*055*/  "start of function body without function header\n",  
/*056*/  "arrays, local variables and function arguments cannot be public (variable \"%s\")\n",  
/*057*/  "unfinished expression before compiler directive\n",  
/*058*/  "duplicate argument; same argument is passed twice\n",  
/*059*/  "function argument may not have a default value (variable \"%s\")\n",  
/*060*/  "multiple \"#else\" directives between \"#if ... #endif\"\n",  
/*061*/  "\"#elseif\" directive follows an \"#else\" directive\n",  
/*062*/  "number of operands does not fit the operator\n",  
/*063*/  "function result tag of operator \"%s\" must be \"%s\"\n",  
/*064*/  "cannot change predefined operators\n",  
/*065*/  "function argument may only have a single tag (argument %d)\n",  
/*066*/  "function argument may not be a reference argument or an array (argument \"%s\")\n",  
/*067*/  "variable cannot be both a reference and an array (variable \"%s\")\n",  
/*068*/  "invalid rational number precision in #pragma\n",  
/*069*/  "rational number format already defined\n",  
/*070*/  "rational number support was not enabled\n",  
/*071*/  "user-defined operator must be declared before use (function \"%s\")\n",  
/*072*/  "\"sizeof\" operator is invalid on \"function\" symbols\n",  
/*073*/  "function argument must be an array (argument \"%s\")\n",  
/*074*/  "#define pattern must start with an alphabetic character\n",  
/*075*/  "input line too long (after substitutions)\n",  
/*076*/  "syntax error in the expression, or invalid function call\n",  
/*077*/  "malformed UTF-8 encoding, or corrupted file: %s\n",  
/*078*/  "function uses both \"return\" and \"return <value>\"\n",  
/*079*/  "inconsistent return types (array & non-array)\n",  
/*080*/  "unknown symbol, or not a constant symbol (symbol \"%s\")\n",  
/*081*/  "cannot take a tag as a default value for an indexed array parameter (symbol \"%s\")\n",  
/*082*/  "user-defined operators and native functions may not have states\n",  
/*083*/  "a function may only belong to a single automaton (symbol \"%s\")\n",  
/*084*/  "state conflict: one of the states is already assigned to another implementation (symbol \"%s\")\n",  
/*085*/  "no states are defined for function \"%s\"\n",  
/*086*/  "unknown automaton \"%s\"\n",  
/*087*/  "unknown state \"%s\" for automaton \"%s\"\n",  
/*088*/  "number of arguments does not match definition\n"`   
  
Разбор ошибок  
Рассмотрим пример нахождения и самостоятельного решения ошибок при компиляции.  
Допустим у нас есть ошибка:  

> C:\AMXX\example.sma(107) : error 035: argument type mismatch (argument 2)  
> 
  
Теперь давайте попытаемся разобрать эту ошибку по частям:  
1) C:\AMXX\example.sma - это директория, где находится исходник (.sma) нашего плагина.  
2) (107) - это номер строки, в которой есть ошибка. Большинство современных редакторов текста имеют панель с пронумерованными строками (Notepad++, AMXX-Studio и другие).  
3) error 035 - это код ошибки (список ошибок указан выше).  
4) argument type mismatch - это описание ошибки с кодом, указанным до этого. В данном случае нам говорится, что "аргумент имеет неверный тип".  
5) (argument 2) - это более подробное описание ошибки. В данном случае нам указывается, что ошибка во 2 аргументе.  
  
Итого, получаем: в файле example.sma, который находится в директории C:\AMXX, в строке под номером 107 есть ошибка с кодом 035, которая означает, что аргумент 2 имеет неверный тип данных.  
  
Решение ошибок  
Теперь попытаемся исправить нашу ошибку. Идем в строку под номером 107 и видим следующий код:  


Код: [Выделить всё](https://amx-x.ru/viewtopic.php?f=9&t=10) 
    `  
client_print(0,"Welcome to the server!")  
`   
  
Идем на [Вы должны зарегистрироваться, чтобы видеть ссылки.](https://amx-x.ru/ucp.php?mode=login&redirect=.%2Fviewtopic.php%3Ff%3D9%26t%3D10) и читаем описание функции:  

> client_print - Sends a message to a player.   
>   
> Syntax:  
> client_print ( index, type, const message[], ... )   
>   
> id is a player index from 1 to 32. If 0, the message will be sent to all players.   
>   
> The type is one of three types:   
> print_chat - chat text   
> print_console - console message   
> print_notify - console in dev mode   
> print_center - center say  
> 
  
Смотрим синтаксис команды client_print и видим, что первый аргумент index - это номер игрока (id), который может быть от 1 до 32, если же он 0, то сообщение будет отсылаться всем игрокам на сервере. Второй аргумент type - это тип сообщения, который может быть:  

> print_chat - текст в чат  
> print_console - текст в консоль  
> print_notify - текст в консоль в режиме разработчика  
> print_center - текст по центру
  
Третий аргумент message - это и есть текст нашего сообщения. Теперь вернемся, к нашему, коду. Мы видим, что у нас нет второго аргумента (тип сообщения), а сразу идет текст сообщения, исправляем на:  

> client_print(0, print_center, "Welcome to the server!")
  
Теперь компиляция прошла успешно.  
  
Описание ошибок:  
error 001: expected token: "X", but found "Y"  
Ошибка означает, что не найден X, когда найден Y. Наиболее часто возникает, когда забывают поставить недостающие знаки ; { } ( ).  
Пример ошибки:  


Код: [Выделить всё](https://amx-x.ru/viewtopic.php?f=9&t=10) 
    `  
public Function(id)  
{  
    if (is_user_bot(id)  
    return PLUGIN_HANDLED  
      
    // код  
      
    return PLUGIN_CONTINUE  
}  
`   
  
error 017: undefined symbol "X"  
Ошибка означает, что X - неизвестный сивол/команда/переменная/функция. Поэтому такую функцию или переменную нужно объявить перед использованием. Например, функция is_user_hacker не существует.  
Пример ошибки:  


Код: [Выделить всё](https://amx-x.ru/viewtopic.php?f=9&t=10) 
    `  
public Function(id)  
{  
    if (is_user_hacker(id))  
    return PLUGIN_HANDLED  
      
    // код  
      
    return PLUGIN_CONTINUE  
}  
`   
error 032: array index out of bounds (variable X)  
Ошибка означает, что в мы вышли за предел размера массива X.  
Пример ошибки:  


Код: [Выделить всё](https://amx-x.ru/viewtopic.php?f=9&t=10) 
    `  
new s_Name[32]  
s_Name[33]="*"  
`   
  
error 033: array must be indexed (variable X)  
Ошибка означает, что массив должен быть проиндексирован. Например, мы не указали размер массива при его объявлении.  
Пример ошибки:  


Код: [Выделить всё](https://amx-x.ru/viewtopic.php?f=9&t=10) 
    `  
new s_String ="My string"  
`   
  
error 035: argument type mismatch (argument X)  
Ошибка означает, что аргумент X имеет неверный тип данных. Например, когда вместо целочисленного аргумента передаем строку.  
Пример ошибки:  


Код: [Выделить всё](https://amx-x.ru/viewtopic.php?f=9&t=10) 
    `  
public Function1(id)  
{  
    Function2(id,"10")  
}  
  
public Function2(id, count)  
{  
// код  
}  
`   
  
error 040: duplicate "case" label (value X)  
Ошибка означает, что имеется дубль оператора case со значением X.  
Пример ошибки:  


Код: [Выделить всё](https://amx-x.ru/viewtopic.php?f=9&t=10) 
    `  
public Function(id)  
{  
    switch(count)  
{  
        case 1: count += 1  
    case 2: count += 2  
    case 2: count += 3  
    }  
}  
`   
  
error 075: input line too long (after substitutions)  
Ошибка означает, что указанная строка слишком длинная. Например, около 500 символов.  
Пример ошибки:  


Код: [Выделить всё](https://amx-x.ru/viewtopic.php?f=9&t=10) 
    `  
public Function(id)  
{  
    server_print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")  
}  
`   
  
error 078: function uses both "return" and "return <value>"  
Ошибка означает, что функция использует, как return, так и return <значение>.  
Пример ошибки:  


Код: [Выделить всё](https://amx-x.ru/viewtopic.php?f=9&t=10) 
    `  
public Function(id)  
{  
    if (is_user_alive(id))      
        return  
      
    return PLUGIN_HANDLED  
}  
`   
  
error 088: number of arguments does not match definition  
Ошибка означает, что количество переданных аргументов не соответсвует количеству объявленных аргументов.  
Пример ошибки:  


Код: [Выделить всё](https://amx-x.ru/viewtopic.php?f=9&t=10) 
    `  
public Function1(id)  
{  
    Function2(id)  
}  
  
public Function2(id, count)  
{  
// код  
}  
`
