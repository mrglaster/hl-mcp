# NRS (NPC Register System): Краткое руководство по созданию NPC-зомби


## 1. Установка NRS

### Шаги:

1. Скачайте последнюю версию мода с [zombie-mod.com](https://zombie-mod.com) или с официального форума.
2. Распакуйте файлы по соответствующим папкам (`cstrike/`, `amxmodx/` и т.д.).
3. Вместо редактирования `plugins.ini`:
   - Перейдите в `cstrike/amxmodx/configs/`
   - Создайте файл `plugins-nrs.ini`
   - Все плагины NRS будут автоматически загружены при запуске сервера.

> **Преимущество**: Файлы вида `plugins-*.ini` автоматически подгружаются AMXX.

---

## 2. Создание первого NPC-зомби

### Обязательные include-файлы

c
#include <amxmodx>
#include <fakemeta_util>
#include <nrs_main>
#include <nrs_const>


> Эти заголовки необходимы для работы с NRS.

---

### Основные настройки NPC

Создайте глобальные переменные для настройки характеристик зомби:


// Модель
new g_class_pmodel[164] = "models/player/nrs_cso_big/nrs_cso_big.mdl"
new g_class_modelindex
new g_npc_id

// Настройки (пример)
#define CLASS_NAME              "Мой Зомби"
#define CLASS_TIP               "Опасный тип!"
#define NPC_HEALTH              2000.0
#define NPC_SPEED               300.0
#define NPC_ATTACK              50.0
#define NPC_KNOCKBACK           1.0
#define NPC_ANI_IDLE            0
#define NPC_ANI_RUN             1
#define NPC_ANI_WALK            2
#define NPC_ANI_ATTACK          3
#define NPC_ANI_ATTACKED        4
#define NPC_ANI_DEATH_HEADSHOT  5
#define NPC_ANI_DEATH_NORMAL_SIMPLE  6
#define NPC_ANI_DEATH_NORMAL_BACK    7
#define NPC_ANI_DEATH_NORMAL_FORWARD 8
#define NPC_ANI_DEATH_NORMAL_SPECIAL 9
#define NPC_ANI_MADNESS         10
#define NPC_EVENT               EVENT_SEE_ENEMY
#define NPC_ATTACK_RELOADING    1.0      // Время атаки
#define NPC_ATTACK_RELOADING_WAITTIME 1.1 // Интервал между атаками (должен быть > на 0.1)


> **Примечание**: Номера анимаций можно посмотреть в HL Model Viewer (например, Jed’s HL Model Viewer).

---

### Регистрация NPC в `plugin_precache()`


public plugin_precache()
{
    g_class_modelindex = precache_model(g_class_pmodel);
    
    g_npc_id = register_npc(CLASS_NAME, CLASS_TIP);
    
    if (g_npc_id != -1)
    {
        set_npc_data(g_npc_id, DATA_HEALTH, NPC_HEALTH);
        set_npc_data(g_npc_id, DATA_SPEED, NPC_SPEED);
        set_npc_data(g_npc_id, DATA_ATTACK, NPC_ATTACK);
        set_npc_data(g_npc_id, DATA_KNOCKBACK, NPC_KNOCKBACK);
        
        // Анимации
        set_npc_data(g_npc_id, DATA_ANI_DEATH_HEADSHOT, NPC_ANI_DEATH_HEADSHOT);
        set_npc_data(g_npc_id, DATA_ANI_DEATH_NORMAL_SIMPLE, NPC_ANI_DEATH_NORMAL_SIMPLE);
        set_npc_data(g_npc_id, DATA_ANI_DEATH_NORMAL_BACK, NPC_ANI_DEATH_NORMAL_BACK);
        set_npc_data(g_npc_id, DATA_ANI_DEATH_NORMAL_FORWARD, NPC_ANI_DEATH_NORMAL_FORWARD);
        set_npc_data(g_npc_id, DATA_ANI_DEATH_NORMAL_SPECIAL, NPC_ANI_DEATH_NORMAL_SPECIAL);
        set_npc_data(g_npc_id, DATA_ANI_ATTACKED, NPC_ANI_ATTACKED);
        set_npc_data(g_npc_id, DATA_ANI_IDLE, NPC_ANI_IDLE);
        set_npc_data(g_npc_id, DATA_ANI_MADNESS, NPC_ANI_MADNESS);
        set_npc_data(g_npc_id, DATA_ANI_ATTACK, NPC_ANI_ATTACK);
        set_npc_data(g_npc_id, DATA_ANI_RUN, NPC_ANI_RUN);
        set_npc_data(g_npc_id, DATA_ANI_WALK, NPC_ANI_WALK);
        
        // Поведение
        set_npc_data(g_npc_id, DATA_EVENT, NPC_EVENT);
        set_npc_data(g_npc_id, DATA_ATTACK_RELOADING, NPC_ATTACK_RELOADING);
        set_npc_data(g_npc_id, DATA_ATTACK_WAITTIME, NPC_ATTACK_RELOADING_WAITTIME);
        
        // Берсерк-режим
        set_npc_data(g_npc_id, DATA_MADANI_ATTACK, NPC_ANI_ATTACK);
        set_npc_data(g_npc_id, DATA_MADANI_ATTACK_TIME, NPC_ATTACK_RELOADING);
        set_npc_data(g_npc_id, DATA_MADANI_ATTACK_WAIT, NPC_ATTACK_RELOADING_WAITTIME);
        set_npc_data(g_npc_id, DATA_MADANI_IDLE, NPC_ANI_IDLE);
        set_npc_data(g_npc_id, DATA_MADANI_WALK, NPC_ANI_RUN);
        set_npc_data(g_npc_id, DATA_MADANI_RUN, NPC_ANI_RUN);
        
        // Установка модели
        set_npc_model(g_npc_id, g_class_pmodel);
    }
}


---

### Обязательная инициализация


public plugin_init()
{
    register_plugin("NRS Zombie", "1.0", "zombie-mod.com");
}


---

## 3. Обработка событий NPC

NRS предоставляет автоматические callback-функции. Всегда проверяйте, что событие относится именно к вашему NPC:


if (get_npc_id(ent) == g_npc_id)


### Смерть NPC


public event_npc_death(dead_ent, killer)
{
    if (get_npc_id(dead_ent) == g_npc_id)
    {
        // Выдать награду игроку (killer)
        // Пример: give_item(killer, "weapon_awp")
    }
}


### Инициализация NPC


public event_npc_init(ent)
{
    if (get_npc_id(ent) == g_npc_id)
    {
        // Настроить при создании: светиться, спать, телепортироваться и т.д.
        // Пример: entity_set_rendering(ent, kRenderFxGlowShell, 255, 0, 0, kRenderNormal, 25);
    }
}


### Получение урона


public event_npc_damage(ent, victim, Float:damage)
{
    if (get_npc_id(ent) == g_npc_id)
    {
        // ent — NPC, victim — игрок, нанесший урон
        // Можно активировать берсерк при низком HP:
        // if (get_ent_data_float(ent, "m_flHealth") < 500.0)
        //     npc_set_berserker(ent, 1);
    }
}


> **Берсерк**: `npc_set_berserker(ent, 1)` — усиливает урон и скорость NPC.

# Примеры плагинов, использующих NPC Register System

## Простой зомби

```
#include <amxmodx>
#include <hamsandwich>
#include <fakemeta_util>
#include <engine>
#include <nrs_main>
#include <nrs_const>

//#define WAR3FT_SUPPORT	1

#if defined WAR3FT_SUPPORT
#include <la2a>
#endif

#define	CLASS_NAME				"npc_cso_zm4"
#define	CLASS_TIP				"CSO Zombie (4)"
#define NPC_HEALTH 				100.0
#define NPC_SPEED 				230.0
#define NPC_GRAVITY 				250.5
#define NPC_ATTACK 				15.0
#define NPC_DEFENCE 				1.0
#define NPC_HEDEFENCE 				0.0
#define NPC_HITSPEED 				0.0
#define NPC_HITDELAY				0.0
#define NPC_REGENDLY				0.0
#define NPC_HITREGENDLY				0.0
#define NPC_KNOCKBACK				1.0
#define NPC_ANI_DEATH_HEADSHOT			104.0
#define NPC_ANI_DEATH_NORMAL_SIMPLE 		101.0
#define NPC_ANI_DEATH_NORMAL_BACK		107.0
#define NPC_ANI_DEATH_NORMAL_FORWARD 		109.0
#define NPC_ANI_DEATH_NORMAL_SPECIAL 		103.0
#define NPC_ANI_ATTACKED			99.0
#define NPC_ANI_IDLE				1.0
#define NPC_ANI_MADNESS				1.0
#define NPC_ANI_ATTACK				76.0
#define NPC_ANI_RUN				4.0
#define NPC_ANI_WALK				3.0
#define NPC_ANI_JUMP				6.0
#define NPC_EVENT				1.0
#define NPC_ATTACK_RELOADING			1.7
#define NPC_ATTACK_RELOADING_WAITTIME		2.3


new g_class_modelindex
new g_class_pmodel[164] = "models/player/nrs_cso_drowned/nrs_cso_drowned.mdl"




new const zombie_death[][] = {
	"npc_shared_sounds/zombi_death_1.wav",
	"npc_shared_sounds/zombi_death_2.wav"
}
new const zombie_pain[][] = {
	"npc_shared_sounds/zombi_hurt_01.wav",
	"npc_shared_sounds/zombi_hurt_02.wav"
}
stock zombie_sound_precache()
{
	new i;
	for(i = 0; i < sizeof(zombie_death); i++)
		engfunc(EngFunc_PrecacheSound, zombie_death[i])
	for(i = 0; i < sizeof(zombie_pain); i++)
		engfunc(EngFunc_PrecacheSound, zombie_pain[i])
}


stock ChatColor(const id, const input[], any:...)
{
	new count = 1, players[32]
	static msg[191]
	vformat(msg, 190, input, 3)
    
	replace_all(msg, 190, "!g", "^4") 
	replace_all(msg, 190, "!y", "^1") 
	replace_all(msg, 190, "!r", "^3") 
	replace_all(msg, 190, "!b", "^0")
    
	if (id) players[0] = id; else get_players(players, count, "ch")
	{
		for (new i = 0; i < count; i++)
		{
			if (is_user_connected(players[i]))
			{
				message_begin(MSG_ONE_UNRELIABLE, get_user_msgid("SayText"), {0,0,0}, players[i])
				write_byte(players[i]);
				write_string(msg);
				message_end();
			}
		}
	}
}


new g_npc_id

public plugin_init() 
{         
	register_plugin("CSO : NPC Classic Zombie","1.0","Good_Hash")
}



public event_npc_death(dead_ent, killer)
{
	if ( !pev_valid(dead_ent) || ( get_npc_id(dead_ent) != g_npc_id ))
		return;
	
	emit_sound(dead_ent, CHAN_AUTO, zombie_death[random_num(0, charsmax(zombie_death))], 0.8, ATTN_NORM, 0, PITCH_NORM)
	
	#if defined WAR3FT_SUPPORT
		new to_give = random_num(35, 75)
		change_user_xp(killer, to_give )
		ChatColor(killer, "!gЗа убийство зомби !r+%i!g опыта!", to_give)
	#endif
}
	
public event_npc_init(ent)
{
	if ( !pev_valid(ent) )
		return;
	if ( get_npc_id(ent) == g_npc_id )
	{
		set_npc_events(ent, EVENT_AGRESSION)//EVENT_ZOMBIE_VOID)
		if ( random_num(0,10) <= 3 )
			npc_set_berserker(ent, 1)
	}
}

public event_npc_damage(ent, victim, Float:damage)
	if ( pev_valid(ent) )
		if ( get_npc_id(ent) == g_npc_id )
		{
			if ( is_user_alive(victim) )
				if ( random_num(0,10) <= 3 )
					npc_set_berserker(ent, 1)
			emit_sound(victim, CHAN_AUTO, zombie_pain[random_num(0, charsmax(zombie_pain))], damage > 50.0 ? 1.0 : 0.8, ATTN_NORM, 0, PITCH_NORM)
		}
		
		
public plugin_precache()
{
	g_class_modelindex = precache_model(g_class_pmodel);
	
	g_npc_id = register_npc(CLASS_NAME, CLASS_TIP)

	if(g_npc_id != -1)
	{
		set_npc_data(g_npc_id, DATA_HEALTH, NPC_HEALTH)
		set_npc_data(g_npc_id, DATA_SPEED, NPC_SPEED)
		set_npc_data(g_npc_id, DATA_ATTACK, NPC_ATTACK)
		set_npc_data(g_npc_id, DATA_SPEED, NPC_SPEED)
		set_npc_data(g_npc_id, DATA_DEFENCE, NPC_DEFENCE)
		set_npc_data(g_npc_id, DATA_HEDEFENCE, NPC_HEDEFENCE)
		set_npc_data(g_npc_id, DATA_HITSPEED, NPC_HITSPEED)
		set_npc_data(g_npc_id, DATA_HITDELAY, NPC_HITDELAY)
		set_npc_data(g_npc_id, DATA_REGENDLY, NPC_REGENDLY)
		set_npc_data(g_npc_id, DATA_HITREGENDLY, NPC_HITREGENDLY)
		set_npc_data(g_npc_id, DATA_KNOCKBACK, NPC_KNOCKBACK)
		set_npc_data(g_npc_id, DATA_ANI_DEATH_HEADSHOT, NPC_ANI_DEATH_HEADSHOT)
		set_npc_data(g_npc_id, DATA_ANI_DEATH_NORMAL_SIMPLE, NPC_ANI_DEATH_NORMAL_SIMPLE)
		set_npc_data(g_npc_id, DATA_ANI_DEATH_NORMAL_BACK, NPC_ANI_DEATH_NORMAL_BACK)
		set_npc_data(g_npc_id, DATA_ANI_DEATH_NORMAL_FORWARD, NPC_ANI_DEATH_NORMAL_FORWARD)
		set_npc_data(g_npc_id, DATA_ANI_DEATH_NORMAL_SPECIAL, NPC_ANI_DEATH_NORMAL_SPECIAL)
		set_npc_data(g_npc_id, DATA_ANI_ATTACKED, NPC_ANI_ATTACKED)
		set_npc_data(g_npc_id, DATA_ANI_IDLE, NPC_ANI_IDLE)
		set_npc_data(g_npc_id, DATA_ANI_MADNESS, NPC_ANI_MADNESS)
		set_npc_data(g_npc_id, DATA_ANI_ATTACK, NPC_ANI_ATTACK)
		set_npc_data(g_npc_id, DATA_ANI_RUN, NPC_ANI_RUN)
		set_npc_data(g_npc_id, DATA_ANI_WALK, NPC_ANI_WALK)
		set_npc_data(g_npc_id, DATA_EVENT, NPC_EVENT)
		set_npc_data(g_npc_id, DATA_ATTACK_RELOADING, NPC_ATTACK_RELOADING)
		set_npc_data(g_npc_id, DATA_MODEL_INDEX, float(g_class_modelindex))
		set_npc_data(g_npc_id, DATA_ATTACK_WAITTIME, NPC_ATTACK_RELOADING_WAITTIME)
		
		// Berserker ability..
		set_npc_data(g_npc_id, DATA_MADANI_ATTACK, NPC_ANI_ATTACK)
		set_npc_data(g_npc_id, DATA_MADANI_ATTACK_TIME, NPC_ATTACK_RELOADING)
		set_npc_data(g_npc_id, DATA_MADANI_ATTACK_WAIT, NPC_ATTACK_RELOADING_WAITTIME)
		set_npc_data(g_npc_id, DATA_MADANI_IDLE, NPC_ANI_IDLE)
		set_npc_data(g_npc_id, DATA_MADANI_WALK, NPC_ANI_RUN)
		set_npc_data(g_npc_id, DATA_MADANI_RUN, NPC_ANI_RUN)
		
		set_npc_model(g_npc_id, g_class_pmodel)
		set_npc_data(g_npc_id, DATA_BLOOD_COLOR, 194.0)
	}
	
	zombie_sound_precache()
}
```

## NPC паук

```
#include <amxmodx>
#include <hamsandwich>
#include <fakemeta_util>
#include <engine>
#tryinclude <cstrike>
#include <nrs_main>
#include <nrs_const>

#define WAR3FT_SUPPORT	1

#if defined WAR3FT_SUPPORT
#include <la2a>
#endif

#define	CLASS_NAME				"npc_spider"
#define	CLASS_TIP				"Spider (Bonus Round)"
#define NPC_HEALTH 				55.0
#define NPC_SPEED 				450.0
#define NPC_GRAVITY 				90.5
#define NPC_ATTACK 				10.0
#define NPC_DEFENCE 				1.0
#define NPC_HEDEFENCE 				0.0
#define NPC_HITSPEED 				0.0
#define NPC_HITDELAY				0.0
#define NPC_REGENDLY				0.0
#define NPC_HITREGENDLY				0.0
#define NPC_KNOCKBACK				1.0
#define NPC_ANI_DEATH_HEADSHOT			0.0
#define NPC_ANI_DEATH_NORMAL_SIMPLE 		0.0
#define NPC_ANI_DEATH_NORMAL_BACK		0.0
#define NPC_ANI_DEATH_NORMAL_FORWARD 		0.0
#define NPC_ANI_DEATH_NORMAL_SPECIAL 		0.0
#define NPC_ANI_ATTACKED			8.0
#define NPC_ANI_IDLE				1.0
#define NPC_ANI_MADNESS				2.0
#define NPC_ANI_ATTACK				7.0
#define NPC_ANI_RUN				4.0
#define NPC_ANI_WALK				3.0
#define NPC_ANI_JUMP				6.0
#define NPC_EVENT				0.0
#define NPC_ATTACK_RELOADING			1.0
#define NPC_ATTACK_RELOADING_WAITTIME		1.5


new g_class_modelindex
new g_class_pmodel[164] = "models/player/nrs_spider/nrs_spider.mdl"


stock ChatColor(const id, const input[], any:...)
{
	new count = 1, players[32]
	static msg[191]
	vformat(msg, 190, input, 3)
    
	replace_all(msg, 190, "!g", "^4") 
	replace_all(msg, 190, "!y", "^1") 
	replace_all(msg, 190, "!r", "^3") 
	replace_all(msg, 190, "!b", "^0")
    
	if (id) players[0] = id; else get_players(players, count, "ch")
	{
		for (new i = 0; i < count; i++)
		{
			if (is_user_connected(players[i]))
			{
				message_begin(MSG_ONE_UNRELIABLE, get_user_msgid("SayText"), {0,0,0}, players[i])
				write_byte(players[i]);
				write_string(msg);
				message_end();
			}
		}
	}
}


new g_npc_id

public plugin_init() 
{         
	register_plugin("NRS : NPC Simple Spider","1.0","Good_Hash")
	if(is_module_loaded("cstrike"))     
	{
		const fake = (1<<1)
		log_amx("[NRS] Cstrike support activated!")
		#if fake & (1<<1)
			#define g_Cstrike 1
		#endif
	}
}



public event_npc_death(dead_ent, killer)
{
	if ( !pev_valid(dead_ent) || ( get_npc_id(dead_ent) != g_npc_id ))
		return;
	#if defined WAR3FT_SUPPORT
		new to_give = random_num(5, 15)
		change_user_xp(killer, to_give )
		ChatColor(killer, "!gЗа убийство паукана !r+%i!g опыта!", to_give)
	#endif
}
	
public event_npc_damage(npc_id, attacker_id, Float:damage)
{
	if ( !pev_valid(npc_id) || ( get_npc_id(npc_id) != g_npc_id ))
		return;
	if ( is_user_alive(attacker_id) )
	{
		#if defined g_Cstrike
			cs_set_user_money(attacker_id, cs_get_user_money(attacker_id) + floatround(damage) )
		#endif
	}
}
	
public event_npc_init(ent)
{
	if ( !pev_valid(ent) )
		return;
	if ( get_npc_id(ent) == g_npc_id )
	{
		//set_npc_think(ent_id, value)
		set_npc_events(ent, EVENT_AGRESSION)//EVENT_ZOMBIE_VOID)
	}
}


public plugin_precache()
{
	g_class_modelindex = precache_model(g_class_pmodel);
	
	g_npc_id = register_npc(CLASS_NAME, CLASS_TIP)

	if(g_npc_id != -1)
	{
		set_npc_data(g_npc_id, DATA_HEALTH, NPC_HEALTH)
		set_npc_data(g_npc_id, DATA_SPEED, NPC_SPEED)
		set_npc_data(g_npc_id, DATA_ATTACK, NPC_ATTACK)
		set_npc_data(g_npc_id, DATA_SPEED, NPC_SPEED)
		set_npc_data(g_npc_id, DATA_DEFENCE, NPC_DEFENCE)
		set_npc_data(g_npc_id, DATA_HEDEFENCE, NPC_HEDEFENCE)
		set_npc_data(g_npc_id, DATA_HITSPEED, NPC_HITSPEED)
		set_npc_data(g_npc_id, DATA_HITDELAY, NPC_HITDELAY)
		set_npc_data(g_npc_id, DATA_REGENDLY, NPC_REGENDLY)
		set_npc_data(g_npc_id, DATA_HITREGENDLY, NPC_HITREGENDLY)
		set_npc_data(g_npc_id, DATA_KNOCKBACK, NPC_KNOCKBACK)
		set_npc_data(g_npc_id, DATA_ANI_DEATH_HEADSHOT, NPC_ANI_DEATH_HEADSHOT)
		set_npc_data(g_npc_id, DATA_ANI_DEATH_NORMAL_SIMPLE, NPC_ANI_DEATH_NORMAL_SIMPLE)
		set_npc_data(g_npc_id, DATA_ANI_DEATH_NORMAL_BACK, NPC_ANI_DEATH_NORMAL_BACK)
		set_npc_data(g_npc_id, DATA_ANI_DEATH_NORMAL_FORWARD, NPC_ANI_DEATH_NORMAL_FORWARD)
		set_npc_data(g_npc_id, DATA_ANI_DEATH_NORMAL_SPECIAL, NPC_ANI_DEATH_NORMAL_SPECIAL)
		set_npc_data(g_npc_id, DATA_ANI_ATTACKED, NPC_ANI_ATTACKED)
		set_npc_data(g_npc_id, DATA_ANI_IDLE, NPC_ANI_IDLE)
		set_npc_data(g_npc_id, DATA_ANI_MADNESS, NPC_ANI_MADNESS)
		set_npc_data(g_npc_id, DATA_ANI_ATTACK, NPC_ANI_ATTACK)
		set_npc_data(g_npc_id, DATA_ANI_RUN, NPC_ANI_RUN)
		set_npc_data(g_npc_id, DATA_ANI_WALK, NPC_ANI_WALK)
		set_npc_data(g_npc_id, DATA_EVENT, NPC_EVENT)
		set_npc_data(g_npc_id, DATA_ATTACK_RELOADING, NPC_ATTACK_RELOADING)
		set_npc_data(g_npc_id, DATA_MODEL_INDEX, float(g_class_modelindex))
		set_npc_data(g_npc_id, DATA_ATTACK_WAITTIME, NPC_ATTACK_RELOADING_WAITTIME)
		
		set_npc_model(g_npc_id, g_class_pmodel)
	}
}
```

## Стреляющий зомби 

```
#include <amxmodx>
#include <hamsandwich>
#include <fakemeta_util>
#include <engine>
#include <nrs_main>
#include <nrs_const>

//#define WAR3FT_SUPPORT	1

#if defined WAR3FT_SUPPORT
#include <la2a>
#endif

#define	CLASS_NAME				"npc_miku"
#define	CLASS_TIP				"Miku ( Shooting )"
#define NPC_HEALTH 				100.0
#define NPC_SPEED 				260.0
#define NPC_GRAVITY 				250.5
#define NPC_ATTACK 				15.0
#define NPC_DEFENCE 				1.0
#define NPC_HEDEFENCE 				0.0
#define NPC_HITSPEED 				0.0
#define NPC_HITDELAY				0.0
#define NPC_REGENDLY				0.0
#define NPC_HITREGENDLY				0.0
#define NPC_KNOCKBACK				0.5
#define NPC_ANI_DEATH_HEADSHOT			104.0
#define NPC_ANI_DEATH_NORMAL_SIMPLE 		101.0
#define NPC_ANI_DEATH_NORMAL_BACK		107.0
#define NPC_ANI_DEATH_NORMAL_FORWARD 		109.0
#define NPC_ANI_DEATH_NORMAL_SPECIAL 		103.0
#define NPC_ANI_ATTACKED			75.0
#define NPC_ANI_IDLE				1.0
#define NPC_ANI_MADNESS				1.0
#define NPC_ANI_ATTACK				76.0
#define NPC_ANI_RUN				4.0
#define NPC_ANI_WALK				3.0
#define NPC_ANI_JUMP				6.0
#define NPC_EVENT				0.0
#define NPC_ATTACK_RELOADING			2.0
#define NPC_ATTACK_RELOADING_WAITTIME		1.8
#define NPC_ANI_IDLE_SHOOT 			34.0
#define NPC_ANI_RELOAD				35.0
#define NPC_WEAPON_DAMAGE			19.0
#define NPC_WEAPON_CLIP				30.0


new g_class_modelindex
new g_class_pmodel[164] = "models/player/nrs_npc_miku/nrs_npc_miku.mdl"


stock ChatColor(const id, const input[], any:...)
{
	new count = 1, players[32]
	static msg[191]
	vformat(msg, 190, input, 3)
    
	replace_all(msg, 190, "!g", "^4") 
	replace_all(msg, 190, "!y", "^1") 
	replace_all(msg, 190, "!r", "^3") 
	replace_all(msg, 190, "!b", "^0")
    
	if (id) players[0] = id; else get_players(players, count, "ch")
	{
		for (new i = 0; i < count; i++)
		{
			if (is_user_connected(players[i]))
			{
				message_begin(MSG_ONE_UNRELIABLE, get_user_msgid("SayText"), {0,0,0}, players[i])
				write_byte(players[i]);
				write_string(msg);
				message_end();
			}
		}
	}
}


new g_npc_id

public plugin_init() 
{         
	register_plugin("L4D : NPC Classic Zombie","1.0","Good_Hash")
	
	register_concmd("npc_test", "cmd_create")
}


public cmd_create(id)
{
	set_pev(id, pev_health, 10000.0)
}

public event_npc_death(dead_ent, killer)
{
	if ( !pev_valid(dead_ent) || ( get_npc_id(dead_ent) != g_npc_id ))
		return;
	#if defined WAR3FT_SUPPORT
		new to_give = random_num(35, 75)
		change_user_xp(killer, to_give )
		ChatColor(killer, "!gЗа убийство зомби !r+%i!g опыта!", to_give)
	#endif
}
	
public event_npc_init(ent)
{
	if ( !pev_valid(ent) )
		return;
	if ( get_npc_id(ent) == g_npc_id )
	{
		//set_npc_think(ent_id, value)
		set_npc_events(ent, EVENT_SHOOTER)//EVENT_ZOMBIE_VOID)
	}
}


public plugin_precache()
{
	g_class_modelindex = precache_model(g_class_pmodel);
	
	g_npc_id = register_npc(CLASS_NAME, CLASS_TIP)

	if(g_npc_id != -1)
	{
		set_npc_data(g_npc_id, DATA_HEALTH, NPC_HEALTH)
		set_npc_data(g_npc_id, DATA_SPEED, NPC_SPEED)
		set_npc_data(g_npc_id, DATA_ATTACK, NPC_ATTACK)
		set_npc_data(g_npc_id, DATA_SPEED, NPC_SPEED)
		set_npc_data(g_npc_id, DATA_DEFENCE, NPC_DEFENCE)
		set_npc_data(g_npc_id, DATA_HEDEFENCE, NPC_HEDEFENCE)
		set_npc_data(g_npc_id, DATA_HITSPEED, NPC_HITSPEED)
		set_npc_data(g_npc_id, DATA_HITDELAY, NPC_HITDELAY)
		set_npc_data(g_npc_id, DATA_REGENDLY, NPC_REGENDLY)
		set_npc_data(g_npc_id, DATA_HITREGENDLY, NPC_HITREGENDLY)
		set_npc_data(g_npc_id, DATA_KNOCKBACK, NPC_KNOCKBACK)
		set_npc_data(g_npc_id, DATA_ANI_DEATH_HEADSHOT, NPC_ANI_DEATH_HEADSHOT)
		set_npc_data(g_npc_id, DATA_ANI_DEATH_NORMAL_SIMPLE, NPC_ANI_DEATH_NORMAL_SIMPLE)
		set_npc_data(g_npc_id, DATA_ANI_DEATH_NORMAL_BACK, NPC_ANI_DEATH_NORMAL_BACK)
		set_npc_data(g_npc_id, DATA_ANI_DEATH_NORMAL_FORWARD, NPC_ANI_DEATH_NORMAL_FORWARD)
		set_npc_data(g_npc_id, DATA_ANI_DEATH_NORMAL_SPECIAL, NPC_ANI_DEATH_NORMAL_SPECIAL)
		set_npc_data(g_npc_id, DATA_ANI_ATTACKED, NPC_ANI_ATTACKED)
		set_npc_data(g_npc_id, DATA_ANI_IDLE, NPC_ANI_IDLE)
		set_npc_data(g_npc_id, DATA_ANI_MADNESS, NPC_ANI_MADNESS)
		set_npc_data(g_npc_id, DATA_ANI_ATTACK, NPC_ANI_ATTACK)
		set_npc_data(g_npc_id, DATA_ANI_RUN, NPC_ANI_RUN)
		set_npc_data(g_npc_id, DATA_ANI_WALK, NPC_ANI_WALK)
		set_npc_data(g_npc_id, DATA_EVENT, EVENT_SHOOTER)
		set_npc_data(g_npc_id, DATA_ATTACK_RELOADING, NPC_ATTACK_RELOADING)
		set_npc_data(g_npc_id, DATA_MODEL_INDEX, float(g_class_modelindex))
		set_npc_data(g_npc_id, DATA_ATTACK_WAITTIME, NPC_ATTACK_RELOADING_WAITTIME)
		set_npc_data(g_npc_id, DATA_WEAPON_TYPE, WEAPON_M4A1)
		set_npc_data(g_npc_id, DATA_ANI_IDLE_SHOOT, NPC_ANI_IDLE_SHOOT)
		set_npc_data(g_npc_id, DATA_ANI_RELOAD, NPC_ANI_RELOAD)
		set_npc_data(g_npc_id, DATA_WEAPON_DAMAGE, 19.0)
		set_npc_data(g_npc_id, DATA_WEAPON_CLIP, NPC_WEAPON_CLIP)

		
		set_npc_model(g_npc_id, g_class_pmodel)
	}
}
```


