
import uuid
from functools import reduce

from jinja2 import Template

from QAStrategyCenter.Loader.preset import backtest_preset


class QAStrategyRender():

    def __init__(self, user: str = 'quantaxis', password: str = 'quantaxis', portfolio: str = 'default',
                 account_cookie: str = 'example_gen', spms: str = 'spms_gen',
                 start: str = '2019-08-01', end: str = '2019-09-01', init_cash: int = 50000,
                 frequence: str = '15min', ip: str = '127.0.0.1', port: int = 8010, source_code: str = 'text', **kwargs):
        self.user = user
        self.password = password
        self.account_cookie = str(
            uuid.uuid4()) if account_cookie is None else account_cookie

        self.portfolio = portfolio
        self.spms = spms

        self.init_cash = init_cash

        self.start = start
        self.end = end
        self.frequence = frequence
        self.ip = ip
        self.port = portfolio

        self.source_code = source_code

        self.kwargs = kwargs

    @property
    def template(self):
        print(self.source_code)
        res = self.source_code + backtest_preset
        return Template(res)

    @staticmethod
    def fn(x):
        return reduce(lambda x, y: [str(i)+'*$*'+str(j) for i in x for j in y], x)

    def load_parameter(self):
        pass

    def save_parameter(self):
        pass

    def render(self,  **kwargs):

        res = {'username': self.user, 'password': self.password, 'SPMSNAME': self.spms, 'start': self.start,
               'account_cookie': self.account_cookie,
               'end': self.end, 'init_cash': self.init_cash,
               'frequence': self.frequence, 'portfolio': self.portfolio}

        self.kwargs = kwargs

        for item in kwargs.keys():
            res[item] = kwargs[item]

        resx = [dict(zip(res.keys(), item.split('*$*'))) for item in self.fn(
            [item if isinstance(item, list) else [item] for item in res.values()])]

        jobmapper = len(resx)

        print('## start {} jobs with portfolio id {}'.format(
            jobmapper, self.portfolio))
        print(resx)

        for item in resx:
            print(item)
            content = self.template.render(item)
            yield content


if __name__ == "__main__":
    for i in QAStrategyRender(source_code='{{a}}').render(a=[1, 2, 3], b=['x', 'y']):
        print(i)
