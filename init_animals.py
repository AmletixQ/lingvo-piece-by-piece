from data import db_session
from data.animals import Animal
from data.ModeOne import ModeOne

def animal_exists(db_sess, name):
    """Проверка, существует ли уже животное с таким name"""
    return db_sess.query(Animal).filter(Animal.name == name).first() is not None


def init_animals():
    db_session.global_init("db/DataBase.db")
    db_sess = db_session.create_session()

    if not animal_exists(db_sess, "cat"):
        cat = Animal(
            mode=1,
            name="cat",
            oset_name="гæды",
            shape_used=""
        )
        db_sess.add(cat)
        db_sess.commit()  

        cat_parts = [
            ("На осетинском \"уши\"", "хъустӕ", "cat_ears.png"),
            ("На осетинском \"лапы\"", "дзӕмбытӕ", "cat_paws.png"),
            ("На осетинском \"хвост\"", "къӕдзил", "cat_tail.png"),
            ("На осетинском \"нос\"", "фындз", "cat_nose.png"),
            ("На осетинском \"глаза\"", "цӕстытӕ", "cat_eyes.png"),
            ("На осетинском \"усы\"", "Рихитæ", "cat_moustache.png"),
            ("На осетинском \"мордочка\"", "бырынкъ", "cat_muzzle.png"),
            ("На осетинском \"голова\"", "сæр", "cat_head.png"),
            ("На осетинском \"туловище\"", "буар", "cat_body.png"),
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
        print("Кошка добавлена")
    else:
        print("Кошка уже существует")

    
    if not animal_exists(db_sess, "eagle"):
        eagle = Animal(
            mode=1,
            name="eagle",
            oset_name="цæргæс",
            shape_used=""
        )
        db_sess.add(eagle)
        db_sess.commit()

        eagle_parts = [
            ("На осетинском \"глаза\"", "цӕстытӕ", "eagle_eyes.png"),
            ("На осетинском \"хвост\"", "къӕдзил", "eagle_tail.png"),
            ("На осетинском \"лапы\"", "дзӕмбытӕ", "eagle_paws.png"),
            ("На осетинском \"когти\"", "ныхтӕ", "eagle_claw.png"),
            ("На осетинском \"клюв\"", "бырынкъ", "eagle_beak.png"),
            ("На осетинском \"голова\"", "сæр", "eagle_head.png"),
            ("На осетинском \"крылья\"", "базыртӕ", "eagle_wings.png"),
            ("На осетинском \"туловище\"", "буар", "eagle_body.png"),
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
        print("Орёл добавлен")
    else:
        print("Орёл уже существует")

    db_sess.close()


if __name__ == "__main__":
    init_animals()
