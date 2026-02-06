# Pattern Matching

# statusCode = 405
statusCode = 200

match statusCode:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case _:
        print("Unknown Status Code")