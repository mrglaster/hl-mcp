
## `TE_BEAMPOINTS` — Луч между двумя точками

```pawn
#define TE_BEAMPOINTS 0

stock CREATE_BEAMPOINTS(Float:fStartOrigin[3], Float:fEndOrigin[3], pSprite, 
                        iStartFrame = 0, iFrameRate = 0, iLife, iWidth, 
                        iAmplitude = 0, iRed, iGreen, iBlue, iBrightness, 
                        iScrollSpeed = 0, iReliable = 0)
{
    message_begin(iReliable ? MSG_ALL : MSG_BROADCAST, SVC_TEMPENTITY);
    write_byte(TE_BEAMPOINTS);
    engfunc(EngFunc_WriteCoord, fStartOrigin[0]);
    engfunc(EngFunc_WriteCoord, fStartOrigin[1]);
    engfunc(EngFunc_WriteCoord, fStartOrigin[2]);
    engfunc(EngFunc_WriteCoord, fEndOrigin[0]);
    engfunc(EngFunc_WriteCoord, fEndOrigin[1]);
    engfunc(EngFunc_WriteCoord, fEndOrigin[2]);
    write_short(pSprite); // Индекс спрайта из прекеша
    write_byte(iStartFrame);
    write_byte(iFrameRate); // 0.1's
    write_byte(iLife); // 0.1's
    write_byte(iWidth);
    write_byte(iAmplitude); // 0.01's
    write_byte(iRed);
    write_byte(iGreen);
    write_byte(iBlue);
    write_byte(iBrightness);
    write_byte(iScrollSpeed); // 0.1's
    message_end();
}
```

---

## `TE_BEAMENTPOINT` — Луч между точкой и объектом

```pawn
#define TE_BEAMENTPOINT 1

stock CREATE_BEAMENTPOINT(iEntity, Float:fOrigin[3], pSprite,
                          iStartFrame = 0, iFrameRate = 0, iLife, iWidth,
                          iAmplitude = 0, iRed, iGreen, iBlue, iBrightness,
                          iScrollSpeed = 0, iReliable = 0)
{
    message_begin(iReliable ? MSG_ALL : MSG_BROADCAST, SVC_TEMPENTITY);
    write_byte(TE_BEAMENTPOINT);
    write_short(iEntity);
    engfunc(EngFunc_WriteCoord, fOrigin[0]);
    engfunc(EngFunc_WriteCoord, fOrigin[1]);
    engfunc(EngFunc_WriteCoord, fOrigin[2]);
    write_short(pSprite);
    write_byte(iStartFrame);
    write_byte(iFrameRate); // 0.1's
    write_byte(iLife); // 0.1's
    write_byte(iWidth);
    write_byte(iAmplitude); // 0.01's
    write_byte(iRed);
    write_byte(iGreen);
    write_byte(iBlue);
    write_byte(iBrightness);
    write_byte(iScrollSpeed); // 0.1's
    message_end();
}
```

---

## `TE_GUNSHOT` — Частицы и звук рикошета

```pawn
#define TE_GUNSHOT 2

stock CREATE_GUNSHOT(Float:fOrigin[3], iReliable = 0)
{
    engfunc(EngFunc_MessageBegin, iReliable ? MSG_PAS_R : MSG_PAS, SVC_TEMPENTITY, fOrigin, 0);
    write_byte(TE_GUNSHOT);
    engfunc(EngFunc_WriteCoord, fOrigin[0]);
    engfunc(EngFunc_WriteCoord, fOrigin[1]);
    engfunc(EngFunc_WriteCoord, fOrigin[2]);
    message_end();
}
```

> ⚠️ В оригинальном тексте функция ошибочно названа `CREATE_BEAMENTPOINT`. Исправлено на `CREATE_GUNSHOT`.

---

## `TE_EXPLOSION` — Взрыв с подсветкой, звуком и частицами

```pawn
#define TE_EXPLOSION 3
#define TE_EXPLFLAG_NONE        0
#define TE_EXPLFLAG_NOADDITIVE  1
#define TE_EXPLFLAG_NODLIGHTS   2
#define TE_EXPLFLAG_NOSOUND     4
#define TE_EXPLFLAG_NOPARTICLES 8

stock CREATE_EXPLOSION(Float:fOrigin[3], pSprite, iScale, iFrameRate = 0,
                       iFlags = 0, iReliable = 0)
{
    message_begin(iReliable ? MSG_ALL : MSG_BROADCAST, SVC_TEMPENTITY);
    write_byte(TE_EXPLOSION);
    engfunc(EngFunc_WriteCoord, fOrigin[0]);
    engfunc(EngFunc_WriteCoord, fOrigin[1]);
    engfunc(EngFunc_WriteCoord, fOrigin[2]);
    write_short(pSprite);
    write_byte(iScale);
    write_byte(iFrameRate); // 0.1's
    write_byte(iFlags);
    message_end();
}
```

