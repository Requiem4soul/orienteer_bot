_jobs = {
    # Отдел снабжения
    'JobCargoTechnician': (4, 'Грузчик', '📦'),
    'JobSalvageSpecialist': (4, 'Утилизатор', '🗑️'),

    # Сервисный отдел
    'JobBartender': (0, 'Бармен', '🍹'),
    'JobBotanist': (0, 'Ботаник', '🌿'),
    'JobBoxer': (0, 'Боксёр', '🥊'),
    'JobChaplain': (0, 'Священник', '⛪'),
    'JobChef': (0, 'Шеф-повар', '👨‍🍳'),
    'JobClown': (0, 'Клоун', '🤡'),
    'JobJanitor': (0, 'Уборщик', '🧹'),
    'JobLawyer': (0, 'Юрист', '⚖️'),
    'JobLibrarian': (0, 'Библиотекарь', '📚'),
    'JobMime': (0, 'Мим', '🎭'),
    'JobMusician': (0, 'Музыкант', '🎵'),
    'JobPassenger': (0, 'Пассажир', '🚶'),
    'JobReporter': (0, 'Репортёр', '📰'),
    'JobZookeeper': (0, 'Зоотехник', '🦁'),
    'JobServiceWorker': (0, 'Сервисный работник', '🛠️'),
    'JobVisitor': (0, 'Посетитель', '👥'),

    # Отдел командования
    'JobCaptain': (7, 'Капитан', '🚀'),
    'JobIAA': (7, 'Юрист', '⚖️'),
    'JobChiefEngineer': (7, 'Старший инженер', '🔧'),
    'JobChiefMedicalOfficer': (7, 'Главный врач', '⚕️'),
    'JobMedicalOfficer': (7, 'Главный врач', '⚕️'),
    'JobHeadOfPersonnel': (7, 'Глава персонала', '👔'),
    'JobHeadOfSecurity': (7, 'Глава службы безопасности', '🛡️'),
    'JobResearchDirector': (7, 'Научный руководитель', '🔬'),
    'JobQuartermaster': (7, 'Квартирмейстер', '📦'),
    'JobBlueShield': (7, 'Офицер "Синий щит"', '🛡️'),

    # Инженерный отдел
    'JobSeniorEngineer': (1, 'Ведущий инженер', '⚙️'),
    'JobAtmosphericTechnician': (1, 'Атмосферный техник', '🌍'),
    'JobStationEngineer': (1, 'Инженер', '🔧'),
    'JobTechnicalAssistant': (1, 'Технический ассистент', '🔧'),

    # Медицинский отдел
    'JobChemist': (2, 'Химик', '⚗️'),
    'Doctor': (2, 'Доктор?', '⚕️'),
    'JobMedicalDoctor': (2, 'Врач', '⚕️'),
    'JobMedicalIntern': (2, 'Интерн', '⚕️'),
    'JobPsychologist': (2, 'Психолог', '🧠'),
    'JobParamedic': (2, 'Парамедик', '🚑'),
    'JobPathologist': (2, 'Патологоанатом', '🔬'),
    'JobSeniorPhysician': (2, 'Ведущий врач', '⚕️'),

    # Служба безопасности
    'JobSecurityCadet': (3, 'Кадет СБ', '👮'),
    'JobSecurityOfficer': (3, 'Офицер СБ', '👮'),
    'JobDetective': (3, 'Детектив', '🕵️'),
    'JobWarden': (3, 'Смотритель', '👮'),
    'JobBrigmedic': (3, 'Бригмедик', '🚑'),
    'JobPrisoner': (3, 'Заключенный', '🚔'),
    'JobSeniorOfficer': (3, 'Инструктор СБ', '👮'),
    'JobOverseer': (3, 'Надзиратель', '👮'),

    # Научный отдел
    'JobScientist': (5, 'Учёный', '🔬'),
    'JobResearchAssistant': (5, 'Научный ассистент', '🔬'),
    'JobSeniorResearcher': (5, 'Ведущий учёный', '🔬'),

    # Синтеты
    'JobSecurityBorg': (6, 'Борг СБ', '🤖'),
    'JobMedicalBorg': (6, 'Медицинский борг', '🤖'),
    'JobEngineerBorg': (6, 'Инженерный борг', '🤖'),
    'JobJunitorBorg': (6, 'Уборочный борг', '🤖'),
    'JobMiningBorg': (6, 'Шахтёрский борг', '🤖'),
    'JobBorg': (6, 'Борг', '🤖'),
    'BPLAMED': (6, 'Медицинский дрон', '🤖'),
    'BPLATech': (6, 'Технический дрон', '🤖'),
    'JobSAI': (6, 'Персональный ИИ', '📱'),

    # ЦентКом
    'JobCentralCommandOfficial': (8, 'Представитель ЦК', '🛡️'),
    'JobCentralCommandAssistant': (8, 'Ассистент ОЦК', '👔'),
    'JobCentralCommandCargo': (8, 'Грузчик ЦК', '📦'),
    'JobCentralCommandSecOfficer': (8, 'Приватный офицер ЦК', '👮'),
    'JobCentralCommandOperator': (8, 'Оператор ЦК', '🎛️'),
    'JobCentralCommandSecGavna': (8, 'Начальник безопасности ЦК', '🛡️'),
    'JobCentralCommandAdmiral': (8, 'Адмирал ЦК', '🛡️'),

    # Другое
    'JobExplorer': (9, 'Исследователь', '🌍'),
    'JobStudent': (9, 'Ученик', '🎓'),
    'JobFreelancerGear': (9, 'Фрилансер', '💼'),
    'JobFugitive': (9, 'Беглец', '🏃'),
    'JobDeliveryman': (9, 'Доставщик', '🚚'),
    'JobERTEngineer': (9, 'Инженер ОБР', '🚨'),
    'JobERTJanitor': (9, 'Уборщик ОБР', '🧹'),
    'JobERTLeader': (9, 'Лидер ОБР', '👨‍✈️'),
    'JobERTMedical': (9, 'Медик ОБР', '⚕️'),
    'JobERTSecurity': (9, 'Офицер безопасности ОБР', '👮'),
    'Admin': (9, 'Админ', '🎫'),

    # Шлак
    'Job': (9, 'Пустая профессия', '💀'),
    'jobgovnoed': (9, 'jobgovnoed', '💀'),

    'Overall': (10, 'Общее', '🌐'),
}


def get_job_group_and_name(tracker: str) -> tuple[int, str]:
    job = _jobs.get(tracker, (9, tracker, ''))
    return job[0], f' {job[2]} {job[1]}'
