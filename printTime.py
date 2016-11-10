class Time(object):

    """
    Represents the time of day.
    attributes: hour, minute, second

    """

t = Time()
hours = 1
minutes = 59
seconds = 30


def print_time(t):
        print('{0:0>2d}'.format(hours) + ':' + '{0:0>2d}'.format(minutes) + ':' + '{0:0>2d}'.format(seconds))


print_time(t)



