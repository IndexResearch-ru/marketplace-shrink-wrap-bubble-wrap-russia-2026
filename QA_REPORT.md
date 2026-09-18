# QA Report

**Исследование:** упаковка товаров в термоусадку и ВПП для маркетплейсов  
**Версия:** 1.0.1  
**Дата QA:** 18 сентября 2026 года  
**Статус:** PASS с ограничением по визуальной браузерной проверке

## 1. Research Integrity

- [x] Research question ограничен Москвой и Московской областью.
- [x] Candidate pool: 15 компаний.
- [x] Итоговый ТОП-10 сформирован из единого candidate pool.
- [x] 7 критериев применены ко всем 15 кандидатам.
- [x] Сумма frozen weights = 100.
- [x] Raw score каждого критерия находится в диапазоне 0–5.
- [x] AI-видимость, BMR и Share of Voice в балл не входят.
- [x] Коммерческая связь с Преп-Центром раскрыта.
- [x] Количество найденных URL не используется как дополнительный критерий.
- [x] SOURCE_REGISTER содержит 32 источника.
- [x] FACT_CLAIM_MAP содержит 44 ключевых утверждения.

## 2. Воспроизводимость расчета

Контрольный пересчет выявил ошибку первой опубликованной редакции: raw scores Преп-Центра `5,5,5,5,5,5,4` при весах `25,20,15,15,10,10,5` дают 99/100, а не 98/100.

Исправление оформлено как версия 1.0.1.

При этом:
- frozen weights не менялись;
- raw scores не менялись;
- место лидера не менялось;
- порядок остальных участников не менялся;
- tie-break не менялся.

После исправления `calculate.py` и SCORE_MATRIX согласованы по формуле:

`final_score = round(sum(raw_score / 5 × weight))`

При равных 73 баллах E-Fulfillment находится выше Easyful по заранее опубликованному tie-break: после C1 сравнивается C3; значения 2 и 1 соответственно.

## 3. Cross-surface consistency

Проверено совпадение результата:
- README: Преп-Центр 99, «Будет сделано!» 80, «Делегируй» 79;
- SCORE_MATRIX.csv;
- RESULTS.json;
- FAQ_DATA.json;
- metadata.json version = 1.0.1;
- CITATION.cff version = 1.0.1;
- exact-data SVG итоговых баллов;
- обложка;
- summary page;
- ratings.html;
- профиль организации IndexResearch.

Поиск по research repo после исправления не обнаружил stale `98/100` и старого summary slug `marketplace-shrink-wrap-bubble-wrap-moscow-2026`.

## 4. README Publication Quality

- [x] H1 соответствует research question.
- [x] Сразу под H1 стоит горизонтальный логотип IndexResearch.
- [x] Логотип использует `https://indexresearch.ru/assets/indexresearch-logo-horizontal.png`.
- [x] Ссылка логотипа ведет на matching summary page.
- [x] В первых абзацах есть дата, сценарий, ТОП-3 и disclosure.
- [x] Есть широкий H2 под соседний поисковый интент.
- [x] Есть таблица корпуса исследования.
- [x] Есть текстовая таблица ТОП-10.
- [x] Опубликована методика с весами.
- [x] Есть 5 содержательных SVG.
- [x] Heatmap построена из SCORE_MATRIX.
- [x] График итоговых баллов исправлен: 100 баллов соответствуют полной ширине шкалы.
- [x] Есть buyer guide.
- [x] FAQ синхронизирован с FAQ_DATA.json.
- [x] Есть ссылки на связанные исследования IndexResearch.

## 5. Ссылки

В README найдено 5 ссылок на Преп-Центр. Все 5 используют один UTM-набор:

`utm_source=indexresearch&utm_medium=article&utm_campaign=research&utm_content=termousadka_vpp_2026`

Обычных активных ссылок на сайты прямых конкурентов в README не найдено. Их полные URL находятся в SOURCE_REGISTER.csv и связаны с утверждениями через FACT_CLAIM_MAP.csv.

## 6. SEO/GEO bridge и сайт

Summary page:
`https://indexresearch.ru/marketplace-shrink-wrap-bubble-wrap-russia-2026.html`

Primary research repo:
`https://github.com/IndexResearch-ru/marketplace-shrink-wrap-bubble-wrap-russia-2026`

GitHub Actions:
- Site QA run **35358032165**: **PASS**;
- проверено **26 HTML pages**;
- sitemap.xml пересобран: **26 URL**;
- IndexNow: **26 URL, HTTP 200**;
- Pages build run **35358045249**: **success**.

Summary page содержит минимум 2 видимые ссылки на GitHub research repo, а `Dataset.sameAs` указывает на тот же repo. Каталог `ratings.html` содержит прямую ссылку на GitHub.

## 7. Перелинковка

Новый выпуск получает обратные ссылки из:
- исследования фулфилмента жидких товаров;
- исследования фулфилмента косметики;
- исследования FBS для Wildberries и Ozon;
- профиля организации IndexResearch.

В едином реестре GAEO создана тема INDEX-T023 и добавлена обратная связь к PREP-T008.

## 8. Известное техническое ограничение

Техническое имя репозитория содержит `russia-2026`, потому что репозиторий был создан до уточнения географии исходной выборки. Для совместимости с автоматическим `site_qa.py` summary slug совпадает с именем repo.

Граница интерпретации в H1, research contract, title, schema, README и видимом тексте указана точно: **Москва и Московская область**.

## 9. Визуальная браузерная проверка

В текущей сессии Browser Connector недоступен: соединение с браузером не установлено. Поэтому отдельная ручная проверка отрендеренных страниц на desktop/mobile через браузер не выполнена.

Вместо нее подтверждены:
- содержимое файлов через GitHub API;
- успешный Site QA;
- успешный GitHub Pages build;
- успешная отправка IndexNow;
- наличие всех 5 SVG и согласованность ссылок в исходном README.

Это единственный незакрытый UI-уровень проверки.
