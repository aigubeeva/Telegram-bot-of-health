from random import choice
from asyncio import run

dict = [
    # '''злость'''
    [
        'Глубокий вдох и выдох: Перед тем как реагировать на злость, возьмите глубокий вдох, чтобы успокоиться и избежать непродуманных действий.',
        'Попробуйте понять причину: Разберитесь, что именно вызвало ваше негодование. Это может помочь вам лучше контролировать свои эмоции.',
        'Дайте себе время: Не реагируйте моментально. Позвольте себе немного времени для остывания и размышлений перед тем, как высказаться или действовать.',
        'Используйте "Ясообщения": Выражайте свои чувства, используя конструктивные "Ясообщения" вместо обвинений, чтобы избежать агрессии.',
        'Физическая активность: Занятие спортом или физической активностью может помочь освободить отрицательную энергию.',
        'Практика терпения: Учите себя терпению и способности к прощению. Это снижает уровень злости и помогает поддерживать более здоровые отношения.',
        'Используйте юмор: Иногда смех может разрядить напряжение. Научитесь смеяться над собой и некоторыми ситуациями.',
        'Расскажите близкому человеку: Обсудите свои чувства с кемто доверенным, чтобы получить поддержку и понимание.',
        'Медитация и релаксация: Практика медитации и релаксации помогает управлять стрессом и злостью.',
        'Обратитесь за помощью к профессионалу: При необходимости консультируйтесь с психологом или терапевтом для разработки стратегий по управлению злостью.'
        ],
    # '''радость'''
    ['Примите момент: Наслаждайтесь моментом радости и осознавайте положительные чувства.',
     'Поделитесь радостью: Радость удваивается, когда вы ею делятесь. Расскажите близким о своих позитивных переживаниях.',
     'Запишите благодарность: Ведение дневника благодарности помогает фиксировать положительные моменты и создает оптимистическую перспективу.',
     'Создавайте планы на будущее: Планируйте события, которые приносят радость, чтобы увеличить ожидание положительных моментов.',
     'Занимайтесь хобби: Погружение в хобби может приносить радость и удовлетворение.',
     'Укрепляйте социальные связи: Взаимодействие с друзьями и семьей способствует укреплению положительных эмоций.',
     'Оцените мелкие радости: Обратите внимание на маленькие приятные моменты в повседневной жизни.',
     'Осознанность (mindfulness): Практикуйте осознанность, чтобы находить радость в текущем моменте.',
     'Ставьте перед собой цели: Развивайте себя и ставьте перед собой достижимые цели, что способствует удовлетворению.',
     'Создавайте позитивные традиции: Внедряйте в свою жизнь позитивные ритуалы, которые приносят радость.',
     ],
    # '''тревога'''
    ['Дыхание и релаксация: Практикуйте глубокое дыхание и релаксацию для снятия физического напряжения.',
     'Анализируйте мысли: Оцените, насколько реальными являются ваши беспокойства, и постарайтесь привести их в соответствие с реальностью.',
     'Планирование: Создавайте планы действий для решения проблем, которые вызывают тревогу.',
     'Создайте список успехов: Вспоминайте и записывайте свои прошлые достижения, чтобы поддерживать уверенность в себе.',
     'Физическая активность: Занимайтесь спортом, чтобы высвободить накопившееся напряжение и стресс.',
     'Обратитесь за поддержкой: Расскажите близким о своих беспокойствах, чтобы получить поддержку и понимание.',
     'Освоение техник релаксации: Изучайте техники релаксации, такие как йога или медитация.',
     'Ограничьте временное планирование: Ограничьте время, которое вы тратите на бесполезное беспокойство, чтобы избежать зацикливания на проблемах.',
     'Избегайте стимулов: Сократите контакт с факторами, которые усиливают вашу тревогу, когда это возможно.',
     'Поощряйте самоуважение: Напоминайте себе о собственной стойкости и способности справляться с трудностями.'
     ],
    # '''страх'''
    ['Развивайте понимание: Изучайте свои страхи, чтобы лучше понимать их и принимать меры по их управлению.',
     'Постепенная экспозиция: Постепенно привыкайте к тому, что вызывает у вас страх, начиная с менее страшных ситуаций.',
     'Обращайтесь за поддержкой: Разговаривайте с друзьями или специалистами, чтобы получить поддержку и совет.',
     'Позитивные аффирмации: Используйте позитивные утверждения для укрепления уверенности и снижения страха.',
     'Занимайтесь регулярно физической активностью: Это помогает сбросить излишнюю энергию и стресс, связанный со страхом.',
     'Изучение источников страха: Понимайте, откуда идет ваш страх, чтобы более эффективно бороться с ним.',
     'Техники релаксации: Пробуйте техники релаксации, такие как глубокое дыхание, чтобы снизить физиологическую реакцию на страх.',
     'Освоение навыков управления стрессом: Обучайтесь методам управления стрессом для смягчения воздействия страха на организм.',
     'Внимание к своим мыслям: Будьте внимательны к негативным мыслям и постарайтесь заменять их более позитивными.',
     'Самоподдержка: Поддерживайте себя и признавайте свои маленькие успехи в преодолении страха.'
     ],
    # '''отвращение'''
    ['Анализируйте причины: Попробуйте понять, что именно вызывает у вас отвращение.',
     'Избегайте токсичных ситуаций: Стремитесь минимизировать контакт с тем, что вызывает вас отвращение.',
     'Применяйте техники релаксации: Дыхательные упражнения и медитация могут помочь справиться с отвращением.',
     'Поиск позитивных сторон: Попытайтесь найти положительные аспекты того, что вызывает у вас отвращение.',
     'Обратитесь за поддержкой: Разговаривайте с доверенными людьми о своих чувствах.',
     'Учитесь прощать: Принятие и прощение могут помочь освободиться от отвращения.',
     'Занимайтесь спортом: Физическая активность помогает уменьшить стресс и негативные эмоции.',
     'Развивайте чувство юмора: Ирония и смех могут помочь в смягчении отвращения.',
     'Работайте над самопринятием: Принимайте себя таким, какой вы есть, чтобы уменьшить внутреннее напряжение.',
     'Консультируйтесь с психологом: Если отвращение сильно мешает вашей жизни, обратитесь за профессиональной помощью.'
     ],
    # '''грусть'''
    ['Разговаривайте с близкими: Поделитесь своими чувствами с доверенными людьми.',
     'Практикуйте медитацию: Сосредотачивайтесь на дыхании, чтобы успокоить ум.',
     'Творчество: Занимайтесь рисованием, письмом или музыкой для выражения своих чувств.',
     'Физическая активность: Спорт помогает выработать эндорфины, улучшая настроение.',
     'Установите малые цели: Достижения даже в мелочах могут приносить радость.',
     'Обращение к прошлому: Вспомните моменты счастья, чтобы освежить положительные воспоминания.',
     'Поставьте границы: Не бойтесь отклонять негативные воздействия, защищайте себя.',
     'Пишите дневник: Выражайте свои мысли на бумаге для чистки ума.',
     'Будьте добры к себе: Позвольте себе переживать, не обвиняйте себя в грусти.',
     'Получайте поддержку профессионалов: Психотерапевт может помочь вам понять и преодолеть грусть.'
     ],
    # '''скука'''
    ['Найдите новое хобби: Исследуйте новые увлечения и хобби, чтобы добавить разнообразие в свою жизнь.',
     'Путешествуйте: Изучайте новые места и культуры, чтобы ощутить свежесть впечатлений.',
     'Общение с новыми людьми: Знакомьтесь с разными людьми, общение с которыми может приносить новые идеи и перспективы.',
     'Обучение новому: Прокачивайте свои навыки и знания, занимаясь чемто новым.',
     'Творчество: Попробуйте себя в творческом процессе, будь то живопись, музыка или писательство.',
     'Физическая активность: Занимайтесь спортом или фитнесом, чтобы поддерживать свое тело в хорошей форме.',
     'Волонтёрство: Помогайте другим, выполняя добровольные работы, что может приносить удовлетворение и смысл.',
     'Планирование приключений: Создавайте планы на будущее, например, путешествия, чтобы держать себя в подвижности.',
     'Чтение книг: Погружайтесь в литературные произведения различных жанров для разнообразия.',
     'Медитация и релаксация: Практикуйте методы релаксации и медитации для уменьшения стресса и повышения внутреннего комфорта.'
     ],
    # '''интерес'''
    ['Исследование увлечений: Открывайте новые области знаний и углубляйтесь в них.',
     'Обучение новым навыкам: Развивайте свои умения в различных областях для постоянного роста.',
     'Участие в обсуждениях: Вовлекайтесь в обсуждения с интересными людьми, чтобы узнать новые точки зрения.',
     'Смотрите документальные фильмы: Изучайте реальные события и факты через документальные фильмы и передачи.',
     'Следите за новостями: Будьте в курсе текущих событий и развития технологий.',
     'Решение головоломок: Занимайтесь головоломками и логическими задачами для стимуляции ума.',
     'Посещение мероприятий: Ходите на выставки, конференции и другие мероприятия, связанные с вашими интересами.',
     'Чтение статей и книг: Изучайте материалы, касающиеся ваших увлечений и профессиональных интересов.',
     'Общение с экспертами: Общайтесь с профессионалами в области, которая вас интересует, чтобы получить ценные знания.',
     'Экспериментирование: Пробуйте новые подходы и методы в решении задач и проблем.'
     ],
    # '''любовь'''
    ['Общение: Активно слушайте и общайтесь с партнером, чтобы поддерживать открытую и честную коммуникацию.',
     'Совместные занятия: Находите общие увлечения и хобби, чтобы проводить больше времени вместе.',
     'Поддержка и понимание: Будьте поддержкой для партнера в трудных моментах и старайтесь понять его точку зрения.',
     'Разнообразие в отношениях: Экспериментируйте с новыми впечатлениями, чтобы не допустить рутины в отношениях.',
     'Празднование успехов: Радуйтесь вместе за достижения друг друга и подчеркивайте положительные моменты.',
     'Внимание к деталям: Замечайте и цените мелкие заботы и внимание партнера.',
     'Совместные путешествия: Путешествуйте вместе, чтобы создавать совместные воспоминания и укреплять связь.',
     'Обучение компромиссу: Учитесь находить компромиссы в решении разногласий, чтобы сохранять гармонию.',
     'Внимание к эмоциональным потребностям: Будьте внимательны к эмоциональным потребностям партнера и поддерживайте его в этом.',
     'Экспрессия любви: Выражайте свои чувства словами и действиями, чтобы партнер всегда чувствовал вашу любовь.'
     ]

]


async def rand_com(emotion_id):
    match emotion_id:
        case 1:
            return choice(dict[0])
        case 2:
            return choice(dict[1])
        case 3:
            return choice(dict[2])
        case 4:
            return choice(dict[3])
        case 5:
            return choice(dict[4])
        case 6:
            return choice(dict[5])
        case 7:
            return choice(dict[6])
        case 8:
            return choice(dict[7])
        case 9:
            return choice(dict[8])