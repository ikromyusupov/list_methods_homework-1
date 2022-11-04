def main(numbers1, numbers2):
    """
    You are given a list called numbers1 and numbers2.
    Delete the last item in the first list and add that deleted item to the beginning of the second list.
    Merge the first list into the second and return.
    Args:
        numbers1(list): parameter
        numbers2(list): parameter
    Returns:
        list: return answer
    """
    x = numbers1[-1]
    numbers1.pop(-1)
    numbers2.insert(0,x)
    numbers1.extend(numbers2)
    return numbers1
print(main(["sA",3,432,"FFG"],[1,2,3,4]))

