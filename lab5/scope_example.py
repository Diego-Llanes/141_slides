GLOBAL_VAR = 10
def func1():
    print(GLOBAL_VAR)
    var1 = 5
    print(var1)
def func2(arg1):
    print(arg1)
    print(GLOBAL_VAR)
if __name__ == "__main__":
    func1()
