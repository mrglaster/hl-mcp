# Return Value Constants Константы возвращаемого значения
[The Fakemeta Module](http://amxxmodx.ru/fakemeta/) [fakemeta_const.inc](http://amxxmodx.ru/fakemeta/fakemeta_constinc/)
Если вы работаете с функциями движка, то необходимо вернуть значение, например заблокировать стандартное выполнение операции или продолжить.  
Всего таких констант 4  
  
Это фактическое возвращаемое значение функции, используйте их вместо PLUGIN_HANDLED и т.п. при возврате из зарегистрированного форварда.  
Константы возвращаемого значения:  
```
  
#define FMRES_IGNORED    1  
#define FMRES_HANDLED    2  
#define FMRES_OVERRIDE    3  
#define FMRES_SUPERCEDE    4  

```
  
  

    * **FMRES_IGNORED** - Продолжить выполнение вернуть нормальное значение  

    * **FMRES_HANDLED** - Говорит движку что вы что то сделали и возвращает нормальное значение  

    * **FMRES_OVERRIDE** - Со слов более опытных скритеров, это значение не особо правильно работает, и рекомендуется использовать FMRES_SUPERCEDE  

    * **FMRES_SUPERCEDE** - Блокирование выполнение функции и возвращение вашего значения  

  
  
Использование:  
```
return FMRES_SUPERCEDE
```
  
  
Дополнительная информация:  
[Использование FMRES_OVERRIDE](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteG1vZHgudWNvei5ydS9mb3J1bS85LTI1MjgtMQ%3D%3D)
