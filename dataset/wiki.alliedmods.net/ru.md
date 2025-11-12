# ConVars (SourceMod Scripting)/ru
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/ConVars_\(SourceMod_Scripting\)/ru#mw-head), [search](https://wiki.alliedmods.net/ConVars_\(SourceMod_Scripting\)/ru#p-search)
**Language:** |  **[English](https://wiki.alliedmods.net/ConVars_\(SourceMod_Scripting\) "ConVars \(SourceMod Scripting\)")** русский  
---|---  
Квары - _это консольные переменные._ Они могут иметь числовое или строчное значение. Их значения могут быть изменены через консоль или с помощью .cfg файлов, а иногда сохраняются для всех сеансов сервера. 
## Contents
  * [1 Введение](https://wiki.alliedmods.net/ConVars_\(SourceMod_Scripting\)/ru#.D0.92.D0.B2.D0.B5.D0.B4.D0.B5.D0.BD.D0.B8.D0.B5)
    * [1.1 Поиск кваров](https://wiki.alliedmods.net/ConVars_\(SourceMod_Scripting\)/ru#.D0.9F.D0.BE.D0.B8.D1.81.D0.BA_.D0.BA.D0.B2.D0.B0.D1.80.D0.BE.D0.B2)
    * [1.2 Создание кваров](https://wiki.alliedmods.net/ConVars_\(SourceMod_Scripting\)/ru#.D0.A1.D0.BE.D0.B7.D0.B4.D0.B0.D0.BD.D0.B8.D0.B5_.D0.BA.D0.B2.D0.B0.D1.80.D0.BE.D0.B2)
  * [2 Использование/Изменение значений](https://wiki.alliedmods.net/ConVars_\(SourceMod_Scripting\)/ru#.D0.98.D1.81.D0.BF.D0.BE.D0.BB.D1.8C.D0.B7.D0.BE.D0.B2.D0.B0.D0.BD.D0.B8.D0.B5.2F.D0.98.D0.B7.D0.BC.D0.B5.D0.BD.D0.B5.D0.BD.D0.B8.D0.B5_.D0.B7.D0.BD.D0.B0.D1.87.D0.B5.D0.BD.D0.B8.D0.B9)
  * [3 Флаги](https://wiki.alliedmods.net/ConVars_\(SourceMod_Scripting\)/ru#.D0.A4.D0.BB.D0.B0.D0.B3.D0.B8)
  * [4 Change Callbacks](https://wiki.alliedmods.net/ConVars_\(SourceMod_Scripting\)/ru#Change_Callbacks)


# Введение
Квары доступны через Handle`s. Есть 2 способа получить Handle квара. Создать новый квар или найти существующий. Если вы создадите уже существующий квар, автоматически будет использоваться старый. 
_Примечание: Handle`s для кваров являются уникальными, их не нужно закрывать или присваивать INVALID_HANDLE. Они должны существовать пока SourceMod запущен._
## Поиск кваров
Искать квары очень просто. Например, вы хотите найти `mp_startmoney` из Counter-Strike:Source: 
```
new g_hStartMoney
 
public OnPluginStart()
{
	g_hStartMoney = FindConVar("mp_startmoney")
}
```

_Примечание: FindConVar() вернет_` INVALID_HANDLE` _если квар не найден. Keep this in mind if you are trying to read ConVars from other plugins._
## Создание кваров
Простейший квар требует всего 2 значения: имя и значение по умолчанию. Тем не менее, он может содержать описание: 
```
new Handle:g_hEnabled
 
public OnPluginStart()
{
	g_hEnabled = CreateConVar("myplugin_enabled", "1", "Включение/Выключение плагина.")
}
```

Вы так же имеете возможностю ограничить значение. Например, давайте создадим квар названием `myplugin_ratio`, который не может быть выше 1,0 и ниже 0,1. 
```
new Handle:g_hEnabled
 
public OnPluginStart()
{
	g_hEnabled = CreateConVar("myplugin_ratio",
			"0.6",
			"Sets a vote ratio",
			_,	/* Флаги (будут обсуждаться позже) */
			true,	/* Включить минимальное значение */
			0.1,
			true,	/* Включить максимальное значение */
			1.0)
}
```

Значение по умолчанию может иметь любой тип данных, и оно не ограничивает будущие типы данных, которые можно использовать. Тем не менее, минимальные и максимальные ограничения всегда должны быть числом с плавающей точкой (float). 
Если вы создаете квар, который уже существует, вы получите Handle на этот квар. Кроме того, сами Handle будут идентичны, поскольку плагин будет владеть Handle. Описание, значение по умолчанию, или ограничения не будут изменены. 
# Использование/Изменение значений
Использовать квары очень просто. Например, мы хотим изменить `mp_startmoney`, но сохранить старое значение и восстановить его позже. Повторно используем наш код `mp_startmoney` от раздела `Получение кваров`: 
```
new g_oldmoney
 
SetStartMoney(newmoney)
{
	g_oldmoney = GetConVarInt(g_hStartMoney)
	SetConVarInt(g_hStartMoney, newmoney)
}
 
RestoreStartMoney()
{
	SetConVarInt(g_hStartMoney, g_oldmoney)
}
```

Хотя существуют различные функции для типов значений (с плавающей точкой, строки, и так далее), внутренние данные всегда сохраняются так же. Например, этот код будет работать: 
```
public GetStartMoney()
{
	decl String:buffer[128]
 
	GetConVarString(g_hStartMoney, buffer, sizeof(buffer))
 
	return StringToInt(buffer)
}
```

Несмотря на то, что `mp_startmoney` целое число, он может использоваться как строка. 
# Флаги
Квары могут иметь ряд флагов, в зависимости от которых могут менять свое поведение. Основные флаги: 
  * `FCVAR_PROTECTED` - Секретная информация (не должны подвергаться воздействию клиентов или логов).
  * `FCVAR_NOTIFY` - Уведомление клиентов об изменении.
  * `FCVAR_CHEAT` - Могут использоваться только в случае если `sv_cheats` равно 1.
  * `FCVAR_REPLICATED` - Принудительная установка значения квара на клиенте.


Например, мы хотим изменить значение квара с флагом FCVAR_CHEAT. The following two functions could be used: 
```
UnsetCheatVar(Handle:hndl)
{
	new flags = GetConVarFlags(hndl)
	flags &= ~FCVAR_CHEAT
	SetConVarFlags(hndl, flags)
}
 
SetCheatVar(Handle:hndl)
{
	new flags = GetConVarFlags(hndl)
	flags |= FCVAR_CHEAT
	SetConVarFlags(hndl, flags)
}
```

# Change Callbacks
As of Half-Life 2, it is possible to know when ConVars change. While this is a very powerful feature, you must be careful not to set a ConVar inside a ConVar change hook such that it re-invokes he same callback. This results in _infinite recursion_. 
For example, let's say you want to detect when `bot_quota` changes and to prevent it from going below 2: 
```
new Handle:g_hBotQuota
 
public OnPluginStart()
{
	g_hBotQuota = FindConVar("bot_quota")
	if (g_hBotQuota != INVALID_HANDLE)
	{
		HookConVarChange(g_hBotQuota, OnBotQuotaChange)
	}
}
 
public OnBotQuotaChange(Handle:cvar, const String:oldVal[], const String:newVal[])
{
	if (StringToInt(newVal) < 2)
	{
		SetConVarInt(cvar, 2)
	}
}
```

**Note 1:** You do not need to explicitly unhook ConVarChange functions on shutdown. These hooks are removed when your plugin unloads. 
**Note 2:** You cannot prevent cvar changes from happening; you can only change the value again. If the engine or game mod already have a change function installed for a ConVar, that function will always be called first. 
