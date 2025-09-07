#4. Counting Passengers in a Bus
(A city bus stops at different stations, and passengers board at each stop. The bus conductor 
notes down the number of passengers at each stop for 5 stops. Write a Python program to take 
input for each stop and calculate the total number of passengers at the end.)

total_passengers = 0
for i in range(1,6):
    passengers = int(input(f"Enter no. of passenger at stop {i}"))
    total_passengers += passengers    

print(f"total number of passengers at the end are {total_passengers}")
