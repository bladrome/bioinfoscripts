import esabomethod
import spearman


ep = esabomethod.esabopositive
en = esabomethod.esabonegative

sp = spearman.spearmanpositive
sn = spearman.spearmannegative


print("EP:" + str(len(ep)))
print("EN:" + str(len(en)))
print("SP:" + str(len(sp)))
print("SN:" + str(len(sn)))


print(ep.intersection(sp))
print(en.intersection(sn))
