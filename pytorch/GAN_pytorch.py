#%% https://github.com/RedstoneWill/MachineLearningInAction/blob/master/GAN/GAN_1.py
import numpy as np
import matplotlib.pyplot as plt
import torch
from torch import nn

#%% hyper params
BATCH_SIZE = 64
LR_G = 0.0001 # learning rate for generator
LR_D = 0.0001 # learning rate for discriminator
N_IDEAS = 5
ART_COMPONENTS = 15
PAINT_POINTS = np.vstack([np.linspace(-1, 1, ART_COMPONENTS) for _ in range(BATCH_SIZE)])

#%% real target
def real_target():
    r = 0.02 * np.random.randn(1, ART_COMPONENTS)
    target = np.sin(PAINT_POINTS * np.pi) + r
    target = torch.from_numpy(target).float()
    return target

#%% G--generator
G = nn.Sequential(
        nn.Linear(N_IDEAS, 128),
        nn.ReLU(),
        nn.Linear(128, ART_COMPONENTS)
        )

#%% D--discriminator
D = nn.Sequential(
        nn.Linear(ART_COMPONENTS, 128),
        nn.ReLU(),
        nn.Linear(128,1),
        nn.Sigmoid()
        )

#%% set optmizer
optmizer_G = torch.optim.Adam(G.parameters(), lr=LR_G)
optmizer_D = torch.optim.Adam(D.parameters(), lr=LR_D)

plt.ion() # continuous plotting

G_loss_history = []
D_loss_history = []

for step in range(10000):
    target = real_target()
    G_ideas = torch.randn(BATCH_SIZE, N_IDEAS)
    G_result = G(G_ideas)
    
    prob_target0 = D(target) #try to decrease this score
    prob_target1 = D(G_result)#try to increase this score
    
    D_loss = - torch.mean(torch.log(prob_target0) + torch.log(1. - prob_target1))
    G_loss = torch.mean(torch.log(1. - prob_target1))
    D_loss_history.append(D_loss)
    G_loss_history.append(G_loss)
    
    optmizer_D.zero_grad()
    D_loss.backward(retain_graph=True)    # reusing computational graph
    optmizer_D.step()
    
    optmizer_G.zero_grad()
    G_loss.backward()
    optmizer_G.step()
    
    if step%500 == 0:
        plt.cla()
        plt.plot(PAINT_POINTS[0], G_result.data.numpy()[0], c='#4AD631', lw=3,  label='Gen')
        plt.plot(PAINT_POINTS[0], np.sin(PAINT_POINTS[0] * np.pi), c='#74BCFF', lw=3, label='Target')
        print('D score = ', torch.mean(prob_target0).data.numpy())
        print('D loss = ', - D_loss.data.numpy())
        plt.ylim((-1, 1))
        plt.legend(loc='upper right', fontsize=10)
        plt.draw()
        plt.pause(0.01)

#x = np.array(range(len(D_loss_history)))    
plt.plot(D_loss_history,c='#74BCFF', lw=3, label='G_loss')
plt.legend(loc='upper right', fontsize=10)
plt.ioff()
plt.show()