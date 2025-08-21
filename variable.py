# Global variable
count = 10

def update_variable():
    global count  
    local_var = 5
    print("Initial global variable:", count)
    print("Local variable:", local_var)
    
    # Modify global variable
    count = count + 20
    print("Modified global variable inside function:", count)

# Call the function
update_variable()

# Print final global value outside function
print("Final global variable outside function:", count)
