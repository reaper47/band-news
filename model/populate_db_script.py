import sys
import os
dir = ''.join([os.path.dirname(__file__), '../src/api'])
sys.path.append(dir)
import db_master

STATE_FILE = 'data_state.txt'


def construct_state_dict():
    state = {}

    with open(STATE_FILE, 'r') as f:
        for line in f:
            s = line.split('=')

            key = s[0]
            val = int(s[1])
            state[key] = val

    return state



def overwrite_state_file(state_dict):
    with open(STATE_FILE, 'w') as f:
        for key in state_dict:
            line = '{0}={1}'.format(key, state_dict[key])
            f.write(line)



if __name__ == '__main__':
    state = construct_state_dict()

    master = db_master.DbMaster()
    master.open_connection()

    if state['countries'] == 0:
        master.push_countries_to_db()
        state['countries'] = 1
        overwrite_state_file(state)

    master.close_connection()



    


