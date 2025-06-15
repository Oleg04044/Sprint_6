Автотесты для учебного сервиса «Яндекс Самокат»

Описание:
Этот проект содержит автотесты UI для сайта (https://qa-scooter.praktikum-services.ru).  
Реализованы сценарии заказа самоката, взаимодействия с блоком FAQ и проверка переходов по логотипам.

Что проверяют тесты:
Позитивный сценарий заказа самоката (2 набора данных)
Проверка выпадающих вопросов в FAQ
Переход по логотипу «Яндекс» (в новое окно)
Переход по логотипу «Самокат» (на главную)

---

## 📁 Структура проекта
pages/ Page Object-классы и локаторы
  base_page.py
  main_page.py
  order_page.py
  faq_page.py
  logo_page.py
  locators.py

tests/ Автотесты
  conftest.py
  test_order_button.py
  test_faq_questions.py
  test_logo_navigation.py

requirements.txt # Зависимости проекта
.gitignore # Исключения Git
README.md # Документация проекта
