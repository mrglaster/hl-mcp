# Создание собственного оружия для Haf-Life средствами WeaponMod 

В 2012-м году KORD_12.7 начал написание статьи по разработке собственного оружия с использованием Weapon Mod. Статья так и не была завершена. Исправить это недразумение постараемся мы. В данной статье будут расмотрены методы создания нового оружия для Half-Life средствами модуля Weapon Mod, начиная от простого, заканчивая наворотами.  

## Создание простого оружия 

### Регистрация оружия 

В качестве самого первого примера реализуем винтовку M16, имеющую только автоматический режим огня и использующую патроны от MP5.

Для начала подключим необходимый модуль:

```c
#include <amxmodx>
#include <hl_wpnmod> // Weapon Mod
```

Теперь необходимо задать основные параметры нашего оружия 

```c
#define WEAPON_NAME "weapon_m16a1ep" // Название оружия
#define WEAPON_SLOT	3 // Слот
#define WEAPON_POSITION	5 // Положение в слоте
#define WEAPON_PRIMARY_AMMO	"9mmAR" // Название боеприпасов
#define WEAPON_PRIMARY_AMMO_MAX	200 // Максимальное количество патронов
#define WEAPON_SECONDARY_AMMO	"" // Название второго типа боезапаса (например, гранаты для подствольника) 
#define WEAPON_SECONDARY_AMMO_MAX	0 // Их же максимальное количество
#define WEAPON_MAX_CLIP	30 // Количество патронов в одной обойме. Поставьте значение -1, если не хотите разделения на обоймы (перезарядки тоже не будет)
#define WEAPON_DEFAULT_AMMO	 200 // Количество патронов при подборе оружия 
#define WEAPON_FLAGS	0
#define WEAPON_WEIGHT	20 // "Вес" оружия. По этому параметру происходит определение, какое оружие "круче" при автоподборе. 
#define WEAPON_DAMAGE	70.0 // Урон оружия при основной атаке
#define ANIM_EXTENSION	"mp5" // Анимация игрока при использовании оружия
```

Опишем анимации. Делается это, чтобы использовать название анимации вместо её номера.   

```c
enum _:cz_VUL
{
	ANIM_IDLE,
	ANIM_SHOOT1,
	ANIM_SHOOT2,
	ANIM_RELOAD,
	ANIM_DRAW,
	ANIM_SHOOT3,
	ANIM_SHOOT4
}; 
```

Порядок их должен быть таким же, как и во вьювере. Названия могут отличаться 

<img width="230" height="131" alt="image" src="https://github.com/user-attachments/assets/b20dcebe-0da9-4aad-92f2-2d5b6d5da4a2" />

Если затронули модели, то опишем уже и все ресурсы, используемые плагином: 

```c
// Models
#define MODEL_WORLD	"models/hl-hev/m16a1/w_m16a1ep.mdl"
#define MODEL_VIEW	"models/hl-hev/m16a1/v_m16a1ep_hev.mdl"
#define MODEL_PLAYER	"models/hl-hev/m16a1/p_m16a1ep.mdl"

// Hud
#define WEAPON_HUD_TXT	"sprites/weapon_m16a1ep.txt"
#define WEAPON_HUD_BAR	"sprites/640hud79.spr"

// Sounds
#define SOUND_FIRE	"weapons/hl-hev/m16a1/m16a1ep_shoot.wav"
#define SOUND_BOLTUP 	"weapons/hl-hev/m16a1/m16a1ep_boltpull.wav"
#define SOUND_RELOAD	"weapons/hl-hev/m16a1/m16a1ep_clipout.wav"
#define SOUND_DEPLOY "weapons/hl-hev/m16a1/m16a1ep_deploy.wav"
#define SOUND_CLIPIN "weapons/hl-hev/m16a1/m16a1ep_clipin.wav"
```

И загрузим их в методе ```plugin_precache```

```c
public plugin_precache()
{
	PRECACHE_MODEL(MODEL_VIEW);
	PRECACHE_MODEL(MODEL_WORLD);
	PRECACHE_MODEL(MODEL_PLAYER);
	
	PRECACHE_SOUND(SOUND_RELOAD);
	PRECACHE_SOUND(SOUND_FIRE);
	PRECACHE_SOUND(SOUND_CLIPIN);
	PRECACHE_SOUND(SOUND_BOLTUP);
	PRECACHE_SOUND(SOUND_DEPLOY);
	
	PRECACHE_GENERIC(WEAPON_HUD_TXT);
	PRECACHE_GENERIC(WEAPON_HUD_BAR);
}
```



Теперь нам необходимо зарегестрировать наше оружие в модуле, для этого используем натив ```wpnmod_register_weapon``` в методе ```plugin_init```. И так, давайте сделаем это. Для этого нам понадобятся созданные ранее макросы.

```c
public plugin_init() {
	register_plugin(PLUGIN, VERSION, AUTHOR);
	new M16 = wpnmod_register_weapon
	(
		WEAPON_NAME,
		WEAPON_SLOT,
		WEAPON_POSITION,
		WEAPON_PRIMARY_AMMO,
		WEAPON_PRIMARY_AMMO_MAX,
		WEAPON_SECONDARY_AMMO,
		WEAPON_SECONDARY_AMMO_MAX,
		WEAPON_MAX_CLIP,
		WEAPON_FLAGS,
		WEAPON_WEIGHT
	);
}
```
Мы его зарегистрировали, в M16 находится ID нашего оружия. Что с ним делать? С помошью этого ID мы можем регистрировать различные хуки нашего оружия, для этого используем натив ```wpnmod_register_weapon_forward```. 

```c
wpnmod_register_weapon_forward(M16,Fwd_Wpn_Spawn,"M16_Spawn"); // Спавн оружия на земле
wpnmod_register_weapon_forward(M16,Fwd_Wpn_Deploy,"M16_Deploy"); // Появление оружия (опционально; используй, если есть анимация)
wpnmod_register_weapon_forward(M16,Fwd_Wpn_Holster,"M16_Holster"); // Анимация смены оружия (опционально; используй, если есть анимация)
wpnmod_register_weapon_forward(M16,Fwd_Wpn_Idle,"M16_Idle"); // Поведение в состоянии Idle
wpnmod_register_weapon_forward(M16,Fwd_Wpn_PrimaryAttack,"M16_PrimaryAttack"); // Хук для основной атаки
wpnmod_register_weapon_forward(M16,Fwd_Wpn_Reload,"M16_Reload"); // Хук для перезарадки
```

Помимо этих существуют другие хуки, например, на работу с дополнительной атакой или использовании при создании собственных типов боеприпасов. Работа с ними будет описано в разделе "Усложнения".

По итогу ```plugin_init``` принимает следующий вид: 

```c
public plugin_init() {
	register_plugin(PLUGIN, VERSION, AUTHOR);
	new M16 = wpnmod_register_weapon
	(
		WEAPON_NAME,
		WEAPON_SLOT,
		WEAPON_POSITION,
		WEAPON_PRIMARY_AMMO,
		WEAPON_PRIMARY_AMMO_MAX,
		WEAPON_SECONDARY_AMMO,
		WEAPON_SECONDARY_AMMO_MAX,
		WEAPON_MAX_CLIP,
		WEAPON_FLAGS,
		WEAPON_WEIGHT
	);

	wpnmod_register_weapon_forward(M16,Fwd_Wpn_Spawn,"M16_Spawn"); // Спавн оружия на земле
	wpnmod_register_weapon_forward(M16,Fwd_Wpn_Deploy,"M16_Deploy"); // Появление оружия (опционально; используй, если есть анимация)
	wpnmod_register_weapon_forward(M16,Fwd_Wpn_Holster,"M16_Holster"); // Анимация смены оружия (опционально; используй, если есть анимация)
	wpnmod_register_weapon_forward(M16,Fwd_Wpn_Idle,"M16_Idle"); // Поведение в состоянии Idle
	wpnmod_register_weapon_forward(M16,Fwd_Wpn_PrimaryAttack,"M16_PrimaryAttack"); // Хук для основной атаки
	wpnmod_register_weapon_forward(M16,Fwd_Wpn_Reload,"M16_Reload"); // Хук для перезарадки
}
```
### Реализация хуков 

#### Спавн оружия 

Начнем с реализации метода ```M16_Spawn```, который срабатывает при спавне сущности оружия. В нем мы задаем модель оружия, а также количество боеприпасов, которое получит игрок при подборе. 

```c
public M16_Spawn(const iItem)
{
	//Set model to floor
	SET_MODEL(iItem, MODEL_WORLD);
	
	// Give a default ammo to weapon
	wpnmod_set_offset_int(iItem, Offset_iDefaultAmmo, WEAPON_DEFAULT_AMMO);
}
```

#### "Развертывание" оружия 

