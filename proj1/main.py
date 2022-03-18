import funcs as f

if __name__ == '__main__':
    int_list = f.generate_random_int_list(10)
    int_arr = f.generate_random_int_array(10)
    print("integer list")
    print(int_list)
    print("integer array")
    print(int_arr)
    val = int(input("type int between 1 and 1000000: "))
    print("index of value in integer list: %d " %f.search_in(int_list, val))
    print("index of value in numpy array: %d " %f.search_in(int_arr, val))

