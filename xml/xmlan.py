# -*- coding: utf-8 -*-
# @Author: kyqia
# @Date:   2017-12-04 19:56:51
# @Last Modified by:   kyqia
# @Last Modified time: 2017-12-04 23:47:00
import re
import numpy as np
import xml.etree.ElementTree as ET

file = 'nscf.xml'
tree = ET.parse(file)
root = tree.getroot()

with open('data', 'w') as f:
    for eigen in root.iter('eigenvalues'):
        if float(eigen.attrib['weight']) < 0.001:
            a = eigen.text
            m = re.sub('<|>|/|[a-zA-Z]|(\n)', ' ', a)
            m = re.sub(' +', ' ', m)
            m = m.split(' ')
            f.write(np.array2string(np.array([float(i) for i in eigen.attrib['kpoint'].split(' ') +
                                              m[1:9] + [0]]), max_line_width=300, precision=5) + '\n')
