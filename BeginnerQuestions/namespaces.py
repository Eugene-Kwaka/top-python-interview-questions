# global_var is in the global namespace
global_var = 5

def local_function():
    #  local_var is in the local namespace 
    local_var = 10

    def inner_function():
        #  inner_var is in the nested local namespace 
        inner_var = 15
        print("Inner variable: ", inner_var)

    print("Local variable: ", local_var)

    inner_function()

# print the value of the global variable
print("Global variable: ", global_var)

# call the local function and print local and nested local variables
local_function()