Теперь реализуем метод ```M16_Deploy```. Этот метод вызывается, когда игрок достает данное оружие. В методе мы задаем view модель, анимацию доставания, время, через которое можно начать стрельбу, а также проигрываем звук, если это необходимо.

```c
public M16_Deploy(const iItem, const iPlayer, const iClip)
{
	wpnmod_set_offset_float(iItem, Offset_flNextPrimaryAttack, 1.0); // Стрелять сможем начать через 1 секунду
	wpnmod_set_offset_float(iItem, Offset_flTimeWeaponIdle, 1.2); // Если ничего не делаем, то переходим в состояние Idle через 1.2 секунды.
	emit_sound(iPlayer, CHAN_WEAPON, SOUND_DEPLOY, 0.9, ATTN_NORM, 0, PITCH_NORM);
	return wpnmod_default_deploy(iItem, MODEL_VIEW, MODEL_PLAYER, ANIM_DRAW, ANIM_EXTENSION);
}
```
#### Состояние покоя 

Для обработки состояния Idle реализуем соответствующий метод. 

```c
public M16_Idle(const iItem)
{
	wpnmod_reset_empty_sound(iItem);

	
	if (wpnmod_get_offset_float(iItem, Offset_flTimeWeaponIdle) > 0.0)
	{
		return;
	}

	wpnmod_send_weapon_anim(iItem, ANIM_IDLE); // Анимация состояния покоя 
	wpnmod_set_offset_float(iItem, Offset_flTimeWeaponIdle, 6.0); // Через сколько анимация будет проиграна повторно
}
```

#### Убираем оружие в инвентарь 

Реализуем метод обратный методу доставания - метод ```M16_Holster```. В методе мы указываем анимацию, которая будет проиграна при смене оружия, а также останавливаем все прочие процессы (например, перезарядку). 

```c
public M16_Holster(const iItem , iPlayer)
{
	// Cancel any reload in progress.
	wpnmod_set_offset_int(iItem, Offset_iInSpecialReload, 0);
	// wpnmod_send_weapon_anim(iItem, ANIM_HOLSTER) - В нашей v_ модели нет такой анимации. Поэтому строка закомментирована. 
}
```


#### Перезарядка

Реализуем метод ```M16_Reload```, отвечающий за перезарядку. В Weaponmod за перезарядку отвечает функция ```wpnmod_default_reload``` и одним из её аргументов является длительность анимации перезарядке. Оно рассчитывается как Количество кадров анимации  / FPS анимаци. Узнать их можно в любом просмотрщике моделей, выбрав соответствующую анимацию.  В нашем случае количество кадров было 114, а FPS 30. Получаем значение 3.8.

<img width="457" height="101" alt="image" src="https://github.com/user-attachments/assets/239367c3-9db5-4af3-8b38-549690ac1ad3" />


```c
public M16_Reload(const iItem, const iPlayer, const iClip, const iAmmo)
{
	if (iAmmo <= 0 || iClip >= WEAPON_MAX_CLIP)
	{
		return;
	}
	
	wpnmod_default_reload(iItem, WEAPON_MAX_CLIP, ANIM_RELOAD, 3.8); // 3.8 - длительность анимации перезарядки

	// Проигрыш отдельных звуков при перезарядке. Опционально, если проиграть только один звук или не проигрывать звуков вовсе, то ничего не поменяется.
	//Clip out
	set_task(1.8 , "M16_Reload_Step1" , iPlayer);
	//Clip in
	set_task(3.0 , "M16_Reload_Step2" , iPlayer);
	//Boltup
	set_task(3.8 , "M16_Reload_Step1" , iPlayer);
}

public M16_Reload_Step1(iPlayer)
{
	emit_sound(iPlayer, CHAN_WEAPON, SOUND_RELOAD, 0.9, ATTN_NORM, 0, PITCH_NORM);
}

public M16_Reload_Step2(iPlayer)
{
	emit_sound(iPlayer, CHAN_WEAPON, SOUND_CLIPIN, 0.9, ATTN_NORM, 0, PITCH_NORM);
}
public M16_Reload_Step3(iPlayer)
{
	emit_sound(iPlayer, CHAN_WEAPON, SOUND_BOLTUP, 0.9, ATTN_NORM, 0, PITCH_NORM);
}
```

#### Стрельба 

Передем к самому главному - стрельбе. Реализуем метод 

```c
public M16_PrimaryAttack(const iItem, const iPlayer, iClip)
{
	// Проверка возможна ли стрельба: если нет патронов в магазине или игрок под водой - не стреляем
	if (pev(iPlayer, pev_waterlevel) == 3 || iClip <= 0)
	{
		wpnmod_play_empty_sound(iItem);
		wpnmod_set_offset_float(iItem, Offset_flNextPrimaryAttack, 0.15);
		return;
	}

	wpnmod_set_offset_int(iItem, Offset_iClip, iClip -= 1); // Уменьшаем количество патронов в обойме на 1
	wpnmod_set_offset_int(iPlayer, Offset_iWeaponVolume, LOUD_GUN_VOLUME); // Настройка громкости выстрела
	wpnmod_set_offset_int(iPlayer, Offset_iWeaponFlash, BRIGHT_GUN_FLASH); // Вспышка от выстрела

	wpnmod_set_offset_float(iItem, Offset_flNextPrimaryAttack, 0.08); // Через сколько можно выстрелить в следующий раз
	wpnmod_set_offset_float(iItem, Offset_flTimeWeaponIdle, 1.0);

	wpnmod_set_player_anim(iPlayer, PLAYER_ATTACK1); // Анимация модели игрока 
	wpnmod_send_weapon_anim(iItem, ANIM_SHOOT1); // Анимация от первого лица

	wpnmod_fire_bullets(
		iPlayer, // Игрок
		iPlayer, // Атакующий
		1, // Количество выпускаемых пуль
		VECTOR_CONE_1DEGREES, // Как будут лететь пули: d 
		8192.0, // Максимальное дистанция выстрела
		WEAPON_DAMAGE, // Урон 1 пули
		DMG_BULLET | DMG_NEVERGIB, // Тип наносимого урона
		1 // как часто пули будут оставлять след в воздухе
	);

	emit_sound(iPlayer, CHAN_WEAPON, SOUND_FIRE, 0.9, ATTN_NORM, 0, PITCH_NORM); // Проигрываем звук выстрела

	set_pev(iPlayer, pev_effects, pev(iPlayer, pev_effects) | EF_MUZZLEFLASH); // Эффект вспышки
	set_pev(iPlayer, pev_punchangle, Float:{-1.0, 0.0, 0.0}); // Отдача
}
```
#### Итог

По итогу мы получаем следующий код простого плагина: 