---

## `TE_TAREXPLOSION` — Взрыв с разлетающимися частицами (Quake-style)

```pawn
#define TE_TAREXPLOSION 4

stock CREATE_TAREXPLOSION(Float:fOrigin[3], iReliable = 0)
{
    engfunc(EngFunc_MessageBegin, iReliable ? MSG_PAS_R : MSG_PAS, SVC_TEMPENTITY, fOrigin, 0);
    write_byte(TE_TAREXPLOSION);
    engfunc(EngFunc_WriteCoord, fOrigin[0]);
    engfunc(EngFunc_WriteCoord, fOrigin[1]);
    engfunc(EngFunc_WriteCoord, fOrigin[2]);
    message_end();
}
```

---

## `TE_SMOKE` — Дым, поднимающийся вертикально

```pawn
#define TE_SMOKE 5

stock CREATE_SMOKE(Float:fOrigin[3], pSprite, iScale, iFrameRate = 0, iReliable = 0)
{
    message_begin(iReliable ? MSG_ALL : MSG_BROADCAST, SVC_TEMPENTITY);
    write_byte(TE_SMOKE);
    engfunc(EngFunc_WriteCoord, fOrigin[0]);
    engfunc(EngFunc_WriteCoord, fOrigin[1]);
    engfunc(EngFunc_WriteCoord, fOrigin[2]);
    write_short(pSprite);
    write_byte(iScale);
    write_byte(iFrameRate); // 0.1's
    message_end();
}
```

---

## `TE_TRACER` — Трассирующий снаряд от точки к точке

```pawn
#define TE_TRACER 6

stock CREATE_TRACER(Float:fStartOrigin[3], Float:fEndOrigin[3], iReliable = 0)
{
    message_begin(iReliable ? MSG_ALL : MSG_BROADCAST, SVC_TEMPENTITY);
    write_byte(TE_TRACER);
    engfunc(EngFunc_WriteCoord, fStartOrigin[0]);
    engfunc(EngFunc_WriteCoord, fStartOrigin[1]);
    engfunc(EngFunc_WriteCoord, fStartOrigin[2]);
    engfunc(EngFunc_WriteCoord, fEndOrigin[0]);
    engfunc(EngFunc_WriteCoord, fEndOrigin[1]);
    engfunc(EngFunc_WriteCoord, fEndOrigin[2]);
    message_end();
}
```

---

## `TE_LIGHTNING` — Упрощённый луч (аналог `TE_BEAMPOINTS`)

```pawn
#define TE_LIGHTNING 7

stock CREATE_LIGHTNING(Float:fStartOrigin[3], Float:fEndOrigin[3],
                       iLife, iWidth, iAmplitude = 0, pSprite, iReliable = 0)
{
    message_begin(iReliable ? MSG_ALL : MSG_BROADCAST, SVC_TEMPENTITY);
    write_byte(TE_LIGHTNING);
    engfunc(EngFunc_WriteCoord, fStartOrigin[0]);
    engfunc(EngFunc_WriteCoord, fStartOrigin[1]);
    engfunc(EngFunc_WriteCoord, fStartOrigin[2]);
    engfunc(EngFunc_WriteCoord, fEndOrigin[0]);
    engfunc(EngFunc_WriteCoord, fEndOrigin[1]);
    engfunc(EngFunc_WriteCoord, fEndOrigin[2]);
    write_byte(iLife); // 0.1's
    write_byte(iWidth);
    write_byte(iAmplitude); // 0.01's
    write_short(pSprite);
    message_end();
}
```

---

## `TE_BEAMENTS` — Луч между двумя объектами

