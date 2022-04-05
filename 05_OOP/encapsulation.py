"""
- public
- protected
- private
"""


class Computer:
    def __init__(self, cpu, memory, hdd):
        self.__cpu = cpu                        # private
        self._memory = memory                   # protected
        self.hdd = hdd                          # public

    def print_computor(self):                   # public method
        print('CPU: {} MHz,\nMemory: {} Mb,\nHDD: {} Gb'.format(
            self.__cpu,
            self._memory,
            self.hdd
        ))


comp = Computer(2300, 16000, 2000)
comp.print_computor()
print(dir(comp))
print(comp._Computer__cpu)
print(comp._memory)
print(comp.hdd)