```c
#include <amxmodx>
#include <hl_wpnmod>

#define PLUGIN "Weapon M16"
#define VERSION "1.0"
#define AUTHOR "Demo"

// Основные параметры оружия
#define WEAPON_NAME "weapon_m16a1ep"
#define WEAPON_SLOT 4
#define WEAPON_POSITION 5
#define WEAPON_PRIMARY_AMMO "9mmAR"
#define WEAPON_PRIMARY_AMMO_MAX 200
#define WEAPON_SECONDARY_AMMO ""
#define WEAPON_SECONDARY_AMMO_MAX 0
#define WEAPON_MAX_CLIP 30
#define WEAPON_DEFAULT_AMMO 200
#define WEAPON_FLAGS 0
#define WEAPON_WEIGHT 20
#define WEAPON_DAMAGE 70.0
#define ANIM_EXTENSION "mp5"

// Анимации
enum _:cz_VUL
{
	ANIM_IDLE,
	ANIM_SHOOT1,
	ANIM_SHOOT2,
	ANIM_RELOAD,
	ANIM_DRAW,
	ANIM_SHOOT3,
	ANIM_SHOOT4
};

// Модели
#define MODEL_WORLD "models/hl-hev/m16a1/w_m16a1ep.mdl"
#define MODEL_VIEW "models/hl-hev/m16a1/v_m16a1ep_hev.mdl"
#define MODEL_PLAYER "models/hl-hev/m16a1/p_m16a1ep.mdl"

// HUD
#define WEAPON_HUD_TXT "sprites/weapon_m16a1ep.txt"
#define WEAPON_HUD_BAR "sprites/640hud79.spr"

// Звуки
#define SOUND_FIRE "weapons/hl-hev/m16a1/m16a1ep_shoot.wav"
#define SOUND_BOLTUP "weapons/hl-hev/m16a1/m16a1ep_boltpull.wav"
#define SOUND_RELOAD "weapons/hl-hev/m16a1/m16a1ep_clipout.wav"
#define SOUND_DEPLOY "weapons/hl-hev/m16a1/m16a1ep_deploy.wav"
#define SOUND_CLIPIN "weapons/hl-hev/m16a1/m16a1ep_clipin.wav"

// Глобальный ID оружия
new g_iM16;

public plugin_precache()
{
	PRECACHE_MODEL(MODEL_VIEW);
	PRECACHE_MODEL(MODEL_WORLD);
	PRECACHE_MODEL(MODEL_PLAYER);

	PRECACHE_SOUND(SOUND_RELOAD);
	PRECACHE_SOUND(SOUND_FIRE);
	PRECACHE_SOUND(SOUND_CLIPIN);
	PRECACHE_SOUND(SOUND_BOLTUP);
	PRECACHE_SOUND(SOUND_DEPLOY);

	PRECACHE_GENERIC(WEAPON_HUD_TXT);
	PRECACHE_GENERIC(WEAPON_HUD_BAR);
}

public plugin_init()
{
	register_plugin(PLUGIN, VERSION, AUTHOR);

	g_iM16 = wpnmod_register_weapon(
		WEAPON_NAME,
		WEAPON_SLOT,
		WEAPON_POSITION,
		WEAPON_PRIMARY_AMMO,
		WEAPON_PRIMARY_AMMO_MAX,
		WEAPON_SECONDARY_AMMO,
		WEAPON_SECONDARY_AMMO_MAX,
		WEAPON_MAX_CLIP,
		WEAPON_FLAGS,
		WEAPON_WEIGHT
	);

	// Регистрация хуков
	wpnmod_register_weapon_forward(g_iM16, Fwd_Wpn_Spawn, "M16_Spawn");
	wpnmod_register_weapon_forward(g_iM16, Fwd_Wpn_Deploy, "M16_Deploy");
	wpnmod_register_weapon_forward(g_iM16, Fwd_Wpn_Holster, "M16_Holster");
	wpnmod_register_weapon_forward(g_iM16, Fwd_Wpn_Idle, "M16_Idle");
	wpnmod_register_weapon_forward(g_iM16, Fwd_Wpn_PrimaryAttack, "M16_PrimaryAttack");
	wpnmod_register_weapon_forward(g_iM16, Fwd_Wpn_Reload, "M16_Reload");
}

// Спавн оружия на земле
public M16_Spawn(const iItem)
{
	SET_MODEL(iItem, MODEL_WORLD);
	wpnmod_set_offset_int(iItem, Offset_iDefaultAmmo, WEAPON_DEFAULT_AMMO);
}

// Доставание оружия
public M16_Deploy(const iItem, const iPlayer, const iClip)
{
	wpnmod_set_offset_float(iItem, Offset_flNextPrimaryAttack, 1.0);
	wpnmod_set_offset_float(iItem, Offset_flTimeWeaponIdle, 1.2);
	emit_sound(iPlayer, CHAN_WEAPON, SOUND_DEPLOY, 0.9, ATTN_NORM, 0, PITCH_NORM);
    return wpnmod_default_deploy(iItem, MODEL_VIEW, MODEL_PLAYER, ANIM_DRAW, ANIM_EXTENSION);
}

// Состояние покоя
public M16_Idle(const iItem)
{
	wpnmod_reset_empty_sound(iItem);

	
	if (wpnmod_get_offset_float(iItem, Offset_flTimeWeaponIdle) > 0.0)
	{
		return;
	}

	wpnmod_send_weapon_anim(iItem, ANIM_IDLE); // Анимация состояния покоя 
	wpnmod_set_offset_float(iItem, Offset_flTimeWeaponIdle, 6.0); // Через сколько анимация будет проиграна повторно
}

// Убирание оружия
public M16_Holster(const iItem, iPlayer)
{
	wpnmod_set_offset_int(iItem, Offset_iInSpecialReload, 0);
	// wpnmod_send_weapon_anim(iItem, ANIM_HOLSTER); // Если есть анимация
}

// Idle (ничего не делаем, можно оставить пустым)
public M16_Idle(const iItem, const iPlayer)
{
	// Можно добавить анимацию или звук по таймеру, если нужно
}

// Перезарядка
public M16_Reload(const iItem, const iPlayer, const iClip, const iAmmo)
{
	if (iAmmo <= 0 || iClip >= WEAPON_MAX_CLIP)
	{
		return;
	}

	wpnmod_default_reload(iItem, WEAPON_MAX_CLIP, ANIM_RELOAD, 3.8);

	// Пошаговые звуки перезарядки
	set_task(1.8, "M16_Reload_Step1", iPlayer);
	set_task(3.0, "M16_Reload_Step2", iPlayer);
	set_task(3.8, "M16_Reload_Step3", iPlayer);
}

public M16_Reload_Step1(iPlayer)
{
	emit_sound(iPlayer, CHAN_WEAPON, SOUND_RELOAD, 0.9, ATTN_NORM, 0, PITCH_NORM);
}

public M16_Reload_Step2(iPlayer)
{
	emit_sound(iPlayer, CHAN_WEAPON, SOUND_CLIPIN, 0.9, ATTN_NORM, 0, PITCH_NORM);
}

public M16_Reload_Step3(iPlayer)
{
	emit_sound(iPlayer, CHAN_WEAPON, SOUND_BOLTUP, 0.9, ATTN_NORM, 0, PITCH_NORM);
}

// Основная атака (автоматический огонь)
public M16_PrimaryAttack(const iItem, const iPlayer, iClip)
{
	if (pev(iPlayer, pev_waterlevel) == 3 || iClip <= 0)
	{
		wpnmod_play_empty_sound(iItem);
		wpnmod_set_offset_float(iItem, Offset_flNextPrimaryAttack, 0.15);
		return;
	}

	wpnmod_set_offset_int(iItem, Offset_iClip, --iClip);
	wpnmod_set_offset_int(iPlayer, Offset_iWeaponVolume, LOUD_GUN_VOLUME);
	wpnmod_set_offset_int(iPlayer, Offset_iWeaponFlash, BRIGHT_GUN_FLASH);

	wpnmod_set_offset_float(iItem, Offset_flNextPrimaryAttack, 0.08);
	wpnmod_set_offset_float(iItem, Offset_flTimeWeaponIdle, 1.0);

	wpnmod_set_player_anim(iPlayer, PLAYER_ATTACK1);
	wpnmod_send_weapon_anim(iItem, ANIM_SHOOT1);

	wpnmod_fire_bullets(
		iPlayer,
		iPlayer,
		1,
		VECTOR_CONE_1DEGREES,
		8192.0,
		WEAPON_DAMAGE,
		DMG_BULLET | DMG_NEVERGIB,
		1
	);

	emit_sound(iPlayer, CHAN_WEAPON, SOUND_FIRE, 0.9, ATTN_NORM, 0, PITCH_NORM);
	set_pev(iPlayer, pev_effects, pev(iPlayer, pev_effects) | EF_MUZZLEFLASH);
	set_pev(iPlayer, pev_punchangle, Float:{-1.0, 0.0, 0.0});
}
```

В следующих разделах рассмотрим, как можно разнообразить разрабатываемое вооружение.

## Усложнения 

### Альтернативная атака

Weaponmod поддерживает возможность добавления альтернативной атаки. Для её реализации вам необходимо сделать следующее: 

1) в ```plugin_ini``` вам необходимо зарегистрировать форвард на дополнительную атаку. Выглядеть это будет следующим образом:

```c
public plugin_init(){
	...
	wpnmod_register_weapon_forward(iSG, Fwd_Wpn_SecondaryAttack, "Weapon_SecondaryAttack"); // Регистрируем форвард на дополнительную атаку 	
}
```

2) Теперь вам необходимо реализовать натив ```Weapon_SecondaryAttack```. Реализация у него точно такая же, как и у метода для основной атаки.

```c
public Weapon_SecondaryAttack(const iItem, const iPlayer) {
    // Ваш код натива
}
```

### Собственный тип боеприпасов

Одной из возможностей Weapon Mod является создание уникальных типов боеприпасов, которые не существуют в оригинальной игре Half-Life. Это позволяет реализовать, например, энергетические патроны, крио-заряды, кислотные гранаты и прочие фантастические боеприпасы, не конфликтуя с уже существующими типами вроде "9mm", "357" или "uranium". Рассмотрим создание собственного типа боеприпасов. 

1) Зададим имена типу патронов и класснейм аммобоксу с ними

```c
#define WEAPON_PRIMARY_AMMO		"762" // Это название будет использовано при регистрации оружия
#define AMMOBOX_CLASSNAME		"ammo_762" // Класс для оружейного ящика
#define MODEL_CLIP			"models/w_m40a1clip.mdl" // Модель для подбираемых патронов
```

2) Зарегистрируем новый тип боезапаса. В ```plugin_init``` вам необходимо прописать:

