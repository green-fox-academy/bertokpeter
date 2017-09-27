class Sum(object):

    def summ(self, numbers):
        for i in range(len(numbers)):
            if numbers[i] == None:
                numbers[i]=0
        return sum(numbers)