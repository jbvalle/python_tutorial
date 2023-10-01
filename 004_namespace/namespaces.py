def func1():

    print('Yoo this is func1')

    def func2():

        print('Yoo this is func2')

    print('Yoo this is still func1 but its running after a locally defined func')

    func2()


func1()
