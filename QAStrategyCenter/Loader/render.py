
import uuid
from functools import reduce

from jinja2 import Template

from QAStrategyCenter.Loader.preset import backtest_preset


def render(user, password, account_cookie, spms, start, end, init_cash, frequence, ip, port, portfolio, source_code, args):
    res = source_code + backtest_preset
    print(args)
    template = Template(res)
    res = {'username': user, 'password': password, 'SPMSNAME': spms, 'start': start, 'account_cookie': str(uuid.uuid4()) if account_cookie is None else account_cookie,
           'end': end, 'init_cash': init_cash, 'frequence': frequence, 'portfolio': portfolio}
    for item in args:
        _t = item.split('=')
        res[_t[0]] = eval(_t[1])
    print(res)
    def fn(x): return reduce(lambda x, y: [
        str(i)+'*$*'+str(j) for i in x for j in y], x)
    resx = [dict(zip(res.keys(), item.split('*$*'))) for item in fn(
        [item if isinstance(item, list) else [item] for item in res.values()])]

    jobmapper = len(resx)
    print('## start {} jobs with portfolio id {}'.format(jobmapper, portfolio))
    print(resx)
    for item in resx:
        item['account_cookie'] = str(uuid.uuid4())
        content = template.render(item)
        yield content
