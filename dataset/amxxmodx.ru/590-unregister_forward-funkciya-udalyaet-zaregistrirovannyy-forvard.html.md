# unregister_forward - Функция удаляет зарегистрированный форвард.
[The Fakemeta Module](http://amxxmodx.ru/fakemeta/) [fakemeta.inc](http://amxxmodx.ru/fakemeta/fakemetainc/)
Инфо из **fakemeta.inc**  
  
```
/* Unregisters a forward.  
 * The registerId must be from register_forward, and  
 * post/forwardtype must match what you registered the forward as.  
 */  
native unregister_forward(_forwardType, registerId, post=0);
```
  
  
**Синтаксис:**  

unregister_forward(_forwardType, registerId, post=0)
  

    * **_forwardType** - Forward константа  

    * **registerId** - номер зарегистрированного форварда.  

    * **post=0** - пре или пост(по умолчанию пре)  

  
**Тип функции:**  

**native**
  
  
**Описание:**  
Функция удаляет зарегистрированный пользователем форвард по его id.  
  
  
**Пример:**  
Заходим на сервер.  
Пробуем убить себя, у нас ничего не получается.  
Пишем в чат **/delete**   
Пробуем убить себя - получилось.  
Ну и теперь можно посмотреть консоль сервера(или просто свою консоль если проверяете на локалке.)  
  
```
#include <amxmodx>  
#include <fakemeta>  
  
// Создадим переменную для хранения id форварда  
new forwardId  
  
public plugin_init()  
{  
    // Зарегистрируем консольную команду, для удаления форварда.  
    register_clcmd("say /delete", "delete_forwards")  
      
    // Зарегистрируем форвард, и запишем его айди в переменную.  
    forwardId = register_forward(FM_ClientKill, "client_kill_pre")  
    // Выведем в консоль сервера его номер для наглядности.  
    server_print("^nid = %i^n", forwardId)  
}  
public delete_forwards(id)  
{  
    // Удаляем  
    unregister_forward(FM_ClientKill, forwardId)  
    server_print("^nregister_forward id = %i^n", forwardId)  
}  
public client_kill_pre(id)  
{  
    // Получаем имя игрока  
    new name[33]; get_user_name(id, name, charsmax(name))  
    // Выводим в консоль сервера id и имя самоубийцы  
    server_print("^nclient kill %i %s^n", id, name)  
    // Блокируем событие  
    return FMRES_SUPERCEDE  
}
```
  
  
**Вот ещё небольшой пример(удаление моделей из прекэша):**  

![](http://amxxmodx.ru/templates/3week92/dleimages/spoiler-plus.gif) [Показать / Скрыть текст](javascript:ShowOrHide\('sp4ce9aad11cb27c9cae21fc1eacfa7df7'\))
```
#include <amxmodx>  
#include <fakemeta>  
  
new forward_prec_model  
  
new const block_model[][] =  
{  
    "models/v_ak47.mdl",  
    "models/p_ak47.mdl",  
    "models/w_ak47.mdl"  
}  
  
public plugin_init()  
{  
    unregister_forward(FM_PrecacheModel, forward_prec_model)  
}  
public plugin_precache()  
{  
    forward_prec_model = register_forward(FM_PrecacheModel, "precache_models_pre")  
}  
public precache_models_pre(model[])  
{  
    for(new i = 0; i < sizeof(block_model); i++)  
    {  
        if(equal(model, block_model[i])) return FMRES_SUPERCEDE  
    }  
    return FMRES_IGNORED  
}
```

