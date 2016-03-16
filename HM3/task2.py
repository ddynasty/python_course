class Observable(object):

    def __init__(self, name, work, jobs, titles):
        self.name = name
        self.work = work
        self.jobs = jobs
        self.titles = titles

    def __str__(self):
        return 'Observable(name:{}, work:{}, jobs:{}, titles:{})'.format(self.name, self.work, self.jobs, self.titles)

obs = Observable(name='Jack', work='dev', jobs=('developer', '2 year'), titles={'senior dev': 'Google'})
print (obs.name)
print (obs)

