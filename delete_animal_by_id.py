from data import db_session
from data.animals import Animal
from data.ModeOne import ModeOne

def delete_animal_by_id(animal_id):
    db_session.global_init("db/DataBase.db")
    db_sess = db_session.create_session()

    animal = db_sess.query(Animal).filter(Animal.id == animal_id).first()

    if not animal:
        print(f"Животное с id={animal_id} не найдено")
        return

    # удаляем части
    parts = db_sess.query(ModeOne).filter(ModeOne.id_animal == animal.id).all()
    for p in parts:
        db_sess.delete(p)

    # удаляем животное
    db_sess.delete(animal)
    db_sess.commit()

    print(f"Животное id={animal_id} ({animal.name}) удалено")

    db_sess.close()


if __name__ == "__main__":
    delete_animal_by_id(6)   # ← УДАЛЯЕМ ВТОРУЮ КОШКУ