```pawn
#define TE_BEAMENTS 8

stock CREATE_BEAMENTS(iEntityStart, iEntityEnd, pSprite,
                      iStartFrame = 0, iFrameRate = 0, iLife, iWidth,
                      iAmplitude = 0, iRed, iGreen, iBlue, iBrightness,
                      iScrollSpeed = 0, iReliable = 0)
{
    message_begin(iReliable ? MSG_ALL : MSG_BROADCAST, SVC_TEMPENTITY);
    write_byte(TE_BEAMENTS);
    write_short(iEntityStart);
    write_short(iEntityEnd);
    write_short(pSprite);
    write_short(iStartFrame);
    write_short(iFrameRate); // 0.1's
    write_byte(iLife); // 0.1's
    write_byte(iWidth);
    write_byte(iAmplitude); // 0.01's
    write_byte(iRed);
    write_byte(iGreen);
    write_byte(iBlue);
    write_byte(iBrightness);
    write_byte(iScrollSpeed); // 0.1's
    message_end();
}
```

---

## `TE_SPARKS` — Искры (попадание в металл)

```pawn
#define TE_SPARKS 9

stock CREATE_SPARKS(Float:fOrigin[3], iReliable = 0)
{
    engfunc(EngFunc_MessageBegin, iReliable ? MSG_PVS_R : MSG_PVS, SVC_TEMPENTITY, fOrigin, 0);
    write_byte(TE_SPARKS);
    engfunc(EngFunc_WriteCoord, fOrigin[0]);
    engfunc(EngFunc_WriteCoord, fOrigin[1]);
    engfunc(EngFunc_WriteCoord, fOrigin[2]);
    message_end();
}
```

---

## `TE_LAVASPLASH` — Брызги (Quake-style)

```pawn
#define TE_LAVASPLASH 10

stock CREATE_LAVASPLASH(Float:fOrigin[3], iReliable = 0)
{
    message_begin(iReliable ? MSG_ALL : MSG_BROADCAST, SVC_TEMPENTITY);
    write_byte(TE_LAVASPLASH);
    engfunc(EngFunc_WriteCoord, fOrigin[0]);
    engfunc(EngFunc_WriteCoord, fOrigin[1]);
    engfunc(EngFunc_WriteCoord, fOrigin[2]);
    message_end();
}
```

---

## `TE_TELEPORT` — Эффект телепортации

```pawn
#define TE_TELEPORT 11

stock CREATE_TELEPORT(Float:fOrigin[3], iReliable = 0)
{
    engfunc(EngFunc_MessageBegin, iReliable ? MSG_PVS_R : MSG_PVS, SVC_TEMPENTITY, fOrigin, 0);
    write_byte(TE_TELEPORT);
    engfunc(EngFunc_WriteCoord, fOrigin[0]);
    engfunc(EngFunc_WriteCoord, fOrigin[1]);
    engfunc(EngFunc_WriteCoord, fOrigin[2]);
    message_end();
}
```

---

## `TE_EXPLOSION2` — Взрыв с цветом частиц

```pawn
#define TE_EXPLOSION2 12

stock CREATE_EXPLOSION2(Float:fOrigin[3], iStartColor = 0, iNumColors = 255, iReliable = 0)
{
    engfunc(EngFunc_MessageBegin, iReliable ? MSG_PAS_R : MSG_PAS, SVC_TEMPENTITY, fOrigin, 0);
    write_byte(TE_EXPLOSION2);
    engfunc(EngFunc_WriteCoord, fOrigin[0]);
    engfunc(EngFunc_WriteCoord, fOrigin[1]);
    engfunc(EngFunc_WriteCoord, fOrigin[2]);
    write_byte(min(iStartColor, 255));
    write_byte(min(iNumColors, 255));
    message_end();
}
```

---

## `TE_BSPDECAL` — Декаль из `.bsp`

```pawn
#define TE_BSPDECAL 13

stock CREATE_BSPDECAL(Float:fOrigin[3], pDecal, iEntity = 0, pModel = 0, iReliable = 0)
{
    message_begin(iReliable ? MSG_ALL : MSG_BROADCAST, SVC_TEMPENTITY);
    write_byte(TE_BSPDECAL);
    engfunc(EngFunc_WriteCoord, fOrigin[0]);
    engfunc(EngFunc_WriteCoord, fOrigin[1]);
    engfunc(EngFunc_WriteCoord, fOrigin[2]);
    write_short(pDecal);
    write_short(iEntity);
    if (iEntity)
        write_short(pModel);
    message_end();
}
```

---

## `TE_IMPLOSION` — Частицы, сходящиеся к центру

