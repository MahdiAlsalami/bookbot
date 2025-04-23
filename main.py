def main():
    print("================ BOOKBOT ================")

    file_name = input("Enter file name: ")

    print(f"Analyzing book for in readings/{file_name}...")

    print("------------- WORD COUNT -------------")

    total_word_counter = 0 
    with open(f"readings/{file_name}", "r") as f:
        for line in f:
            total_word_counter += len(line.split())
        print(total_word_counter)

    print("------------- CHARACTER COUNT -------------")


    for char in line:
        print(char)
        
        

if __name__== '__main__':
    main()



'''

final steps:


2. count each letter and see how much there are staring with most letters in text file to least



'''
