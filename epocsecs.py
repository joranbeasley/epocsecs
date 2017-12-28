from datetime import datetime

import sys

import os
from dateutil.parser import parse as date_parse

def safe_call(cast_to,cast_what,default=None):
    try:
        return cast_to(cast_what)
    except Exception as e:
        return default
def get_date(base_dt):
    if isinstance(base_dt,datetime):
        return base_dt
    if isinstance(base_dt,basestring):
        dt = safe_call(int, base_dt, safe_call(float, base_dt, base_dt))
        if isinstance(dt,basestring):
            dt = date_parse(dt)
    else:
        dt = base_dt
    if isinstance(dt,(int,float)):
        try:
            date_potentials = [datetime.fromordinal(dt),datetime.fromtimestamp(dt)]
            dt = min(date_potentials,key=lambda dx:abs(datetime.now()-dx).total_seconds())
        except:
            dt = datetime.fromtimestamp(dt)
    if not isinstance(dt,datetime):
        raise ValueError("Unable To Convert %r to a datetime"%base_dt)
    return dt

def epocsecs(target_date=None,base_dt="1/1/2000"):
    if target_date is None:
        target_date=datetime.now()
    else:
        target_date = get_date(target_date)
    base_dt = get_date(base_dt)
    return (target_date-base_dt).total_seconds()


def parse_args():
    import argparse
    parser = argparse.ArgumentParser(prog=os.path.basename(sys.argv[0]))
    parser.add_argument("-t", "--target", help="SEE: target_date")
    parser.add_argument("-e", "--epoc", help="SEE: epoc_date")
    parser.add_argument("target_date", nargs="?", default=None, help="The Target date(default=now) to convert")
    parser.add_argument("epoc_date", nargs="?", default="1/1/2000", help="The Epoc date(default=1/1/2000) to use")
    args = parser.parse_args()
    epoc = args.epoc or args.epoc_date
    target = args.target or args.target_date
    print epocsecs(target, epoc)

if __name__ == "__main__":
    parse_args()