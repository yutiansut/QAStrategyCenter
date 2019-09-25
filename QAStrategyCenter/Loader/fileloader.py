import click
import configparser
from QAStrategyCenter.Loader.render import QASPMSRender


def load_config(configfile):
    try:
        conf = configparser.ConfigParser()
        conf.read(configfile, encoding='gbk')
        # print(conf.)
        sections = conf.sections()
        config = {}
        for sec in sections:
            for item in conf.options(sec):
                if item in ['auto_reload', 'if_monitor']:
                    config[item] = conf.getboolean(sec, item)
                else:
                    try:
                        config[item] = eval(conf.get(sec, item))
                    except:
                        config[item] = conf.get(sec, item)

        return config

    except Exception as e:
        print(e)


@click.command()
@click.option('--t', default='QASPMS')
@click.option('--f', default='E:/QAStrategyCenter/template/spmstemplate.py',)
@click.option('--c', default='E:/QAStrategyCenter/conf/conf.ini')
def load_from_file(t, f, c):
    if t == 'QASPMS':
        try:
            with open(f, 'r', encoding='gbk') as f:
                source = f.read()
                QArender = QASPMSRender(source_code=source)
                conf = load_config(c)
                for item in QArender.render(conf=conf):
                    print('under is strategy content')
                    print(item)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    # print(load_config('E:/QAStrategyCenter/conf/conf.ini'))
    load_from_file()
