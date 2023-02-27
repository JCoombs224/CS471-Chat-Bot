from response_gen import get_response

def main():
    print("Chat-Bot Testing: Type input when > symbol is shown\n")
    while True:
        message = input("> ")

        print("\n"+get_response(None, message))

if __name__ == "__main__":
    main()