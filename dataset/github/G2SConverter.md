# G2SConverter — Конвертер моделей из GoldSource в Source с ИИ-улучшением текстур

## Метаданные

- **Репозиторий**: `mrglaster/G2SConverter`
- **Автор**: Egor Pristavka (mrglaster)
- **Последнее обновление**: 10 октября 2022 (`7d7a99f`)
- **Язык**: Python 100%
- **Лицензия**: Не указана (предполагается open-source)
- **Темы**: `converter`, `ai`, `model`, `source-engine`, `goldsource`, `upscaling`, `normalmap`, `deblur`
- **Звёзды**: 16 ⭐ | **Форки**: 5 | **Watchers**: 2
- **Релиз**: v1.0 (26 июля 2022)

---

## Описание

**G2SConverter** — это Python-утилита для конвертации 3D-моделей из устаревшего движка **GoldSource** (Half-Life 1, CS 1.6) в современный **Source Engine** (Half-Life 2, TF2, CS:GO и др.).

Уникальная особенность: **автоматическое улучшение качества текстур с помощью ИИ**, включая:

- **Апскейлинг** (увеличение разрешения) через Real-ESRGAN.
- **Деблюринг** (устранение размытия) через Scale-recurrent Network.
- **Генерация нормал-карт** через DeepBump.

Это позволяет дать "вторую жизнь" старым моделям с визуальным качеством, приближенным к современному уровню.

---

## Ключевые возможности

- Конвертация `.mdl` моделей GoldSource → Source Engine.
- **ИИ-апгрейд текстур**:
  - Увеличение масштаба: x2, x4, x8.
  - Устранение размытия (до 10 итераций).
  - Автоматическая генерация нормал-карт для реализма освещения.
- Поддержка пакетной обработки (можно указать папку с моделями).
- Интеграция с `studiomdl.exe` для компиляции в финальный `.mdl` Source.

---

## Установка и зависимости

### 1. Установите зависимости Python:

```bash
pip install -r requirements.txt
pip install opencv-contrib-python
```

Или вручную:

```bash
pip install imageio==2.14.0 numpy==1.22.1 onnx==1.10.2 onnxoptimizer==0.2.6 onnxruntime==1.10.0 opencv_python_headless==3.4.17.61 opencv-contrib-python Pillow==9.0.1 scikit_image==0.19.1 scipy==1.7.3 skimage==0.0 tensorflow==2.7.0 tf_slim==1.1.0 torch==1.10.1
```

### 2. (Опционально, но рекомендуется) Установите **CUDA Toolkit**

> Без CUDA обработка текстур на CPU может занимать **очень много времени**.

Скачать: [https://developer.nvidia.com/cuda-toolkit](https://developer.nvidia.com/cuda-toolkit)

---

## Использование

Запустите конвертацию командой:

```bash
python converter.py \
  --input cactus.mdl \
  --studiomdl "D:\\SteamLibrary\\steamapps\\common\\Team Fortress 2\\bin\\studiomdl.exe" \
  --compiled "D:\\SteamLibrary\\steamapps\\common\\Team Fortress 2\\tf\\models\\" \
  --upscaling True \
  --scaling_factor 4 \
  --normalmaps True \
  --deconvolution True \
  --iterations 4
```

### Аргументы командной строки:

| Аргумент           | Тип      | Описание |
|--------------------|----------|----------|
| `--input`          | `str`    | Путь к файлу `.mdl` или папке с моделями. |
| `--studiomdl`      | `str`    | Путь к `studiomdl.exe` (находится в `/bin/` папке игры на Source). |
| `--compiled`       | `str`    | Папка `/models/` игры, куда будет сохранена скомпилированная модель. |
| `--upscaling`      | `bool`   | Включить апскейлинг текстур? (`True`/`False`) |
| `--scaling_factor` | `int`    | Множитель масштаба: `2`, `4`, `8`. |
| `--normalmaps`     | `bool`   | Генерировать нормал-карты? (`True`/`False`) |
| `--deconvolution`  | `bool`   | Включить деблюринг текстур? (`True`/`False`) |
| `--iterations`     | `int`    | Количество итераций деблюринга (рекомендуется 4–8, максимум 10). |

---

##  Используемые ИИ-модели и технологии

- **Апскейлинг**: [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) — генерация высококачественных деталей.
- **Деблюринг**: [SRN-Deblur](https://github.com/jiangsutx/SRN-Deblur) — Scale-recurrent Network для глубокого устранения размытия.
- **Нормал-карты**: [DeepBump](https://github.com/HugoTini/DeepBump) — генерация карт нормалей из 2D-текстур.
- **Работа с VTF**: [VTFLib](https://github.com/NeilJed/VTFLib) — для обработки текстур Source Engine.

---
