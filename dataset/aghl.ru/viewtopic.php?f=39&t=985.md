# Half-Life и Adrenaline Gamer форум


## [Metamod - Полезные функции](https://aghlru.ds-servers.com/forum/viewtopic.php?f=39&t=985)
**Функция приводит углы в диапазон [ 0 - 359(+/-)]**  
  
Не секрет что полный оборот (вокруг своей оси) равен 360°, однако угол поворота может рассматриваться как исключительно положительное значение где 0 == 360(начальные значения в градусах - либо полный оборот), так и относительно вращения в обратную сторону (с отрицательными значениями). Такое устройство двоякого представления не повлияет на работоспособность данной функции, т.к. к примеру -180° == 180°.  
  
Q - _для чего же нужна эта функция ?_  
A - Для корректировки градусов в тех случаях когда значения градусов явно не несут смысловой нагрузки, к примеру -> {-14567.0, 130.0, 2663.0}. В данном примере результат калькуляции векторов, вне зависимости от этих космических значений ![:\)](https://aghlru.ds-servers.com/forum/images/smilies/smile.gif) проекция (к примеру модели) будет отображаться верно. Но даже этот факт не исключает применение данной функции, примером этому могут служить ситуации когда нужно сравнивать градусы либо же производить калькуляцию относительно константных значений(градусов).  
  
Результатом манипуляций с данным в примере вектором, выдаст истинные значения -> {-167.0, 130.0, 143.0}  
**Код:** 
```
void UTIL_AnglesNormalize(Vector& vec_fSource)  
{  
   vec_fSource[0]=((vec_fSource[0]-(int)vec_fSource[0])+((int)vec_fSource[0]%360));  
   vec_fSource[1]=((vec_fSource[1]-(int)vec_fSource[1])+((int)vec_fSource[1]%360));  
   vec_fSource[2]=((vec_fSource[2]-(int)vec_fSource[2])+((int)vec_fSource[2]%360));  
}  

```
 **Получение "_типа_ " поверхности** 
  
Любая поверхность игрового мира делится(по типу) на несколько категорий(каждая из которых имеет подтипы):  
  
I)Горизонтальная : I)Пол, II)Потолок(обратка "полу")  
II)Вертикальная : I)Ось "X" II)Ось "Y" III)Ос**и** "XY" (Оси "X" и "Y" Имеют свои противоположности, гибридная-же Ось "XY" - не уверен ![:\)](https://aghlru.ds-servers.com/forum/images/smilies/smile.gif), но в коде присутствует проверка и на нее ![:D](https://aghlru.ds-servers.com/forum/images/smilies/biggrin.gif))  
III)Имеющая уклон : I)Ось "X" II)Ось "Y" III)Ос**и** "XY" (+уклоны с противоположными значениями)  
**[▼](https://aghlru.ds-servers.com/forum/viewtopic.php?f=39&t=985) Код** **Код:** 
```
#define GROUND_TYPE_VERTICAL_X (1<<0)  
#define GROUND_TYPE_AXIS_X (1<<1)  
#define GROUND_TYPE_VERTICAL_Y (1<<2)  
#define GROUND_TYPE_AXIS_Y (1<<3)  
#define GROUND_TYPE_VERTICAL_XY (1<<4)  
#define GROUND_TYPE_AXIS_XY (1<<5)  
#define GROUND_TYPE_HORIZONTAL (1<<6)  
#define GROUND_TYPE_NEGATIVE (1<<7)  
#define GROUND_TYPE_REVERSE (1<<8)  
  
unsignedshortint UTIL_GetGroundType(constTraceResult&TraceData)  
{  
unsignedshortint iReturn;  
unsignedshortint iCell =0;  
unsignedshortint iOffSet =0;  
unsignedshortint iBitReverse =0;  
  
if(TraceData.vecPlaneNormal[2]==1.0)// Ground -> Horizontal (floor)  
{  
      iReturn = GROUND_TYPE_HORIZONTAL;  
}  
  
elseif(TraceData.vecPlaneNormal[2]==0.0)// Ground -> Vertical  
{  
      iReturn = GROUND_TYPE_VERTICAL_XY;  
}  
  
elseif(TraceData.vecPlaneNormal[2]==-1.0)// Ground -> Horizontal (ceiling)  
{  
      iReturn =(GROUND_TYPE_HORIZONTAL | GROUND_TYPE_NEGATIVE);  
}  
  
else// Ground -> Has Angles  
{  
if(TraceData.vecPlaneNormal[2]<0.0)  
{  
         iBitReverse = GROUND_TYPE_REVERSE;  
}  
  
      iReturn = GROUND_TYPE_AXIS_XY;  
      iOffSet =1;  
}  
  
if(iReturn &(GROUND_TYPE_AXIS_XY | GROUND_TYPE_VERTICAL_XY))  
{  
bool bGroundInitialized =true;  
  
if(TraceData.vecPlaneNormal[0]==0.0)  
{  
         iReturn = GROUND_TYPE_VERTICAL_Y;  
         iCell =1;  
}  
  
elseif(TraceData.vecPlaneNormal[1]==0.0)  
{  
         iReturn = GROUND_TYPE_VERTICAL_X;  
}  
  
else  
{  
         iReturn = GROUND_TYPE_VERTICAL_XY;  
         bGroundInitialized =false;  
}  
  
      iReturn <<= iOffSet;// If - "iOffSet" :: Convert Flags From "VERTICAL" To "AXIS"  
  
if((bGroundInitialized ?(TraceData.vecPlaneNormal[iCell]<0.0):((TraceData.vecPlaneNormal[0]<0.0)||(TraceData.vecPlaneNormal[1]<0.0))))  
{  
         iReturn |= GROUND_TYPE_NEGATIVE;  
}  
}  
  
   iReturn |= iBitReverse;  
  
return iReturn;  
}  

```
К примеру чтобы узнать потолок или нет - нужно проверить на флаги, в общем, любой тип поверхности можно отловить с помощью этих флагов ![:\)](https://aghlru.ds-servers.com/forum/images/smilies/smile.gif)  
**Код:** 
```
/*  
     Потолок может быть как горизонтальным так и иметь уклон, по этому рассмотрим оба варианта  
  
     X - ВАШ ЭКЗЕМПЛЯР СТРУКТУРЫ - "TraceResult"  
*/  
  
unsignedshortint iType = UTIL_GetGroundType(X);  
  
if(iType ==(GROUND_TYPE_HORIZONTAL | GROUND_TYPE_NEGATIVE))  
{  
// Горизонтальный потолок  
}  
  
if(iType &(GROUND_TYPE_AXIS_X | GROUND_TYPE_AXIS_Y | GROUND_TYPE_AXIS_XY))// Определяем наличие уклона  
{  
if(iType & GROUND_TYPE_REVERSE)  
{  
// Потолок под уклоном  
}  
}  
  
/*  
     1) GROUND_TYPE_NEGATIVE 2) GROUND_TYPE_REVERSE  
  
     При проверке часто эти флаги попросту не нужны, по этому исключаем 1н из них или сразу оба из битсуммы и получаем "чистое" значение типа поверхности  
  
     iType &= ~(GROUND_TYPE_NEGATIVE | GROUND_TYPE_REVERSE);  
*/  

```
PS  
В скором времени выложу код выставления углов моделькам относительно "типа" поверхности - используя данную функцию Обновлено: 1)Добавлен флаг - "GROUND_TYPE_REVERSE" (определяет является-ли уклон частью "потолка") 2)Переписано определение флага "GROUND_TYPE_NEGATIVE" 
