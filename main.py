def main():
    print("================ BOOKBOT ================")

    file_name = input("Enter file name: ")

    print(f"Analyzing book for in readings/{file_name}...")

    print("------------- WORD COUNT -------------")

    num_line = 0
    with open(f"readings/{file_name}", "r") as f:
        for line in f:
            print(line)

        
    
        
        

if __name__== '__main__':
    main()

