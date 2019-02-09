"""timeflux.core.schedule: run nodes"""

import sys
import signal
import logging
from time import time, sleep
from copy import deepcopy
from timeflux.core.exceptions import WorkerInterrupt
from timeflux.core.registry import Registry

class Scheduler:

    def __init__(self, path, nodes, rate):
        self._path = path
        self._nodes = nodes
        self._rate = rate

    def run(self):
        try:
            while True:
                start = time()
                Registry.cycle_start = start
                self.next()
                duration = time() - start
                if self._rate > 0:
                    max_duration = 1. / self._rate
                    if duration > max_duration:
                        logging.debug('Congestion')
                    sleep(max(0, max_duration - duration))
        except WorkerInterrupt as error:
            logging.debug(error)
        logging.info('Terminating')

    def next(self):
        for step in self._path:
            # Clear ports
            self._nodes[step['node']].clear()
            # Update inputs from predecessor outputs
            if step['predecessors']:
                for predecessor in step['predecessors']:
                    # Get a generator so dynamic ports are expanded
                    src_ports = self._nodes[predecessor['node']].iterate(predecessor['src_port'])
                    for name, suffix, src_port in src_ports:
                        if predecessor['copy']:
                            if src_port.data is not None:
                                src_port.data = src_port.data.copy(deep=True)
                            if src_port.meta is not None:
                                src_port.meta = deepcopy(src_port.meta)
                        dst_port = getattr(self._nodes[step['node']], predecessor['dst_port'] + suffix)
                        dst_port.data = src_port.data
                        dst_port.meta = src_port.meta
            # Update node
            self._nodes[step['node']].update()
