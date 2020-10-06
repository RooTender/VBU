import os
import vidCombiner

if not os.path.exists('output'):
    os.makedirs('output')

vidCombiner.combine('test', 'output')
