from response_gen import get_response
from things.actors import actor

def main():
    print("Chat-Bot Testing: Type input when > symbol is shown\n")
    act = actor('123-456-7890')
    while True:
        message = input("> ")

        print("\n"+get_response(act, message))

if __name__ == "__main__":
    main()