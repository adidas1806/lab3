import datetime
from contextlib import contextmanager


class cm_timer_1:
    def __init__(self, scope_name):
        self.scope_name = scope_name

    def __enter__(self):
        # do stuff before code in context
        self.begin_time = datetime.datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # do stuff after code in context
        end_time = datetime.datetime.now()
        print(self.scope_name, 'finished in: ',
              (end_time - self.begin_time).total_seconds(), ' seconds')


@contextmanager
def cm_timer_2(scope_name):
    # everything before yield statement is like __enter__ method in class
    begin_time = datetime.datetime.now()
    yield  # yield statement can return object to work with in scope
    # we assign this object by using as key word
    # everything after yield statement is like __exit__ method in class
    end_time = datetime.datetime.now()
    print(scope_name, 'finished in: ',
          (end_time - begin_time).total_seconds(), ' seconds')
