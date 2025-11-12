# Урок 25. Работа со словарями
[Уроки по скриптингу для начинающих](http://amxxmodx.ru/lessons-on-pawn/)
**Введение:**  
Данная статья предназначена для тех, кто хотел бы сделать свой сервер, либо отдельный плагин мультиязычным. Для этого существуют словари - файлы, содержащие в себе набор переменных, каждой из которых присвоено своё значение (слово или фраза на одном или нескольких языках). Эта статья как раз и посвящена словарям, точнее, работе с ними. Не будем углубляться в теорию, тем более, что, в данном случае, её почти и нет, разберём всё подробно на практике...  
  
**Практическая часть:**  
Для начала нам необходимо зарегистрировать наш файл словаря:  
```
#include <amxmodx>  
  
#pragma semicolon 1  
  
public plugin_init()  
{  
    register_plugin("Test Dictionary", "0.1a", "[onserver.org] #dev.tm");  
    register_dictionary("test_dictionary.txt"); // регистрация нового файла словаря с именем 'test_dictionary.txt'  
}
```
  
По умолчанию файл должен находиться в директории _./cstrike/addons/amxmodx/data/lang_. В файле словаря (_test_dictionary.txt_) пишем текст следующего содержания:  
  

[en]  
TD_HELLO = Hello, world!  
  
[ru]  
TD_HELLO = Привет, мир!
  
Сохраняем файл в кодировке _UTF-8 без BOM_. Рассмотрим, что же мы написали. Мы создали файл словаря, который поддерживает перевод на два языка: английский и русский. _en_ и _ru_ - это значения ключа _lang_ (_setinfo "lang" "en"_). _TD_HELLO_ - это переменная, _Hello, world!_ и _Привет, мир!_ - её значения для английского и русского языков, соответственно. Переменные, расположенные ниже строки _[en]_ , относятся к переводу на английский язык. Соответственно, переменные, расположенные ниже строки _[ru]_ , относятся к переводу на русский язык. Теперь зарегистрируем команду, при выполнении которой всем игрокам в чат будет выводиться наше сообщение:  
```
#include <amxmodx>  
  
#pragma semicolon 1  
  
public plugin_init()  
{  
    register_plugin("Test Dictionary", "0.1a", "[onserver.org] #dev.tm");  
    register_dictionary("test_dictionary.txt");  
    register_clcmd("say /hello", "CmdHello"); // регистрация команды /hello для отправки сообщения всем игрокам (общий чат)  
    register_clcmd("say_team /hello", "CmdHello"); // регистрация команды /hello для отправки сообщения всем игрокам (командный чат)  
}
```
  
Добавим функцию обработки команды _/hello_ (вывода сообщения):  
```
#include <amxmodx>  
  
#pragma semicolon 1  
  
public plugin_init()  
{  
    register_plugin("Test Dictionary", "0.1a", "[onserver.org] #dev.tm");  
    register_dictionary("test_dictionary.txt");  
    register_clcmd("say /hello", "CmdHello");  
    register_clcmd("say_team /hello", "CmdHello");  
}  
  
public CmdHello()  
{  
    client_print(0, print_chat, "%L", LANG_PLAYER, "TD_HELLO"); // отправка нашего сообщения всем игрокам  
    return PLUGIN_HANDLED; // блокировка отправки команды /hello  
}
```
  
Мы получили простейшую функцию вывода сообщения '_Hello, world!_ ' или '_Привет, мир!_ ' (в зависимости от языковых настроек игрока-получателя сообщения) по команде _/hello_. Как вы, наверное, уже поняли, символы _%L_ в сообщении заменяются на то значение, которое соответствует переменной _TD_HELLO_. Добавим в сообщение никнейм игрока, который вызывает эту функцию (выполняет команду _/hello_):  
```
#include <amxmodx>  
  
#pragma semicolon 1  
  
public plugin_init()  
{  
    register_plugin("Test Dictionary", "0.1a", "[onserver.org] #dev.tm");  
    register_dictionary("test_dictionary.txt");  
    register_clcmd("say /hello", "CmdHello");  
    register_clcmd("say_team /hello", "CmdHello");  
}  
  
public CmdHello(const id)  
{  
    new szName[32]; // объявление нового массива szName  
    get_user_name(id, szName, charsmax(szName)); // получение никнейма игрока, который выполнил команду /hello, в массив szName  
    client_print(0, print_chat, "%s: %L", szName, LANG_PLAYER, "TD_HELLO");  
    return PLUGIN_HANDLED;  
}
```
  
Теперь наше сообщение имеет вид: '_Player: Hello, world!_ ' или '_Player: Привет, мир!_ '. В данном случае мы использовали константу _LANG_PLAYER_ (также можно использовать константу _LANG_SERVER_ , либо _индекс получателя_ , но об этом чуть позже). Обратите внимание, что константа _LANG_PLAYER_ располагается всегда перед переменной _TD_HELLO_ и между ними не должно быть никаких иных аргументов. То есть, подобные варианты:  
```
client_print(0, print_chat, "%s: %L", LANG_PLAYER, szName, "TD_HELLO");
```
  
```
client_print(0, print_chat, "%s: %L", szName, "TD_HELLO", LANG_PLAYER);
```
  
ошибочны и, либо не будут работать вовсе, либо будут работать некорректно. Также для каждой переменной должна быть объявлена своя _константа_. Рассмотрим на конкретном примере. Добавим в файл словаря ещё одну переменную:  
  

[en]  
TD_HELLO = Hello, world!  
TD_SAID = said  
  
[ru]  
TD_HELLO = Привет, мир!  
TD_SAID = сказал
  
Добавим новую переменную в наше сообщение:  
```
#include <amxmodx>  
  
#pragma semicolon 1  
  
public plugin_init()  
{  
    register_plugin("Test Dictionary", "0.1a", "[onserver.org] #dev.tm");  
    register_dictionary("test_dictionary.txt");  
    register_clcmd("say /hello", "CmdHello");  
    register_clcmd("say_team /hello", "CmdHello");  
}  
  
public CmdHello(const id)  
{  
    new szName[32];  
    get_user_name(id, szName, charsmax(szName));  
    client_print(0, print_chat, "%L (%L %s)", LANG_PLAYER, "TD_HELLO", LANG_PLAYER, "TD_SAID", szName);  
    return PLUGIN_HANDLED;  
}
```
  
Теперь сообщение приняло следующий вид: '_Hello, world! (said Player)_ ' или '_Привет, мир! (сказал Player)_ '. С основной частью разобрались, переходим к деталям. Разберём, в каких случаях необходимо использовать константы _LANG_PLAYER_ , _LANG_SERVER_ и _индекс получателя_.  
  
_LANG_PLAYER_ необходимо использовать в тех случаях, когда _индекс получателя_ заранее неизвестен. Например, при отправке сообщения всем игрокам, что мы и делали выше. Во всех остальных случаях желательно использовать _индекс получателя_. Рассмотрим пример. Добавим в словарь ещё одну переменную:  
  

[en]  
TD_HELLO = Hello, world!  
TD_SAID = said  
TD_HEALTH = Your health  
  
[ru]  
TD_HELLO = Привет, мир!  
TD_SAID = сказал  
TD_HEALTH = Ваше здоровье
  
Немного изменим наш код:  
```
#include <amxmodx>  
  
#pragma semicolon 1  
  
public plugin_init()  
{  
    register_plugin("Test Dictionary", "0.1a", "[onserver.org] #dev.tm");  
    register_dictionary("test_dictionary.txt");  
    register_clcmd("say /health", "CmdHealth"); // замена команды /hello на /health (общий чат)  
    register_clcmd("say_team /health", "CmdHealth"); // замена команды /hello на /health (командный чат)  
}  
  
public CmdHealth(const id)  
{  
    client_print(id, print_chat, "%L: %d", id, "TD_HEALTH", get_user_health(id)); // отправка сообщения игроку, выполнившему команду /health  
    return PLUGIN_HANDLED;  
}
```
  
Теперь наше сообщение имеет вид: '_Your health: 100_ ' или '_Ваше здоровье: 100_ '. Как видите, вместо константы _LANG_PLAYER_ перед переменной _TD_HEALTH_ расположен индекс получателя, _id_ , на языковые настройки которого и будет сориентирована система при отправке сообщения.  
  
_LANG_SERVER_ необходимо использовать в тех случаях, когда вы хотите, чтобы при отправке сообщения или его форматировании система была сориентирована на языковые настройки сервера. Также эту константу можно использовать в тех же случаях, что и _LANG_PLAYER_ (то есть, если _индекс получателя_ заранее неизвестен). На практике используется достаточно редко, но, иногда, бывает весьма полезной для решения нестандартных задач.  
  
**Важные детали:**  
Ну и последние детали, на которые следует обратить внимание. Как при составлении файла словаря правильно называть переменные. Я не случайно в начале каждой переменной указал префикс _TD__ (первые буквы от названия плагина, '_Test Dictionary_ '). Переменные с одинаковыми именами могут "пересекаться" между собой, в результате чего мы можем наблюдать в сообщениях плагина совсем не тот текст, который указан в нашем файле словаря. Чтобы этого не случалось, нужно просто не допускать появления переменных с одинаковыми именами в разных файлах словаря.  
  
И ещё один небольшой, но не менее важный нюанс, о котором следует знать и помнить: имена переменных чувствительны к регистру символов, то есть, _TD_HEALTH_ и _TD_health_ - это две разные переменные и при подобных несовпадениях мы получим ошибку типа _ML_NOTFOUND: TD_HEALTH_ , которая означает, что переменная _TD_HEALTH_ не найдена в файле словаря.  
  
**Источник:** [onserver.org](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL29uc2VydmVyLm9yZy90b3BpYy8zMDA0LXR1dC1yYWJvdGEtc28tc2xvdmFyaWFtaS8%3D)
