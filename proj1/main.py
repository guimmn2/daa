import funcs as f
if __name__ == '__main__':
    int_list = f.generate_random_int_list(100)
    int_array = f.generate_random_int_array(100)

    int_list_item = f.get_random_item_of(int_list)
    int_array_item = f.get_random_item_of(int_array)

    print("3")
    print(" ---------------------------------- ")
    print("search_in(int_list, val)")
    print(" ---------------------------------- ")
    print(f"a: {f.get_avg_duration(f.search_in(int_list, -1), 35)}")
    print(f"b: {f.get_avg_duration(f.search_in(int_list, int_list_item), 35)}")
    print(" ---------------------------------- ")
    print("search_in(int_array, val)")
    print(" ---------------------------------- ")
    print(f"a: {f.get_avg_duration(f.search_in(int_array, -1), 35)}")
    print(f"b: {f.get_avg_duration(f.search_in(int_array, int_array_item), 35)}")
    print("4")
    print(" ---------------------------------- ")
    print("search_in(int_list, val)")
    print(" ---------------------------------- ")

