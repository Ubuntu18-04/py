import io
try:
    f=open("Q1input.txt")
    f.writelines(input("enter lines: "))
    f.close()
except io.UnsupportedOperation as e:
    print("Unsupported Operation",e)
except Exception as e:
    print(e)
finally:
    print("Program ended")
