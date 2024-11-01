def main():
    money_inserted()

def money_inserted():

    total = 0
    cost = 50

    while total < cost:
        coin = int(input("insert a coin "))
        if coin in [25, 10,5]:
            total += coin
            if total < cost:
                print(f"Amount Due: {cost-total}")

            else:
                print(f"Change Owed: {total-cost}")
        else:
            print("Amount Due: 50")
main()






