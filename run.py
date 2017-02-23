from markov_python.cc_markov import MarkovChain

mc = MarkovChain()
mc.add_file('/Users/mobpro/desktop/winereviews.txt')

mc.add_string("red")

print str(mc.generate_text(10))


