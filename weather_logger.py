# List to store the temperatures entered by the user
temperatures = []
    
# Main loop to collect temperatures from the user
while(True):
    temp = input("Enter the temperature ('done' to stop): ")
    
    if temp == "done":
        break
    else:
        temperatures.append(float(temp))
            