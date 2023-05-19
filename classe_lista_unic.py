class List(list):
    def only_unique(self):
        res = []
        for item in self:
            if item not in res:
                res.append(item)
        return res


if __name__ == '__main__':
    li = List([1, 2, 3, 2, 3, 4])
    print(li.only_unique())
