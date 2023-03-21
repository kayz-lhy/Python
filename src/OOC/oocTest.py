class Test:
    def __init__(self, subject_num=int):
        self.__subject = subject_num
        self.__sublist = [None]
        self.__scorelist = [None] * 10

    def __add__(self, *p):
        self.__sublist.append(p[0])
        self.__scorelist[self.__sublist.index(p[0])] = p[1]


    def set_subject_num(self, value):
        self.__subject = value

    def add_subject(self, sub):
        self.__sublist.append(sub)

    def show_list(self):
        print(self.__sublist)

    def add_score(self, score=(int, float), subject=str):
        if not isinstance(score, (int, float)) \
                or not isinstance(subject, str):
            raise Exception('value error, score must be int or float, subject must be string')
        if subject not in self.__sublist:
            raise Exception('subject not found')
        i = self.__sublist.index(subject)
        self.__scorelist[i] = score

    def show_score(self, subject):
        print(subject, ':', self.__scorelist[self.__sublist.index(subject)])


def main():
    t = Test()
    t.add_subject('math')
    t.add_subject('physics')
    t.add_score(score=90.0, subject="math")
    t.show_score('math')
    t + ('PE', 85.0)
    t.show_score('PE')


main()
