def split_and_join(line):
    return "-".join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#Time Complexity : O(1)
#Space Complexity : O(1)
#time : 4 min
