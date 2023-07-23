from modules.library_item import LibraryItem


class CD(LibraryItem):
    def __init__(self, title, upc, subject, artist):
        LibraryItem.__init__(self, title, upc, subject)
        self.artist = artist