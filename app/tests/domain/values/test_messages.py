from datetime import datetime
from uuid import uuid4

import pytest
from faker import Faker

from domain.entities.messages import Message, Chat
from domain.events.messages import NewMessageReceivedEvent
from domain.exceptions.message import TitleTooLongException
from domain.values.messages import Text, Title

fake = Faker()


@pytest.mark.parametrize("text", [
    fake.pystr(min_chars=50, max_chars=100),
    fake.pystr(min_chars=500, max_chars=600),
])
def test_create_message(text: str) -> None:
    text = Text(text)
    message = Message(text=text, chat_oid=str(uuid4()))

    assert message.text == text
    assert message.created_at.date() == datetime.today().date()


@pytest.mark.parametrize("title", [
    fake.pystr(min_chars=50, max_chars=100),
    fake.pystr(min_chars=255, max_chars=255),
])
def test_create_chat_success(title: str) -> None:
    title = Title(title)
    chat = Chat(title)

    assert chat.title == title
    assert not chat.messages
    assert chat.created_at.date() == datetime.today().date()


@pytest.mark.parametrize("title", [
    fake.pystr(min_chars=256, max_chars=256),
    fake.pystr(min_chars=500, max_chars=600),
])
def test_create_chat_title_too_long(title: str) -> None:
    with pytest.raises(TitleTooLongException):
        Title(title)


@pytest.mark.parametrize("text,title", [
    (fake.pystr(), fake.pystr(max_chars=255)),
])
def test_add_message_to_chat(text: str, title: str) -> None:
    text = Text(text)
    message = Message(text=text, chat_oid=str(uuid4()))

    title = Title(title)
    chat = Chat(title)

    chat.add_message(message)

    assert message in chat.messages


@pytest.mark.parametrize("text,title", [
    (fake.pystr(), fake.pystr(max_chars=255)),
])
def test_new_message_events(text: str, title: str) -> None:
    text = Text(text)
    message = Message(text=text, chat_oid=str(uuid4()))

    title = Title(title)
    chat = Chat(title)

    chat.add_message(message)
    events = chat.pull_events()
    pulled_events = chat.pull_events()

    assert not pulled_events, pulled_events
    assert len(events) == 1, events

    new_event = events[0]

    assert isinstance(new_event, NewMessageReceivedEvent), new_event
    assert new_event.message_oid == message.oid
    assert new_event.message_text == message.text.as_generic_type()
    assert new_event.chat_oid == chat.oid
    