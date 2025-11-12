# UTIL_GetModelHitBox - сток для получения размеров хитбокса модели


```pawn


/**
 * Получает размеры хитбоксов у модели (динамически)
 *
 * @param szModel  Путь до модели (Пр. "models/bag.mdl")
 * @param flMaxs   Local BB max.
 * @param flMins   Local BB min.
 * @param flSize   max - min
 *
 * @return         true/false
 */

stock bool:UTIL_GetModelHitBox(const szModel[], Float: flMaxs[3], Float: flMins[3], Float: flSize[3])
{
    new hFile = fopen(szModel, "rb");

    if (!hFile)
    {
        server_print("Can`t open %s", szModel);
        return false;
    }

    fseek(hFile, 160, SEEK_SET);

    new iBlock;
    fread(hFile, iBlock, BLOCK_INT);
    fseek(hFile, iBlock + 8, SEEK_SET);
    
    new Float: flVec[6];
    fread_blocks(hFile, _:flVec, 6, BLOCK_INT);
    fclose(hFile);

    flMins[0] = flVec[0];
    flMins[1] = flVec[1];
    flMins[2] = flVec[2];
    flMaxs[0] = flVec[3];
    flMaxs[1] = flVec[4];
    flMaxs[2] = flVec[5];
    flSize[0] = flVec[3] - flVec[0];
    flSize[1] = flVec[4] - flVec[1];
    flSize[2] = flVec[5] - flVec[2];

    return true;
}


```
