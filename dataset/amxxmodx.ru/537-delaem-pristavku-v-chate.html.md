# Делаем приставку в чате
[Готовые скрипты](http://amxxmodx.ru/scripts/)
В этой статье опишу как сделать приставку в чате для админов и випов на ваше усмотрение...  
Ну начнём пожалуй   
Подключаем нужные нам инклюды  
  
```
#include <amxmodx>  
#include <amxmisc>  
#include <cstrike>
```
  
  
Они нам понадобятся в дальнейшем   
регистрируем плагин название автора версию  
```
  
#include <amxmodx>  
#include <amxmisc>  
#include <cstrike>  
  
#define PLGUIN "Message mod for http://amxxmodx.ru"  
#define AUTHOR "Nesquik" Вписать ваше имя ))   
#define VERSION "1.0"  
  
public plugin_init()  
{  
 register_plugin(PLUGIN,AUTHOR,VERSION)  
 register_cvar("admin_acces","m")  
 register_message(get_user_msgid("SayText"),"Tekst") // Отлавливаем событие написания игроком сообщения   
}  
  
//Теперь перейдём к созданию нашего сообщения  
  
public Tekst(msgId,msgDest,msgEnt)  
{  
 new id = get_msg_arg_int(1) // сокращаем ид игрока который пишет сообщения   
 Отлавливаем подключен ли игрок к серверу или нет  
 if(!is_user_connected(id))   
 return PLUGIN_CONTINUE;  
 if(get_user_flags(id) & admin_acces()) // Проверяем на наличие нужных нам флагов  
 {  
  new szTmp[256],szTmp2[256];   
  get_msg_arg_string(2,szTmp, charsmax( szTmp ) ) // поулчаем написаное сообщение  
  
  new szPrefix[64] = "^x04[Админ]"; // Наш префикс   
  
  if(!equal(szTmp,"#Cstrike_Chat_All")) // Если чат между коммандой  
  {  
   add(szTmp2,charsmax(szTmp2),szPrefix); // Ставим наш префикс  
   add(szTmp2,charsmax(szTmp2)," ");  
   add(szTmp2,charsmax(szTmp2),szTmp); // Сообщение  
  }else{ // Если чат общий  
   add(szTmp2,charsmax(szTmp2),szPrefix); //наш префикс   
   add(szTmp2,charsmax(szTmp2)," ^x03%s1^x01: ^x04%s2") // Имя игрока и сообщение  
  }  
  set_msg_arg_string(2,szTmp2); //Устанавливаем вид который мы сделали выше  
 }  
 return PLUGIN_CONTINUE // Продолжаем работу плагина  
}  
  
public admin_acces() // Эта функция получает флаг для определенного доступа в нашем случае это доступ к префиксу  
{  
 new szFlags[24]  
 get_cvar_string("admin_acces",szFlags,charsmax(szFlags)) // Здесь получаем какой флаг   
 return (read_flags(szFlags)) // Читаем флаг   
}
```
  
  
Ну вот собственно у нас получился неплохой чат с префиксом )))  

[![Делаем приставку в чате](http://amxxmodx.ru/uploads/posts/2013-04/thumbs/1366522241_0uryaw7w2tvb.png)](http://amxxmodx.ru/uploads/posts/2013-04/1366522241_0uryaw7w2tvb.png)