```c
public plugin_init(){
    new iAmmo762 = wpnmod_register_ammobox(AMMOBOX_CLASSNAME); // Регистрируем новый тип боезапаса
    wpnmod_register_ammobox_forward(iAmmo762, Fwd_Ammo_Spawn, "Ammo762_Spawn"); // В методе Ammo762_Spawn мы задаем модель для подбираемых поеприпасов
    wpnmod_register_ammobox_forward(iAmmo762, Fwd_Ammo_AddAmmo, "Ammo762_AddAmmo"); // Логика выдачи патронов игроку
}
```

3) Реализуем метод, вызываемый при спавне патронов

```c
public Ammo762_Spawn(const iItem)
{
	// Setting world model
	SET_MODEL(iItem, MODEL_CLIP);
}
```

4) Реализуем логику подбора боезапаса

```c
//**********************************************
//* Extract ammo from box to player.           *
//**********************************************

public Ammo762_AddAmmo(const iItem, const iPlayer)
{
	new iResult = 
	(
		ExecuteHamB
		(
			Ham_GiveAmmo, 
			iPlayer, 
			WEAPON_MAX_CLIP, 
			WEAPON_PRIMARY_AMMO, 
			WEAPON_PRIMARY_AMMO_MAX
		) != -1
	);
	
	if (iResult)
	{
		emit_sound(iItem, CHAN_ITEM, "items/9mmclip1.wav", 1.0, ATTN_NORM, 0, PITCH_NORM);
	}
	
	return iResult;
}
```

## Часто используемый функционал


### Выстрел из дробовика 

Для реализации выстрела из дробовика вы можете воспользоваться следующей функцией. Она использовалась в плагине USAS-12 от @Glaster

```c
public S12_PrimaryAttack(const iItem, const iPlayer, iClip)
{
	if (pev(iPlayer, pev_waterlevel) == 3 || iClip <= 0)
	{
		wpnmod_play_empty_sound(iItem);
		wpnmod_set_offset_float(iItem, Offset_flNextPrimaryAttack, 0.7);
		return;
	}

	wpnmod_set_offset_int(iItem, Offset_iClip, iClip -= 1);
	wpnmod_set_offset_int(iPlayer, Offset_iWeaponVolume, LOUD_GUN_VOLUME);
	wpnmod_set_offset_int(iPlayer, Offset_iWeaponFlash, BRIGHT_GUN_FLASH);

	wpnmod_fire_bullets(
		iPlayer, // Индекс игрока, владельца оружия.
		iPlayer, // Индекс атакующего, как правило владельца оружия.
		10, // Кол-во выстрелов за раз.
		VECTOR_CONE_15DEGREES, // Разброс
		3048.0, // Дальность выстрела.
		WEAPON_DAMAGE, // Урон
		DMG_BULLET, // Тип урона (DMG_ биты).
		15 // Частота трасеров.
);
	wpnmod_set_offset_float(iItem, Offset_flNextPrimaryAttack, WEAPON_RATE_OF_FIRE);
	wpnmod_set_offset_float(iItem, Offset_flTimeWeaponIdle, 7.0);

	wpnmod_set_player_anim(iPlayer, PLAYER_ATTACK1);
	wpnmod_send_weapon_anim(iItem, shot1);
	emit_sound(iPlayer, CHAN_WEAPON, SOUND_FIRE, 0.9, ATTN_NORM, 0, PITCH_NORM);

}
```

Може сделать ещё боле интересно. Нижен представлен код, используемый в плагине Shotgunman от dima_mark7. Плагин реализует дробовик из Gunman Chronicles. Основная "фишка" данного оружия - регулируемое количество выпущенных пуль (регулировка происходит на альтернативную атаку). Также, реализована отдача. 

```c
// Основная атака
public shotgunman_primaryattack(const iItem, const iPlayer, iClip, iAmmo)
{
        if (pev(iPlayer, pev_waterlevel) == 3 || iAmmo <= 0)
        {
                wpnmod_play_empty_sound(iItem);
                wpnmod_set_offset_float(iItem, Offset_flNextPrimaryAttack, 0.15);
                return;
        }
       
        shotgunman_ShotBullets(iItem, iPlayer, g_bullet[iPlayer], iAmmo);
       
        wpnmod_set_offset_float(iItem, Offset_flNextPrimaryAttack, 0.92);
        wpnmod_set_offset_float(iItem, Offset_flNextSecondaryAttack, 0.92);
        wpnmod_set_offset_float(iItem, Offset_flTimeWeaponIdle, 0.92);
       
        wpnmod_set_player_anim(iPlayer, PLAYER_ATTACK1);
        emit_sound(iPlayer, CHAN_WEAPON, SOUND_FIRE, 0.92, ATTN_NORM, 0, PITCH_NORM);
}

// Функция выстрел определенного количества снарядов
shotgunman_ShotBullets(const iItem, const iPlayer, iBullets, const iAmmo)
{
        static Float: flMult;
        static Float: flZVel;
        static Float: vecAngle[3];
        static Float: vecForward[3];
        static Float: vecVelocity[3];
        static Float: vecPunchangle[3];
       
        if (iAmmo < iBullets)
        {
                iBullets = iAmmo;
        }
 
        wpnmod_fire_bullets(iPlayer, iPlayer, iBullets * 4, VECTOR_CONE_15DEGREES, 2048.0, WEAPON_DAMAGE, DMG_BULLET, iBullets * 4);
       
        for (new i = 0; i < iBullets; i++)
        {
                wpnmod_eject_brass(iPlayer, shell, TE_BOUNCE_SHOTSHELL, 16.0, -18.0, 6.0);
        }
       
        wpnmod_send_weapon_anim(iItem, GUN_IDLE2 + iBullets);
        wpnmod_set_player_ammo(iPlayer, WEAPON_PRIMARY_AMMO, iAmmo - iBullets);
               
        global_get(glb_v_forward, vecForward);
       
        pev(iPlayer, pev_v_angle, vecAngle);
        pev(iPlayer, pev_velocity, vecVelocity);
        pev(iPlayer, pev_punchangle, vecPunchangle);
               
        xs_vec_add(vecAngle, vecPunchangle, vecPunchangle);
        engfunc(EngFunc_MakeVectors, vecPunchangle);
               
        flZVel = vecVelocity[2];
        flMult = float(iBullets);
               
        xs_vec_mul_scalar(vecForward, 100.0 * flMult, vecPunchangle);
        xs_vec_sub(vecVelocity, vecPunchangle, vecVelocity);
               
        vecPunchangle[2] = 0.0;
        vecVelocity[2] = flZVel;
       
        vecPunchangle[0] = random_float(-1.0 * flMult, 1.0 * flMult);
        vecPunchangle[1] = random_float(-(++flMult), flMult);
               
        set_pev(iPlayer, pev_velocity, vecVelocity);
        set_pev(iPlayer, pev_punchangle, vecPunchangle);
}
```


### Прицеливание 

Нюансы реализации прицеливания могут отличаться от плагина к плагину: для отображения прицеливания можно использовать как простой спрайт, так и отдельную v_ модель. Однако для всех случаев для начала нам нужно помимо остновного ```weapon_name.txt``` создать  ```weapon_name_scp.txt``` (например,  ```weapon_sniperrifle.txt``` и ```weapon_sniperrifle_scp.txt```).  

weapon_sniperrifle.txt 

```
6
ammo            640	640hud7		24  72  24  24
crosshair		640 crosshairs	72	0	24	24
zoom			640 crosshairs	72	0	24	24
autoaim			640 crosshairs	72	48	24	24
weapon          640 weapon_sniperrifle	0   0  170 45
weapon_s        640 weapon_sniperrifle	0   45  170 45
```

weapon_sniperrifle_scp.txt

```
6
ammo            640	640hud7		24  72  24  24
crosshair		640 ofch2  0  0   256  256
zoom            640 ofch2  0  0   256  256
autoaim			640 ofch2  0  0   256  256
weapon          640 weapon_sniperrifle	0   0  170 45
weapon_s        640 weapon_sniperrifle	0   45  170 45
```

Можно заменить, что файлы отличаются между собой секциями crosshair, zoom и autoaim, в них идет описание прицела. В первом случае будет использоваться стандартный прицел 

<img width="133" height="68" alt="image" src="https://github.com/user-attachments/assets/49aa1979-b115-4cc0-82d2-beafbf5842aa" />

А во втором - прицел для зума 

<img width="266" height="258" alt="image" src="https://github.com/user-attachments/assets/26d6269a-4145-482f-b87b-7d6fceae8312" />


#### Прицеливание с использованием спрайта

Продолжим развите прицела для снайперской винтовки. Код, реализующий прицеливание приведен ниже 

