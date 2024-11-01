def main():
    user=input("what are the names of your parents? ")
    snakecase(user)



def snakecase(answer):
    result=""
    for s in answer:
        if s.isupper():
            result+= "_" + s.lower()
        else:
            result+=s
    print (result.strip("-"))

main()



