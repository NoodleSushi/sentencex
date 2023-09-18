import re

from sentencex.base import Language


class Finnish(Language):
    language = "fi"
    MONTHS = {
        "tammikuu",
        "helmikuu",
        "maaliskuu",
        "huhtikuu",
        "toukokuu",
        "kesäkuu",
        "heinäkuu",
        "elokuu",
        "syyskuu",
        "lokakuu",
        "marraskuu",
        "joulukuu",
    }

    abbreviations = {
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
        "Å",
        "Ä",
        "Ö",
        # List of titles.
        # These are often followed by upper-case names, but do not indicate sentence breaks
        "alik",
        "alil",
        "amir",
        "apul",
        "apul.prof",
        "arkkit",
        "ass",
        "assist",
        "dipl",
        "dipl.arkkit",
        "dipl.ekon",
        "dipl.ins",
        "dipl.kielenk",
        "dipl.kirjeenv",
        "dipl.kosm",
        "dipl.urk",
        "dos",
        "Dr",
        "erikoiseläinl",
        "erikoishammasl",
        "erikoisl",
        "erikoist",
        "ev.luutn",
        "evp",
        "fil",
        "ft",
        "hallinton",
        "hallintot",
        "hammaslääket",
        "jatk",
        "jääk",
        "kansaned",
        "kapt",
        "kapt.luutn",
        "kenr",
        "kenr.luutn",
        "kenr.maj",
        "kers",
        "kirjeenv",
        "kom",
        "kom.kapt",
        "komm",
        "konst",
        "korpr",
        "luutn",
        "maist",
        "maj",
        "Mr",
        "Mrs",
        "Ms",
        "M.Sc",
        "neuv",
        "nimim",
        "Ph.D",
        "prof",
        "puh.joht",
        "pääll",
        "res",
        "san",
        "siht",
        "suom",
        "sähköp",
        "säv",
        "toht",
        "toim",
        "toim.apul",
        "toim.joht",
        "toim.siht",
        "tuom",
        "ups",
        "vänr",
        "vääp",
        "ye.ups",
        "ylik",
        "ylil",
        "ylim",
        "ylimatr",
        "yliop",
        "yliopp",
        "ylip",
        "yliv",
        # misc - odd period-ending items that NEVER indicate breaks (p.m. does NOT fall
        # into this category - it sometimes ends a sentence)
        "e.g",
        "ent",
        "esim",
        "huom",
        "i.e",
        "ilm",
        "l",
        "mm",
        "myöh",
        "nk",
        "nyk",
        "par",
        "po",
        "t",
        "v",
    }

    def continue_in_next_word(self, text_after_boundary) -> bool:
        if re.match(r"^\W*[0-9a-z]", text_after_boundary):
            return True
        next_word = text_after_boundary.strip().split(" ")[0]

        if len(next_word) == 0:
            return False
        if next_word in self.MONTHS or (next_word[0].upper() + next_word[1:] in self.MONTHS):
            return True
        return False
