

def is_in_response_table():
    """
    checks if the particular request is there in the response table

    return: True or False
    """


def add_to_requests_table():
    """
    If the in_response_table is False, then we run this
    """


def delete_from_requests():
    """
    Deletes the given request from the requests table
    """

def add_to_response():
    """
    adds the given to the response table
    """

def served(ticker, lookupstep, epochs, accuracy_score, price_prediction, filepath):
    # TODO: Convert all of these into keyword arguments with the same names, like ive done in the add_to_response function
    """
    Will call this function to notify that this request has been served
    """
    delete_from_requests()
    add_to_response(filepath=filepath)


def get_new_requests(old, new):
    """
    Read the two objects, and return a dictionary of the different values.

    If there is no difference, return None
    """

def return_all_request_table_rows():
    """
    Must return all the request table rows in whatever format you please, either as a pandas dataframe or something else
    """
    return None


def check_and_add():
    if not is_in_response_table():
        add_to_requests_table()
