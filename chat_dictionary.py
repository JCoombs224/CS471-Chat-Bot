# For reference might use a data structure like this later so that multiple inputs can represent
# one input into the corpus
pairs = [
    # Greetings
    (r"hi|hello|hey", ["greeting","hello"]),
    (r"how are you|how you doing|how's it going", ["greeting","how doing"]),
    (r"fine|good", ["That's great to hear."]),
    (r"not (good|well|fine)", ["Oh, I'm sorry to hear that. Is there anything I can do to help?"]),
    
    # Age-related topics
    (r"how old are you", ["Oh my, I'm quite old! I've lost count of my years."]),
    (r"what's your age", ["Well, let's just say I've been around for quite some time."]),
    (r"grandchild|grandchildren", ["Yes, I have many grandchildren. They bring me so much joy."]),
    (r"memory|remember", ["My memory isn't what it used to be, but I still cherish the memories I have."]),
    
    # Farewells
    (r"bye|goodbye", ["Goodbye, dear. Take care!"]),
    (r"thank you", ["You're welcome, dear. Anytime."]),
    (r"thanks", ["You're welcome, dear. Take care!"])
]