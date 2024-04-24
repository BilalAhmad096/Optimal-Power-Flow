from src.logger import logger
import time

from pathlib import Path



def write_res(bus_result,line_res, net):
    try:
        timestr = time.strftime('%d%m%Y-%H%M%S')
        res_dir = Path(__file__).parent/'Results'
        res_dir.mkdir(parents= True, exist_ok= True)
        res_filename = 'res_'+timestr+'.txt'
        res_filepath = res_dir.joinpath(res_filename)
        
        # Writing results to the file
        with open(res_filepath, 'a') as file:
            file.write("# System Description\n")
            file.write(str(net))
            file.write("\n")
            file.write("# Bus Results\n")
            file.write(str(bus_result))
            file.write("\n")
            file.write("# Line Results\n")
            file.write(str(line_res))
    except Exception as e:
        logger.error(str(e))