import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):  
    """This block is a RF VCO and works as following:
    The custom block e_RF_VCO_ff implements 
    a Voltage-Controlled Oscillator (VCO) 
    to generate a modulated radiofrequency(RF) 
    signal from two input signals: an 
    amplitude signal (A) and a phase signal(Q).
    The core operation of the block involves 
    producing a discrete signal y[nTs] by 
    multiplying the amplitude A with a cosine
    function, which generates the modulated 
    carrier. In the formula, fc represents
    the carrier frequency, Ts is the sampling
    period defined as Ts=1/fs and n is the
    discrete time index.
    In the code implementation, a time vector
    generated using the np.linspace function
    is employed to simulate the temporal 
    continuity of the process through the
    self.n_m accumulator. This vector 
    represents the sampling instants required
    to compute the modulating cosine function.
    The purpose of this block is to facilitate
    the conversion of baseband signals to the
    radiofrequency (RF) domain.""""

    def __init__(self, fc=128000, samp_rate=320000):  
        gr.sync_block.__init__(
            self,
            name='e_RF_VCO_ff',   
            in_sig=[np.float32, np.float32],
            out_sig=[np.float32]
        )
        self.fc = fc
        self.samp_rate = samp_rate
        self.n_m=0

    def work(self, input_items, output_items):
        A=input_items[0]
        Q=input_items[1]
        y=output_items[0]
        N=len(A)
        n=np.linspace(self.n_m,self.n_m+N-1,N)
        self.n_m += N
        y[:]=A*np.cos(2*math.pi*self.fc*n/self.samp_rate+Q)
        return len(output_items[0])


