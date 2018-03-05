import pprint
from BCBio.GFF import GFFExaminer
from BCBio import GFF

in_file = "./ASM_chr_100.gff"

# examiner = GFFExaminer()
# in_handle = open(in_file)
# pprint.pprint(examiner.available_limits(in_handle))
# in_handle.close()

print('#' * 10)

in_handle = open(in_file)
for rec in GFF.parse(in_handle):
    # pprint.pprint(len(rec[0]))
    # pprint.pprint(type(rec[0]))
    # pprint.pprint((rec.name))
    # pprint.pprint((rec.description))
    # pprint.pprint((rec.letter_annotations))
    # pprint.pprint((rec.annotations))
    print('#' * 10)
    for i in rec.features:
        pprint.pprint(i.qualifiers)
    # pprint.pprint((rec.features[2].type))
    # pprint.pprint((rec.features[2].location))
    # pprint.pprint((rec.features[2].qualifiers))
    # pprint.pprint((rec.features[2].sub_features))
    # pprint.pprint((rec.dbxrefs))
in_handle.close()
