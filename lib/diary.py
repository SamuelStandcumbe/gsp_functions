import math
class DiaryEntry():

    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.read_offset = 0 #tracker for reading_chunks

    def format(self):
        formatted_entry = f"{self.title}: {self.contents}"
        return formatted_entry

    def count_words(self):
        if not self.contents.strip():
            return 0
        return len(self.contents.split())

    def reading_time(self, wpm):
        if wpm <= 0:
            raise ValueError("WPM must be greater than 0.")
        word_count = self.count_words()
        return math.ceil(word_count / wpm)

    def reading_chunk(self, wpm, minutes):
        #how many words we can read
        words_to_read = wpm * minutes
        words = self.contents.split()

        #if already read, restart
        if self.read_offset >= len(words):
            self.read_offset = 0

        #chunk of words for this session
        start = self.read_offset
        end = start + words_to_read
        chunk_words = words[start:end]

        #update for next call
        self.read_offset = end
        return " ".join(chunk_words)