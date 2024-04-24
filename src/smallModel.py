import pandapower as pp
from src.logger import logger
from src.writeResults import write_res
class testSystem:
    def __init__(self):
        self.flag = None

    def smallModel():
        try:
            # create empty net
            net = pp.create_empty_network()

            # define voltage limits
            min_vm_pu = 0.95
            max_vm_pu = 1.05

            # create buses
            bus1 = pp.create_bus(net, vn_kv=20.0, min_vm_pu=min_vm_pu, max_vm_pu=max_vm_pu, name="Bus 1")
            bus2 = pp.create_bus(net, vn_kv=0.40, min_vm_pu=min_vm_pu, max_vm_pu=max_vm_pu, name="Bus 2")
            bus3 = pp.create_bus(net, vn_kv=0.40, min_vm_pu=min_vm_pu, max_vm_pu=max_vm_pu, name="Bus 3")
            bus4 = pp.create_bus(net, vn_kv=0.40, min_vm_pu=min_vm_pu, max_vm_pu=max_vm_pu, name="Bus 4")
            bus5 = pp.create_bus(net, vn_kv=0.40, min_vm_pu=min_vm_pu, max_vm_pu=max_vm_pu, name="Bus 5")

            # create connections
            line1 = pp.create_line(net, from_bus=bus1, to_bus=bus2, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 1")
            line2 = pp.create_line(net, from_bus=bus2, to_bus=bus3, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 2")
            line3 = pp.create_line(net, from_bus=bus2, to_bus=bus4, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 3")
            line4 = pp.create_line(net, from_bus=bus4, to_bus=bus5, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 4")

            # connect generators
            gen1 = pp.create_gen(net, bus1, p_mw=1.0, min_p_mw=0.0, max_p_mw=1.0, vm_pu=1.0, controllable=True, slack=True)
            gen2 = pp.create_gen(net, bus2, p_mw=0.2, min_p_mw=0.0, max_p_mw=0.2, vm_pu=1.0, controllable=True)
            gen3 = pp.create_gen(net, bus3, p_mw=0.2, min_p_mw=0.0, max_p_mw=0.2, vm_pu=1.0, controllable=True)
            gen4 = pp.create_gen(net, bus4, p_mw=0.2, min_p_mw=0.0, max_p_mw=0.2, vm_pu=1.0, controllable=True)

            # create polynomial cost functions for generators
            pp.create_poly_cost(net, element=gen1, et="gen", cp1_eur_per_mw=45)
            pp.create_poly_cost(net, element=gen2, et="gen", cp1_eur_per_mw=25)
            pp.create_poly_cost(net, element=gen3, et="gen", cp1_eur_per_mw=25)
            pp.create_poly_cost(net, element=gen4, et="gen", cp1_eur_per_mw=30)

            # connect loads
            pp.create_load(net, bus=bus2, p_mw=0.10, q_mvar=0.060, name="Load at bus 2")
            pp.create_load(net, bus=bus3, p_mw=0.10, q_mvar=0.050, name="Load at bus 3")
            pp.create_load(net, bus=bus4, p_mw=0.03, q_mvar=0.005, name="Load at bus 4")
            pp.create_load(net, bus=bus5, p_mw=0.05, q_mvar=0.035, name="Load at bus 5")

            # run OPF
            pp.runopp(net, numba=False)

            write_res(net.res_bus,net.res_line, net)
            # print(net.res_cost)


        except Exception as e:
            logger.error(str(e))