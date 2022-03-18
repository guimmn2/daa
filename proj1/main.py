import funcs as f

if __name__ == '__main__':
    int_list = f.generate_random_int_list(1000)
    #int_arr = f.generate_random_int_array(1000)
    print("integer list")
    print(int_list)
    #print("integer array")
    #print(int_arr)
    val = int(input("type int between 1 and 1000000: "))
    #print("index of value in integer list: %d " %f.search_in(int_list, val))
    #print("index of value in numpy array: %d " %f.search_in(int_arr, val))
    nr_of_calls = int(input("type nr of calls to be made to the func per repeat: "))
    print("durations of %d calls to search_in(int_list, val): " %nr_of_calls)
    durations_list = f.get_durations(f.search_in(int_list, val), nr_of_calls)
    print(durations_list)
    print("average duration of search_in(int_list, val): %f" %f.get_avg_duration(durations_list))