```c

//**********************************************
//* Secondary attack of a weapon is triggered. *
//**********************************************

public M40A1_SecondaryAttack(const iItem, const iPlayer)
{
	new Float: flFov;
	
	if (pev(iPlayer, pev_fov, flFov) && flFov != 0.0)
	{
		MakeZoom(iItem, iPlayer, "weapon_sniperrifle", 0.0);
		
	}
	else if (flFov != 20.0)
	{
		MakeZoom(iItem, iPlayer, "weapon_sniperrifle_scp", 20.0);
	}
	
	emit_sound(iPlayer, CHAN_ITEM, SOUND_ZOOM, random_float(0.95, 1.0), ATTN_NORM, 0, PITCH_NORM);
	
	wpnmod_set_offset_float(iItem, Offset_flNextPrimaryAttack, 0.1);
	wpnmod_set_offset_float(iItem, Offset_flNextSecondaryAttack, 0.8);
}

MakeZoom(const iItem, const iPlayer, const szWeaponName[], const Float: flFov)
{
	static msgWeaponList;
	
	set_pev(iPlayer, pev_fov, flFov);
	wpnmod_set_offset_int(iPlayer, Offset_iFOV, _:flFov);
		
	if (msgWeaponList || (msgWeaponList = get_user_msgid("WeaponList")))		
	{
		message_begin(MSG_ONE, msgWeaponList, .player = iPlayer);
		write_string(szWeaponName);
		write_byte(wpnmod_get_offset_int(iItem, Offset_iPrimaryAmmoType));
		write_byte(WEAPON_PRIMARY_AMMO_MAX);
		write_byte(wpnmod_get_offset_int(iItem, Offset_iSecondaryAmmoType));
		write_byte(WEAPON_SECONDARY_AMMO_MAX);
		write_byte(WEAPON_SLOT - 1);
		write_byte(WEAPON_POSITION - 1);
		write_byte(get_user_weapon(iPlayer));
		write_byte(WEAPON_FLAGS);
		message_end();
	}
}
```

При прицеливании мы изменяем ```pev_fov``` игрока, перерисовываем интерфейс и выбираем нужный txt файл с прицеливанием (```weapon_sniperrifle_scp``` для включения, ```weapon_sniperrifle``` для выключения)


#### Прицеливание с использованием отдельной v_ модели

Использование отдельной модели под прицеливание может выглядеть интересно. Например, это реализовано в плагине TAR-21 от KORD_12.7 и Koshak. Там для прицеливания используется отдельная модель ```v_tar21_sight_koshak```. 

<img width="599" height="506" alt="image" src="https://github.com/user-attachments/assets/ca2b8686-32af-4c7d-a080-830b17fe078d" />

Обновленный код с использованием этой модели приведён ниже. 

```c
//**********************************************
//* Secondary attack of a weapon is triggered. *
//**********************************************

public TAR_SecondaryAttack(const iItem, const iPlayer)
{
	new iInZoom = wpnmod_get_offset_int(iItem, Offset_iInZoom);
	
	if (!iInZoom)
	{
		SetThink(iItem, "TAR_SightThink", 0.3);
	}
	else
	{
		MakeZoom(iItem, iPlayer, WEAPON_NAME, MODEL_VIEW, 0.0);
	}
	
	wpnmod_set_offset_int(iItem, Offset_iInZoom, !iInZoom);
	wpnmod_set_offset_float(iItem, Offset_flNextPrimaryAttack, 0.35);
	wpnmod_set_offset_float(iItem, Offset_flNextSecondaryAttack, 0.5);
	wpnmod_send_weapon_anim(iItem, iInZoom ? ANIM_SIGHT_END : ANIM_SIGHT_BEGIN);
}

//**********************************************
//* Enable sight.                              *
//**********************************************

public TAR_SightThink(const iItem, const iPlayer)
{
	MakeZoom(iItem, iPlayer, WEAPON_NAME_SIGHT, MODEL_VIEW_SIGHT, 60.0);
}

//**********************************************
//* Apply zoom.                                *
//**********************************************

MakeZoom(const iItem, const iPlayer, const szWeaponName[], const szViewModel[], const Float: flFov)
{
	static msgWeaponList;
	
	set_pev(iPlayer, pev_fov, flFov);
	set_pev(iPlayer, pev_viewmodel2, szViewModel);
	
	wpnmod_set_offset_int(iPlayer, Offset_iFOV, floatround(flFov));
		
	if (msgWeaponList || (msgWeaponList = get_user_msgid("WeaponList")))		
	{
		message_begin(MSG_ONE, msgWeaponList, .player = iPlayer);
		write_string(szWeaponName);
		write_byte(wpnmod_get_offset_int(iItem, Offset_iPrimaryAmmoType));
		write_byte(wpnmod_get_weapon_info(iItem, ItemInfo_iMaxAmmo1));
		write_byte(wpnmod_get_offset_int(iItem, Offset_iSecondaryAmmoType));
		write_byte(wpnmod_get_weapon_info(iItem, ItemInfo_iMaxAmmo2));
		write_byte(wpnmod_get_weapon_info(iItem, ItemInfo_iSlot));
		write_byte(wpnmod_get_weapon_info(iItem, ItemInfo_iPosition));
		write_byte(wpnmod_get_weapon_info(iItem, ItemInfo_iId));
		write_byte(wpnmod_get_weapon_info(iItem, ItemInfo_iFlags));
		message_end();
	}
}
```

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3ed524e6-692b-4584-8345-86e8d27028f6" />


### Использование снарядов и прочего вместо пуль

Помимо пуль мы также можем использовать при стрельбе прочие снаряды. Рассмотрим на несколькиз примерах.

#### Создание гранатомёта

В Half-Life Weaponmod есть возможность использовать некоторые некоторые виды гранат. К ним относятся контактная граната, взрывающася при касании любой поверхности, а также граната с таймеров, которая взорвется по истечению некоторого времени.

```c

/**
 * Fire default contact grenade from player's weapon.
 *
 * @param iPlayer			Player index.
 * @param vecStart			Start position.
 * @param vecVelocity		Velocity.
 * @param szCallBack		The forward to call on explode.
 *
 * @return					Contact grenade index or -1 on failure. (integer)
 */
native wpnmod_fire_contact_grenade(const iPlayer, const Float: vecStart[3], const Float: vecVelocity[3], const szCallBack[] = "");

/**
 * Fire default timed grenade from player's weapon.
 *
 * @param iPlayer			Player index.
 * @param vecStart			Start position.
 * @param vecVelocity		Velocity.
 * @param flTime			Time before detonate.
 * @param szCallBack		The forward to call on explode.
 *
 * @return					Contact grenade index or -1 on failure. (integer)
 */
native wpnmod_fire_timed_grenade(const iPlayer, const Float: vecStart[3], const Float: vecVelocity[3], const Float: flTime = 3.0, const szCallBack[] = "");
```

Рассмотрим использование натива ```wpnmod_fire_contact_grenade``` на примере плагина RPG-7.

