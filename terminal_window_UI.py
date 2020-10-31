# -*- coding: utf-8 -*-
import pandas as  pd
import numpy as np
from progress.bar import Bar

bar = Bar('Processing', max=20)
for i in range(20):
    s=pd.array(np.random.randn(100000))
    print(s)
    np.exp(s)
    bar.next()
bar.finish()
