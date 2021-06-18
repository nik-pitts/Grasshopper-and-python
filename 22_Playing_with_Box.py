import rhinoscriptsyntax as rs
import ghpythonlib.treehelpers as th


raw_bb_base = th.tree_to_list(b,retrieve_base=None)
bb_base = rs.coercebrep(raw_bb_base)

print bb_base