```c
//**********************************************
//* Запускаем ракету                           *
//**********************************************

RPG7_Fire(const iPlayer)
{
	new iRocket;
	
	new Float: vecOrigin[3];
	new Float: vecVelocity[3];
	
	wpnmod_get_gun_position(iPlayer, vecOrigin, 16.0, 6.0, 0.0);
	velocity_by_aim(iPlayer, ROCKET_VELOCITY, vecVelocity);
		
	// Создаем гранату
	iRocket = wpnmod_fire_contact_grenade(iPlayer, vecOrigin, vecVelocity, "Rocket_Explode");
	
	if (pev_valid(iRocket))
	{
		new Float: flGameTime = get_gametime();
		
		// Dont draw default fireball on explode and do not inflict damage
		set_pev(iRocket, pev_spawnflags, SF_EXPLOSION_NODAMAGE | SF_EXPLOSION_NOFIREBALL);
		
		// Задаем класснейм
		set_pev(iRocket, pev_classname, ROCKET_CLASSNAME);
		
		// Задаем тип движения
		set_pev(iRocket, pev_movetype, MOVETYPE_FLY);
		
		// Задаем урон при касании
		set_pev(iRocket, pev_dmg, WEAPON_DAMAGE);
		
		// Добавляем свечение
		set_pev(iRocket, pev_effects, pev(iRocket, pev_effects) | EF_LIGHT);
		
		// Задаем угловую скорость
		set_pev(iRocket, pev_avelocity, Float: {0.0, 0.0, 1000.0});
		
		// Задаем модель
		SET_MODEL(iRocket, MODEL_ROCKET);
		
		// Задаем callback на think для сущности ракеты
		wpnmod_set_think(iRocket, "Rocket_FlyThink");
		
		// Указываем, через сколько сработает think
		set_pev(iRocket, pev_nextthink, flGameTime + 0.1);
		
		// Задаем максимальное время полета
		set_pev(iRocket, pev_dmgtime, flGameTime + 3.0);
		
		// Реализация следа за ракетой 
		message_begin(MSG_BROADCAST, SVC_TEMPENTITY);
		write_byte(TE_BEAMFOLLOW);
		write_short(iRocket); // entity
		write_short(g_iModelIndexTrail); // model
		write_byte(10); // life
		write_byte(4); // width
		write_byte(224); // r, g, b
		write_byte(224); // r, g, b
		write_byte(255); // r, g, b
		write_byte(255); // brightness
		message_end();
		
		emit_sound(iRocket, CHAN_VOICE, SOUND_ROCKET_FLY, 1.0, 0.5, 0, PITCH_NORM);
	}
}

//**********************************************
//* Фунукция think для сущности  		       *
//**********************************************

public Rocket_FlyThink(const iRocket)
{
	static Float: flDmgTime;
	static Float: flGameTime;
	
	pev(iRocket, pev_dmgtime, flDmgTime);
	set_pev(iRocket, pev_nextthink, (flGameTime = get_gametime()) + 0.2);

	if (pev(iRocket, pev_waterlevel) != 0)
	{
		new Float: vecVelocity[3];
		
		pev(iRocket, pev_velocity, vecVelocity);
		xs_vec_mul_scalar(vecVelocity, 0.5, vecVelocity);
		set_pev(iRocket, pev_velocity, vecVelocity);
	}
	
	if (flDmgTime <= flGameTime)
	{
		set_pev(iRocket, pev_movetype, MOVETYPE_TOSS);
		set_pev(iRocket, pev_effects, pev(iRocket, pev_effects) &~ EF_LIGHT);
		
		emit_sound(iRocket, CHAN_VOICE, SOUND_ROCKET_FLY, 0.0, 0.0, SND_STOP, PITCH_NORM);
	}
}

//**********************************************
//* Реализация взрыва            		       *
//**********************************************

public Rocket_Explode(const iRocket)
{	
	new iOwner;
	
	new Float: flDamage;
	new Float: vecOrigin[3];
	
	iOwner = pev(iRocket, pev_owner);
	
	pev(iRocket, pev_dmg, flDamage);
	pev(iRocket, pev_origin, vecOrigin);
	
	engfunc(EngFunc_MessageBegin,MSG_PAS, SVC_TEMPENTITY, vecOrigin, 0);
	write_byte(TE_EXPLOSION);
	engfunc(EngFunc_WriteCoord, vecOrigin[0]);
	engfunc(EngFunc_WriteCoord, vecOrigin[1]);
	engfunc(EngFunc_WriteCoord, vecOrigin[2]);
	write_short(engfunc(EngFunc_PointContents, vecOrigin) != CONTENTS_WATER ? g_iModelIndexFireball : g_iModelIndexWExplosion);
	write_byte(35);
	write_byte(15); 
	write_byte(TE_EXPLFLAG_NONE);
	message_end();
	
	message_begin(MSG_BROADCAST,SVC_TEMPENTITY); 
	write_byte(TE_KILLBEAM); 
	write_short(iRocket);
	message_end(); 
	
	// Reset to attack owner too
	set_pev(iRocket, pev_owner, 0);
	
	// Наносим уров по радиусу
	wpnmod_radius_damage2(vecOrigin, iRocket, iOwner, flDamage, flDamage * 2.0, CLASS_NONE, DMG_BLAST);
	
	// Stop fly sound
	emit_sound(iRocket, CHAN_VOICE, SOUND_ROCKET_FLY, 0.0, 0.0, SND_STOP, PITCH_NORM);
}


//**********************************************
//* Основная атака                             *
//**********************************************

public RPG7_PrimaryAttack(const iItem, const iPlayer, const iClip)
{
	if (pev(iPlayer, pev_waterlevel) == 3 || iClip <= 0)
	{
		wpnmod_play_empty_sound(iItem);
		wpnmod_set_offset_float(iItem, Offset_flNextPrimaryAttack, 0.15);
		return;
	}
	
	wpnmod_set_offset_int(iItem, Offset_iClip, iClip - 1);
	wpnmod_set_offset_int(iPlayer, Offset_iWeaponVolume, LOUD_GUN_VOLUME);
	wpnmod_set_offset_int(iPlayer, Offset_iWeaponFlash, BRIGHT_GUN_FLASH);
	
	wpnmod_set_offset_float(iItem, Offset_flNextPrimaryAttack, 0.7);
	wpnmod_set_offset_float(iItem, Offset_flTimeWeaponIdle, 0.7);
	
	wpnmod_set_player_anim(iPlayer, PLAYER_ATTACK1);
	wpnmod_send_weapon_anim(iItem, ANIM_FIRE);
	
	emit_sound(iPlayer, CHAN_WEAPON, SOUND_FIRE, 1.0, ATTN_NORM, 0, PITCH_NORM);
	
	CNAHGE_ANIM_EXT(iPlayer, ANIM_EXTENSION_2, MODEL_PLAYER_2);

    // Создаем ракету
	RPG7_Fire(iPlayer);
}
```


#### Создание собственного снаряда.

А что если мы хотим создать свой уникальный снаряд и обычные гранаты нам не подходят? Рассмотрим на примере реализации из CSO Plasmagun от KORD_12.7. 

