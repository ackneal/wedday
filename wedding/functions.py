def storeIntoDB(data):
    return data

# 驗證參數
def valid_param(form, columns):
    for column in columns:
        if column not in form:
            return False

        if not form[column].strip():
            return False

    return True


