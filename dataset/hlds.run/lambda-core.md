# Работа с Lambda Core, системой статистики для Half-Life. 

## Настройка 

```
; Активировать систему ранков?
; 0 - нет, ранки игроков не будут записываться и обрабатываться, say команды /rank и /top будут недоступны
; 1 - да
lc_rank_system 1

; Как ввести учет статистики
; 1 - по никам
; 2 - по ip
; 3 - по steamid
lc_track_mode 1

; Записывать/логировать ботов в статистику?
; 0 - нет
; 1 - да
lc_rank_bots 1

; Количество дней, через которые из статистики будут удаляться неактивные игроки
; Если указать значение 0, то очистка статы от неактивных игроков проводиться не будет
lc_prune_days 0

; Логирование статистики в главный лог сервера (triggered "weaponstats", triggered "weaponstats2", triggered "time", triggered "latency")
; 0 - не логировать
; 1 - при дисконекте игрока (подходит для HLStats и Psychostats)
; 2 - логировать после смерти игрока (необходмио для HLStatsX CE)
lc_stats_loging 1

; Показывать информацию о плагине после смерти игрока (в левом верхнем углу)?
lc_show_info 1

; Рекламировать информацию о доступных say командах?
lc_show_adv 1

; Перерыв между рекламными сообщениями (в секундах)
lc_adv_freq 300
```

## Доступные нативы (AMX MOD X API)

```


/*
 * Natives
 */

/* Gets stats from given weapon index. If wpnindex is 0
* then the stats are from all weapons. If weapon has not been used function
* returns 0 in other case 1.

* Fields in stats are:
* 0 - kills
* 1 - deaths
* 2 - headshots
* 3 - teamkilling
* 4 - shots
* 5 - hits
* 6 - damage

* Fields in bodyhits are:
* 0 - generic (none)
* 1 - head
* 2 - chest
* 3 - stomach
* 4 - leftarm
* 5 - rightarm
* 6 - leftleg
* 7 - rightleg */
native lc_get_user_wstats(index, wpnindex, stats[8], bodyhits[8]);

/* Gets respawn stats from given weapon index.*/
native lc_get_user_wrstats(index, wpnindex, stats[8], bodyhits[8]);

/* Gets overall stats which are stored in file on server
* and updated on user disconnect.
* Function returns the position in stats by diff. kills to deaths. */
native lc_get_user_stats(index, stats[8], bodyhits[8]);

/* Gets respawn stats of player. */
native lc_get_user_rstats(index, stats[8], bodyhits[8]);

/* Gets stats with which user have killed/hurt his victim. If victim is 0
* then stats are from all victims. If victim has not been hurt, function
* returns 0 in other case 1. User stats are reset on his respawn. */
native lc_get_user_vstats(index, victim, stats[8], bodyhits[8], wpnname[] = "", len = 0);

/* Gets stats with which user have been killed/hurt. If killer is 0
* then stats are from all attacks. If killer has not hurt user, function
* returns 0 in other case 1. User stats are reset on his respawn. */
native lc_get_user_astats(index, killer, stats[8], bodyhits[8], wpnname[] = "", len = 0);

/* Resets life, weapon, victims and attackers user stats. */
native lc_reset_user_wstats(index);

/* Gets overall stats which stored in lc_stats.dat file in amx folder
* and updated on every mapchange or user disconnect.
* Function returns next index of stats entry or 0 if no more exists. */
native lc_get_stats(index, stats[8], bodyhits[8], name[], len, authid[] = "", authidlen = 0);

/* Returns number of all entries in stats. */
native lc_get_statsnum();

/*
 * Forwards
 */

/* Function is called after player to player attacks ,
* if players were damaged by teammate TA is set to 1 */
forward lc_client_damage(attacker, victim, damage, wpnindex, hitplace, TA);

/* Function is called after player death ,
* if player was killed by teammate TK is set to 1 */
forward lc_client_death(killer, victim, wpnindex, hitplace, TK);
```

