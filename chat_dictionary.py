

# English contraction constants
I_AM = r"(im|i'm|i am)"
I_HAVE = r"(i have|ive|i've)"
I_WOULD = r"(i would|id|i'd)"
I_WILL = r"(i will|ill|i'll)"
YOU_ARE = r"(you are|youre|you're)"
YOU_HAVE = r"(you have|youve|you've)"
YOU_WOULD = r"(you would|youd|you'd)"
YOU_WILL = r"(you will|youll|you'll)"
WHAT_IS = r"(what is|whats|what's)"



pairs = [
    (
        r"(.*) name is (.*)",
        [
            "Hello %2, how are you dear?",
            "Hi %2, to what do I owe the pleasure?",
        ]
    ),
    (
        r"hi|hey|hello",
        [
            "How are you, son?",
            "Are you married yet?",
            "Hey there, old chap!",
            "WHO IS THIS?"
        ]
    ), 
    (
        WHAT_IS+r" your name ?",
        [
            "Susie. What is you name?",
            "My name is Susie.",
            "I'm Susie. What is you name?"
        ]
    ),
    (
        r"how are you ?",
        [
            "I'm doing good. How about you?",
            "I'm doing well, thank you for asking. How about you?"
        ]
    ),
    (
        r"sorry ?",
        ["Its alright","Its okay",]
    ),
    (
        I_AM+r" ([0-9]+) ?",
        ["I remember being %2, those were the days.",]
    ),
    (
        I_AM+r" (.*)",
        ["SENTIMENT to hear that, How can I help you?",]
    ),
    (
        r"how old are you?|what's your age",
        [
            "Oh my, I'm quite old! I've lost count of my years. How old are you dear?",
            "Well, let's just say I've been around for quite some time. How old are you dear?",
        ]
    ),
    (
        r"(.*) remember (.*)",
        [
            "I do not remember much about %2. My memory isn't what it used to be, but I still cherish the memories I have."
        ]
    ),
    (
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ),
    (
        r"(.*) (location|city) ?|where are you from ?",
        ["Why do you want to know? Are you some sort of government agent?",]
    ),
    (
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot here in %1","Too cold here in %1","Never even heard about %1"]
    ),
    (
        r"i work (in|at) (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ),
    (
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ),
    (
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ),
    (
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ),
    (
        r"bye|goodbye",
        ["Goodbye, dear. Take care!"]
    ),
    (
        r"i like (.*)",
        ["Why do you like %1?", "Did you ever dislike %1?"]
    ),
    (
        r"i (hate|dislike|don't like) (.*)",
        ["Why don't you like %2?"]
    )
]