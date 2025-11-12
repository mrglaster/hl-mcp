# Где скачать HldsUpdateTool и как пользоваться.
[Downloads](http://amxxmodx.ru/downloads/)
# Внимание! С 2014 г. этот инструмент загрузки **более не актуален**.
  
  

## Что такое HldsUpdateTool
[![Где скачать HldsUpdateTool и как пользоваться.](http://amxxmodx.ru/uploads/posts/2012-04/thumbs/1334867800_install.jpg)](http://amxxmodx.ru/uploads/posts/2012-04/1334867800_install.jpg)**HldsUpdateTool** - Это официальная утилита от VALVE для обновления или скачивания игровых серверов на базе движков SourceGoldSrc.  
Используя эту утилиту вы всегда можете быть уверены в том что у вас последняя официальная версия движка для сервера, без каких либо троянских коней(бекдоров),без скачек с левых серверов и абсолютно бесплатно.  
  

## Где скачать HldsUpdateTool
Необходимую любому админу утилиту вы можете скачать с [официального сайта steam](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL3N0b3JlLnN0ZWFtcG93ZXJlZC5jb20vZG93bmxvYWQvaGxkc3VwZGF0ZXRvb2wuZXhl)  
Или прямо от сюда:  
**Скачать HldsUpdateTool** :  
Вы не можете скачивать файлы с нашего сервера  
  

## Как пользоваться (Windows)
Скачав файл запустите его и следуйте процессу установки. Та нет ни чего сложного, главное выберите регион Европа.После того как установили откройте указанную папку при установке.  
  
Далее необходимо создать текстовый файл, ну например **update.txt** и изменить расширение файла txt на bat, что бы получился файл **update.bat**.  
Это будет конфигурационный файл, в котором необходимо указать следующее:  
  

hldsupdatetool.exe -command update -game cstrike -dir с:\valve\myserver -verify_all  
pause
  

    * **-game cstrike** - Какую игру обновляем/скачиваем  

    * **-dir с:\valve\myserver** - В какую папку, путь не должен содержать русские буквы  

    * **-verify_all** - Обновляем все файлы (если уже есть сервер и его необходимо обновить)  

    * **pause** необходимо просто для того что бы окно после завершения работы не закрылось и вы смогли видеть окончание работы программы.  

После этого запустите получившийся файл. Откроется консоль, в которой вы сможете видеть процесс скачки или обновления вашего сервера.  

[![Где скачать HldsUpdateTool и как пользоваться.](http://amxxmodx.ru/uploads/posts/2012-04/thumbs/1334869913_start-hldsupdatetool.jpg)](http://amxxmodx.ru/uploads/posts/2012-04/1334869913_start-hldsupdatetool.jpg)
[![Где скачать HldsUpdateTool и как пользоваться.](http://amxxmodx.ru/uploads/posts/2012-04/thumbs/1334870021_process-hldsupdatetool.jpg)](http://amxxmodx.ru/uploads/posts/2012-04/1334870021_process-hldsupdatetool.jpg)
[![Где скачать HldsUpdateTool и как пользоваться.](http://amxxmodx.ru/uploads/posts/2012-04/thumbs/1334869828_finish-hldsupdatetool.jpg)](http://amxxmodx.ru/uploads/posts/2012-04/1334869828_finish-hldsupdatetool.jpg)
  
  

### Какие игры можно скачать с ее помощью
Актуальный список на 20 апреля 2012 года.  
Получить же его вы можете сами, поменяв содержимое бат файла на это:  

hldsupdatetool.exe -command list  
pause
  

![](http://amxxmodx.ru/templates/3week92/dleimages/spoiler-plus.gif) [Показать / Скрыть текст](javascript:ShowOrHide\('spcb4c28b071818377c5c9937c8f96ec7d'\))
E:\Valve\HLServer>hldsupdatetool.exe -command list  
Checking bootstrapper version ...  
** 'game' options for Source DS Install:  
  
"Counter-Strike Source"  
"ageofchivalry"  
"alienswarm"  
"cssbeta"  
"diprip"  
"dods"  
"dystopia"  
"episode1"  
"esmod"  
"garrysmod"  
"garrysmodbeta"  
"hl2mp"  
"insurgency"  
"l4d_full"  
"left4dead"  
"left4dead2"  
"left4dead2_demo"  
"orangebox"  
"pvkii"  
"smashball"  
"synergy"  
"tf"  
"tf_beta"  
"zps"  
  
** 'game' options for HL1 DS Install:  
  
"cstrike"  
"cstrike_beta"  
"czero"  
"dmc"  
"dod"  
"gearbox"  
"ricochet"  
"tfc"  
"valve"  
  
** 'game' options for Third-Party game servers:  
  
"ageofchivalry"  
"aliensvspredator"  
"americasarmy3"  
"brink"  
"darkesthour"  
"darkmessiah"  
"defencealliance2"  
"dinodday"  
"diprip"  
"dystopia"  
"esmod"  
"garrysmod"  
"garrysmodbeta"  
"hauntedhellsreach"  
"homefront"  
"homefrontjpn"  
"insurgency"  
"killingfloor"  
"killingfloor_beta"  
"marenostrum"  
"modernwarfare3"  
"mondaynightcombat"  
"naturalselection2"  
"nucleardawn"  
"pvkii"  
"redorchestra"  
"redorchestra2"  
"redorchestra_beta"  
"serioussam3"  
"serioussamhdse"  
"ship"  
"sin"  
"smashball"  
"synergy"  
"tshb"  
"zps"  
  
E:\Valve\HLServer>pause  
Для продолжения нажмите любую клавишу . . .
