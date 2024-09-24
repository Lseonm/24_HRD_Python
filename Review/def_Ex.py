def function1() :
    print("function1")

def function2(func):
    return func()

function2(function1)

func = function1
function2(func)