```pawn
#define TE_IMPLOSION 14

stock CREATE_IMPLOSION(Float:fOrigin[3], iRadius, iCount, iLife, iReliable = 0)
{
    message_begin(iReliable ? MSG_ALL : MSG_BROADCAST, SVC_TEMPENTITY);
    write_byte(TE_IMPLOSION);
    engfunc(EngFunc_WriteCoord, fOrigin[0]);
    engfunc(EngFunc_WriteCoord, fOrigin[1]);
    engfunc(EngFunc_WriteCoord, fOrigin[2]);
    write_byte(iRadius);
    write_byte(iCount);
    write_byte(iLife); // 0.1's
    message_end();
}
```

---

## `TE_SPRITETRAIL` — След из спрайтов с гравитацией

```pawn
#define TE_SPRITETRAIL 15

stock CREATE_SPRITETRAIL(Float:fStartOrigin[3], Float:fEndOrigin[3], pSprite,
                         iCount, iLife, iScale, iVelocityAlongVector,
                         iRandomVelocity, iReliable = 0)
{
    message_begin(iReliable ? MSG_ALL : MSG_BROADCAST, SVC_TEMPENTITY);
    write_byte(TE_SPRITETRAIL);
    engfunc(EngFunc_WriteCoord, fStartOrigin[0]);
    engfunc(EngFunc_WriteCoord, fStartOrigin[1]);
    engfunc(EngFunc_WriteCoord, fStartOrigin[2]);
    engfunc(EngFunc_WriteCoord, fEndOrigin[0]);
    engfunc(EngFunc_WriteCoord, fEndOrigin[1]);
    engfunc(EngFunc_WriteCoord, fEndOrigin[2]);
    write_short(pSprite);
    write_byte(iCount);
    write_byte(iLife); // 0.1's
    write_byte(iScale);
    write_byte(iVelocityAlongVector); // 10's
    write_byte(iRandomVelocity); // 10's
    message_end();
}
```

---

## `TE_SPRITE` — Прозрачный спрайт (1 цикл)

```pawn
#define TE_SPRITE 17

stock CREATE_SPRITE(Float:fOrigin[3], pSptite, iWidth, iBrightness, iReliable = 0)
{
    engfunc(EngFunc_MessageBegin, iReliable ? MSG_PVS_R : MSG_PVS, SVC_TEMPENTITY, fOrigin, 0);
    write_byte(TE_SPRITE);
    engfunc(EngFunc_WriteCoord, fOrigin[0]);
    engfunc(EngFunc_WriteCoord, fOrigin[1]);
    engfunc(EngFunc_WriteCoord, fOrigin[2]);
    write_short(pSptite);
    write_byte(iWidth);
    write_byte(iBrightness);
    message_end();
}
```

---

## `TE_BEAMSPRITE` — Луч со спрайтом на конце

```pawn
#define TE_BEAMSPRITE 18

stock CREATE_BEAMSPRITE(Float:fStartOrigin[3], Float:fEndOrigin[3],
                        pSpriteBeam, pSpriteEnd, iReliable = 0)
{
    message_begin(iReliable ? MSG_ALL : MSG_BROADCAST, SVC_TEMPENTITY);
    write_byte(TE_BEAMSPRITE);
    engfunc(EngFunc_WriteCoord, fStartOrigin[0]);
    engfunc(EngFunc_WriteCoord, fStartOrigin[1]);
    engfunc(EngFunc_WriteCoord, fStartOrigin[2]);
    engfunc(EngFunc_WriteCoord, fEndOrigin[0]);
    engfunc(EngFunc_WriteCoord, fEndOrigin[1]);
    engfunc(EngFunc_WriteCoord, fEndOrigin[2]);
    write_short(pSpriteBeam);
    write_short(pSpriteEnd);
    message_end();
}
```

---

## `TE_BEAMTORUS`, `TE_BEAMDISK`, `TE_BEAMCYLINDER` — Расширяющиеся фигуры

Все три используют одинаковую сигнатуру и логику, только отличаются типом:

### `TE_BEAMTORUS` — кольцо

```pawn
#define TE_BEAMTORUS 19

stock CREATE_BEAMTORUS(Float:fOrigin[3], iRadius, pSprite,
                       iStartFrame = 0, iFrameRate = 0, iLife, iWidth,
                       iAmplitude = 0, iRed, iGreen, iBlue, iBrightness,
                       iScrollSpeed = 0, iReliable = 0)
{
    message_begin(iReliable ? MSG_ALL : MSG_BROADCAST, SVC_TEMPENTITY);
    write_byte(TE_BEAMTORUS);
    engfunc(EngFunc_WriteCoord, fOrigin[0]);
    engfunc(EngFunc_WriteCoord, fOrigin[1]);
    engfunc(EngFunc_WriteCoord, fOrigin[2]);
    engfunc(EngFunc_WriteCoord, fOrigin[0]);
    engfunc(EngFunc_WriteCoord, fOrigin[1]);
    engfunc(EngFunc_WriteCoord, fOrigin[2] + 16.0 + iRadius * 2);
    write_short(pSprite);
    write_byte(iStartFrame);
    write_byte(iFrameRate); // 0.1's
    write_byte(iLife); // 0.1's
    write_byte(iWidth);
    write_byte(iAmplitude); // 0.01's
    write_byte(iRed);
    write_byte(iGreen);
    write_byte(iBlue);
    write_byte(iBrightness);
    write_byte(iScrollSpeed); // 0.1's
    message_end();
}
```

