# -*- coding: utf-8 -*-
import pandas as  pd
import numpy as np
import progress

bar = progress.FillingSquaresBar('Processing', max=20)
for i in range(20):
    s=pd.array(np.random.randn(10000))
    for item in s:
        np.exp(item)
    bar.next()
bar.finish()
