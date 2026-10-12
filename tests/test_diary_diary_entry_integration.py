from lib.diary import *
from lib.diary_entry import *

# check that the diary can store entries and return them
def test_add_entry_and_retrieve_all():
    diary = Diary()
    entry_1 = DiaryEntry("Monday", "Walked the dog")
    entry_2 = DiaryEntry("Tuesday", "Cleaned the car")

    diary.add(entry_1)
    diary.add(entry_2)

    assert diary.all() == [entry_1, entry_2]

# diary.count_words should use the count_words from diary_entry

def test_count_words_in_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Monday", "Walked the dog")
    entry_2 = DiaryEntry("Tuesday", "Cleaned the car")
    
    diary.add(entry_1)
    diary.add(entry_2)
    
    assert diary.count_words() == 6