import arrow

brewing_time=arrow.utcnow()
brewing_time.to("US/Pacific")

from collections import namedtuple
chaiProfile=namedtuple("ChaiProfile",["flavor","caffeine","milk"])