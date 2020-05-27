import json


def sample_operation():
    return {"result": "sampleout"}


def json_read(db_path):
    with open(db_path, encoding='utf-8') as f:
        original_data = json.load(f)

    with open(db_path, 'w') as f:
        json.dump(original_data, f)


def sum_of_nums(num1, num2):
    return num1 + num2


def fib(num1):
    return num1


def reg_book(username, password, book_catg, check_book):
    db_path = r"/Users/Srikanth/PycharmProjects/PythonWorkShopConcordia/GPS_DJANGO_SERVICE-master/GPS_GET_DATA/db/db.json"

    with open(db_path, encoding='utf-8') as f:
        db = json.load(f)

    # username = "negar"
    # password = "negar"
    # check_book = "Python"
    # book_catg = "COMPUTER SCIENCE"

    password_from_db = db.get("user_table").get(username).get("password")

    print("True password: ", password_from_db)
    if password == password_from_db:
        print("Login successful")
        total_books_avilable = db.get("books_list").get(book_catg).get(check_book)

        if total_books_avilable > 0:
            print("Book exists and total no of books available: ", total_books_avilable)
            # adding book to the username
            db['user_table'][username]['books_reg'][book_catg].append(check_book)
            # updating the no of books in the book catg
            db['books_list'][book_catg][check_book] = db.get('books_list').get(book_catg).get(check_book) - 1

            print("After update: \n", db)
            # saving the updated db into the same json file

            with open(db_path, 'w') as f:
                json.dump(db, f)
            return "Book successfully added, total no of books available after update: %s" % (total_books_avilable)
        else:
            return "Book out of stock"

    else:
        return "Login Failed"


def get_all_books():
    db_path = r"/Users/Srikanth/PycharmProjects/PythonWorkShopConcordia/GPS_DJANGO_SERVICE-master/GPS_GET_DATA/db/db.json"

    with open(db_path, encoding='utf-8') as f:
        db = json.load(f)

    return db['books_list']


def login(username, password):
    db_path = r"/Users/Srikanth/PycharmProjects/PythonWorkShopConcordia/GPS_DJANGO_SERVICE-master/GPS_GET_DATA/db/db.json"

    with open(db_path, encoding='utf-8') as f:
        db = json.load(f)

    password_from_db = db.get("user_table").get(username).get("password")

    if password == password_from_db:
        return True
    else:
        return False


def getAllUsers():
    db_path = r"/Users/Srikanth/PycharmProjects/PythonWorkShopConcordia/GPS_DJANGO_SERVICE-master/GPS_GET_DATA/db/db.json"

    with open(db_path, encoding='utf-8') as f:
        db = json.load(f)
    return db['user_table'].keys()


def returnBook(username, password, book, book_cat):

    db_path = r"/Users/Srikanth/PycharmProjects/PythonWorkShopConcordia/GPS_DJANGO_SERVICE-master/GPS_GET_DATA/db/db.json"

    with open(db_path, encoding='utf-8') as f:
        db = json.load(f)
    # write code to verify the password using the already defined login function

    db['user_table'][username]['books_reg'][book_cat].remove(book)

    # updating the total no of books in the book list
    db['books_list'][book_cat][book] += 1

    with open(db_path, 'w') as f:
        json.dump(db, f)

    return "Book return successfully"
