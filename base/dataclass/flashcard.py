from abc import ABCMeta, abstractmethod, abstractproperty
from kivy.properties import StringProperty, NumericProperty, ObjectProperty


class FlashCardBase(object):

    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def key(self):
        pass

    @property
    @abstractmethod
    def id_as_string(self):
        pass

    @property
    @abstractmethod
    def text(self):
        pass

    @property
    @abstractmethod
    def review_time(self):
        pass




