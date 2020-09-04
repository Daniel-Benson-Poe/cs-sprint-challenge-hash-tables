# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    finder_dict = {}
    for file in files:
        split_file = (file.split("/"))
        if split_file[-1] in finder_dict.keys():
            finder_dict[split_file[-1]].append(file)
        else:
            finder_dict[split_file[-1]] = [file]

    results = []
    final_result = []

    [results.append(finder_dict[query]) for query in queries if query in finder_dict.keys()]
    
    for result in results:
        final_result += result 
    return final_result


if __name__ == "__main__":
    # files = [
    #     '/bin/foo',
    #     '/bin/bar',
    #     '/usr/bin/baz'
    # ]
    # queries = [
    #     "foo",
    #     "qux",
    #     "baz"
    # ]

    files = []

    for i in range(500000):
        files.append(f"/dir{i}/file{i}")

    for i in range(500000):
        files.append(f"/dir{i}/dirb{i}/file{i}")

    queries = []

    for i in range(1000000):
        queries.append(f"nofile{i}")

    queries += [
            "file3490",
            "file256",
            "file999999",
            "file8192"
        ]

    print(finder(files, queries))
