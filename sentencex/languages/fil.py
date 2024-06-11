from sentencex.base import Language
from .en import English


class Filipino(Language):
    language = "fil"

    abbreviations = English.abbreviations.union(
        {
            # Days of the Week
            "ling",
            "lun",
            "mart",
            "miyer",
            "huweb",
            "biyer",
            "sab",

            # Months
            "ene",
            "peb",
            "mar",
            "abr",
            "may",
            "hun",
            "hul",
            "ago",
            "set",
            "okt",
            "nob",
            "dis",

            # Tagalog
            "ago",
            "atbp",
            "bb",
            "blg",
            "bo",
            "brgy",
            "dra",
            "gng",
            "gob",
            "hal"
            "hen",
            "hul",
            "hun",
            "kap",
            "kapt",
            "ma",
            "n.g",
            "n.h",
            "n.t",
            "n.u",
            "pam",
            "pang",
            "pob",
            "prop",
            "sta",
            "sto",

            # Cebuano
            "dga",
            "gn",
            "mlbn",
            "ubp",
            "ugbp",
        }
    )
