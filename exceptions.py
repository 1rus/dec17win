class SframeExceptions(Exception):
    pass


class InvalidLocatorString(SframeExceptions):

    def get(self):
        return self.__m

    def set(self, message):
        self.__m = message

    __m = property(get, set)


class WaitForElementTimeout(SframeExceptions):

    def get_m(self):
        return self._message

    def set_m(self, message):
        self._message = message

    _message = property(get_m, set_m)


class WaitForTextTimeout(SframeExceptions):

    def get_m(self):
        return self._message

    def set_m(self, message):
        self._message = message

    _message = property(get_m, set_m)


class ElementNotFound(SframeExceptions):

    def get_m(self):
        return self._message

    def set_m(self, message):
        self._message = message

    _message = property(get_m, set_m)


class ProfileNotFound(SframeExceptions):

    def get_m(self):
        return self._message

    def set_m(self, message):
        self._message = message

    _message = property(get_m, set_m)

