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

```c
#include <amxmodx>
#include <fakemeta_util>
#include <nrs_main>
#include <nrs_const>
```

> Эти заголовки необходимы для работы с NRS.

---

### Основные настройки NPC

Создайте глобальные переменные для настройки характеристик зомби:

```
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
```

> **Примечание**: Номера анимаций можно посмотреть в HL Model Viewer (например, Jed’s HL Model Viewer).

---

### Регистрация NPC в `plugin_precache()`

```
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
```

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

```
public event_npc_init(ent)
{
    if (get_npc_id(ent) == g_npc_id)
    {
        // Настроить при создании: светиться, спать, телепортироваться и т.д.
        // Пример: entity_set_rendering(ent, kRenderFxGlowShell, 255, 0, 0, kRenderNormal, 25);
    }
}
```

### Получение урона

```
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
```

> **Берсерк**: `npc_set_berserker(ent, 1)` — усиливает урон и скорость NPC.
