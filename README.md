##### Distortion


#### Оглавление

	1. О проекте
	2. Архитектура проекта и необходимые библиотеки
	3. Работа с .wav-файлами
	4. Фильтры
	5. Эквалайзер
	6. Дисторшн


#### О проекте

Хотя изначально этот проект был назван "Distortion", его задачи с течением времени вышли из рамок написания
лишь симуляции жёсткого гитарного перегруза. Если говорит кратко, то в рамках данного проекта была предпринята
попытка создания мини-VST для электрогитары, работающего с записями гитары в формате .wav. Он состоит из двух
наиболее важных частей для электрогитары: эквалайзера и дисторшн.

Если говорить о структуре проекта, то она выглядит так:
**int_channel.py** -- _class_ WavFile (класс .wav-файла)
**int3.py** -- функция sign_int3() (необходима для работы с 3-байтовыми сэмплами)