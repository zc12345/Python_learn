import matplotlib.pyplot as plt

def parse_log(log_path):
    loss_list = {
        'epoch': [],
        'step': [],
        'ct_loss': [],
        'wh_loss': [],
        'ex_loss': [],
        'py_loss': []
    }
    with open(log_path, 'r') as f:
        for line in f.readlines():
            words = line.split()
            # ----- train ------
            if len(words) != 30:
                continue
            loss_list['epoch'].append(int(words[9]))
            loss_list['step'].append(int(words[11]))
            loss_list['ct_loss'].append(float(words[13]))
            loss_list['wh_loss'].append(float(words[15])*0.1)
            loss_list['ex_loss'].append(float(words[17]))
            loss_list['py_loss'].append(float(words[19]))
            # ------ val -------
            # if len(words) != 16:
            #     continue
            # loss_list['ct_loss'].append(float(words[7][:-2]))
            # loss_list['wh_loss'].append(float(words[9][:-2])*0.1)
            # loss_list['ex_loss'].append(float(words[11][:-2]))
            # loss_list['py_loss'].append(float(words[13][:-2]))
        if not loss_list['step']: # val log
            loss_list['step'] = list(range(len(loss_list['ct_loss'])))
    return loss_list

def plot_loss(loss_list):
    print(len(loss_list['step']))
    index = 10
    step = 10
    plt.plot(loss_list['step'][index::step], loss_list['ct_loss'][index::step])
    plt.plot(loss_list['step'][index::step], loss_list['wh_loss'][index::step])
    plt.plot(loss_list['step'][index::step], loss_list['ex_loss'][index::step])
    plt.plot(loss_list['step'][index::step], loss_list['py_loss'][index::step])
    plt.legend(['ct_loss', 'wh_loss', 'ex_loss', 'py_loss'])
    plt.show()

if __name__ == '__main__':
    loss_list = parse_log('./train.log')
    plot_loss(loss_list)
