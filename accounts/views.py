
    if account_user.username == str(request.user):
        account_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)