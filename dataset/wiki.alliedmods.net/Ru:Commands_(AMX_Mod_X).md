# Ru:Commands (AMX Mod X)
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Ru:Commands_\(AMX_Mod_X\)#mw-head), [search](https://wiki.alliedmods.net/Ru:Commands_\(AMX_Mod_X\)#p-search)
**Warning:** This template (and by extension, language format) should not be used, any pages using it should be switched to [Template:Languages](https://wiki.alliedmods.net/Template:Languages "Template:Languages")  
---  
**View this page in:** English [Russian](https://wiki.alliedmods.net/index.php?title=Ru:Ru:Commands_\(AMX_Mod_X\)&action=edit&redlink=1 "Ru:Ru:Commands \(AMX Mod X\) \(page does not exist\)") [简体中文(Simplified Chinese)](https://wiki.alliedmods.net/index.php?title=Zh_cn:Ru:Commands_\(AMX_Mod_X\)&action=edit&redlink=1 "Zh cn:Ru:Commands \(AMX Mod X\) \(page does not exist\)") |   
## Contents
  * [1 Перевод](https://wiki.alliedmods.net/Ru:Commands_\(AMX_Mod_X\)#.D0.9F.D0.B5.D1.80.D0.B5.D0.B2.D0.BE.D0.B4)
  * [2 Введение](https://wiki.alliedmods.net/Ru:Commands_\(AMX_Mod_X\)#.D0.92.D0.B2.D0.B5.D0.B4.D0.B5.D0.BD.D0.B8.D0.B5)
  * [3 Команды администратора](https://wiki.alliedmods.net/Ru:Commands_\(AMX_Mod_X\)#.D0.9A.D0.BE.D0.BC.D0.B0.D0.BD.D0.B4.D1.8B_.D0.B0.D0.B4.D0.BC.D0.B8.D0.BD.D0.B8.D1.81.D1.82.D1.80.D0.B0.D1.82.D0.BE.D1.80.D0.B0)
  * [4 Команды для чата](https://wiki.alliedmods.net/Ru:Commands_\(AMX_Mod_X\)#.D0.9A.D0.BE.D0.BC.D0.B0.D0.BD.D0.B4.D1.8B_.D0.B4.D0.BB.D1.8F_.D1.87.D0.B0.D1.82.D0.B0)
  * [5 Команды голосования](https://wiki.alliedmods.net/Ru:Commands_\(AMX_Mod_X\)#.D0.9A.D0.BE.D0.BC.D0.B0.D0.BD.D0.B4.D1.8B_.D0.B3.D0.BE.D0.BB.D0.BE.D1.81.D0.BE.D0.B2.D0.B0.D0.BD.D0.B8.D1.8F)
  * [6 Команды статистики](https://wiki.alliedmods.net/Ru:Commands_\(AMX_Mod_X\)#.D0.9A.D0.BE.D0.BC.D0.B0.D0.BD.D0.B4.D1.8B_.D1.81.D1.82.D0.B0.D1.82.D0.B8.D1.81.D1.82.D0.B8.D0.BA.D0.B8)
  * [7 Команды в чате](https://wiki.alliedmods.net/Ru:Commands_\(AMX_Mod_X\)#.D0.9A.D0.BE.D0.BC.D0.B0.D0.BD.D0.B4.D1.8B_.D0.B2_.D1.87.D0.B0.D1.82.D0.B5)
  * [8 Команды меню](https://wiki.alliedmods.net/Ru:Commands_\(AMX_Mod_X\)#.D0.9A.D0.BE.D0.BC.D0.B0.D0.BD.D0.B4.D1.8B_.D0.BC.D0.B5.D0.BD.D1.8E)
  * [9 Config Commands](https://wiki.alliedmods.net/Ru:Commands_\(AMX_Mod_X\)#Config_Commands)
  * [10 Команды RCON](https://wiki.alliedmods.net/Ru:Commands_\(AMX_Mod_X\)#.D0.9A.D0.BE.D0.BC.D0.B0.D0.BD.D0.B4.D1.8B_RCON)


# Перевод
Данный перевод является любительским, может содержать ошибки и неточности. Автор перевода не несёт ответственности за лбые несоответствия оригиналу. На данный момент перевод не закончен... 
# Введение
Консольные команды следует вводить по следующей схеме:: 
```
amx_<команда> <опция1> <опция2> [опция3]
```

Обязательные параметры помечены <>, необязательные - []. Символы <> и [] вводить не требуется. 
Для просмотра всех доступных команд, введите в консоле: 
```
amx_help
```

# Команды администратора      Команда  | Формат  | Доступ  | Описание   
---|---|---|---  
amx_kick  | <имя или #userid> [причина]  | ADMIN_KICK  | Кикнуть указанного игрока.   
amx_ban  | <имя или #userid> <время> [причина]  | ADMIN_BAN  | Забанить указанного игрока.   
amx_addban  | <authid или ip> <время> [причина]  | ADMIN_BAN  | Добавить бан в бан-лист сервера.   
amx_unban  | <authid или ip> | ADMIN_BAN  | Разбанить игрока.   
amx_slay  | <имя или #userid> | ADMIN_SLAY  | Убить играка.   
amx_slap  | <имя или #userid> [урон]  | ADMIN_SLAY  | Ударить игрока на несколько хелсов.   
amx_leave  | <тег> [тег1] [тег2] [тег3]  | ADMIN_KICK  | Кикнуть всех игроков, не содержищихся в списке.   
amx_pause  |  | ADMIN_CVAR  | Остановить или продолжить игру.   
amx_who  |  | ADMIN_ADMIN  | Паказать всех, кто на сервера.   
amx_cvar  | <cvar> [value]  | ADMIN_CVAR  | Показать или изменить значения cvar.   
amx_map  | <карта> | ADMIN_MAP  | Сменить карту.   
amx_nick  | <исходное имя> <новое имя> | ADMIN_LEVEL_A  | Изменить ник игрока.   
amx_cfg  | <имя файла> | ADMIN_CFG  | Подключить файл конфигурации   
amx_rcon  | <rcon command line> | ADMIN_RCON  | Выполнить команду в консоли сервера.   
amx_plugins  |  | ADMIN_ADMIN  | Списки всех загружаемых плагинов.   
amx_modules  |  | ADMIN_ADMIN  | Списки всех загружаемых модулей.   
# Команды для чата      Команда  | Формат  | Доступ  | Описание   
---|---|---|---  
amx_say  | <сообщение> | ADMIN_CHAT  | Отправить сообщение всем игрокам.   
amx_chat  | <сообщение> | ADMIN_CHAT  | Отправить сообщение всем администраторам.   
amx_psay  | <имя или #userid> <сообщение> | ADMIN_CHAT  | Отправить приватное сообщение пользователю.   
amx_tsay  | <цвет> <сообщение> | ADMIN_CHAT  | Отправить сообщение определённого цвета над чатом.   
amx_csay  | <цвет> <сообщение> | ADMIN_CHAT  | Отправить сообщение определённого цвета посередине экрана.   
# Команды голосования      Команда  | Формат  | Доступ  | Описание   
---|---|---|---  
amx_votemap  | <карта> [карта] [карта] [карта]  | ADMIN_VOTE  | Голосование на смену карты.   
amx_votekick  | <имя или #userid> | ADMIN_VOTE  | Голосование на кик игрока.   
amx_voteban  | <имя или #userid> | ADMIN_VOTE  | Голосование на бан игрока.   
amx_vote  | <Вопрос> <Ответ1> <ответ2> [ответ3]  | ADMIN_VOTE  | Запустить произвольное голосование.   
amx_cancelvote  |  | ADMIN_VOTE  | Остановить запущенное голосование.   
# Команды статистики      Команда  | Описание   
---|---  
say /hp  | Вывести информацию о вашем убийце.   
say /statsme  | Вывести Вашу статистику.   
say /stats  | отображает статистику других игроков.   
say /top15  | Выводит топ-15 игроков.   
say /rank  | Вывести Ваш ранк на сервере.   
# Команды в чате      Команда  | Описание   
---|---  
say nextmap  | Вывести название следующей карты.   
say timeleft  | Вывести время до смены карты.   
say thetime  | Вывести время сервера.   
# Команды меню
`**Note:** Для этих команд нужен ACCESS_LEVEL_A доступ не "a", а "m".  Смотри: Access Levels[](https://wiki.alliedmods.net/Adding_Admins_\(AMX_Mod_X\)#Access_Levels "Adding Admins \(AMX Mod X\)").[eng]`      Команда  | Доступ  | Описание   
---|---|---  
amxmodmenu  | ADMIN_MENU  | Отображает основное меню AMX Мод Х.   
amx_cvarmenu  | ADMIN_CVAR  | Отобразить меню CVAR.   
amx_mapmenu  | ADMIN_MAP  | Отобразить меню смены карт.   
amx_votemapmenu  | ADMIN_MAP  | Отобразить меню голосования на смену карты.   
amx_kickmenu  | ADMIN_KICK  | Отобразить меню киков.   
amx_banmenu  | ADMIN_BAN  | Отобразить бан-меню.   
amx_slapmenu  | ADMIN_SLAY  | Отобразить меню slap/slay.   
amx_teammenu  | ADMIN_LEVEL_A  | Отобразить меню команд игроков.   
amx_clcmdmenu  | ADMIN_LEVEL_A  | Отобразить меню команд клиента.   
amx_cmdmenu  | ???  | Меню команд сервера.   
amx_restmenu  | ADMIN_CFG  | Отобразить меню оружия.   
amx_teleportmenu  | ADMIN_CFG  | Меню телепорта.   
amx_pausecfgmenu  | ADMIN_CFG  | Меню паузы.   
amx_statscfgmenu  | ADMIN_CFG  | Меню статистики.   
# Config Commands      Command:  | amx_pausecfg   
---|---  
Format:  | <command> [name]   
Access:  | ADMIN_CFG   
Description:  | Pauses a plugin.  
Command list:  

  * off - Pauses all plugins not in the list.
  * on - Unpauses all plugins.
  * stop <file> - Stops a plugin.
  * pause <file> - Pauses a plugin.
  * enable <file> - Enables a plugin.
  * save - Saves a list of stopped plugins.
  * clear - Clears a list of stopped plugins.
  * list [id] - Lists plugins.
  * add <title> - Marks a plugin as unpauseable.

     Command:  | amx_statscfg   
---|---  
Format:  | <command> [parameters]   
Access:  | ADMIN_CFG   
Description:  | Changes a stats setting.  
Command list:  

  * on <variable> - Enable specific option.
  * off <variable> - Disable specific option.
  * save - Save stats configuration.
  * load - Load stats configuration.
  * list [id] - List stats statuses.
  * add <name> <variable> - Add stat variable to the list.

  
# Команды RCON      Команда:  | amxx   
---|---  
Формат:  | <Команда> [параметры]   
Доступ:  |   
Описание:  | Список команд:  

  * amxx version - Показать версию.
  * amxx modules - Отобразить модули.
  * amxx plugins - Отобразить плагины.
  * amxx gpl - Вывести GNU General Public License
  * amxx cvars - Показать команды AMX Mod X для CVARs.
  * amxx cmds - Показать зарегистрированные команды AMX Mod X.
  * amxx pause - остановка плагинов.
  * amxx unpause - Возобнавить работу плагинов из списка

  
  

