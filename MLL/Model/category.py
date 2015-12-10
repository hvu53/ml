__author__ = 'Zhiyu'

metaCategory = ['price','quality','amount','diet','style','waste','others']

class category:
    def __init__(self,metaname=None,name=None,likelihood=1):
        self.metaCategory = metaname
        self.name = name
        self.setLikelihood(likelihood)
        self.value = 1

    def setMetaCategory(self,meta):
        if meta not in metaCategory:
            _meta = 'others'
        else:
            _meta = meta
        self.metaCategory = _meta

    def setLikelihood(self,likelihood):
        if likelihood > 1:
            _likelihood = 1
        elif likelihood < 1e-10:
            _likelihood = 1e-10
        else:
            _likelihood = likelihood
        self.likelihood = _likelihood






