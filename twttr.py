def main():
    chats= input("whats on your mind? ").lower()
    user(chats)


def user(chats):

    vowels = "aeiou"
    edited = ""

    for chat in chats:
        if chat not in vowels:
            edited += chat
    print(edited)

main()


