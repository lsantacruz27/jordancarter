import time

def main():
    cookies = 0
    cookies_per_click = 1
    cookies_per_second = 0
    last_time = time.time()

    cursors = 0
    grandmas = 0
    farms = 0
    mines = 0
    factories = 0
    banks = 0
    temples = 0
    wizard_towers = 0

    cursor_cost = 10
    grandma_cost = 50
    farm_cost = 100
    mine_cost = 200
    factory_cost = 500
    bank_cost = 1000
    temple_cost = 2000
    wizard_tower_cost = 5000

    while True:
        # Calculate time elapsed since last iteration
        current_time = time.time()
        elapsed_time = current_time - last_time
        last_time = current_time

        # Update cookies based on production rate
        cookies += cookies_per_second * elapsed_time

        # Print current status
        print(f"Cookies: {int(cookies)}")
        print(f"Cookies per click: {cookies_per_click}")
        print(f"Cookies per second: {cookies_per_second}")
        print("\nOptions:")
        print("1. Click (c)")
        print(f"2. Buy Cursor (cost: {cursor_cost} cookies, +1 cookie/second)")
        print(f"3. Buy Grandma (cost: {grandma_cost} cookies, +5 cookies/second)")
        print(f"4. Buy Farm (cost: {farm_cost} cookies, +10 cookies/second)")
        print(f"5. Buy Mine (cost: {mine_cost} cookies, +20 cookies/second)")
        print(f"6. Buy Factory (cost: {factory_cost} cookies, +50 cookies/second)")
        print(f"7. Buy Bank (cost: {bank_cost} cookies, +100 cookies/second)")
        print(f"8. Buy Temple (cost: {temple_cost} cookies, +200 cookies/second)")
        print(f"9. Buy Wizard Tower (cost: {wizard_tower_cost} cookies, +500 cookies/second, +2 cookies per click)")
        print("10. Exit (q)")

        # Get user input
        choice = input("Choose an option: ").strip().lower()

        # Process user choice
        if choice == 'c':
            cookies += cookies_per_click
        elif choice == '1':
            if cookies >= cursor_cost:
                cookies -= cursor_cost
                cursors += 1
                cookies_per_second += 1
                cursor_cost = int(cursor_cost * 1.2)  # Increase cursor cost for next purchase
            else:
                print("Not enough cookies to buy a cursor!")
        elif choice == '2':
            if cookies >= grandma_cost:
                cookies -= grandma_cost
                grandmas += 1
                cookies_per_second += 5
                grandma_cost = int(grandma_cost * 1.2)  # Increase grandma cost for next purchase
            else:
                print("Not enough cookies to hire a grandma!")
        elif choice == '3':
            if cookies >= farm_cost:
                cookies -= farm_cost
                farms += 1
                cookies_per_second += 10
                farm_cost = int(farm_cost * 1.2)  # Increase farm cost for next purchase
            else:
                print("Not enough cookies to buy a farm!")
        elif choice == '4':
            if cookies >= mine_cost:
                cookies -= mine_cost
                mines += 1
                cookies_per_second += 20
                mine_cost = int(mine_cost * 1.2)  # Increase mine cost for next purchase
            else:
                print("Not enough cookies to buy a mine!")
        elif choice == '5':
            if cookies >= factory_cost:
                cookies -= factory_cost
                factories += 1
                cookies_per_second += 50
                factory_cost = int(factory_cost * 1.2)  # Increase factory cost for next purchase
            else:
                print("Not enough cookies to buy a factory!")
        elif choice == '6':
            if cookies >= bank_cost:
                cookies -= bank_cost
                banks += 1
                cookies_per_second += 100
                bank_cost = int(bank_cost * 1.2)  # Increase bank cost for next purchase
            else:
                print("Not enough cookies to buy a bank!")
        elif choice == '7':
            if cookies >= temple_cost:
                cookies -= temple_cost
                temples += 1
                cookies_per_second += 200
                temple_cost = int(temple_cost * 1.2)  # Increase temple cost for next purchase
            else:
                print("Not enough cookies to buy a temple!")
        elif choice == '8':
            if cookies >= wizard_tower_cost:
                cookies -= wizard_tower_cost
                wizard_towers += 1
                cookies_per_second += 500
                cookies_per_click += 2
                wizard_tower_cost = int(wizard_tower_cost * 1.2)  # Increase wizard tower cost for next purchase
            else:
                print("Not enough cookies to buy a wizard tower!")
        elif choice == 'q':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
