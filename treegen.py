from __future__ import print_function
import json
import sys

# Tree in JSON format
s = '{"AP Statistics": {"children": [{"Algebra 2": {"children": [{"Geometry with Algebra": {"children": [{"Algebra 1": {"data": null}}], "data": null}}, {"Geometry with Proof": {"children": [{"Algebra 1": {"data": null}}], "data": null}}], "data": null}}, {"Precalculus with Analysis": {"children": [{"Algebra 2": {"children": [{"Geometry with Algebra": {"children": [{"Algebra 1": {"data": null}}], "data": null}}, {"Geometry with Proof": {"children": [{"Algebra 1": {"data": null}}], "data": null}}], "data": null}}], "data": null}}, {"Precalculus with Calculus": {"children": [{"Algebra 2 with Trigonometry": {"children": [{"Geometry with Proof": {"children": [{"Algebra 1": {"data": null}}], "data": null}}], "data": null}}], "data": null}}, {"Precalculus with Statistics": {"children": [{"Algebra 2": {"children": [{"Geometry with Algebra": {"children": [{"Algebra 1": {"data": null}}], "data": null}}, {"Geometry with Proof": {"children": [{"Algebra 1": {"data": null}}], "data": null}}], "data": null}}, {"Algebra 2 Foundations": {"children": [{"Geometry with Algebra": {"children": [{"Algebra 1": {"data": null}}], "data": null}}], "data": null}}], "data": null}}], "data": null}}'

# Convert JSON tree to a Python dict
data = json.loads(s)

# Convert back to JSON & print to stderr so we can verify that the tree is correct.
print(json.dumps(data, indent=4), file=sys.stderr)

# Extract tree edges from the dict
edges = []

def get_edges(treedict, parent=None):
    name = next(iter(treedict.keys()))
    if parent is not None:
        edges.append((parent, name))
    for item in treedict[name]["children"]:
        if isinstance(item, dict):
            get_edges(item, parent=name)
        else:
            edges.append((name, item))

get_edges(data)

# Dump edge list in Graphviz DOT format
print('strict digraph tree {')
for row in edges:
    print('    {0} -> {1};'.format(*row))
print('}')
