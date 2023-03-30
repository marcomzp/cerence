import re

def search_corpus(regex, curr_list):
  comp_reg = re.compile(regex)
  return list(filter(comp_reg.search, curr_list))

voiceless_gems_re = re.compile('p p|t t|k k')
voiceless_gems = list(filter(voiceless_gems_re.search, transcriptions))

print('Voiceless gems', len(search_corpus('p p|t t|k k', transcriptions)))
print('Voiced gems', len(search_corpus('b b|d d|g g', transcriptions)))

print('BOBBO', len(search_corpus('(b|d|g).*(b b|d d|g g)', transcriptions)))
print('BOPPO', len(search_corpus('(b|d|g).*(p p|t t|k k)', transcriptions)))
print('POPPO', len(search_corpus('(p|t|k).*(p p|t t|k k)', transcriptions)))
print('POBBO', len(search_corpus('(p|t|k).*(b b|d d|g g)', transcriptions)))
print('XOBBO', len(search_corpus('^[^bdg]+(b b|d d|g g)', transcriptions)))
print('XOPPO', len(search_corpus('^[^bdg]+(p p|t t|k k)', transcriptions)))



[x for x in boppo if x in bobbo + xobbo + xoppo]