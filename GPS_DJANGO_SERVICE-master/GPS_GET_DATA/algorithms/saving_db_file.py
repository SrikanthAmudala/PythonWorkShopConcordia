import json



def reg_book(username, password, book_catg, check_book):
    db_path = r"/Users/Srikanth/PycharmProjects/PythonWorkShopConcordia/GPS_DJANGO_SERVICE-master/GPS_GET_DATA/db/db.json"

    with open(db_path, encoding='utf-8') as f:
        db = json.load(f)

    print("before update: \n", db)

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
