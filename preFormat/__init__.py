from collections import deque


def initial_Format(wholeText):

    """
       Removes consecutive empty strings using a deque.

       Args:
           data: A list of strings.

       Returns:
           A new list with consecutive empty strings removed.
       """
    cleaned_data = []
    dq = deque(maxlen=1)  # Maximum size of 1 for tracking consecutive empty strings
    for item in wholeText:
        if item:
            cleaned_data.append(item)
            dq.clear()  # Clear the deque if a non-empty string is encountered
        elif not dq:  # Only append an empty string if there's no previous empty string
            cleaned_data.append(item)
            dq.append(item)

    if (len(cleaned_data) > 0) and (cleaned_data[0]==''):
        return cleaned_data[1:]
    return cleaned_data