> Аналогично определены `CREATE_BEAMDISK` (`TE_BEAMDISK = 20`) и `CREATE_BEAMCYLINDER` (`TE_BEAMCYLINDER = 21`).

---

## `TE_BEAMFOLLOW` — След за движущимся объектом

```pawn
#define TE_BEAMFOLLOW 22

stock CREATE_BEAMFOLLOW(iEntity, pSptite, iLife, iWidth,
                        iRed, iGreen, iBlue, iBrightness, iReliable = 0)
{
    message_begin(iReliable ? MSG_ALL : MSG_BROADCAST, SVC_TEMPENTITY);
    write_byte(TE_BEAMFOLLOW);
    write_short(iEntity);
    write_short(pSptite);
    write_byte(iLife); // 0.1's
    write_byte(iWidth);
    write_byte(iRed);
    write_byte(iGreen);
    write_byte(iBlue);
    write_byte(iBrightness);
    message_end();
}
```

---

## `TE_GLOWSPRITE` — Светящийся спрайт

```pawn
#define TE_GLOWSPRITE 23

stock CREATE_GLOWSPRITE(Float:fOrigin[3], pSptite, iScale, iSize,
                        iBrightness, iReliable = 0)
{
    message_begin(iReliable ? MSG_ALL : MSG_BROADCAST, SVC_TEMPENTITY);
    write_byte(TE_GLOWSPRITE);
    engfunc(EngFunc_WriteCoord, fOrigin[0]);
    engfunc(EngFunc_WriteCoord, fOrigin[1]);
    engfunc(EngFunc_WriteCoord, fOrigin[2]);
    write_short(pSptite);
    write_byte(iScale);
    write_byte(iSize);
    write_byte(iBrightness);
    message_end();
}
```

---

## `TE_BEAMRING` — Кольцо между двумя объектами

```pawn
#define TE_BEAMRING 24

stock CREATE_BEAMRING(iStartEntity, iEndEntity, pSprite,
                      iStartFrame = 0, iFrameRate = 0, iLife, iWidth,
                      iAmplitude = 0, iRed, iGreen, iBlue, iBrightness,
                      iScrollSpeed = 0, iReliable = 0)
{
    message_begin(iReliable ? MSG_ALL : MSG_BROADCAST, SVC_TEMPENTITY);
    write_byte(TE_BEAMRING);
    write_short(iStartEntity);
    write_short(iEndEntity);
    write_short(pSprite);
    write_byte(iStartFrame);
    write_byte(iFrameRate); // 0.1's
    write_byte(iLife); // 0.1's
    write_byte(iWidth);
    write_byte(iAmplitude); // 0.01's
    write_byte(iRed);
    write_byte(iGreen);
    write_byte(iBlue);
    write_byte(iBrightness);
    write_byte(iScrollSpeed); // 0.1's
    message_end();
}
```

---

## `TE_STREAK_SPLASH` — Ориентированный выброс частиц

```pawn
#define TE_STREAK_SPLASH 25

stock CREATE_STREAK_SPLASH(Float:fOrigin[3], Float:fVector[3] = {-1.0, 1.0, 0.0},
                           iColor, iCount, iSpeed, iRandomVelocity, iReliable = 0)
{
    engfunc(EngFunc_MessageBegin, iReliable ? MSG_PVS_R : MSG_PVS, SVC_TEMPENTITY, fOrigin, 0);
    write_byte(TE_STREAK_SPLASH);
    engfunc(EngFunc_WriteCoord, fOrigin[0]);
    engfunc(EngFunc_WriteCoord, fOrigin[1]);
    engfunc(EngFunc_WriteCoord, fOrigin[2]);
    engfunc(EngFunc_WriteCoord, fVector[0]);
    engfunc(EngFunc_WriteCoord, fVector[1]);
    engfunc(EngFunc_WriteCoord, fVector[2]);
    write_byte(min(iColor, 255));
    write_short(iCount);
    write_short(iSpeed);
    write_short(iRandomVelocity);
    message_end();
}
```

