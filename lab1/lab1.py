from owlready2 import *
onto = get_ontology("file://C:/Users/arine/OneDrive/Документы/3курс2сем/МДК 06.04/musictrack").load()
print("Система рекомендации музыкального трека")
user_input1 = input("Тип исполнителя (Performer, Band): ").strip()
user_input2 = input("Жанр трека (Hip-hop, Pop, Rock): ").strip()
user_input3 = int(input("Период выпуска трека (1960, 2000, 2010): ").strip())
print("Результаты рекомендации:")
found = False
for track in onto.MusicTrack.instances():
    try:
        performer_type = track.PerformerOrBand[0]
        genre = track.Genre[0]
        year = track.Year[0]
        if (
            performer_type.lower() == user_input1.lower()
            and genre.lower() == user_input2.lower()
            and year == user_input3
        ):
            print(f"{track.name.replace('_', ' ')}")
            found = True
    except IndexError:
        pass
if not found:
    print("Подходящих треков не найдено.")

