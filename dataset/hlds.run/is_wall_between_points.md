# is_wall_between_points - сток для проверки наличия препятствий между 2 точками

Данный сток предназначен для для проверки наличия физических препятствий (в основном стен) между двумя точками. Метод выполняет трассировку луча между заданными координатами, игнорируя стекло, монстров, игроков и снаряды, и возвращает true, если луч столкнулся с чем-то на пути, и false, если путь свободен.

```pawn
stock is_wall_between_points(Float: start[3], Float: end[3], ignore_ent) {
    // Create the trace handle! It is best to create it!
    new ptr = create_tr2()

    // The main traceline function!
    // This function ignores GLASS, MISSILE and MONSTERS!
    // Here is an example of how you should combine all the flags!
    engfunc(EngFunc_TraceLine, start, end, IGNORE_GLASS | IGNORE_MONSTERS | IGNORE_MISSILE, ignore_ent, ptr)

    // We are interested in the fraction parameter
    new fraction
    get_tr2(ptr, TR_flFraction, fraction)

    // Free the trace handle (don't forget to do this!)
    free_tr2(ptr)

    // If = 1.0 then it didn't hit anything!
    return (fraction != 1.0)
}
```
