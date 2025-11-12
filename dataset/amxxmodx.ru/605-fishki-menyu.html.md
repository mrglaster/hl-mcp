# Фишки меню
[Ядро AMXx](http://amxxmodx.ru/core/) [amxmodx.inc](http://amxxmodx.ru/core/amxmodxinc/) [Старое меню](http://amxxmodx.ru/core/amxmodxinc/oldmenu/)
**• скрытие меню у игроков**  
Чтобы убрать меню с экрана игрока, ему нужно отправить новое меню, но без клавиш для выбора. Какой текст - не важно, разумнее использовать пустышку. Ну и минимальное время показа - 1 секунда.  
  
Скрыть меню у определённого игрока:  
```
show_menu( id, 0, "^n", 1 )
```
Скрыть меню у всех игроков:  
```
show_menu( 0, 0, "^n", 1 )
```
  
Таким же способом скрываются и 'новые' меню (см. _newmenus.inc_ ): они всего лишь обёртка на т.н. 'старыми': на самом деле в игре меню одно и то же. Важно не забыть предварительно 'нажать' кнопку _Выход_ за игрока с помощью:  
```
menu_cancel(id)
```
  
  
**• длинные строки в меню**  
Максимальный размер текста меню - 512 символов. Но размер пунктов меню **не лимитируется** : они могут быть произвольного размера. Ограничивается только длина текста, не содержащего служебные тэги \d, \r, \w, \y и \R - 80 символов. Поэтому если нужен длинный пункт - просто дополните текст тэгами в нужных местах. На экране помещаются 90 символов при разрешении 800x600 и 115 - при 1024x768. Пример ниже.  
  
**• трансляция команд в клавиши**  
Это встроенная возможность игры. В тексте меню указывается команда, а при показе меню она автоматически заменяется на кнопку, на которую назначена **у игрока**. Работает такая возможность **только для 'плюсовых' команд** : _+attack_ , _+use_ , _+hook_ и т.д., но **для любых** из них.  
  
Пример на последние 2 случая:  

![](http://amxxmodx.ru/templates/3week92/dleimages/spoiler-plus.gif) [Код](javascript:ShowOrHide\('spbd0472135e2c93d9f87a59a04e213114'\))
```
/**  
*    Demonstration of 2 menu features: 'translation' and long items.  
*/  
  
#include <amxmodx />  
  
#define PLUGIN "Menu Features Test"  
#define VERSION "0.1"  
#define AUTHOR "Safety1st"  
  
public plugin_init() {  
    register_plugin( PLUGIN, VERSION, AUTHOR )  
  
    register_clcmd( "menu_test", "MenuCommand" )  
}  
  
public MenuCommand(id) {  
    new szMenu[512]     // it is maximum allowed menu size  
    new iLen = formatex( szMenu, charsmax(szMenu), "\yMenu Test:^n^n" )  
  
    #define ITEMS 3  
    static const szMenuItem[ITEMS][] = {  
        "Sample bind USE key: \y+use",  
        "Sample bind TEST key: \y+test",  
        "Собака серая Собака белая | \wСобака серая Собака белая2 | \wСобака серая Собака белая3 | \yСобака жёлтая"  
    }  
  
    for( new i; i < sizeof szMenuItem; i++ )  
        iLen += formatex( szMenu[iLen], charsmax(szMenu) - iLen, "\y%d. \w%s^n", i + 1, szMenuItem[i] )  
  
    const MENU_KEYS = MENU_KEY_1|MENU_KEY_2|MENU_KEY_3|MENU_KEY_4|MENU_KEY_5|MENU_KEY_6|MENU_KEY_7|MENU_KEY_8|MENU_KEY_9|MENU_KEY_0  
    show_menu( id, MENU_KEYS, szMenu )  
  
    return PLUGIN_HANDLED  
}
```

  
  

[![Фишки меню](http://amxxmodx.ru/uploads/posts/2014-08/thumbs/1407395942_gst.png)](http://amxxmodx.ru/uploads/posts/2014-08/1407395942_gst.png)
  
Чтобы меню выглядело как на скриншоте, необходимо предварительно забиндить клавишу:  

bind "?" "+test"
