#imports
import csv

class Main:

    def __init__():
        Main.read_csv()

    def read_csv():
        csv_count = input("How many files would you like to sort?")
        csv_path = []
        i = 0
        while i < int(csv_count):
            csv_path.append(input("Please enter csv file path: "))
            i += 1
        row_organize = int(input("Which column would you like to organize? 0 is the first column: "))
        rows = []

        for i in csv_path:
            with open(i, 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                #saves content of entire first column into a list
                for row in csvreader:
                    rows.append(row[row_organize])
                print(rows)
        Main.sort_csv(rows)

    def sort_csv(arr):
        n = len(arr)
        sorted = False

        while(not sorted):
            sorted = True
            for i in range(n-1):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    sorted = False
        print(arr)
        Main.save_csv(arr)
    
    def save_csv(arr):
        csv_path = input("Please enter csv file path: ")
        with open(csv_path, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            for i in arr:
                csvwriter.writerow([i])




if __name__ == "__main__":
    Main.__init__()
