class Stack:
    __data = []
    __min = []

    def pop(self) -> int:
        if self.__data:
            if self.__data[0] == self.__min[0]:
                self.__min.pop(0)
                return self.__data.pop(0)
            else:
                return self.__data.pop(0)

    def push(self, data: int) -> None:
        if not self.__data:
            self.__data = [data]
            self.__min = [data]
        else:
            self.__data = [data] + self.__data
            if data <= self.__min[0]:
                self.__min = [data] + self.__min

    def get_min(self) -> int:
        if self.__min:
            return self.__min[0]

    def __str__(self) -> str:
        return str(self.__data)