```c
// Ресурсы снаряда
#define PLASMA_MODEL			"sprites/plasmaball.spr" // Спрайт снаряда
#define PLASMA_EXPLODE			"sprites/plasmabomb.spr" // Спрайт взрыва
#define PLASMA_VELOCITY			1200 // Скорость снаряда
#define CLASS_PLASMA			"monster_plasma" // Класс создаваемой entity

//
// Спавним снаряд
//
CPlasmab__Spawn( pPlayer )
{
	new pPlasma = create_entity( "env_sprite" );
	
	if( pPlasma <= 0 )
		return 0;
		
	message_begin( MSG_BROADCAST, SVC_TEMPENTITY );
	write_byte( TE_KILLBEAM );
	write_short( pPlasma );
	message_end( );
		
	// Задаем имя класса
	entity_set_string( pPlasma, EV_SZ_classname, CLASS_PLASMA );
	
	// Задаем модель
	entity_set_model( pPlasma, PLASMA_MODEL );
	
	// Задаем координаты
	static Float:vecSrc[ 3 ];
	wpnmod_get_gun_position( pPlayer, vecSrc, 25.0, 16.0, -7.0 );
	entity_set_origin( pPlasma, vecSrc );

	entity_set_int( pPlasma, EV_INT_movetype, MOVETYPE_FLY );
	entity_set_int( pPlasma, EV_INT_solid, SOLID_BBOX );
	
	// Задаем размер
	entity_set_size( pPlasma, gVecZero, gVecZero );
	
	// Убираем черный квадрат вокруг спрайта
	entity_set_float( pPlasma, EV_FL_renderamt, 255.0 );
	entity_set_float( pPlasma, EV_FL_scale, 0.3 );
	entity_set_int( pPlasma, EV_INT_rendermode, kRenderTransAdd );
	entity_set_int( pPlasma, EV_INT_renderfx, kRenderFxGlowShell );
	
	// Задаем скорость
	static Float:vecVelocity[ 3 ];
	velocity_by_aim( pPlayer, PLASMA_VELOCITY, vecVelocity );
	entity_set_vector( pPlasma, EV_VEC_velocity, vecVelocity );
	 
	// Задаем углы
	static Float:vecAngles[ 3 ];
	engfunc( EngFunc_VecToAngles, vecVelocity, vecAngles );
	entity_set_vector( pPlasma, EV_VEC_angles, vecAngles );
	
	// Задаем владельца
	entity_set_edict( pPlasma, EV_ENT_owner, pPlayer );

	// Задаем фукцию касания	
	wpnmod_set_touch( pPlasma, "CPlasmab__Touch" );
	
	return 1;
}
// 
// Отработка тача снаряда
//
public CPlasmab__Touch( pPlasma, pOther )
{
	if( !is_valid_ent( pPlasma ) )
		return;

	// Создаем эффект взрыва
	static Float:vecSrc[ 3 ];
	entity_get_vector( pPlasma, EV_VEC_origin, vecSrc );
	
	engfunc( EngFunc_MessageBegin, MSG_PVS, SVC_TEMPENTITY, vecSrc, 0 );
	write_byte( TE_EXPLOSION );
	engfunc( EngFunc_WriteCoord, vecSrc[ 0 ] );
	engfunc( EngFunc_WriteCoord, vecSrc[ 1 ] );
	engfunc( EngFunc_WriteCoord, vecSrc[ 2 ] );
	write_short( g_sModelIndexExplode );
	write_byte( 5 );
	write_byte( 15 );
	write_byte( TE_EXPLFLAG_NOPARTICLES | TE_EXPLFLAG_NOSOUND );
	message_end( );

	// Проигрываем звук взрыва
	emit_sound( pPlasma, CHAN_WEAPON, SOUND_EXPLODE, 1.0, 1.0, 0, 100 );

	// Создаем взрыв, наносим урон
	wpnmod_radius_damage( vecSrc, pPlasma, entity_get_edict( pPlasma, EV_ENT_owner ), WEAPON_DAMAGE, WEAPON_RADIUS, CLASS_NONE, DMG_ACID | DMG_ENERGYBEAM );	
	remove_entity( pPlasma );	
}

//
// Основная атака оружия
//
public CPlasma__PrimaryAttack( pItem, pPlayer, iClip, rgAmmo )
{
	if( iClip <= 0 || entity_get_int( pPlayer, EV_INT_waterlevel ) == 3 )
	{
		wpnmod_play_empty_sound( pItem );
		wpnmod_set_offset_float( pItem, Offset_flNextPrimaryAttack, 0.25 );
		return;
	}
	
	if( CPlasmab__Spawn( pPlayer ) )
	{
		//fire effects
		wpnmod_set_offset_int( pPlayer, Offset_iWeaponVolume, NORMAL_GUN_VOLUME );
		wpnmod_set_offset_int( pPlayer, Offset_iWeaponFlash, DIM_GUN_FLASH );
		
		//remove ammo
		wpnmod_set_offset_int( pItem, Offset_iClip, iClip -= 1 );
		
		entity_set_int( pPlayer, EV_INT_effects, entity_get_int( pPlayer, EV_INT_effects ) | EF_MUZZLEFLASH );
		wpnmod_set_player_anim( pPlayer, PLAYER_ATTACK1 );
	
		wpnmod_set_offset_float( pItem, Offset_flNextPrimaryAttack, WEAPON_REFIRE_RATE );
		wpnmod_set_offset_float( pItem, Offset_flTimeWeaponIdle, WEAPON_REFIRE_RATE + 3.0 );
		
		emit_sound( pPlayer, CHAN_WEAPON, SOUND_FIRE, 0.9, ATTN_NORM, 0, PITCH_NORM );
		wpnmod_send_weapon_anim( pItem, SEQ_FIRE );
		entity_set_vector( pPlayer, EV_VEC_punchangle, Float:{ -5.0, 0.0, 0.0 } );
	}
}

```
![20250928203217_1](https://github.com/user-attachments/assets/aa8828a5-065b-4bed-bbd3-021e2a555860)

#### Лазерное оружие 

Ещё одним вариантом основной атаки может быть использование лазера. Рассмотрим на примере плагина CSO Ethereal

```c
// Подключим инклюды
#include <beams>
#include <xs>

// Sprites
#define SPRITE_LIGHTNING		"sprites/lgtning.spr"

// Beam
#define BEAM_LIFE			0.09
#define BEAM_COLOR			{100.0, 50.0, 253.0}
#define BEAM_BRIGHTNESS			255.0
#define BEAM_SCROLLRATE			10.0


//**********************************************
//* Основная атака                             *
//**********************************************

public Ethereal_PrimaryAttack(const iItem, const iPlayer, const iClip)
{
	if (pev(iPlayer, pev_waterlevel) == 3 || iClip <= 0)
	{
		wpnmod_play_empty_sound(iItem);
		wpnmod_set_offset_float(iItem, Offset_flNextPrimaryAttack, 0.15);
		return;
	}
	
	new Float: vecSrc[3], Float: vecEnd[3], iBeam, iTrace = create_tr2();
	
	wpnmod_get_gun_position(iPlayer, vecSrc);
	global_get(glb_v_forward, vecEnd);
	
	xs_vec_mul_scalar(vecEnd, 8192.0, vecEnd);
	xs_vec_add(vecSrc, vecEnd, vecEnd);
	
	engfunc(EngFunc_TraceLine, vecSrc, vecEnd, DONT_IGNORE_MONSTERS, iPlayer, iTrace);
	get_tr2(iTrace, TR_vecEndPos, vecEnd);
	
	if (pev_valid((iBeam = Beam_Create(SPRITE_LIGHTNING, 25.0))))
	{
		Beam_PointEntInit(iBeam, vecEnd, iPlayer);
		Beam_SetEndAttachment(iBeam, 1);
		Beam_SetBrightness(iBeam, BEAM_BRIGHTNESS);
		Beam_SetScrollRate(iBeam, BEAM_SCROLLRATE);
		Beam_SetColor(iBeam, BEAM_COLOR);
		Beam_SetLife(iBeam, BEAM_LIFE);
	}
	
	wpnmod_radius_damage2(vecEnd, iPlayer, iPlayer, WEAPON_DAMAGE, WEAPON_DAMAGE * 2.0, CLASS_NONE, DMG_ENERGYBEAM | DMG_ALWAYSGIB);
	
	engfunc(EngFunc_EmitSound, iPlayer, CHAN_AUTO, SOUND_FIRE, 0.9, ATTN_NORM, 0, PITCH_NORM);
	engfunc(EngFunc_EmitAmbientSound, 0, vecEnd, SOUND_IMPACT, 0.9, ATTN_NORM, 0, PITCH_NORM);
	
	engfunc(EngFunc_MessageBegin, MSG_PVS, SVC_TEMPENTITY, vecEnd, 0);
	write_byte(TE_DLIGHT);
	engfunc(EngFunc_WriteCoord, vecEnd[0]);
	engfunc(EngFunc_WriteCoord, vecEnd[1]);
	engfunc(EngFunc_WriteCoord, vecEnd[2]);
	write_byte(10);
	write_byte(100);
	write_byte(50);
	write_byte(253);
	write_byte(255);
	write_byte(25);
	write_byte(1);
	message_end();
	
	engfunc(EngFunc_MessageBegin, MSG_PVS, SVC_TEMPENTITY, vecEnd, 0);
	write_byte(TE_SPARKS);
	engfunc(EngFunc_WriteCoord, vecEnd[0]);
	engfunc(EngFunc_WriteCoord, vecEnd[1]);
	engfunc(EngFunc_WriteCoord, vecEnd[2]);
	message_end();
	
	wpnmod_decal_trace(iTrace, engfunc(EngFunc_DecalIndex, "{smscorch1") + random_num(0, 2));
	
	wpnmod_set_offset_int(iItem, Offset_iClip, iClip - 1);
	wpnmod_set_offset_int(iPlayer, Offset_iWeaponVolume, LOUD_GUN_VOLUME);
	wpnmod_set_offset_int(iPlayer, Offset_iWeaponFlash, BRIGHT_GUN_FLASH);
	
	wpnmod_set_offset_float(iItem, Offset_flNextPrimaryAttack, 0.1);
	wpnmod_set_offset_float(iItem, Offset_flTimeWeaponIdle, 1.03);
	
	wpnmod_set_player_anim(iPlayer, PLAYER_ATTACK1);
	wpnmod_send_weapon_anim(iItem, random_num(ANIM_FIRE_1, ANIM_FIRE_3));
	
	free_tr2(iTrace);
}

```

### Реализация удара прикладом (оружие ближнего боя) 

Рассмотрим реализацию удара штыком при альтернативной атаке мы можем найти в плагине  AK-47: Avtomat Kalashnikova от KORD_12.7

```c
//**********************************************
//* Альтернативная атака                       *
//**********************************************

public AK47_SecondaryAttack(const iItem, const iPlayer)
{
	wpnmod_set_think(iItem, "AK47_Stab");
	wpnmod_send_weapon_anim(iItem, ANIM_STAB);
	
	wpnmod_set_offset_float(iItem, Offset_flNextPrimaryAttack, 0.65);
	wpnmod_set_offset_float(iItem, Offset_flNextSecondaryAttack, 0.65);
	wpnmod_set_offset_float(iItem, Offset_flTimeWeaponIdle, 5.0);
	
	set_pev(iItem, pev_nextthink, get_gametime() + 0.3);
}

//**********************************************
//* Обработка удара штыком                     *
//**********************************************

public AK47_Stab(const iItem, const iPlayer)
{
	#define Offset_trHit Offset_iuser1
	#define Instance(%0) ((%0 == -1) ? 0 : %0)
	
	new iClass;
	new iTrace;
	new iEntity;
	new iHitWorld;
	
	new Float: vecSrc[3];
	new Float: vecEnd[3];
	new Float: vecUp[3];
	new Float: vecAngle[3];
	new Float: vecRight[3];
	new Float: vecForward[3];
	
	new Float: flFraction;
	
	iTrace = create_tr2();
	
	pev(iPlayer, pev_v_angle, vecAngle);
	engfunc(EngFunc_MakeVectors, vecAngle);
	
	GetGunPosition(iPlayer, vecSrc);
	
	global_get(glb_v_up, vecUp);
	global_get(glb_v_right, vecRight);
	global_get(glb_v_forward, vecForward);

	xs_vec_mul_scalar(vecUp, -2.0, vecUp);
	xs_vec_mul_scalar(vecRight, 1.0, vecRight);
	xs_vec_mul_scalar(vecForward, 48.0, vecForward);
		
	xs_vec_add(vecUp, vecRight, vecRight);
	xs_vec_add(vecRight, vecForward, vecForward);
	xs_vec_add(vecForward, vecSrc, vecEnd);

	engfunc(EngFunc_TraceLine, vecSrc, vecEnd, DONT_IGNORE_MONSTERS, iPlayer, iTrace);
	get_tr2(iTrace, TR_flFraction, flFraction);
	
	if (flFraction >= 1.0)
	{
		engfunc(EngFunc_TraceHull, vecSrc, vecEnd, DONT_IGNORE_MONSTERS, HULL_HEAD, iPlayer, iTrace);
		get_tr2(iTrace, TR_flFraction, flFraction);
		
		if (flFraction < 1.0)
		{
			new iHit = Instance(get_tr2(iTrace, TR_pHit));
			
			if (!iHit || ExecuteHamB(Ham_IsBSPModel, iHit))
			{
				FindHullIntersection(vecSrc, iTrace, Float: {-16.0, -16.0, -18.0}, Float: {16.0,  16.0,  18.0}, iPlayer);
			}
			
			get_tr2(iTrace, TR_vecEndPos, vecEnd);
		}
	}
	
	get_tr2(iTrace, TR_flFraction, flFraction);
	
	switch (random_num(0, 2))
	{
		case 0: emit_sound(iPlayer, CHAN_WEAPON, SOUND_MISS_1, 1.0, ATTN_NORM, 0, PITCH_NORM);
		case 1: emit_sound(iPlayer, CHAN_WEAPON, SOUND_MISS_2, 1.0, ATTN_NORM, 0, PITCH_NORM);
		case 2: emit_sound(iPlayer, CHAN_WEAPON, SOUND_MISS_3, 1.0, ATTN_NORM, 0, PITCH_NORM);
	}
	
	if (flFraction < 1.0)
	{
		iHitWorld = true;
		iEntity = Instance(get_tr2(iTrace, TR_pHit));
		
		wpnmod_clear_multi_damage();
		
		pev(iPlayer, pev_v_angle, vecAngle);
		engfunc(EngFunc_MakeVectors, vecAngle);	
		
		global_get(glb_v_forward, vecForward);
		ExecuteHamB(Ham_TraceAttack, iEntity, iPlayer, WEAPON_DAMAGE * 2.5, vecForward, iTrace, DMG_CLUB | DMG_NEVERGIB);
		
		wpnmod_apply_multi_damage(iPlayer, iPlayer);
		wpnmod_set_player_anim(iPlayer, PLAYER_ATTACK1);
			
		if (iEntity && (iClass = ExecuteHamB(Ham_Classify, iEntity)) != CLASS_NONE && iClass != CLASS_MACHINE)
		{
			switch (random_num(0, 1))
			{
				case 0: emit_sound(iPlayer, CHAN_ITEM, SOUND_HIT_FLESH_1, 1.0, ATTN_NORM, 0, PITCH_NORM);
				case 1: emit_sound(iPlayer, CHAN_ITEM, SOUND_HIT_FLESH_2, 1.0, ATTN_NORM, 0, PITCH_NORM);
			}
				
			if (!ExecuteHamB(Ham_IsAlive, iEntity))
			{
				return;
			}
				
			iHitWorld = false;
		}
			
		if (iHitWorld)
		{
			wpnmod_set_offset_int(iItem, Offset_trHit, iTrace);
			emit_sound(iPlayer, CHAN_ITEM, SOUND_HIT_WALL, 1.0, ATTN_NORM, 0, PITCH_NORM);
		}
		
		wpnmod_set_think(iItem, "AK47_Smack");
		set_pev(iItem, pev_nextthink, get_gametime() + 0.1);
	}

	free_tr2(iTrace);
}

public AK47_Smack(const iItem)
{
	new iTrace = wpnmod_get_offset_int(iItem, Offset_trHit);
	
	UTIL_DecalTrace(iTrace, get_decal_index("{shot1") + random_num(0, 4));
	free_tr2(iTrace);
}


stock FindHullIntersection(const Float: vecSrc[3], &iTrace, const Float: vecMins[3], const Float: vecMaxs[3], const iEntity)
{
	new i, j, k;
	new iTempTrace;
	
	new Float: vecEnd[3];
	new Float: flDistance;
	new Float: flFraction;
	new Float: vecEndPos[3];
	new Float: vecHullEnd[3];
	new Float: flThisDistance;
	new Float: vecMinMaxs[2][3];
	
	flDistance = 999999.0;
	
	xs_vec_copy(vecMins, vecMinMaxs[0]);
	xs_vec_copy(vecMaxs, vecMinMaxs[1]);
	
	get_tr2(iTrace, TR_vecEndPos, vecHullEnd);
	
	xs_vec_sub(vecHullEnd, vecSrc, vecHullEnd);
	xs_vec_mul_scalar(vecHullEnd, 2.0, vecHullEnd);
	xs_vec_add(vecHullEnd, vecSrc, vecHullEnd);
	
	engfunc(EngFunc_TraceLine, vecSrc, vecHullEnd, DONT_IGNORE_MONSTERS, iEntity, (iTempTrace = create_tr2()));
	get_tr2(iTempTrace, TR_flFraction, flFraction);
	
	if (flFraction < 1.0)
	{
		free_tr2(iTrace);
		
		iTrace = iTempTrace;
		return;
	}
	
	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 2; j++)
		{
			for (k = 0; k < 2; k++)
			{
				vecEnd[0] = vecHullEnd[0] + vecMinMaxs[i][0];
				vecEnd[1] = vecHullEnd[1] + vecMinMaxs[j][1];
				vecEnd[2] = vecHullEnd[2] + vecMinMaxs[k][2];
				
				engfunc(EngFunc_TraceLine, vecSrc, vecEnd, DONT_IGNORE_MONSTERS, iEntity, iTempTrace);
				get_tr2(iTempTrace, TR_flFraction, flFraction);
				
				if (flFraction < 1.0)
				{
					get_tr2(iTempTrace, TR_vecEndPos, vecEndPos);
					xs_vec_sub(vecEndPos, vecSrc, vecEndPos);
					
					if ((flThisDistance = xs_vec_len(vecEndPos)) < flDistance)
					{
						free_tr2(iTrace);
						
						iTrace = iTempTrace;
						flDistance = flThisDistance;
					}
				}
			}
		}
	}
}

stock UTIL_DecalTrace(const iTrace, iDecalIndex)
{
	new iHit;
	new iEntity;
	new iMessage;
	
	new Float: flFraction;
	new Float: vecEndPos[3];
	
	if (iDecalIndex < 0 || get_tr2(iTrace, TR_flFraction, flFraction) && flFraction == 1.0)
	{
		return;
	}
        
	if (pev_valid((iHit = get_tr2(iTrace, TR_pHit))))
	{
		if (iHit && !((pev(iHit, pev_solid) == SOLID_BSP) || (pev(iHit, pev_movetype) == MOVETYPE_PUSHSTEP)))
		{
			return;
		}
		
		iEntity = iHit;
	}
	else
	{
		iEntity = 0;
	}
        
	iMessage = TE_DECAL;
	
	if (iEntity != 0)
	{
		if (iDecalIndex > 255)
		{
			iMessage = TE_DECALHIGH;
			iDecalIndex -= 256;
		}
	}
	else
	{
		iMessage = TE_WORLDDECAL;
		
		if (iDecalIndex > 255)
		{
			iMessage = TE_WORLDDECALHIGH;
			iDecalIndex -= 256;
		}
	}
    
	get_tr2(iTrace, TR_vecEndPos, vecEndPos);
	
	#define write_coord_f(%0) engfunc(EngFunc_WriteCoord,%0)
    
	message_begin(MSG_BROADCAST, SVC_TEMPENTITY);
	write_byte(iMessage);
	write_coord_f(vecEndPos[0]);
	write_coord_f(vecEndPos[1]);
	write_coord_f(vecEndPos[2]);
	write_byte(iDecalIndex);
	
	#undef write_coord_f
        
	if (iEntity)
	{
		write_short(iEntity);
	}
    
	message_end();
}


stock GetGunPosition(const iPlayer, Float: vecResult[3])
{
	new Float: vecViewOfs[3];
	
	pev(iPlayer, pev_origin, vecResult);
	pev(iPlayer, pev_view_ofs, vecViewOfs);
    
	xs_vec_add(vecResult, vecViewOfs, vecResult);
} 
```

![20250928211625_2](https://github.com/user-attachments/assets/e4f42c1e-aad8-40f7-93e1-8ec8abf0fb44)

