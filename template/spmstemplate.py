import datetime
import numpy as np
import pandas as pd
import pymongo
import QUANTAXIS as QA
from QACEPEngine.QPMS.QAPosition import QA_Position
from QACEPEngine.QPMS.QASPMS import QA_SPMS
from QUANTAXIS.QAUtil.QAParameter import (EXCHANGE_ID, MARKET_TYPE,
                                          ORDER_DIRECTION)

# %% %%qarunpms  --spms p --portfolio Rank_T23003 --start 2018-01-01 --end 2019-08-10 --init_cash 20000 --timeout 500 frequence=['30min'] code=['RBL8'] length=list(range(5,70,2)) amp=list(range(10,100,2)) XZ=list(range(8,70,2))


class SPMS_Strategy(QA_SPMS):
    data_exchange = '{{code}}_{{frequence}}_bar'
    _orders = []

    def on_bar(self, bar):
        print(bar)
        print(self.market_data)

auto_reload = True
if_monitor = True


p = SPMS_Strategy(
    QA_Position(
        code="{{code}}",
        account_cookie="{{account_cookie}}",
        portfolio_cookie="{{portfolio_cookie}}",
        user_cookie="{{user_cookie}}",
        name="{{spms_name}}",
        moneypreset=int("{{init_cash}}")),
    auto_reload_data=({{auto_reload}}),
    if_monitor={{if_monitor}})
