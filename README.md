Руководство по настройке веб-приложения:

Скачайте .zip архив проекта на свой ПК

Разархивируйте архив

Откройте терминал и дойдите до пути, где находится папка с проектом

Напишите в терминале: python manage.py runserver

У вас должно все заработать!

Если что для админки:
Надо зайти в localhost/admin (Вместо localhost тут может быть ваш IP адрес и порт на локальной компьютере, где запускается приложение)

Логин: alisher
Пароль: Ali2007.

В ходе процесса проектирования и разработки веб-приложения Star Wars на Django я начал с четкого определения концепции приложения. 
Изначально идея состояла в создании платформы, предназначенной для фанатов вселенной Звездных войн, которая предоставляла бы информацию о персонажах, 
фильмах, планетах и других аспектах этой популярной франшизы.

Одним из ключевых этапов был анализ требований пользователей, в результате которого были выявлены основные функциональные возможности, которые они ожидают 
от приложения. Это помогло сформировать четкий список фич, которые необходимо было внедрить, чтобы удовлетворить потребности пользователей.

Далее я перешел к проектированию базы данных, где определялись основные сущности приложения, их атрибуты и связи между ними. Например, 
я определил сущности, такие как персонажи, фильмы, планеты, атрибуты каждой сущности и их взаимосвязи, что позволило эффективно организовать хранение и доступ к данным.

В процессе разработки приложения я придерживался принципов MVC-архитектуры, что позволило разделить логику приложения на модели, 
представления и контроллеры. Это способствовало более четкому и структурированному коду, а также упростило его поддержку и развитие в будущем.

Одним из основных компромиссов, который пришлось сделать, было ограничение функционала приложения в начальной версии, чтобы уложиться 
в сроки разработки и сосредоточиться на основных возможностях. Также возникли некоторые сложности с проектированием связей между сущностями 
базы данных, но с помощью тщательного анализа и тестирования мы смогли найти оптимальное решение.

В целом, процесс разработки приложения Star Wars на Django был увлекательным и позволил применить разнообразные подходы и методологии для достижения поставленных целей.
