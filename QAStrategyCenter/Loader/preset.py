


header = '\
import datetime\n\
import json\n\
import threading\n\
import numpy as np\n\
import pandas as pd\n\
import pymongo\n\
import requests\n\
import QUANTAXIS as QA\n\
from QACEPEngine.QPMS.QASPMS import QA_SPMS\n\
from QUANTAXIS import QA_Position\n\
from QUANTAXIS.QAUtil.QAParameter import (EXCHANGE_ID, MARKET_TYPE,\
                                          ORDER_DIRECTION)\n\r\n'

"""
start:
end:
frequence:
username:

"""



spms_body = '\n\r\
user_spms = SPMS_Strategy(\n\
    QA_Position(\n\
        code="{{code}}",\n\
        account_cookie="{{account_cookie}}",\n\
        portfolio_cookie="{{portfolio_cookie}}",\n\
        user_cookie="{{user_cookie}}",\n\
        name="{{spms_name}}",\n\
        moneypreset={{init_cash}}),\n\
    auto_reload_data={{auto_reload}},\n\
    if_monitor={{if_monitor}})'

backtest_preset = '\n\r\
from quantaxis_autogeneration.__main__ import QAAG_Executor\n\
with QAAG_Executor(user_spms, "{{start}}", "{{end}}", "{{frequence}}", "{{username}}", "{{password}}", "{{portfolio}}","{{account_cookie}}", float({{init_cash}})) as f: \n\
    for _, bar in f: \n\
        bar = bar.to_dict()\n\
        p.pos.on_pirce_change(bar[\'close\'])\n\
        p.pos.time = bar[\'datetime\']\n\
        p.market_data.append(bar) \n\
        p.on_bar(bar)\n'

sim_runtime = '\n\rp.start()\n'


real_runtime = '\n'