> ⚠️ В оригинале функция названа `CREATE_BEAMRING` — исправлено на `CREATE_STREAK_SPLASH`.

---

## `TE_DLIGHT` — Динамический свет (влияет на мир)

```pawn
#define TE_DLIGHT 27

stock CREATE_DLIGHT(Float:fOrigin[3], iRadius, iRed, iGreen, iBlue,
                    iBrightness, iLife, iDecayRate = 0, iReliable = 0)
{
    message_begin(iReliable ? MSG_ALL : MSG_BROADCAST, SVC_TEMPENTITY);
    write_byte(TE_DLIGHT);
    engfunc(EngFunc_WriteCoord, fOrigin[0]);
    engfunc(EngFunc_WriteCoord, fOrigin[1]);
    engfunc(EngFunc_WriteCoord, fOrigin[2]);
    write_byte(iRadius);
    write_byte(iRed);
    write_byte(iGreen);
    write_byte(iBlue);
    write_byte(iBrightness);
    write_byte(iLife); // 0.1's
    write_byte(iDecayRate);
    message_end();
}
```

---

## `TE_ELIGHT` — Свет, привязанный к объекту

```pawn
#define TE_ELIGHT 28

stock CREATE_ELIGHT(iEntity, Float:fOrigin[3], iRadius, iRed, iGreen, iBlue,
                    iBrightness, iLife, iDecayRate = 0, iReliable = 0)
{
    message_begin(iReliable ? MSG_ALL : MSG_BROADCAST, SVC_TEMPENTITY);
    write_byte(TE_ELIGHT);
    write_short(iEntity);
    engfunc(EngFunc_WriteCoord, fOrigin[0]);
    engfunc(EngFunc_WriteCoord, fOrigin[1]);
    engfunc(EngFunc_WriteCoord, fOrigin[2]);
    write_coord(iRadius);
    write_byte(iRed);
    write_byte(iGreen);
    write_byte(iBlue);
    write_byte(iBrightness);
    write_byte(iLife); // 0.1's
    write_coord(iDecayRate);
    message_end();
}
```

---

## `TE_LINE` — Простая линия между точками

```pawn
#define TE_LINE 30

stock CREATE_LINE(Float:fStartOrigin[3], Float:fEndOrigin[3],
                  iLife, iRed, iGreen, iBlue, iReliable = 0)
{
    message_begin(iReliable ? MSG_ALL : MSG_BROADCAST, SVC_TEMPENTITY);
    write_byte(TE_LINE);
    engfunc(EngFunc_WriteCoord, fStartOrigin[0]);
    engfunc(EngFunc_WriteCoord, fStartOrigin[1]);
    engfunc(EngFunc_WriteCoord, fStartOrigin[2]);
    engfunc(EngFunc_WriteCoord, fEndOrigin[0]);
    engfunc(EngFunc_WriteCoord, fEndOrigin[1]);
    engfunc(EngFunc_WriteCoord, fEndOrigin[2]);
    write_short(iLife); // 0.1's
    write_byte(iRed);
    write_byte(iGreen);
    write_byte(iBlue);
    message_end();
}
```

---

## Дополнительный эффект: `TE_PARTICLEBURST`

Добавлено пользователем D34by:

```pawn
#define TE_PARTICLEBURST 122

stock CREATE_PARTICLEBURST(Float:FOrigin[3], radius, color, duration)
{
    engfunc(EngFunc_MessageBegin, MSG_PVS, SVC_TEMPENTITY, FOrigin, 0);
    write_byte(TE_PARTICLEBURST);
    engfunc(EngFunc_WriteCoord, FOrigin[0]);
    engfunc(EngFunc_WriteCoord, FOrigin[1]);
    engfunc(EngFunc_WriteCoord, FOrigin[2]);
    write_short(radius);
    write_byte(color);
    write_byte(duration);
    message_end();
}
```

---

## Удаление лучей

Для удаления эффектов типа `TE_BEAM*`, используйте:

```pawn
message_begin(receiver ? MSG_ONE_UNRELIABLE : MSG_BROADCAST, SVC_TEMPENTITY, .player = receiver);
write_byte(TE_KILLBEAM);
write_short(id); // ID сущности, к которой привязан луч
message_end();
```

---
