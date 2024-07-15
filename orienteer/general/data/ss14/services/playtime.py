from uuid import UUID

from ..repositories import playtime

from orienteer.general.formatting.time import get_formatted_timedelta

_job_dict = {
    'JobCargoTechnician': (4, 'Грузчик'),
    'JobSalvageSpecialist': (4, 'Утилизатор'),

    'JobBartender': (0, 'Бармен'),
    'JobBotanist': (0, 'Ботаник'),
    'JobBoxer': (0, 'Боксёр'),
    'JobChaplain': (0, 'Священник'),
    'JobChef': (0, 'Шеф-повар'),
    'JobClown': (0, 'Клоун'),
    'JobJanitor': (0, 'Уборщик'),
    'JobLawyer': (0, 'Юрист'),
    'JobLibrarian': (0, 'Библиотекарь'),
    'JobMime': (0, 'Мим'),
    'JobMusician': (0, 'Музыкант'),
    'JobPassenger': (0, 'Пассажир'),
    'JobReporter': (0, 'Репортёр'),
    'JobZookeeper': (0, 'Зоотехник'),
    'JobServiceWorker': (0, 'Сервисный работник'),
    'JobVisitor': (0, 'Посетитель'),

    'JobCaptain': (7, 'Капитан'),
    'JobIAA': (7, 'Юрист'),
    'JobChiefEngineer': (7, 'Старший инженер'),
    'JobChiefMedicalOfficer': (7, 'Главный врач'),
    'JobMedicalOfficer': (7, 'Главный врач'),
    'JobHeadOfPersonnel': (7, 'Глава персонала'),
    'JobHeadOfSecurity': (7, 'Глава службы безопасности'),
    'JobResearchDirector': (7, 'Научный руководитель'),
    'JobQuartermaster': (7, 'Квартирмейстер'),
    'JobBlueShield': (7, 'Офицер "Синий щит"'),

    'JobAtmosphericTechnician': (1, 'Атмосферный техник'),
    'JobStationEngineer': (1, 'Инженер'),
    'JobTechnicalAssistant': (1, 'Технический ассистент'),

    'JobChemist': (2, 'Химик'),
    'JobMedicalDoctor': (2, 'Врач'),
    'JobMedicalIntern': (2, 'Интерн'),
    'JobPsychologist': (2, 'Психолог'),
    'JobParamedic': (2, 'Парамедик'),
    'JobPathologist': (2, 'Патологоанатом'),
    'JobSeniorPhysician': (2, 'Ведущий врач'),

    'JobSecurityCadet': (3, 'Кадет СБ'),
    'JobSecurityOfficer': (3, 'Офицер СБ'),
    'JobDetective': (3, 'Детектив'),
    'JobWarden': (3, 'Смотритель'),
    'JobBrigmedic': (3, 'Бригмедик'),
    'JobPrisoner': (3, 'Заключенный'),
    'JobSeniorOfficer': (3, 'Инструктор СБ'),
    'JobOverseer': (3, 'Надзиратель'),

    'JobScientist': (5, 'Учёный'),
    'JobResearchAssistant': (5, 'Научный ассистент'),
    'JobSeniorResearcher': (5, 'Ведущий учёный'),

    'JobBorgSecurity': (6, 'Борг СБ'),
    'JobBorgMedical': (6, 'Медицинский борг'),
    'JobBorgEngineer': (6, 'Инженерный борг'),
    'JobBorgJunitor': (6, 'Уборочный борг'),
    'JobBorgMining': (6, 'Шахтёрский борг'),
    'JobBorg': (6, 'Борг'),

    'BPLAMED': (6, 'Медицинский дрон'),
    'BPLATech': (6, 'Технический дрон'),

    'JobCentralCommandOfficial': (8, 'Представитель ЦК'),
    'JobCentralCommandAssistant': (8, 'Ассистент ОЦК'),
    'JobCentralCommandCargo': (8, 'Грузчик ЦК'),
    'JobCentralCommandSecOfficer': (8, 'Приватный офицер ЦК'),
    'JobCentralCommandOperator': (8, 'Оператор ЦК'),
    'JobCentralCommandSecGavna': (8, 'Начальник безопасности ЦК'),

    'JobExplorer': (9, 'Исследователь'),
    'JobStudent': (9, 'Ученик'),
    'JobFreelancerGear': (9, 'Фрилансер'),
    'JobFugitive': (9, 'Беглец'),
    'JobERTEngineer': (9, 'Инженер ОБР'),
    'JobERTJanitor': (9, 'Уборщик ОБР'),
    'JobERTLeader': (9, 'Лидер ОБР'),
    'JobERTMedical': (9, 'Медик ОБР'),
    'JobERTSecurity': (9, 'Офицер безопасности ОБР')
}


def _get_job_group_and_name(tracker: str) -> tuple[int, str]:
    return _job_dict.get(tracker, (9, tracker))


async def get_formatted_grouped_trackers(user_id: UUID) -> tuple[str]:
    playtimes = await playtime.get_playtime(user_id)

    groups = ['', '', '', '', '', '', '', '', '', '', '']

    groups[10] = '**Общее время**: '
    for _playtime in playtimes:
        if _playtime['tracker'] == 'Overall':
            groups[10] = f'{get_formatted_timedelta(
                _playtime['time_spent'])}\n\n'
        else:
            name = _get_job_group_and_name(_playtime['tracker'])
            groups[name[0]] += (f'- **{name[1]}**: {
                                get_formatted_timedelta(_playtime['time_spent'])}\n')
    return groups


async def get_most_popular_role(user_id: UUID) -> str:
    return _get_job_group_and_name((await playtime.get_most_popular_tracker(user_id))['tracker'])[1]
