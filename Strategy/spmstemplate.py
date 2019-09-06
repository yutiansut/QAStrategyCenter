import datetime
import numpy as np
import pandas as pd
import pymongo
import QUANTAXIS as QA
from QACEPEngine.QPMS.QASPMS import QA_SPMS
from QUANTAXIS import QA_Position
from QUANTAXIS.QAUtil.QAParameter import (EXCHANGE_ID, MARKET_TYPE,
                                          ORDER_DIRECTION)
from quantaxis_autogeneration.__main__ import QAAG_Executor


class Strategy(QA_SPMS):
    data_exchange = '{{code}}_{{frequence}}_bar'
    _orders = []

    def on_bar(self, bar):
        print(bar)
        print(self.market_data)


p = Strategy(
    QA_Position(
        code="{{code}}",
        account_cookie="{{account_cookie}}",
        portfolio_cookie="{{portfolio_cookie}}",
        user_cookie="{{user_cookie}}",
        name="{{spms_name}}",
        moneypreset={{init_cash}}),
    auto_reload_data={{auto_reload}},
    if_monitor={{if_monitor}})
