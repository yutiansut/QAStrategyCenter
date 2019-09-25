import click
import configparser
from QAStrategyCenter.Loader.render import  QASPMSRender


def load_config(configfile):
    try:
        conf = configparser.ConfigParser()
        conf.read(configfile,encoding='gbk')
        print(conf.)



@click.command()
@click.option('--t', default='QASPMS')
@click.option('--f', default='./template/t1/template.py',)
@click.option('--c', default='./template/t1/conf.ini')
def load_from_file(t,f,c):
    if t == 'QASPMS':
        try:
            with open(f,'r', encoding='gbk') as f:
                source = f.read()
                print(source)
                render = QASPMSRender(source_code = source)
        except Exception as e: 
            print(e)
        
if __name__ == "__main__":
    load_from_file()