import os

def count_files_in_subd(partition):
    print("-------", partition, "-------")
    for root, dirs, files in os.walk("./Dataset/"+partition):
        d = dirs
        break
    for fruit in d:
        count = 0
        first = True
        for root, dirs, files in os.walk("./Dataset/" + partition + '/' + fruit):
            if first:
                first = False
                continue
            count += len(files)
            # print("{} in {}".format(len(files), root))
        print(fruit, ': ', count)



count_files_in_subd(partition = 'Test')
count_files_in_subd(partition = 'Train')
