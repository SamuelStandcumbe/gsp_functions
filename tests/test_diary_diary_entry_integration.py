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

# test if reading_time calculates total reading time for all entries. 10 words, with a 5wpm reading speed

def test_reading_time_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry("One", "One Two Three Four Five")
    entry_2 = DiaryEntry("Two", "Six Seven Eight Nine Ten")

    diary.add(entry_1)
    diary.add(entry_2)

    assert diary.reading_time(5) == 2

# test if the diary can select an entry based on reading speed and available time.


# test what happens when there is no entry you can read

# test what happens if the diary is empty