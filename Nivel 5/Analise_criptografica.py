import re
def Count_Letters(pattern):
    dic = {}
    letter_list = re.findall(r'[A-z]',pattern).copy()
    letter_list = sorted(letter_list)
    for letters in letter_list:
        dic[letters] = letter_list.count(letters)
    for elements in sorted(sorted(dic),reverse = True,key=dic.get):
        print(elements+ " "+str(dic[elements]))
        
   
def main():
    pattern = ''
    num_test = 0
    n = int(input())
    while(True):
        if(n > 0):
            pattern += input()
            pattern = pattern.upper()
            n -= 1
            if(n == 0):
                num_test += 1
                print("TESTE %d"%num_test)
                Count_Letters(pattern)
                n = int(input())
                pattern = ''
                continue
        else:
            break
            
if __name__ == "__main__":
    main()
