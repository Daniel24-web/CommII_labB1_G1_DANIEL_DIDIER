import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):  
    """This block is a CE VCO or baseband VCO and works as following:
    The e_CE_VCO_fc block is a VCO 
    designed to operate in the baseband 
    domain, generating a complex envelope 
    from two input signals: a magnitude 
    A(t) and a phase Q(t). In the formula
    for the complex envelope, A(t) represents
    the in-phase component, while Q(t) 
    corresponds to the instantaneous phase
    (or the quadrature component, when 
    interpreted from the perspective of an
    I/Q modulator). The output is therefore
    a complex signal that encapsulates all 
    amplitude and phase modulation 
    information,enabling the signal to
    be analyzed or transmitted without
    the need to upconvert it directly
    to the radiofrequency (RF) domain."""

    def __init__(self,):  
        gr.sync_block.__init__(
            self,
            name='e_CE_VCO_fc',   
            in_sig=[np.float32, np.float32],
            out_sig=[np.complex64]
        )
        
    def work(self, input_items, output_items):
        A=input_items[0]
        Q=input_items[1]
        y=output_items[0]
        N=len(A)
        y[:]=A*np.exp(1j*Q)
        return len(output_items[0])
