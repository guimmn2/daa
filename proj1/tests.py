import funcs as f
import random as r


def test_search_in_int_list(length):
    print("generating integer list...")
    int_list = f.generate_random_int_list(length)
    nr_of_calls = int(input("type nr of calls to be made to the func per repeat: "))
    #a
    existing_element = int_list[r.randint(0,length)]
    print(f"index of existing element {existing_element} in integer list: {f.search_in(int_list, existing_element)} ")
    durations_list = f.get_durations(f.search_in(int_list, existing_element), nr_of_calls)
    print(f"average duration of search_in(int_list, val) given an existing element: {f.get_avg_duration(durations_list)}")
    #b
    #there are no negative integers
    non_existing_element = -1
    durations_list = f.get_durations(f.search_in(int_list, non_existing_element), nr_of_calls)
    print(f"average duration of search_in(int_list, val) given a non existing element: {f.get_avg_duration(durations_list)}")


def test_search_in_int_arr(length):
    print("generating integer array...")
    int_arr = f.generate_random_int_array(length)
    nr_of_calls = int(input("type nr of calls to be made to the func per repeat: "))
    #a
    # selected midway element
    existing_element = int_arr[r.randint(0, length)]
    print(f"index of existing element {existing_element} in integer list: {f.search_in(int_arr, existing_element)} ")
    durations_list = f.get_durations(f.search_in(int_arr, existing_element), nr_of_calls)
    print(f"average duration of search_in(int_arr, val) given an existing element: {f.get_avg_duration(durations_list)}")
    #b
    #there are no negative integers
    non_existing_element = -1
    durations_list = f.get_durations(f.search_in(int_arr, non_existing_element), nr_of_calls)
    print(f"average duration of search_in(int_arr, val) given a non existing element: {f.get_avg_duration(durations_list)}")
