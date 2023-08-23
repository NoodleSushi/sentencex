# ruff: noqa: E501
GOLDEN_EN_RULES = [
    # 1) Simple period to end sentence
    ("Hello World. My name is Jonas.", ["Hello World.", "My name is Jonas."]),
    # 2) Question mark to end sentence
    ("What is your name? My name is Jonas.", ["What is your name?", "My name is Jonas."]),
    # 3) Exclamation point to end sentence
    ("There it is! I found it.", ["There it is!", "I found it."]),
    # 4) One letter upper case abbreviations
    ("My name is Jonas E. Smith.", ["My name is Jonas E. Smith."]),
    # 5) One letter lower case abbreviations
    ("Please turn to p. 55.", ["Please turn to p. 55."]),
    # 6) Two letter lower case abbreviations in the middle of a sentence
    ("Were Jane and co. at the party?", ["Were Jane and co. at the party?"]),
    # 7) Two letter upper case abbreviations in the middle of a sentence
    (
        "They closed the deal with Pitt, Briggs & Co. at noon.",
        ["They closed the deal with Pitt, Briggs & Co. at noon."],
    ),
    # 8) Two letter lower case abbreviations at the end of a sentence
    ("Let's ask Jane and co. They should know.", ["Let's ask Jane and co.", "They should know."]),
    # 9) Two letter upper case abbreviations at the end of a sentence
    (
        "They closed the deal with Pitt, Briggs & Co. It closed yesterday.",
        ["They closed the deal with Pitt, Briggs & Co.", "It closed yesterday."],
    ),
    # 10) Two letter (prepositive) abbreviations
    ("I can see Mt. Fuji from here.", ["I can see Mt. Fuji from here."]),
    # 11) Two letter (prepositive & postpositive) abbreviations
    (
        "St. Michael's Church is on 5th st. near the light.",
        ["St. Michael's Church is on 5th st. near the light."],
    ),
    # 12) Possesive two letter abbreviations
    ("That is JFK Jr.'s book.", ["That is JFK Jr.'s book."]),
    # 13) Multi-period abbreviations in the middle of a sentence
    ("I visited the U.S.A. last year.", ["I visited the U.S.A. last year."]),
    # 14) Multi-period abbreviations at the end of a sentence
    (
        "I live in the E.U. How about you?",
        ["I live in the E.U.", "How about you?"],
    ),
    # 15) U.S. as sentence boundary
    (
        "I live in the U.S. How about you?",
        ["I live in the U.S.", "How about you?"],
    ),
    # 16) U.S. as non sentence boundary with next word capitalized
    (
        "I work for the U.S. Government in Virginia.",
        ["I work for the U.S. Government in Virginia."],
    ),
    # 17) U.S. as non sentence boundary
    ("I have lived in the U.S. for 20 years.", ["I have lived in the U.S. for 20 years."]),
    # Most difficult sentence to crack
    # 18) A.M. / P.M. as non sentence boundary and sentence boundary
    (
        "At 5 a.m. Mr. Smith went to the bank. He left the bank at 6 P.M. Mr. Smith then went to the store.",
        [
            "At 5 a.m. Mr. Smith went to the bank.",
            "He left the bank at 6 P.M.",
            "Mr. Smith then went to the store.",
        ],
    ),
    # 19) Number as non sentence boundary
    ("She has $100.00 in her bag.", ["She has $100.00 in her bag."]),
    # 20) Number as sentence boundary
    ("She has $100.00. It is in her bag.", ["She has $100.00.", "It is in her bag."]),
    # 21) Parenthetical inside sentence
    (
        "He teaches science (He previously worked for 5 years as an engineer.) at the local University.",
        [
            "He teaches science (He previously worked for 5 years as an engineer.) at the local University."
        ],
    ),
    # 22) Email addresses
    (
        "Her email is Jane.Doe@example.com. I sent her an email.",
        ["Her email is Jane.Doe@example.com.", "I sent her an email."],
    ),
    # 23) Web addresses
    (
        "The site is: https://www.example.50.com/new-site/awesome_content.html. Please check it out.",
        [
            "The site is: https://www.example.50.com/new-site/awesome_content.html.",
            "Please check it out.",
        ],
    ),
    # 24) Single quotations inside sentence
    (
        "She turned to him, 'This is great.' she said.",
        ["She turned to him, 'This is great.' she said."],
    ),
    # 25) Double quotations inside sentence
    (
        'She turned to him, "This is great." she said.',
        ['She turned to him, "This is great." she said.'],
    ),
    # 26) Double quotations at the end of a sentence
    (
        'She turned to him, "This is great." She held the book out to show him.',
        ['She turned to him, "This is great."', "She held the book out to show him."],
    ),
    # 27) Double punctuation (exclamation point)
    ("Hello!! Long time no see.", ["Hello!!", "Long time no see."]),
    # 28) Double punctuation (question mark)
    ("Hello?? Who is there?", ["Hello??", "Who is there?"]),
    # 29) Double punctuation (exclamation point / question mark)
    ("Hello!? Is that you?", ["Hello!?", "Is that you?"]),
    # 30) Double punctuation (question mark / exclamation point)
    ("Hello?! Is that you?", ["Hello?!", "Is that you?"]),
    # 31) List (period followed by parens and no period to end item)
    (
        "1.) The first item 2.) The second item",
        ["1.) The first item", "2.) The second item"],
    ),
    # 32) List (period followed by parens and period to end item)
    (
        "1.) The first item. 2.) The second item.",
        ["1.) The first item.", "2.) The second item."],
    ),
    # 33) List (parens and no period to end item)
    (
        "1) The first item 2) The second item",
        ["1) The first item", "2) The second item"],
    ),
    # 34) List (parens and period to end item)
    ("1) The first item. 2) The second item.", ["1) The first item.", "2) The second item."]),
    # 35) List (period to mark list and no period to end item)
    (
        "1. The first item 2. The second item",
        ["1. The first item", "2. The second item"],
    ),
    # 36) List (period to mark list and period to end item)
    (
        "1. The first item. 2. The second item.",
        ["1. The first item.", "2. The second item."],
    ),
    # 37) List with bullet
    (
        "• 9. The first item • 10. The second item",
        ["• 9. The first item", "• 10. The second item"],
    ),
    # 38) List with hypthen
    (
        "⁃9. The first item ⁃10. The second item",
        ["⁃9. The first item", "⁃10. The second item"],
    ),
    # 39) Alphabetical list
    (
        "a. The first item b. The second item c. The third list item",
        ["a. The first item", "b. The second item", "c. The third list item"],
    ),
    # 40) Geo Coordinates
    (
        "You can find it at N°. 1026.253.553. That is where the treasure is.",
        ["You can find it at N°. 1026.253.553.", "That is where the treasure is."],
    ),
    # 41) Named entities with an exclamation point
    (
        "She works at Yahoo! in the accounting department.",
        ["She works at Yahoo! in the accounting department."],
    ),
    # 42) I as a sentence boundary and I as an abbreviation
    (
        "We make a good team, you and I. Did you see Albert I. Jones yesterday?",
        ["We make a good team, you and I.", "Did you see Albert I. Jones yesterday?"],
    ),
    # 43) Ellipsis at end of quotation
    (
        "Thoreau argues that by simplifying one’s life, “the laws of the universe will appear less complex. . . .”",
        [
            "Thoreau argues that by simplifying one’s life, “the laws of the universe will appear less complex. . . .”"
        ],
    ),
    # 44) Ellipsis with square brackets
    (
        """"Bohr [...] used the analogy of parallel stairways [...]" (Smith 55).""",
        ['"Bohr [...] used the analogy of parallel stairways [...]" (Smith 55).'],
    ),
    # 45) Ellipsis as sentence boundary (standard ellipsis rules)
    (
        "If words are left off at the end of a sentence, and that is all that is omitted, indicate the omission with ellipsis marks (preceded and followed by a space) and then indicate the end of the sentence with a period . . . . Next sentence.",
        [
            "If words are left off at the end of a sentence, and that is all that is omitted, indicate the omission with ellipsis marks (preceded and followed by a space) and then indicate the end of the sentence with a period . . . .",
            "Next sentence.",
        ],
    ),
    # 46) Ellipsis as sentence boundary (non-standard ellipsis rules)
    (
        "I never meant that.... She left the store.",
        ["I never meant that....", "She left the store."],
    ),
    # 47) Ellipsis as non sentence boundary
    (
        "I wasn’t really ... well, what I mean...see . . . what I'm saying, the thing is . . . I didn’t mean it.",
        [
            "I wasn’t really ... well, what I mean...see . . . what I'm saying, the thing is . . . I didn’t mean it."
        ],
    ),
    # 48) 4-dot ellipsis
    (
        "One further habit which was somewhat weakened . . . was that of combining words into self-interpreting compounds. . . . The practice was not abandoned. . . .",
        [
            "One further habit which was somewhat weakened . . . was that of combining words into self-interpreting compounds.",
            ". . . The practice was not abandoned. . . .",
        ],
    ),
]
