#import necessary dependencies
import pandapower as pp

from src.logger import logger

class opf:
    def __init__(self):
        self.flag = None

    def distributionNetwork(self):
        #create an empty network
        net = pp.create_empty_network( name= "33 Bus Distribution Network") 
        
        #create buses
        bus00 = pp.create_bus(net, vn_kv=20., name="Bus 00")
        bus01 = pp.create_bus(net, vn_kv=0.4, name="Bus 01")
        bus02 = pp.create_bus(net, vn_kv=0.4, name="Bus 02")
        bus03 = pp.create_bus(net, vn_kv=0.4, name="Bus 03")
        bus04 = pp.create_bus(net, vn_kv=0.4, name="Bus 04")
        bus05 = pp.create_bus(net, vn_kv=0.4, name="Bus 05")
        bus06 = pp.create_bus(net, vn_kv=0.4, name="Bus 06")
        bus07 = pp.create_bus(net, vn_kv=0.4, name="Bus 07")
        bus08 = pp.create_bus(net, vn_kv=0.4, name="Bus 08")
        bus09 = pp.create_bus(net, vn_kv=0.4, name="Bus 09")
        bus10 = pp.create_bus(net, vn_kv=0.4, name="Bus 10")
        bus11 = pp.create_bus(net, vn_kv=0.4, name="Bus 11")
        bus12 = pp.create_bus(net, vn_kv=0.4, name="Bus 12")
        bus13 = pp.create_bus(net, vn_kv=0.4, name="Bus 13")
        bus14 = pp.create_bus(net, vn_kv=0.4, name="Bus 14")
        bus15 = pp.create_bus(net, vn_kv=0.4, name="Bus 15")
        bus16 = pp.create_bus(net, vn_kv=0.4, name="Bus 16")
        bus17 = pp.create_bus(net, vn_kv=0.4, name="Bus 17")
        bus18 = pp.create_bus(net, vn_kv=0.4, name="Bus 18")
        bus19 = pp.create_bus(net, vn_kv=0.4, name="Bus 19")
        bus20 = pp.create_bus(net, vn_kv=0.4, name="Bus 20")
        bus21 = pp.create_bus(net, vn_kv=0.4, name="Bus 21")
        bus22 = pp.create_bus(net, vn_kv=0.4, name="Bus 22")
        bus23 = pp.create_bus(net, vn_kv=0.4, name="Bus 23")
        bus24 = pp.create_bus(net, vn_kv=0.4, name="Bus 24")
        bus25 = pp.create_bus(net, vn_kv=0.4, name="Bus 25")
        bus26 = pp.create_bus(net, vn_kv=0.4, name="Bus 26")
        bus27 = pp.create_bus(net, vn_kv=0.4, name="Bus 27")
        bus28 = pp.create_bus(net, vn_kv=0.4, name="Bus 28")
        bus29 = pp.create_bus(net, vn_kv=0.4, name="Bus 29")
        bus30 = pp.create_bus(net, vn_kv=0.4, name="Bus 30")
        bus31 = pp.create_bus(net, vn_kv=0.4, name="Bus 31")
        bus32 = pp.create_bus(net, vn_kv=0.4, name="Bus 32")

        # Generators
        pp.create_gen(net, bus00, p_mw=50, min_p_mw=0, max_p_mw=40, controllable=True, slack = True)

        #External Grid
        # pp.create_ext_grid(net, bus=bus00, vm_pu=1.02, name="Grid Connection")

        #Transformer
        # transformer = pp.create_transformer(net, hv_bus=bus00, lv_bus=bus01, std_type="0.4 MVA 20/0.4 kV", name="Transformer")

        #Connections
        line01 = pp.create_line(net, from_bus=bus00, to_bus=bus01, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 00->01")
        line02 = pp.create_line(net, from_bus=bus01, to_bus=bus02, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 01->02")
        line03 = pp.create_line(net, from_bus=bus02, to_bus=bus03, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 02->03")
        line04 = pp.create_line(net, from_bus=bus03, to_bus=bus04, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 03->04")
        line05 = pp.create_line(net, from_bus=bus04, to_bus=bus05, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 04->05")
        line06 = pp.create_line(net, from_bus=bus05, to_bus=bus06, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 05->06")
        line07 = pp.create_line(net, from_bus=bus06, to_bus=bus07, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 06->07")
        line08 = pp.create_line(net, from_bus=bus07, to_bus=bus08, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 07->08")
        line09 = pp.create_line(net, from_bus=bus08, to_bus=bus09, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 08->09")
        line10 = pp.create_line(net, from_bus=bus09, to_bus=bus10, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 09->10")
        line11 = pp.create_line(net, from_bus=bus10, to_bus=bus11, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 10->11")
        line12 = pp.create_line(net, from_bus=bus11, to_bus=bus12, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 11->12")
        line13 = pp.create_line(net, from_bus=bus12, to_bus=bus13, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 12->13")
        line14 = pp.create_line(net, from_bus=bus13, to_bus=bus14, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 13->14")
        line15 = pp.create_line(net, from_bus=bus14, to_bus=bus15, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 14->15")
        line16 = pp.create_line(net, from_bus=bus15, to_bus=bus16, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 15->16")
        line17 = pp.create_line(net, from_bus=bus16, to_bus=bus17, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 16->17")
        line18 = pp.create_line(net, from_bus=bus01, to_bus=bus18, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 01->18")
        line19 = pp.create_line(net, from_bus=bus18, to_bus=bus19, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 18->19")
        line20 = pp.create_line(net, from_bus=bus19, to_bus=bus20, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 19->20")
        line21 = pp.create_line(net, from_bus=bus20, to_bus=bus21, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 20->21")
        line22 = pp.create_line(net, from_bus=bus02, to_bus=bus22, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 02->22")
        line23 = pp.create_line(net, from_bus=bus22, to_bus=bus23, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 22->23")
        line24 = pp.create_line(net, from_bus=bus23, to_bus=bus24, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 23->24")
        line25 = pp.create_line(net, from_bus=bus05, to_bus=bus25, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 05->25")
        line26 = pp.create_line(net, from_bus=bus25, to_bus=bus26, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 25->26")
        line27 = pp.create_line(net, from_bus=bus26, to_bus=bus27, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 26->27")
        line28 = pp.create_line(net, from_bus=bus27, to_bus=bus28, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 27->28")
        line29 = pp.create_line(net, from_bus=bus28, to_bus=bus29, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 28->29")
        line30 = pp.create_line(net, from_bus=bus29, to_bus=bus30, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 29->30")
        line31 = pp.create_line(net, from_bus=bus30, to_bus=bus31, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 30->31")
        line32 = pp.create_line(net, from_bus=bus31, to_bus=bus32, length_km=0.1, std_type="NAYY 4x50 SE", name="Line 31->32")

        #Loads
        load01 = pp.create_load(net, bus=bus01, p_mw=0.100, q_mvar=0.060, name="Load 01")
        load02 = pp.create_load(net, bus=bus02, p_mw=0.090, q_mvar=0.040, name="Load 02")
        load03 = pp.create_load(net, bus=bus03, p_mw=0.120, q_mvar=0.080, name="Load 03")
        load04 = pp.create_load(net, bus=bus04, p_mw=0.060, q_mvar=0.030, name="Load 04")
        load05 = pp.create_load(net, bus=bus05, p_mw=0.060, q_mvar=0.020, name="Load 05")
        load06 = pp.create_load(net, bus=bus06, p_mw=0.200, q_mvar=0.100, name="Load 06")
        load07 = pp.create_load(net, bus=bus07, p_mw=0.200, q_mvar=0.100, name="Load 07")
        load08 = pp.create_load(net, bus=bus08, p_mw=0.060, q_mvar=0.020, name="Load 08")
        load09 = pp.create_load(net, bus=bus09, p_mw=0.060, q_mvar=0.020, name="Load 09")
        load10 = pp.create_load(net, bus=bus10, p_mw=0.045, q_mvar=0.030, name="Load 10")
        load11 = pp.create_load(net, bus=bus11, p_mw=0.060, q_mvar=0.035, name="Load 11")
        load12 = pp.create_load(net, bus=bus12, p_mw=0.060, q_mvar=0.035, name="Load 12")
        load13 = pp.create_load(net, bus=bus13, p_mw=0.120, q_mvar=0.080, name="Load 13")
        load14 = pp.create_load(net, bus=bus14, p_mw=0.060, q_mvar=0.010, name="Load 14")
        load15 = pp.create_load(net, bus=bus15, p_mw=0.060, q_mvar=0.020, name="Load 15")
        load16 = pp.create_load(net, bus=bus16, p_mw=0.060, q_mvar=0.020, name="Load 16")
        load17 = pp.create_load(net, bus=bus17, p_mw=0.090, q_mvar=0.040, name="Load 17")
        load18 = pp.create_load(net, bus=bus18, p_mw=0.090, q_mvar=0.040, name="Load 18")
        load19 = pp.create_load(net, bus=bus19, p_mw=0.090, q_mvar=0.040, name="Load 19")
        load20 = pp.create_load(net, bus=bus20, p_mw=0.090, q_mvar=0.040, name="Load 20")
        load21 = pp.create_load(net, bus=bus21, p_mw=0.090, q_mvar=0.040, name="Load 21")
        load22 = pp.create_load(net, bus=bus22, p_mw=0.090, q_mvar=0.050, name="Load 22")
        load23 = pp.create_load(net, bus=bus23, p_mw=0.420, q_mvar=0.200, name="Load 23")
        load24 = pp.create_load(net, bus=bus24, p_mw=0.420, q_mvar=0.200, name="Load 24")
        load25 = pp.create_load(net, bus=bus25, p_mw=0.060, q_mvar=0.025, name="Load 25")
        load26 = pp.create_load(net, bus=bus26, p_mw=0.060, q_mvar=0.025, name="Load 26")
        load27 = pp.create_load(net, bus=bus27, p_mw=0.060, q_mvar=0.020, name="Load 27")
        load28 = pp.create_load(net, bus=bus28, p_mw=0.120, q_mvar=0.070, name="Load 28")
        load29 = pp.create_load(net, bus=bus29, p_mw=0.200, q_mvar=0.600, name="Load 29")
        load30 = pp.create_load(net, bus=bus30, p_mw=0.150, q_mvar=0.070, name="Load 30")
        load31 = pp.create_load(net, bus=bus31, p_mw=0.210, q_mvar=0.100, name="Load 31")
        load32 = pp.create_load(net, bus=bus32, p_mw=0.060, q_mvar=0.040, name="Load 32")

        try:
            pp.runopp(net, numba=False)
        except Exception as e:
            logger.error(str(e))


        