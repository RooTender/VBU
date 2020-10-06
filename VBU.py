import os
import combiner

if not os.path.exists('output'):
    os.makedirs('output')

combiner.combine('test', 'output')
