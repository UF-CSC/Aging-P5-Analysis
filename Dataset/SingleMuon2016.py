from Dataset.Utils import makeComponentsFromPath
from Core.NanoAODResult.Component import Component

paths_SingleMuon2016F_v1 = ["/cms/data/store/user/hmei/rootfiles_2017/CSCNtuples_2016SingleMu_BCDEFGH_promptReco/SingleMuon/crab_SingleMuon_Run2016F-PromptReco-v1/170322_174355/000%s"%i for i in range(0,3) ]

paths_SingleMuon2016G_v1 = ["/cms/data/store/user/hmei/rootfiles_2017/CSCNtuples_2016SingleMu_BCDEFGH_promptReco/SingleMuon/crab_SingleMuon_Run2016G-PromptReco-v1/170322_174419/000%s"%i for i in range(0,7) ]

paths_SingleMuon2016H_v2 = ["/cms/data/store/user/hmei/rootfiles_2017/CSCNtuples_2016SingleMu_BCDEFGH_promptReco/SingleMuon/crab_SingleMuon_Run2016H-PromptReco-v2/170522_130029/000%s/"%i for i in range(0,7) ]

path_SingleMuon2016H_v3 = "/cms/data/store/user/hmei/rootfiles_2017/CSCNtuples_2016SingleMu_BCDEFGH_promptReco/SingleMuon/crab_SingleMuon_Run2016H-PromptReco-v3/170322_174443/0000/"

comp_SingleMuon2016F_v1 = []
for path in paths_SingleMuon2016F_v1:
    comp_SingleMuon2016F_v1.extend(makeComponentsFromPath(path))

comp_SingleMuon2016G_v1 = []
for path in paths_SingleMuon2016G_v1:
    comp_SingleMuon2016G_v1.extend(makeComponentsFromPath(path))

comp_SingleMuon2016H_v2 = []
for path in paths_SingleMuon2016H_v2:
    comp_SingleMuon2016H_v2.extend(makeComponentsFromPath(path))

comp_SingleMuon2016H_v3 = makeComponentsFromPath(path_SingleMuon2016H_v3)

comp_SingleMuon2016F_v1_anl = []
for path in paths_SingleMuon2016F_v1:
    comp_SingleMuon2016F_v1_anl.append(
        Component(
            path+"/",
            path.split("/")[-1],
            keyword="",
        )
    )
