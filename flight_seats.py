import random
import string


# Function to initialize the seat layout
def initialize_seats(rows, cols):
# this is initializing the seat layout by creating a 2D list of rows and columns and marking the aisles and storage areas by 'X' and 'S' respectively
    seats = [['F' for _ in range(cols)] for _ in range(rows)]
    # going through the rows for each row 
    for i in range(rows):
        # going through the columns for each column
        for j in range(cols):
            # checks if j is equal to 4 or 5 or 6 or 7 if true marks them as x 
            if j == 4 or j == 5 or j == 6 or j == 7:
                seats[i][j] = 'X'
            # checks if j is equl to 77 or 78 or 79 or 80 and marks the position on the matrix ad s 
            if j == 77 or j == 78 or j == 79 or j == 80:
                seats[i][j] = 'S'
    return seats

# Function to display the seat layout
def display_seats(seats):
    # prints seat layout to make it neater 
    print("Seat Layout:")
    # goes through the rows in seats 
    for row in seats:
    # prints the row and joins the row with a space
        print(" ".join(row))

def generate_booking_reference(booking_references):
    reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    # this is to make sure that the reference is unique
    while reference in booking_references:
        reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return reference


# Function to book a seat
def book_seat(seats, row, col, booking_references, customer_data, name, age, contact):
    # checks if the seat is equal to F if true marks the seat as R and prints the seat number was booked successfully
    if seats[row][col] == 'F':
        # marks the seat as R
        seats[row][col] = 'R'
        # defines the booking reference using a reference generator which is our helper function 
        reference = generate_booking_reference(booking_references)
        # adds the reference to the booking references list
        booking_references.add(reference)
        customer_data[reference] = {'Name': name, 'Age': age, 'Contact': contact}
        # prints the seat number that was booked successfully
        print(f"Seat {row+1}{chr(col+65)} booked successfully.")
        print(f"Generated booking reference: {reference}")
    else:
        # prints seat is already booked or invalid
        print("Seat is already booked or invalid.")

def free_seat(seats, row, col, booking_references, customer_data):
    if seats[row][col] == 'R':
        seats[row][col] = 'F'
        for reference, data in customer_data.items():
            if data['Seat'] == (row, col):
                del customer_data[reference]
                print(f"Seat {row+1}{chr(col+65)} freed successfully.")
                break
    else:
        print("Seat is already free or invalid.")
     



# Main function
def main():
    # initializes the rows and columns as the one shows on the for the airlines 
    rows = 6
    cols = 80
    seats = initialize_seats(rows, cols)
    booking_references = set()
    customer_data = {}

    # while loop that runs the menu until the user decides to exit
    while True:
        # menu using print statments 
        print("\nMenu:")
        print("1. Display Seat Layout")
        print("2. Book a Seat")
        print("3. Free a Seat")
        print("4. Exit")
        
        # takes an input by the user 
        choice = input("Enter your choice: ")


        # if and elif statements to take in the user input and do the right takse accordingly to the users input 

        if choice == '1':
            # uses helper function to display the seats
            display_seats(seats)
        elif choice == '2':
            # takes in the row and column from the user and books the seat
            row = int(input("Enter row number (1-6): ")) - 1
            # .uppper makes the input uppercase therefore it is easier to put the input in its ASCII value             
            col = ord(input("Enter column letter (A-H or S): ").upper()) - 65
            # cheks if the inputed position is valid and books the seat
            if 0 <= row < rows and (0 <= col < cols or col == ord('S') - 65):
                name = input("Enter customer name: ")
                age = input("Enter customer age: ")
                contact = input("Enter customer contact: ")
                book_seat(seats, row, col, booking_references, customer_data, name, age, contact)
            else:
                print("Invalid row or column.")
        elif choice == '3':
            row = int(input("Enter row number (1-6): ")) - 1
            col = ord(input("Enter column letter (A-H or S): ").upper()) - 65
            if 0 <= row < rows and (0 <= col < cols or col == ord('S') - 65):
                free_seat(seats, row, col, booking_references, customer_data)
            else:
                print("Invalid row or column.")
        elif choice =='4':
            # if user wants to leave breaks the looop and prints exiting program
            print("Exiting program.")
            break
        else:
            # if user's input is invalid prints invalid choice and asks the user to enter again
            print("Invalid choice. Please enter again.")

if __name__ == "__main__":
    main()