# The nVault Module - Модуль nVault
[The nVault Module](http://amxxmodx.ru/nvaultinc/)
## Для чего нужен nVault модуль
  
**nVault** - инструмент AMX-X, разработанный для хранения и получения данных из файла. Много людей спрашивают, как сохранить данные в плагине при смене карты или при перезапуске сервера. С помощью **nVault** это реализуется достаточно просто.  
  
**nVault** хранит данные, используя **key:data** систему  
У каждого блока данных, которые сохраняете, есть уникальный ключ, который соответствует ему.   
Сохраняемые данные и ключ всегда строкового вида, но данные могут быть получены как целое число (integer) , дробное (float) или строка (string).  
  
Данные сохраняются в _двоичном_ формате, это означает, что вы не можете отредактировать файл в блокноте, но есть nVault редактор, который может открыть и редактировать такой файл.   
Вы не можете скачивать файлы с нашего сервера  
  

## Функции модуля
  
[**nvault_open**](http://amxxmodx.ru/nvaultinc/402-nvault_open-funkciya-otkryvaet-fayl-s-binarnymi-dannymi.html) - Открывает файл по имени (например "myvault").  
[**nvault_close**](http://amxxmodx.ru/nvaultinc/411-nvault_close-funkciya-zakryvaet-fayl.html) - Закрывает файл с данными.  
[**nvault_lookup**](http://amxxmodx.ru/nvaultinc/406-nvault_lookup-funkciya-dlya-poiska-dannyh-po-klyucham.html) - Функция ищет указанное значение для получения полной информации.  
[**nvault_get**](http://amxxmodx.ru/nvaultinc/405-nvault_get-funkciya-poluchaet-znachenie-po-klyuchu-v-integer-float-ili-string.html) - Получает значение по ключу integer, string либо float.  
[**nvault_set**](http://amxxmodx.ru/nvaultinc/403-nvault_set-funkciya-ustanavlivaet-znachenie-s-izmeneniem-vremennoy-metki.html) - Устанавливает значение по ключу с текущей временной меткой (timestamp).  
[**nvault_pset**](http://amxxmodx.ru/nvaultinc/407-nvault_pset-funkciya-zapisyvaet-znachenie-po-klyuchu-ne-izmenyaya-datu.html) - Устанавливает значение по ключу без временной метки.  
[**nvault_touch**](http://amxxmodx.ru/nvaultinc/408-nvault_touch-funkciya-izmenyaet-datu-v-zapisyah-po-klyuchu.html) - Функция для обновления временной метки по ключу  
[**nvault_prune**](http://amxxmodx.ru/nvaultinc/410-nvault_prune-funkciya-udalyayuschaya-dannye-v-zadannom-diapazone.html) - Удалить записи с указанным интервалом временных меток (timestamp). Исключение: значения установленные с помощью nvault_pset..  
[**nvault_remove**](http://amxxmodx.ru/nvaultinc/409-nvault_remove-funkciya-udalyaet-zapisi-po-klyuchu.html) - Функция для удаления записи по ключу
