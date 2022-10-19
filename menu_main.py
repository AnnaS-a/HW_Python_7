import html_creater as hc
import xml_generator as xg

import input_data as d

# import logger as lg


hc.new_create(xg.new_create(d.surname()))
hc.new_create(xg.new_create(d.name()))
hc.new_create(xg.new_create(d.number_tel()))
hc.new_create(xg.new_create(d.comment()))


# lg.surname_logger(d.surname())
# lg.name_logger(d.name())
# lg.number_tel_logger(d.number_tel())
# lg.comment_logger(d.comment())
