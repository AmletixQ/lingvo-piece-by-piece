from data import db_session
from data.animals import Animal

db_session.global_init("db/DataBase.db")
db_sess = db_session.create_session()

animals = db_sess.query(Animal).all()

print("Животные в базе:")
for a in animals:
    print(f"id={a.id}, name={a.name}, oset_name={a.oset_name}, mode={a.mode}")

db_sess.close()
