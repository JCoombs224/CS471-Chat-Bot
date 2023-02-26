# # For reference might use a data structure like this later so that multiple inputs can represent
# # one input into the corpus
# pairs = [
#     # Greetings
#     (r"hi|hello|hey", ["greeting","hello"]),
#     (r"how are you|how you doing|how's it going", ["greeting","how doing"]),
#     (r"fine|good", ["That's great to hear."]),
#     (r"not (good|well|fine)", ["Oh, I'm sorry to hear that. Is there anything I can do to help?"]),
    
#     # Age-related topics
#     (r"how old are you", ["Oh my, I'm quite old! I've lost count of my years."]),
#     (r"what's your age", ["Well, let's just say I've been around for quite some time."]),
#     (r"grandchild|grandchildren", ["Yes, I have many grandchildren. They bring me so much joy."]),
#     (r"memory|remember", ["My memory isn't what it used to be, but I still cherish the memories I have."]),
    
#     # Farewells
#     (r"bye|goodbye", ["Goodbye, dear. Take care!"]),
#     (r"thank you", ["You're welcome, dear. Anytime."]),
#     (r"thanks", ["You're welcome, dear. Take care!"])
# ]

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        [
            "How are you, son?",
            "Are you married yet?",
            "Hey there, old chap!",
            "WHO IS THIS?"
        ]
    ], 
    [
        r"what is your name ?",
        ["I am a bot created by Analytics Vidhya. you can call me crazy!",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "How can I help you?:)",]
    ],
    [
        r"how old are you?",
        ["Oh my, I'm quite old! I've lost count of my years. How old are you dear?",]
    ],
    [
        r"i am (.*) years old",
        ["I remember being %1, those were the days",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["Raghav created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Indore, Madhya Pradesh',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["Crazy_Tech has many great articles with each step explanation along with code, you can explore"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye, dear. Take care!"]
    ],
]