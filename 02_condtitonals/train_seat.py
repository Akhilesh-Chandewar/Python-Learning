seat_type = input("Enter your seat type (sleeper/AC/general/luxury): ").lower().strip()

match seat_type:
    case "sleeper":
        print("Your seat is sleeper")
    case "ac":
        print("Your seat is AC")
    case "general":
        print("Your seat is general")
    case "luxury":
        print("Your seat is luxury")
    case _:
        print("Unknown seat type")
