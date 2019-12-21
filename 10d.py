l=['a',0,2]
for i in l:
    print(i)
    try:
        print("reciprocal: ",1/i )
    except ZeroDivisionError as e:
        print("zero can't be divided ",e)
    except TypeError as e:
        print("can divide only nos ",e)
    except Exception as e:
        print(e)
    finally:
        print("Iteration done")