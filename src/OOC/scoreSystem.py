import time


class Test:
    import time

    def __init__(self, num):
        self.__num = num
        self.__dict = {}
        self.__avg = None
        self.fp = open('log.txt', 'w')

    def add(self, sub, score):
        if len(self.__dict) == self.__num:
            raise Exception('full error')
        if sub in self.__dict:
            raise Exception('subject exist. Please use update')
        else:
            self.__dict[sub] = score
            print('[', time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()), ']', end=':', file=self.fp)
            print('successfully add', sub, file=self.fp)

    def delete_subject(self, subject):
        if subject in self.__dict:
            self.__dict.pop(subject)
            print('[', time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()), ']', end=':', file=self.fp)
            print('successfully delete subject', subject, file=self.fp)
        else:
            print('subject not found')

    def update(self, sub=str, score=(int, float)):
        if sub not in self.__dict:
            raise Exception('subject not found')
        else:
            self.__dict[sub] = score
            print('[', time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()), ']', end=':', file=self.fp)
            print('successfully update', sub, file=self.fp)

    def avg(self) -> float:
        a = 0
        for value in self.__dict.values():
            a += value
        avg = a / len(self.__dict.values())
        return avg

    def mid(self) -> float:
        scores = sorted(list(self.__dict.values()))
        length = len(self.__dict) - 1
        if length == 0:
            raise Exception('no element was found')
        elif length == 1:
            mid = scores[0]
        elif length % 2 == 0:
            mid = (scores[length // 2] + scores[length // 2 + 1]) / 2
        elif length % 2 != 0:
            mid = scores[length // 2]
        return mid

    def show(self, subject):
        if subject in self.__dict:
            print(subject, ':', self.__dict[subject])
        else:
            raise Exception("subject not found")

    def showlist(self):
        print('subject', ' ' * 7, 'score')
        for i, j in self.__dict.items():
            print(i, j, sep=':' + ' ' * (15 - len(i)))


def main():
    May = Test(6)
    May.add('math', 90.0)
    May.add('PE', 85.0)
    May.add('english', 92.0)
    May.add('physics', 95.0)
    May.add('chemical', 93.0)
    May.add('a', 3.0)
    time.sleep(3)
    May.delete_subject('a')
    May.show('math')
    print(May.avg())
    print(May.mid())
    May.showlist()


main()
