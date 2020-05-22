# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from get_data import Data


# Create your views here.
@api_view(["GET"])
def get_data_gps(request):
    try:

        result = {"sunny":123}
        return Response(result, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
@api_view(["POST"])


def get_target_fields(request):
    """
    Config Creation: returns list of target fields for the specific target.
    """

    try:
        target = request.data.get("target", None)
        if not target:
            raise ValueError({"error": "target is empty"})

        json_response = { "result": target}
        return Response(json_response, status=status.HTTP_200_OK)

    except ValueError as e:
        # message = ": {} : {}".format(userID, e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        # raise e
        # message = ": {} : {}".format(user_key_posted, e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)