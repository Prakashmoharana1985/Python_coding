original_str = "the apple fell far from the tree"
found_str = ''
search_str = original_str
start = 0

while start < len(original_str):
    start = search_str.find('from')
    # find() returns the index for the first occurrance of 'the'
    # or returns -1 if the string is not found
    if start != -1:
        stop = start + 4  # the is 3 characters
        found_str = search_str[start:stop]
        print(found_str)

        # reduce the search_str and keep searching
        search_str = search_str[stop:]
        start = 0
    else:
        break  # 'the' not found n search_str
