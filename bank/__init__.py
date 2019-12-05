def test(*params):
        print(params)

def testtt(*params):
    print("testtt works")
    print(params)

def test_1(test,a,b,c):
    test(a,b,c)

if __name__ == "__main__":
    #unittest.main()
    d="1"
    e="2"
    f="3"
    a="1"
    b="f"
    c="c"
    test_1(testtt,d,e,f)
    test_1(test,d,a,c)