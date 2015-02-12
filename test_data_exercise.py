import pickle

def get_test_results():
    with open("test_data.dat", mode = "rb") as testData:
        test_results = pickle.load(testData)
    return test_results

def average_test_result(results):
    total = 0
    for test in results:
        total += test
    average = total/len(results)
    return average

def display_average_result(average):
    print("your average test result is: {0}".format(average))


def main():
    test_results = get_test_results()
    average = average_test_result(test_results)
    display_average_result(average)

if __name__ == "__main__":
    main()

