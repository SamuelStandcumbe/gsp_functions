from lib.reminder import *
import pytest

def test_name_and_task_reminds_task():
    reminder = Reminder("Steve")
    reminder.remind_me_to("Clean")
    assert reminder.remind() == "Clean, Steve!"

def test_name_no_task():
    reminder = Reminder("Steve")
    with pytest.raises(Exception) as e:
        reminder.remind()
    error_message = str(e.value)
    assert error_message == "No task set"

def test_name_empty_task():
    reminder = Reminder("Steve")
    reminder.remind_me_to("")
    assert reminder.remind() == ", Steve!"

    