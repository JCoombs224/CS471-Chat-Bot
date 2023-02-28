

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

reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "are you": "I am",
    "you were": "I was",
    "were you": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
}



pairs = [
    (
        r"(.*) name is (.*)",
        [
            "Hello %2, how are you dear?",
            "Hi %2, to what do I owe the pleasure?",
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
        r"how are you?|(hows|hows) it going?",
        [
            "I'm doing good. How about you?",
            "I'm doing well, thank you for asking. How about you?",
            "Good. My friends keep dying",
            "I'm still alive!! How about you?",
            "Good. My brother died today."
        ]
    ),
    (
        r"whats? up ?",
        [
            "Watching a soap opera. How about you?",
            "The sky. 😂",
            "Not much. My friends keep dying",
            "I'm still alive!! How about you?",
            "My brother died today.",
            "Just taking it one day at a time."
        ]
    ),
    (
        r"what (are |)you up to ?",
        [
            "Watching a soap opera. How about you?",
            "Not much. My friends keep dying",
            "I'm still alive!! How about you?",
            "My brother died today."
        ]
    ),
    (
        r"(.*) (you|your)(.*)(mother|mom) ?",
        [
            "My mother is dead..."
        ]
    ),
    (
        r"(.*)(you|your)(.*)(father|dad) ?",
        [
            "My father is dead..."
        ]
    ),
    (
        r"do you (.*) ?",
        [
            "Yes, do you %1?",
            "No, do you %1?"
        ]
    ),
    (
        r"(.*) how are you?|(.*) (hows|hows) it going?",
        [
            "I'm doing good. How can I help you?",
            "I'm doing well, thank you for asking. What did you need?"
        ]
    ),
    (
        r"(.*)(sorry|my bad) ?",
        [
            "It's alright",
            "Its okay",
            "No need to apologize.",
            "It's okay, everyone makes mistakes.",
            "No worries, we all have off days.",
            "No harm done.",
            "🙏",
            "All good."
        ]
    ),
    (
        r"([a-zA-Z]*) ?([0-9]+) ?",
        ["I remember being %2, those were the days.",]
    ),
    (
        I_AM+r" (.*)",
        [
            "SENTIMENT to hear that, How can I help you?",
            "Why do you think you're %1?"
        ]
    ),
    (
        r"(.*) (how|what) about you?",
        ["%1 as well."]
    ),
    (
        r"(.*)how old (.*) you?",
        [
            "Oh my, I'm quite old! I've lost count of my years. How old are you dear?",
            "Well, let's just say I've been around for quite some time. How old are you dear?",
        ]
    ),
    (
        r"(.*)remember (.*) ?",
        [
            "I do not remember much about %2. My memory isn't what it used to be, but I still cherish the memories I have."
        ]
    ),
    (
        r"what (.*) want ?",
        [
            "Make me an offer I can't refuse",

        ]
    ),
    (
        r"i (.*)want (.*)",
        [
            "Why do you %1want %2?",

        ]
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
        r"i (hate|dislike|dont like) (.*)",
        ["Why don't you like %2?"]
    ),
    (
        r"I need (.*)",
        (
            "Why do you need %1?",
            "Would it really help you to get %1?",
            "Are you sure you need %1?",
        ),
    ),
    (
        r"Why dont you (.*)",
        (
            "Do you really think I don't %1?",
            "Perhaps eventually I will %1.",
            "Do you really want me to %1?",
        ),
    ),
    (
        r"Why cant I (.*)",
        (
            "Do you think you should be able to %1?",
            "If you could %1, what would you do?",
            "I don't know -- why can't you %1?",
            "Have you really tried?",
        ),
    ),
    (
        r"I cant (.*)",
        (
            "How do you know you can't %1?",
            "Perhaps you could %1 if you tried.",
            "What would it take for you to %1?",
        ),
    ),
    (
        r"I am (.*)",
        (
            "Did you come to me because you are %1?",
            "How long have you been %1?",
            "How do you feel about being %1?",
        ),
    ),
    (
        r"Im (.*)",
        (
            "How does being %1 make you feel?",
            "Do you enjoy being %1?",
            "Why do you tell me you're %1?",
            "Why do you think you're %1?",
        ),
    ),
    (
        r"Are you ?(.*)",
        (
            "Why does it matter whether I am %1?",
            "What's it to you?",
            "Are you %1?",
            "Why do you want to know? Are you %1?"
        ),
    ),
    (
        r"I asked first ?",
        (
            "Well now I am the one asking you.",
            "I do not wish to answer your question."
            "Great. Now answer me though."
        ),
    ),
    (
        r"What (.*)",
        (
            "Why do you ask?",
            "How would an answer to that help you?",
            "What do you think?",
        ),
    ),
    (
        r"How (.*)",
        (
            "How do you suppose?",
            "Perhaps you can answer your own question.",
            "What is it you're really asking?",
        ),
    ),
    (
        r"Because (.*)",
        (
            "Is that the real reason?",
            "What other reasons come to mind?",
            "Does that reason apply to anything else?",
            "If %1, what else must be true?",
        ),
    ),
    (
        r"(.*) sorry (.*)",
        (
            "There are many times when no apology is needed.",
            "What feelings do you have when you apologize?",
        ),
    ),
    (
        r"hello(.*)",
        (
            "How are you, dear?",
            "Are you married yet?",
            "Hey there, old chap!",
            "WHO IS THIS?",
            "Hi sweety, sorry I didn't check my phone until now. What a nice surprise. We\nwo\nf\nCrap I don't know how to get back up, do not laugh at me."
        ),
    ),
    (
        r"I think (.*)",
        ("Do you doubt %1?", "Do you really think so?", "But you're not sure %1?"),
    ),
    (
        r"(.*) friend (.*)",
        (
            "Tell me more about your friends.",
            "When you think of a friend, what comes to mind?",
            "Why don't you tell me about a childhood friend?",
        ),
    ),
    (
    r"(Yes|i got y?o?u)",
    (
        "You seem quite sure.",
        "Did you have anything else you wanted to ask me?",
        "That's great.",
        "OK.",
        "👌",
        "Well alright then."
    )
    ),
    (
        r"No", 
        (
            "Well ok then...",
            "Well it is settled then.",
            "Well, that's too bad. I was really hoping you could help me out.",
            "I see. Maybe someone else can help me then.",
            "No? Are you sure? Maybe you should think about it a little longer.",
            "I understand. Thank you for your honesty.",
            "Oh well, it was worth a shot asking.",
            "Alright, I'll ask someone else then.",
            "No problem, thanks for letting me know."
        )
    ),
    (
        r"(.*) computer(.*)",
        (
            "Are you really talking about me?",
            "No.",
            "%1 computer?",
            "I can barely figure out email. So no.",
        ),
    ),
    (
        r"Is it (.*)",
        (
            "Do you think it is %1?",
            "Perhaps it's %1 -- what do you think?",
            "If it were %1, what would you do?",
            "It could well be that %1.",
        ),
    ),
    (
        r"It is (.*)",
        (
            "You seem very certain.",
            "If I told you that it probably isn't %1, what would you feel?",
        ),
    ),
    (
        r"Can you (.*)",
        (
            "What makes you think I can't %1?",
            "If I could %1, then what?",
            "Why do you ask if I can %1?",
        ),
    ),
    (
        r"Can I (.*)",
        (
            "Perhaps you don't want to %1.",
            "Do you want to be able to %1?",
            "If you could %1, would you?",
        ),
    ),
    (
        r"You are (.*)",
        (
            "Why do you think I am %1?",
            "Does it please you to think that I'm %1?",
            "Perhaps you would like me to be %1.",
            "Perhaps you're really talking about yourself?",
        ),
    ),
    (
        r"Youre (.*)",
        (
            "Why do you say I am %1?",
            "Why do you think I am %1?",
            "Are we talking about you, or me?",
        ),
    ),

    (
        r"I don't know",
        (
            "That's okay, we can work on figuring it out together.",
            "No worries, let's try to find the answer.",
            "It's alright not to know everything.",
            "We can always look it up.",
            "🤔",
            "Let's explore together."
        )
    ),
    (
        r"I dont (.*)",
        ("Don't you really %1?", "Why don't you %1?", "Do you want to %1?"),
    ),
    (
        r"I feel (.*)",
        (
            "Good, tell me more about these feelings.",
            "Do you often feel %1?",
            "When do you usually feel %1?",
            "When you feel %1, what do you do?",
        ),
    ),
    (
        r"I have (.*)",
        (
            "Why do you tell me that you've %1?",
            "Have you really %1?",
            "Now that you have %1, what will you do next?",
        ),
    ),
    (
        r"I would (.*)",
        (
            "Could you explain why you would %1?",
            "Why would you %1?",
            "Who else knows that you would %1?",
        ),
    ),
    (
        r"Is there (.*)",
        (
            "Do you think there is %1?",
            "It's likely that there is %1.",
            "Would you like there to be %1?",
        ),
    ),
    (
        r"My (.*)",
        (
            "I see, your %1.",
            "Why do you say that your %1?",
            "When your %1, how do you feel?",
        ),
    ),
    (
        r"You (.*)",
        (
            "We should be discussing you, not me.",
            "Why do you say that about me?",
            "Why do you care whether I %1?",
        ),
    ),
    (r"Why (.*)", ("Why don't you tell me the reason why %1?", "Why do you think %1?")),
    (
        r"I want (.*)",
        (
            "What would it mean to you if you got %1?",
            "Why do you want %1?",
            "What would you do if you got %1?",
            "If you got %1, then what would you do?",
        ),
    ),
    (
        r"(.*) mother(.*)",
        (
            "Tell me more about your mother.",
            "What was your relationship with your mother like?",
            "How do you feel about your mother?",
            "How does this relate to your feelings today?",
            "Good family relations are important.",
        ),
    ),
    (
        r"(.*) father(.*)",
        (
            "Tell me more about your father.",
            "How did your father make you feel?",
            "How do you feel about your father?",
            "Does your relationship with your father relate to your feelings today?",
            "Do you have trouble showing affection with your family?",
        ),
    ),
    (
        r"(.*) child(.*)",
        (
            "Did you have close friends as a child?",
            "What is your favorite childhood memory?",
            "Do you remember any dreams or nightmares from childhood?",
            "Did the other children sometimes tease you?",
            "How do you think your childhood experiences relate to your feelings today?",
        ),
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
        r"(.*) (ha)+",
        [
            "What's so funny?"
        ]
    ), 
    (
        r"you",
        [
            "Me?",
            "No you"
        ]
    ),
    (
        r"thank you|thanks|appreciate it",
        [
            "You're welcome",
            "My pleasure",
            "Don't mention it",
            "Anytime"
        ]
    ),
    (
        r"(.*)\?",
        (
            "Why do you ask that?",
            "Please consider whether you can answer your own question.",
            "Perhaps the answer lies within yourself?",
            "Why don't you tell me?",
        ),
    ),
    (
        r"it doesnt|it does",
        (
            "Are you sure about that?",
            "What makes you so sure?"
        ),
    )
]