import time
import matplotlib.pyplot as pyplot
from search_sort_tests import generate_random_number_list
from search_sort_library import *


def generate_graph_data(function_to_time, data_generator_function, max_data_size):
    """
    :param: function_to_time - a function you would like to time, which takes only a single parameter,
        the data to time it on
    :param: data_generator_function - a function that takes a data size and creates a list of data with that length
    :param: max_data_size -   the largest size of data you want timed
    :return: a tuple of lists, ([x-values], [y-values]) that can be used to make a graph
    """
    step_size = max_data_size//25
    number_list = data_generator_function(max_data_size)
    datasize_x_vals = []
    time_y_vals = []
    print("\nCollecting data for:{}\n========".format(function_to_time.__name__))
    for current_data_size in range(step_size, max_data_size, step_size):
        data_to_test = number_list[:current_data_size]
        start = time.perf_counter()
        function_to_time(data_to_test)
        stop = time.perf_counter()
        elapsed_time = stop - start
        print("{}\t{}".format(current_data_size, elapsed_time))
        datasize_x_vals.append(current_data_size)
        time_y_vals.append(elapsed_time)
    return datasize_x_vals, time_y_vals


def main():
    max_data_size = 1000000

    x_is_sorted, y_is_sorted = generate_graph_data(is_sorted,generate_random_number_list,max_data_size)

    # Collect data for My Sort
    x_my_sort, y_my_sort = generate_graph_data(my_sort, generate_random_number_list, max_data_size)

    # Collect data for System Sort
    x_system_sort, y_system_sort = generate_graph_data(system_sort, generate_random_number_list, max_data_size)

    # Collect data for My Linear Search
    x_my_linear, y_my_linear = generate_graph_data(
        lambda data: my_linear_search(data, data[0]), generate_random_number_list, max_data_size
    )

    # Collect data for My Binary Search
    x_my_binary, y_my_binary = generate_graph_data(
        lambda data: my_binary_search(sorted(data), data[0]), generate_random_number_list, max_data_size
    )

    x_system_linear_search, y_system_linear_search = generate_graph_data(lambda data: system_linear_search(data, data[0]), generate_random_number_list, max_data_size)

    # Plot My Sort
    pyplot.figure(figsize=(10, 6))
    pyplot.plot(x_my_sort, y_my_sort, label="My Sort (Bubble Sort)", color="red")
    pyplot.title("My Sort Runtime (Bubble Sort)")
    pyplot.xlabel("Data Size")
    pyplot.ylabel("Runtime (seconds)")
    pyplot.legend(loc="upper left")
    pyplot.grid(True)
    pyplot.show()

    # Plot System Sort
    pyplot.figure(figsize=(10, 6))
    pyplot.plot(x_system_sort, y_system_sort, label="System Sort (Timsort)", color="blue")
    pyplot.title("System Sort Runtime (Timsort)")
    pyplot.xlabel("Data Size")
    pyplot.ylabel("Runtime (seconds)")
    pyplot.legend(loc="upper left")
    pyplot.grid(True)
    pyplot.show()

    # Plot My Linear Search
    pyplot.figure(figsize=(10, 6))
    pyplot.plot(x_my_linear, y_my_linear, label="My Linear Search", color="green")
    pyplot.title("My Linear Search Runtime")
    pyplot.xlabel("Data Size")
    pyplot.ylabel("Runtime (seconds)")
    pyplot.legend(loc="upper left")
    pyplot.grid(True)
    pyplot.show()

    # Plot My Binary Search
    pyplot.figure(figsize=(10, 6))
    pyplot.plot(x_my_binary, y_my_binary, label="My Binary Search", color="purple")
    pyplot.title("My Binary Search Runtime")
    pyplot.xlabel("Data Size")
    pyplot.ylabel("Runtime (seconds)")
    pyplot.legend(loc="upper left")
    pyplot.grid(True)
    pyplot.show()

    pyplot.figure(figsize=(10, 6))
    pyplot.plot(x_is_sorted, y_is_sorted, label="Is Sorted", color="blue")
    pyplot.title("Is Sorted")
    pyplot.xlabel("Data Size")
    pyplot.ylabel("Runtime (seconds)")
    pyplot.legend(loc="upper left")
    pyplot.grid(True)
    pyplot.show()

    pyplot.figure(figsize=(10, 6))
    pyplot.plot(x_system_linear_search, y_system_linear_search, label="System Linear Search", color="green")
    pyplot.title("System Linear Search")
    pyplot.xlabel("Data Size")
    pyplot.ylabel("Runtime (seconds)")
    pyplot.legend(loc="upper left")
    pyplot.grid(True)
    pyplot.show()


if __name__ == "__main__":
    main()





