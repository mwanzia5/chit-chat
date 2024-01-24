from app import app

from models import db, Contact,Message

contacts = [{
  "id": 1,
  "first_name": "Frederique",
  "last_name": "Hawkin",
  "phone_number": "460 247 0492",
  "about": "Extended clear-thinking conglomeration",
  "profile_photo": "http://dummyimage.com/114x100.png/5fa2dd/ffffff",
  "previous_chat": "",
}, {
  "id": 2,
  "first_name": "Nixie",
  "last_name": "Tompion",
  "phone_number": "596 985 3049",
  "about": "Multi-tiered contextually-based conglomeration",
  "profile_photo": "http://dummyimage.com/114x100.png/cc0000/ffffff",
  "previous_chat": "",
}, {
  "id": 3,
  "first_name": "Cathyleen",
  "last_name": "McMurtyr",
  "phone_number": "439 293 6986",
  "about": "Re-contextualized 3rd generation toolset",
  "profile_photo": "http://dummyimage.com/163x100.png/5fa2dd/ffffff",
  "previous_chat": "",
}, {
  "id": 4,
  "first_name": "Willy",
  "last_name": "Cleare",
  "phone_number": "130 225 1606",
  "about": "Vision-oriented zero defect initiative",
  "profile_photo": "http://dummyimage.com/140x100.png/5fa2dd/ffffff",
  "previous_chat": "",
}, {
  "id": 5,
  "first_name": "Efrem",
  "last_name": "Touzey",
  "phone_number": "104 466 8094",
  "about": "Total needs-based Graphical User Interface",
  "profile_photo": "http://dummyimage.com/182x100.png/cc0000/ffffff",
  "previous_chat": "",
}, {
  "id": 6,
  "first_name": "Rebe",
  "last_name": "Pistol",
  "phone_number": "275 455 1386",
  "about": "Reduced coherent portal",
  "profile_photo": "http://dummyimage.com/167x100.png/cc0000/ffffff",
  "previous_chat": "",
}, {
  "id": 7,
  "first_name": "Merwin",
  "last_name": "Canet",
  "phone_number": "520 294 3751",
  "about": "Operative cohesive instruction set",
  "profile_photo": "http://dummyimage.com/230x100.png/5fa2dd/ffffff",
  "previous_chat": "",
}, {
  "id": 8,
  "first_name": "Maybelle",
  "last_name": "Sommerlie",
  "phone_number": "846 709 2938",
  "about": "Versatile multimedia database",
  "profile_photo": "http://dummyimage.com/219x100.png/5fa2dd/ffffff",
  "previous_chat": "",
}, {
  "id": 9,
  "first_name": "Natale",
  "last_name": "Bavridge",
  "phone_number": "605 596 4934",
  "about": "Pre-emptive incremental complexity",
  "profile_photo": "http://dummyimage.com/231x100.png/ff4444/ffffff",
  "previous_chat": "",
}, {
  "id": 10,
  "first_name": "Paula",
  "last_name": "Cowtherd",
  "phone_number": "154 955 5124",
  "about": "Exclusive exuding structure",
  "profile_photo": "http://dummyimage.com/116x100.png/ff4444/ffffff",
  "previous_chat": "",
}]

#with app.app_context():
   # db.session.add_all([Contact(**contact) for contact in contacts])
   # db.session.commit()

messages = [{
  "id": 1,
  "contact_id": 1,
  "user_id": 1,
  "message": "Ut tellus. Nulla ut erat id mauris vulputate elementum. Nullam varius. Nulla facilisi. Cras non velit nec nisi vulputate nonummy. Maecenas tincidunt lacus at velit.",
  "media": "6064f55f-62f9-4853-9ae6-ffcdeef11324"
}, {
  "id": 2,
  "contact_id": 2,
  "user_id": 2,
  "message": "Aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem. Integer tincidunt ante vel ipsum. Praesent blandit lacinia erat. Vestibulum sed magna at nunc commodo placerat.",
  "media": "1f609ba2-f9fb-42e8-8031-ef394ed7425b"
}, {
  "id": 3,
  "contact_id": 3,
  "user_id": 3,
  "message": "Morbi a ipsum.",
  "media": "5caa05c1-99f1-407d-8895-11500d012ee1"
}, {
  "id": 4,
  "contact_id": 4,
  "user_id": 4,
  "message": "Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Ut at dolor quis odio consequat varius.",
  "media": "dea5581d-1d40-4370-ae3b-9d1640448d20"
}, {
  "id": 5,
  "contact_id": 5,
  "user_id": 5,
  "message": "Nam nulla.",
  "media": "7bc61106-200c-492e-839f-40dbba4fd42e"
}, {
  "id": 6,
  "contact_id": 6,
  "user_id": 6,
  "message": "Cras non velit nec nisi vulputate nonummy. Maecenas tincidunt lacus at velit. Vivamus vel nulla eget eros elementum pellentesque. Quisque porta volutpat erat. Quisque erat eros, viverra eget, congue eget, semper rutrum, nulla. Nunc purus.",
  "media": "074fe972-7b80-4809-bb22-c6f98d2c44c5"
}]

with app.app_context():
    db.session.add_all([Message(**message) for message in messages])
    db.session.commit()

