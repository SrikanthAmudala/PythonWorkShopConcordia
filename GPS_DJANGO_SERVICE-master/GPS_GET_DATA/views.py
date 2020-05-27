# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from GPS_GET_DATA import algorithms


# from get_data import Data


# Create your views here.
@api_view(["GET"])
def get_data_gps(request):
    try:

        result = {"sunny": "updated"}
        return Response(result, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


from GPS_GET_DATA.algorithms import sample_file


@api_view(["POST"])
def sum_of_input_numbers(request):
    """
    Config Creation: returns list of target fields for the specific target.
    """

    try:
        value1 = request.data.get("num1", None)
        if not value1:
            raise ValueError({"error": "num1 is empty"})
        value2 = request.data.get("num2", None)

        if not value2:
            raise ValueError({"error": "num2 is empty"})
        result = sample_file.sum_of_nums(int(value1), int(value2))

        json_response = {"result": result}
        return Response(json_response, status=status.HTTP_200_OK)

    except ValueError as e:
        # message = ": {} : {}".format(userID, e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        # raise e
        # message = ": {} : {}".format(user_key_posted, e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def get_sample_req(request):
    """
    Config Creation: returns list of target fields for the specific target.
    """

    try:
        target = request.data.get("target", None)
        if not target:
            raise ValueError({"error": "target is empty"})

        json_response = {"result": target}
        return Response(json_response, status=status.HTTP_200_OK)

    except ValueError as e:
        # message = ": {} : {}".format(userID, e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        # raise e
        # message = ": {} : {}".format(user_key_posted, e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def getallusers(request):
    try:
        result = algorithms.sample_file.getAllUsers()
        return Response(result, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    try:
        username = request.data.get("username", None)
        password = request.data.get("password", None)

        if not username:
            raise ValueError({"error": "username is empty"})
        if not password:
            raise ValueError({"error": "password is empty"})

        result = algorithms.sample_file.login(username, password)

        json_response = {"result": result}
        return Response(json_response, status=status.HTTP_200_OK)


    except ValueError as e:
        # message = ": {} : {}".format(userID, e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        # raise e
        # message = ": {} : {}".format(user_key_posted, e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def list_all_books(request):
    try:
        result = {'result': algorithms.sample_file.get_all_books()}
        return Response(result, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def reg_books(request):
    # use the function in side save_d_file.py and reg a book

    try:
        # username = "negar"
        # password = "negar"
        # check_book = "Python"
        # book_catg = "COMPUTER SCIENCE"

        username = request.data.get("username", None)
        password = request.data.get("password", None)
        check_book = request.data.get("check_book", None)
        book_catg = request.data.get("book_catg", None)
        if not username:
            raise ValueError({"error": "username is empty"})
        if not password:
            raise ValueError({"error": "password is empty"})
        if not check_book:
            raise ValueError({"error": "check_book is empty"})
        if not book_catg:
            raise ValueError({"error": "book_catg is empty"})

        result = algorithms.sample_file.reg_book(username, password, book_catg, check_book)

        json_response = {"result": result}
        return Response(json_response, status=status.HTTP_200_OK)

    except ValueError as e:
        # message = ": {} : {}".format(userID, e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        # raise e
        # message = ": {} : {}".format(user_key_posted, e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def return_books(request):
    try:
        username = request.data.get("username", None)
        password = request.data.get("password", None)
        book = request.data.get("book", None)
        book_catg = request.data.get("book_catg", None)
        if not username:
            raise ValueError({"error": "username is empty"})
        if not password:
            raise ValueError({"error": "password is empty"})
        if not book:
            raise ValueError({"error": "book is empty"})
        if not book_catg:
            raise ValueError({"error": "book_catg is empty"})

        result = algorithms.sample_file.returnBook(username, password, book, book_catg)

        json_response = {"result":result}
        return Response(json_response, status=status.HTTP_200_OK)
    except ValueError as e:
        # message = ": {} : {}".format(userID, e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        # raise e
        # message = ": {} : {}".format(user_key_posted, e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
