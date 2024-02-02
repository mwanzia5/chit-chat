from app import app

from models import db,Message, Status


messages = [
  {
    "media": "",
    "message": "Hi there. Am a new student",
    "receiver_id": 2,
    "sender_id": 1
  },
  {
    "media": "",
    "message": "Hi there. Welcome to Moringa",
    "receiver_id": 1,
    "sender_id": 2
  },
  {
    "media": "",
    "message": "Thank you",
    "receiver_id": 2,
    "sender_id": 1
  },
  {
    "media": "",
    "message": "I hope you have everything set up and ready",
    "receiver_id": 1,
    "sender_id": 2
  },
  {
    "media": "",
    "message": "Yes. Thank you",
    "receiver_id": 2,
    "sender_id": 1
  },
  {
    "media": "",
    "message": "We can learn from everything",
    "receiver_id": 4,
    "sender_id": 3
  },
  {
    "media": "",
    "message": "That's true. We sure can!",
    "receiver_id": 3,
    "sender_id": 4
  },
  {
    "media": "",
    "message": "Hi",
    "receiver_id": 3,
    "sender_id": 1
  },
  {
    "media": "",
    "message": "Where can I find the career office ?",
    "receiver_id": 3,
    "sender_id": 1
  },
  {
    "media": "",
    "message": "Hallo. It's next to the auditorium ",
    "receiver_id": 1,
    "sender_id": 3
  },
  {
    "media": "",
    "message": "Thanks ",
    "receiver_id": 3,
    "sender_id": 1
  },
  {
    "media": "",
    "message": "Good morning",
    "receiver_id": 2,
    "sender_id": 1
  },
  {
    "media": "",
    "message": "Good morning Mr. Odinga.",
    "receiver_id": 1,
    "sender_id": 2
  },
  {
    "media": "",
    "message": "Good morning Mr. Odinga.",
    "receiver_id": 1,
    "sender_id": 2
  },
  {
    "media": "",
    "message": "Hi Dad",
    "receiver_id": 3,
    "sender_id": 2,
  },
  {
    "media": "",
    "message": "How have you been ?",
    "receiver_id": 3,
    "sender_id": 2
  },
  {
    "media": "",
    "message": "Am settled in school now",
    "receiver_id": 3,
    "sender_id": 2
  },
  {
    "media": "",
    "message": "Hi",
    "receiver_id": 2,
    "sender_id": 3
  },
  {
    "media": "",
    "message": "Glad to hear that",
    "receiver_id": 2,
    "sender_id": 3
  },
  {
    "media": "",
    "message": "Did you attend the orientation last week?",
    "receiver_id": 3,
    "sender_id": 1
  }
]


with app.app_context():
    db.session.add_all([Message(**message) for message in messages])
    db.session.commit()

statuses = [
  {
    "photo_url": "",
    "status_text": "To new beginnings",
    "user_id": 1
  },
  {
    "photo_url": "",
    "status_text": "So help me God ...",
    "user_id": 3
  },
  {
    "photo_url": "",
    "status_text": "We can learn from everything",
    "user_id": 2
  },
  {
    "photo_url": "",
    "status_text": "Hope is a cure",
    "user_id": 4
  },
  {
    "photo_url": "",
    "status_text": "First step in a long journey",
    "user_id": 3
  },
  {
    "photo_url": "",
    "status_text": "Tough times",
    "user_id": 1
  }
]


with app.app_context():
    db.session.add_all([Status(**status) for status in statuses])
    db.session.commit()
