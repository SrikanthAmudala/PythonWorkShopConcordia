db = {
  "user_table": {

    "sunny": {
      "password": "sunny1234",
      "books_reg": {
        "COMPUTER SCIENCE": [],
        "CIISE": []
      }
    },

    "rohit": {
      "password": "rohit",
      "books_reg": {
        "COMPUTER SCIENCE": [],
        "CIISE": []
      }
    },

    "negar": {
      "password": "negar",
      "books_reg": {
        "COMPUTER SCIENCE": [],
        "CIISE": []
      }
    }
  },


  "books_list": {
    "COMPUTER SCIENCE": {
      "C": 1,     # name of the book: count of the book
      "Python": 2,
      "java": 1
    },
    "CIISE": {
      "Quality Systems": 1,
      "DataMining": 1,
      "Project Management": 1
    }
  }
}

print("before update: \n",db)

username = "negar"
password = "negar"
password_from_db = db.get("user_table").get(username).get("password")

print("True password: ", password_from_db)
if password == password_from_db:
  print("Login successful")
else:
  print("Login Failed")


check_book = "Python"
book_catg = "COMPUTER SCIENCE"
total_books_avilable = db.get("books_list").get(book_catg).get(check_book)

if total_books_avilable > 0:
  print("Book exists and total no of books available: ", total_books_avilable)
  # adding book to the username
  db['user_table'][username]['books_reg'][book_catg].append(check_book)
  # updating the no of books in the book catg
  db['books_list'][book_catg][check_book] = db.get('books_list').get(book_catg).get(check_book) - 1

else:
  print("Book out of stock")

print("After update: \n",db)

