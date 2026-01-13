from data import db_session
from data.animals import Animal
from data.ModeOne import ModeOne

def init_animals():
    db_session.global_init("db/DataBase.db")
    db_sess = db_session.create_session()

    cat = Animal(
        mode=1,
        name="cat",
        oset_name="гæды",
        shape_used=""
    )
    db_sess.add(cat)
    db_sess.commit()  

    cat_parts = [

        ("Голова кошки", "голова", "cat_head.png"),
        ("Туловище кошки", "туловище", "cat_body.png"),
        ("Лапы кошки", "лапы", "cat_legs.png"),
        ("Хвост кошки", "хвост", "cat_tail.png"),
    ]

    for task, answer, png in cat_parts:
        db_sess.add(
            ModeOne(
                id_animal=cat.id,
                tasks=task,
                answers=answer,
                png=png
            )
        )

    db_sess.commit()


    eagle = Animal(
        mode=1,
        name="eagle",
        oset_name="цæргæс",
        shape_used=""
    )
    db_sess.add(eagle)
    db_sess.commit()

    eagle_parts = [
        ("Голова орла", "голова", "eagle_head.png"),
        ("Туловище орла", "туловище", "eagle_body.png"),
        ("Крылья орла", "крылья", "eagle_wings.png"),
        ("Лапы орла", "лапы", "eagle_legs.png"),
    ]

    for task, answer, png in eagle_parts:
        db_sess.add(
            ModeOne(
                id_animal=eagle.id,
                tasks=task,
                answers=answer,
                png=png
            )
        )

    db_sess.commit()
    print("✅ Орёл добавлен")

    db_sess.close()
    print("✅ Кошка добавлена")

if __name__ == "__main__":
    init_animals()

